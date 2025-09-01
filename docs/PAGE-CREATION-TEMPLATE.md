# Page Creation Template - Thailand Data Standards Portal

Use this template when creating new single-page HTML applications for the project.

## Quick Start Checklist

### 1. File Setup
- [ ] Create new `.html` file with descriptive name
- [ ] Copy base template structure
- [ ] Update page title and meta description
- [ ] Add page-specific data source references

### 2. Required Dependencies
```html
<!-- Essential CDN Dependencies -->
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

### 3. Base HTML Structure Template
```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] - Thailand Data Standards</title>
    
    <!-- CDN Dependencies -->
    [Add dependencies here]
    
    <style>
        body { font-family: 'Noto Sans Thai', sans-serif; }
        .fade-in { opacity: 0; transform: translateY(20px); }
        .header-gradient { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .card-gradient { background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.8) 100%); backdrop-filter: blur(10px); }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 min-h-screen">
    <div id="app">
        <!-- Header Section -->
        <header class="header-gradient text-white shadow-2xl">
            <!-- Header content -->
        </header>

        <!-- Main Content -->
        <main class="container mx-auto px-6 py-8">
            <!-- Page content -->
        </main>
    </div>

    <script type="module">
        const { createApp, ref, computed, onMounted } = Vue;

        createApp({
            setup() {
                // Reactive data
                
                // Computed properties
                
                // Methods
                
                // Lifecycle
                onMounted(() => {
                    // GSAP animations
                });
                
                return {
                    // Expose to template
                };
            }
        }).mount('#app');
    </script>
</body>
</html>
```

## Specific Page Examples

### metadata-standard.html - Current Implementation

This page demonstrates all the key patterns:

#### 1. Data Management Pattern
```javascript
// Source data reference
const metadataItems = ref([
    // Data extracted from data/metadata_std.xml
]);

// Dynamic categorization
const categories = computed(() => {
    const cats = [...new Set(metadataItems.value.map(item => item.category))];
    return cats.sort();
});

// Search and filter logic
const filteredMetadata = computed(() => {
    return metadataItems.value.filter(item => {
        const matchesSearch = /* search logic */;
        const matchesCategory = /* category logic */;
        return matchesSearch && matchesCategory;
    });
});
```

#### 2. UI Component Pattern
```javascript
// Modal management
const selectedItem = ref(null);
const selectItem = (item) => selectedItem.value = item;
const closeModal = () => selectedItem.value = null;

// Filter controls
const searchQuery = ref('');
const selectedCategory = ref('');
const clearFilters = () => {
    searchQuery.value = '';
    selectedCategory.value = '';
};
```

#### 3. Animation Pattern
```javascript
onMounted(() => {
    // Coordinated page load animation
    const fadeElements = document.querySelectorAll('.fade-in');
    gsap.fromTo(fadeElements, 
        { opacity: 0, y: 20 }, 
        { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power2.out" }
    );

    // Special effects for specific elements
    gsap.fromTo('.stat-card', 
        { scale: 0.8, opacity: 0 }, 
        { scale: 1, opacity: 1, duration: 0.6, stagger: 0.1, delay: 0.5, ease: "back.out(1.7)" }
    );
});
```

## Creating New Pages - Step by Step

### Step 1: Plan Your Data Structure
1. **Identify data source** (XML, JSON, CSV in `/data/` folder)
2. **Define data schema** (what fields each item has)
3. **Plan categories/groupings** for filtering
4. **Design search strategy** (which fields to search)

Example for a new "api-standards.html":
```javascript
const apiStandards = ref([
    {
        id: '1',
        name: 'REST API Standard',
        category: 'API Design',
        description: 'Standard for REST API implementation',
        version: '1.0',
        status: 'Active',
        examples: ['GET /api/v1/users', 'POST /api/v1/users']
    }
]);
```

### Step 2: Implement Core Features
1. **Search functionality** across relevant fields
2. **Category filtering** with computed categories
3. **Statistics dashboard** showing data overview
4. **Detail view/modal** for individual items

### Step 3: Add Visual Design
1. **Header section** with gradient background
2. **Statistics cards** with animated numbers
3. **Data table/grid** with hover effects
4. **Modal overlays** for detailed views
5. **Responsive layout** for mobile devices

### Step 4: Implement Animations
1. **Page load sequence** using GSAP timelines
2. **Hover interactions** with CSS transitions
3. **Data transitions** when filtering/searching
4. **Modal open/close** animations

### Step 5: Test and Optimize
1. **Cross-browser testing** (Chrome, Firefox, Safari, Edge)
2. **Mobile responsiveness** testing
3. **Performance validation** (check frame rates)
4. **Accessibility testing** (keyboard navigation, screen readers)

## Page-Specific Guidelines

### For Data-Heavy Pages
- Use virtual scrolling for >500 items
- Implement debounced search
- Consider pagination or infinite scroll
- Add loading states for slow operations

### For Interactive Visualizations
- Use D3.js for data binding and SVG generation
- Coordinate D3 transitions with GSAP animations
- Implement proper cleanup in Vue lifecycle
- Consider canvas for high-performance graphics

### For Form-Heavy Pages
- Use Vue's form binding (`v-model`)
- Implement client-side validation
- Add proper error states and messaging
- Consider form persistence in localStorage

### For Dashboard-Style Pages
- Create reusable chart components
- Implement real-time data updates
- Use consistent color schemes
- Add export functionality (PDF, Excel)

## Maintenance Workflows

### Adding New Data
1. **Update source file** in `/data/` folder
2. **Extract relevant data** into JavaScript array
3. **Update categories** if new ones are introduced
4. **Test search and filter** functionality
5. **Update statistics** if needed

### Modifying Existing Features
1. **Test current functionality** before changes
2. **Make incremental changes** and test frequently
3. **Update animations** if layout changes
4. **Verify mobile responsiveness** after changes
5. **Update documentation** if public APIs change

### Performance Optimization
1. **Profile with browser dev tools** (Performance tab)
2. **Check for memory leaks** (Memory tab)
3. **Optimize large datasets** with virtual scrolling
4. **Compress images** and use modern formats
5. **Monitor Core Web Vitals** with Lighthouse

## Quality Assurance

### Code Quality Checklist
- [ ] No console errors or warnings
- [ ] Proper Vue.js reactivity patterns
- [ ] Consistent code formatting
- [ ] Meaningful variable names
- [ ] Proper error handling

### Performance Checklist
- [ ] Page loads in <3 seconds
- [ ] Animations run at 60fps
- [ ] No layout thrashing
- [ ] Efficient DOM updates
- [ ] Proper resource cleanup

### Accessibility Checklist
- [ ] Keyboard navigation works
- [ ] Screen reader compatibility
- [ ] Proper heading hierarchy
- [ ] Sufficient color contrast
- [ ] Focus management in modals

### Browser Compatibility
- [ ] Chrome (latest 2 versions)
- [ ] Firefox (latest 2 versions)
- [ ] Safari (latest 2 versions)
- [ ] Edge (latest 2 versions)
- [ ] Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment Preparation

### Pre-deployment Checklist
- [ ] Remove development comments
- [ ] Verify all CDN links are production-ready
- [ ] Test with production data
- [ ] Validate HTML markup
- [ ] Check for broken links
- [ ] Verify meta tags and SEO elements

### Production Considerations
- [ ] Enable gzip compression
- [ ] Set proper cache headers
- [ ] Implement Content Security Policy
- [ ] Add error tracking (Sentry, etc.)
- [ ] Set up monitoring and analytics

## Version Control Best Practices

### Commit Messages
```
feat: add new data visualization to dashboard
fix: resolve mobile layout issue in metadata table
docs: update developer guide with new patterns
style: improve color contrast for accessibility
refactor: optimize search performance
```

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch for new features
- `feature/[name]`: Individual feature branches
- `hotfix/[issue]`: Critical bug fixes

### File Organization
Keep related files together:
```
new-feature.html          # Main page
data/new-feature-data.xml # Source data
docs/new-feature.md       # Documentation
```

---

This template provides a comprehensive foundation for creating and maintaining new single-page HTML applications in the Thailand Data Standards Portal project. Each new page should follow these patterns while adapting to its specific requirements.