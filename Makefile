
.PHONY: all clean

# Variables
PYTHON = python3
SCRIPT = convert.py
XML_FILE = data/metadata_std.xml
JSON_FILE = data/metadata_std.json

# Default target
all: $(JSON_FILE)

# Rule to convert XML to JSON
$(JSON_FILE): $(XML_FILE) $(SCRIPT)
	@echo "Converting XML to JSON..."
	$(PYTHON) $(SCRIPT)

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -f $(JSON_FILE)

help:
	@echo "Available commands:"
	@echo "  make        - Converts the XML data to JSON (default)"
	@echo "  make all    - Same as 'make'"
	@echo "  make clean  - Removes the generated JSON file"
	@echo "  make help   - Shows this help message"

# Explicitly declare phony targets
.PHONY: all clean help
