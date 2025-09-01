# Quick Reference - Common Maintenance Tasks

## metadata-standard.html Maintenance

### Adding New Metadata Items

#### 1. Update Data Array
```javascript
// Add new item to metadataItems array
{
    id: 'new_id',
    nameThai: 'ชื่อภาษาไทย',
    technicalName: 'technical_name',
    description: 'คำอธิบายรายละเอียด',
    format: 'รูปแบบข้อมูล',
    example: 'ตัวอย่างการใช้งาน',
    category: 'หมวดหมู่ใหม่หรือเดิม'
}
```

#### 2. Categories Auto-Update
Categories are computed automatically - no manual update needed!

### Modifying Search Behavior

#### Add New Searchable Fields
```javascript
const filteredMetadata = computed(() => {
    return metadataItems.value.filter(item => {
        const matchesSearch = searchQuery.value === '' || 
            item.nameThai.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            item.technicalName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            item.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            item.newField.toLowerCase().includes(searchQuery.value.toLowerCase()); // ADD THIS LINE
        
        const matchesCategory = selectedCategory.value === '' || 
            item.category === selectedCategory.value;
        
        return matchesSearch && matchesCategory;
    });
});
```

#### Add Search Highlighting
```html
<!-- In table cell -->
<td class="px-6 py-4 font-medium" v-html="highlightSearch(item.nameThai)"></td>
```

```javascript
// Add to methods
const highlightSearch = (text) => {
    if (!searchQuery.value) return text;
    const regex = new RegExp(`(${searchQuery.value})`, 'gi');
    return text.replace(regex, '<mark class="bg-yellow-200">$1</mark>');
};
```

### Customizing Statistics

#### Add New Statistics
```javascript
const statistics = computed(() => [
    { label: 'รายการทั้งหมด', value: metadataItems.value.length },
    { label: 'หมวดหมู่', value: categories.value.length },
    { label: 'ข้อมูลพื้นฐาน', value: metadataItems.value.filter(item => item.category === 'ข้อมูลพื้นฐาน').length },
    { label: 'ข้อมูลเทคนิค', value: metadataItems.value.filter(item => item.category === 'ข้อมูลเทคนิค').length },
    // ADD NEW STATISTICS HERE
    { label: 'รายการใหม่', value: metadataItems.value.filter(item => item.isNew).length }
]);
```

### Animation Modifications

#### Adjust Animation Timing
```javascript
onMounted(() => {
    const fadeElements = document.querySelectorAll('.fade-in');
    gsap.fromTo(fadeElements, 
        { opacity: 0, y: 20 }, 
        { 
            opacity: 1, 
            y: 0, 
            duration: 0.8,    // CHANGE DURATION
            stagger: 0.1,     // CHANGE STAGGER
            ease: "power2.out" // CHANGE EASING
        }
    );
});
```

#### Add New Animation Elements
```html
<!-- Add fade-in class to new elements -->
<div class="new-content fade-in">
    <!-- Content -->
</div>
```

### Styling Updates

#### Color Theme Changes
```css
/* Update gradient colors */
.header-gradient { 
    background: linear-gradient(135deg, #NEW_COLOR_1 0%, #NEW_COLOR_2 100%); 
}

/* Update accent colors */
.text-indigo-600 { color: #NEW_ACCENT_COLOR; }
.bg-indigo-600 { background-color: #NEW_ACCENT_COLOR; }
```

#### Add New Component Styles
```css
.new-component {
    @apply bg-white rounded-xl shadow-lg p-6 transition-all duration-300;
}

.new-component:hover {
    @apply shadow-xl transform scale-105;
}
```

## Common Code Patterns

### Loading States
```javascript
const isLoading = ref(false);
const loadData = async () => {
    isLoading.value = true;
    try {
        // Fetch data
    } finally {
        isLoading.value = false;
    }
};
```

```html
<div v-if="isLoading" class="flex justify-center p-8">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
</div>
```

### Error Handling
```javascript
const error = ref(null);
const handleError = (err) => {
    error.value = err.message;
    console.error('Error:', err);
};
```

```html
<div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
    {{ error }}
</div>
```

### Pagination
```javascript
const currentPage = ref(1);
const itemsPerPage = 10;

const paginatedItems = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return filteredMetadata.value.slice(start, end);
});

const totalPages = computed(() => Math.ceil(filteredMetadata.value.length / itemsPerPage));
```

### Export Functionality
```javascript
const exportToCSV = () => {
    const headers = ['ID', 'ชื่อไทย', 'ชื่อเทคนิค', 'คำอธิบาย'];
    const csvContent = [
        headers.join(','),
        ...filteredMetadata.value.map(item => 
            [item.id, item.nameThai, item.technicalName, item.description].join(',')
        )
    ].join('\n');
    
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'metadata-standards.csv';
    link.click();
    URL.revokeObjectURL(url);
};
```

## Debugging Tips

### Vue DevTools
1. Install Vue DevTools browser extension
2. Open browser DevTools → Vue tab
3. Inspect component data and computed properties
4. Use Time-travel debugging for state changes

### Common Console Commands
```javascript
// Check Vue app instance
document.querySelector('#app').__vue__

// Inspect reactive data
console.log(app.searchQuery)
console.log(app.filteredMetadata)

// Force re-render
app.$forceUpdate()
```

### Performance Debugging
```javascript
// Measure performance
console.time('filter-operation');
// ... filtering code
console.timeEnd('filter-operation');

// Check memory usage
console.log(performance.memory);
```

## Testing Checklist

### Functionality Testing
- [ ] Search works with Thai and English text
- [ ] Category filtering works correctly
- [ ] Modal opens and closes properly
- [ ] Statistics update when data changes
- [ ] Clear filters button resets state

### Responsive Testing
- [ ] Mobile layout (320px width)
- [ ] Tablet layout (768px width)
- [ ] Desktop layout (1024px+ width)
- [ ] Touch interactions work on mobile

### Performance Testing
- [ ] Page load time < 3 seconds
- [ ] Animations run smoothly (60fps)
- [ ] Large datasets don't freeze UI
- [ ] Memory usage stays reasonable

### Accessibility Testing
- [ ] Keyboard navigation works
- [ ] Screen reader announces content
- [ ] Color contrast meets WCAG AA
- [ ] Focus indicators visible

## Emergency Fixes

### Quick Rollback
```bash
# Revert to last working version
git checkout HEAD~1 metadata-standard.html
```

### CDN Fallback
```html
<!-- Add fallback for failed CDN -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
if (!window.Vue) {
    document.write('<script src="./assets/js/vue.global.js"><\/script>');
}
</script>
```

### Quick Performance Fix
```javascript
// Add to setup() for better performance
const searchQuery = ref('');
const debouncedSearch = computed(() => {
    // Debounce search to reduce filtering frequency
    return searchQuery.value;
});

// Use debouncedSearch instead of searchQuery in filter
```

---

Keep this reference handy for quick maintenance tasks! 🚀