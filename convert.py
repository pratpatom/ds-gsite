
import xml.etree.ElementTree as ET
import json
import re
import sys
import os

def get_text_from_element(element):
    if element is None:
        return ""
    return "".join(element.itertext()).strip()

def get_cell_content(cell_element, namespaces, list_styles=None):
    """Extract content from table cell, handling auto-increment lists"""
    if cell_element is None:
        return ""
    
    # Check if this cell contains a list element (auto-increment)
    list_element = cell_element.find('.//text:list', namespaces)
    if list_element is not None and list_styles is not None:
        # Extract the list style name
        style_name = list_element.get(f"{{{namespaces['text']}}}style-name")
        if style_name and style_name in list_styles:
            return str(list_styles[style_name])
    
    # Fallback to regular text extraction
    return get_text_from_element(cell_element)

def extract_list_styles(root, namespaces):
    """Extract list style definitions and their start values"""
    list_styles = {}
    
    # Find all list style definitions
    for list_style in root.findall('.//text:list-style', namespaces):
        style_name = list_style.get(f"{{{namespaces['style']}}}name")
        if style_name:
            # Find the text:start-value attribute
            level_style = list_style.find('.//text:list-level-style-number', namespaces)
            if level_style is not None:
                start_value = level_style.get(f"{{{namespaces['text']}}}start-value")
                if start_value:
                    try:
                        list_styles[style_name] = int(start_value)
                    except ValueError:
                        pass
    
    return list_styles

def parse_table(table_element, namespaces, list_styles=None):
    rows = []
    header_rows = table_element.findall('table:table-header-rows/table:table-row', namespaces)
    body_rows = table_element.findall('table:table-row', namespaces)
    
    for row_element in header_rows + body_rows:
        row_data = []
        for cell_element in row_element.findall('table:table-cell', namespaces):
            row_data.append(get_cell_content(cell_element, namespaces, list_styles))
        rows.append(row_data)
    return rows

def main():
    # Default file paths
    default_xml = 'data/metadata_std.xml'
    default_json = 'data/metadata_std.json'
    
    # Check command line arguments
    if len(sys.argv) == 3:
        xml_file = sys.argv[1]
        json_file = sys.argv[2]
    elif len(sys.argv) == 2:
        xml_file = sys.argv[1]
        # Generate output filename based on input
        base_name = os.path.splitext(os.path.basename(xml_file))[0]
        dir_name = os.path.dirname(xml_file) or 'data'
        json_file = os.path.join(dir_name, f"{base_name}.json")
    else:
        xml_file = default_xml
        json_file = default_json
    
    # Check if input file exists
    if not os.path.exists(xml_file):
        print(f"Error: Input file '{xml_file}' not found.")
        print("Usage: python convert.py [input.xml] [output.json]")
        print("       python convert.py [input.xml]  # Output will be auto-generated")
        print("       python convert.py              # Uses default files")
        return

    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
        'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    }

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract list style definitions for auto-increment handling
    list_styles = extract_list_styles(root, namespaces)

    office_text = root.find('office:body/office:text', namespaces)
    if office_text is None:
        print("Error: <office:text> element not found.")
        return

    elements = list(office_text)
    
    tables = {}
    for i, elem in enumerate(elements):
        if elem.tag == f"{{{namespaces['table']}}}table":
            table_name = elem.get(f"{{{namespaces['table']}}}name")
            title = table_name
            if i > 0 and elements[i-1].tag == f"{{{namespaces['text']}}}p":
                p_text = get_text_from_element(elements[i-1])
                if p_text:
                    title = p_text.strip()
            if table_name:
                tables[table_name] = {"element": elem, "title": title}

    parsed_tables = {}
    for name, table_info in tables.items():
        parsed_tables[name] = parse_table(table_info['element'], namespaces, list_styles)

    lookups = {}
    for table_name, table_info in tables.items():
        title = table_info['title']
        if title and 'รายการที่' in title:
            table_data = parsed_tables.get(table_name)
            if table_data and len(table_data) > 1:
                header = table_data[0]
                options = [dict(zip(header, row)) for row in table_data[1:]]
                
                match = re.search(r'\((.*?)\)', title)
                if match:
                    technical_name = match.group(1).strip()
                    lookups[technical_name] = options
                
                cleaned_title = re.sub(r'\s*\([^)]*\)', '', title).strip()
                lookups[title] = options
                lookups[cleaned_title] = options

    main_table_data = parsed_tables.get('Table1')
    if not main_table_data:
        print("Error: Main table 'Table1' not found.")
        return

    header = main_table_data[0]
    main_metadata = {}

    for row in main_table_data[1:]:
        if not any(row):
            continue
        row_dict = dict(zip(header, row))
        technical_name = row_dict.get('ชื่อทางเทคนิค')
        if technical_name:
            technical_name = re.sub(r'\s+', '', technical_name)
            
            main_metadata[technical_name] = {
                "ลำดับ": row_dict.get("ลำดับ"),
                "ชื่อรายการไทย": row_dict.get("ชื่อรายการไทย"),
                "คำอธิบาย": row_dict.get("คำอธิบาย"),
                "ตัวเลือก/รูปแบบ": row_dict.get("ตัวเลือก/รูปแบบ"),
                "ตัวอย่าง": row_dict.get("ตัวอย่าง"),
            }
            
            if technical_name in lookups:
                main_metadata[technical_name]['options'] = lookups[technical_name]
            else:
                options_text = row_dict.get("ตัวเลือก/รูปแบบ", "")
                match = re.search(r'“([^”]+)”', options_text)
                if match:
                    lookup_key = match.group(1).strip().replace('\n', ' ')
                    lookup_key = re.sub(r'\s+', ' ', lookup_key)
                    
                    for key, value in lookups.items():
                        cleaned_key = re.sub(r'\s*\([^)]*\)', '', key).strip()
                        cleaned_key = re.sub(r'\s+', ' ', cleaned_key)
                        if lookup_key == cleaned_key:
                            main_metadata[technical_name]['options'] = value
                            break

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(main_metadata, f, ensure_ascii=False, indent=2)

    print(f"Successfully converted {xml_file} to {json_file}")

if __name__ == '__main__':
    main()
