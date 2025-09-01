# Developer Guide - Thailand Data Standards Portal

This guide will help new developers understand, maintain, and extend the single-page HTML applications in this project. Each page is a self-contained application using modern web technologies.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Architecture Patterns](#architecture-patterns)
4. [Page-Specific Guides](#page-specific-guides)
5. [Development Workflow](#development-workflow)
6. [Troubleshooting](#troubleshooting)
7. [Deployment](#deployment)

## Project Overview

This project creates data-driven, animated web experiences for Thailand government data standards using single-file HTML applications. Each page is completely self-contained with no build process required.

### Key Principles
- **Zero Build Tools**: Everything runs directly in the browser
- **CDN Dependencies**: All libraries loaded from reliable CDNs
- **Responsive Design**: Mobile-first approach using Tailwind CSS
- **Interactive Animations**: Smooth user experiences with GSAP
- **Thai Language Support**: Proper typography and text rendering

### Project Structure
```
ds-gsite/
├── AGENTS.md                  # Project specifications
├── DEVELOPER-GUIDE.md         # This guide
├── metadata-standard.html     # Metadata standards page
├── data/
│   ├── metadata_std.xml      # Source data for metadata standards
│   └── [other data files]
├── assets/
│   ├── images/
│   └── fonts/
└── docs/
    └── [documentation files]
```

## Technology Stack

### Core Technologies
- **Vue.js 3**: Reactive UI framework with Composition API
- **Tailwind CSS**: Utility-first CSS framework
- **D3.js**: Data manipulation and SVG generation
- **GSAP**: High-performance animations

### CDN Dependencies
```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Vue.js 3 -->
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

<!-- D3.js -->
<script src="https://d3js.org/d3.v7.min.js"></script>

<!-- GSAP -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
```

### Font Dependencies
```html
<!-- Google Fonts for Thai Language Support -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

## Architecture Patterns

### 1. Component Organization
Each page uses Vue 3 Composition API for reactive data management:

```javascript
const { createApp, ref, computed, onMounted } = Vue;

createApp({
    setup() {
        // Reactive data
        const searchQuery = ref('');
        const selectedCategory = ref('');
        
        // Computed properties
        const filteredData = computed(() => {
            // Filter logic here
        });
        
        // Lifecycle hooks
        onMounted(() => {
            // Animation setup
        });
        
        return {
            // Expose to template
        };
    }
}).mount('#app');
```

### 2. Data Flow Pattern
- **Reactive Sources**: Use `ref()` for primitive values, `reactive()` for objects
- **Computed Properties**: For derived data and filtering
- **Event Handlers**: For user interactions
- **Lifecycle Hooks**: For setup and cleanup

### 3. Styling Pattern
- **Utility Classes**: Prefer Tailwind utilities over custom CSS
- **Component Classes**: Create reusable class combinations
- **Responsive Design**: Mobile-first breakpoints
- **Dark Mode**: Consider dark mode variants

### 4. Animation Pattern
- **Page Load**: GSAP timeline for coordinated animations
- **User Interactions**: Smooth transitions for state changes
- **Data Updates**: Animate data changes with D3.js + GSAP

## Page-Specific Guides

## metadata-standard.html

### Overview
Displays Thailand government metadata standards extracted from XML data with interactive search, filtering, and detailed views.

### Data Structure
The page uses a hardcoded array of metadata items extracted from `data/metadata_std.xml`:

```javascript
const metadataItems = ref([
    {
        id: '1',
        nameThai: 'ประเภทข้อมูล',
        technicalName: 'data_type',
        description: 'ชุดข้อมูลนี้เป็นข้อมูลประเภทใด',
        format: 'ตัวเลือก ดูรายละเอียด...',
        example: 'ข้อมูลสถิติ',
        category: 'ข้อมูลพื้นฐาน'
    },
    // ... more items
]);
```

### Key Components

#### 1. Search and Filter System
```javascript
const filteredMetadata = computed(() => {
    return metadataItems.value.filter(item => {
        const matchesSearch = searchQuery.value === '' || 
            item.nameThai.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            item.technicalName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
            item.description.toLowerCase().includes(searchQuery.value.toLowerCase());
        
        const matchesCategory = selectedCategory.value === '' || 
            item.category === selectedCategory.value;
        
        return matchesSearch && matchesCategory;
    });
});
```

#### 2. Statistics Dashboard
```javascript
const statistics = computed(() => [
    { label: 'รายการทั้งหมด', value: metadataItems.value.length },
    { label: 'หมวดหมู่', value: categories.value.length },
    // ... more stats
]);
```

#### 3. Modal System
```javascript
const selectItem = (item) => {
    selectedItem.value = item;
};

const closeModal = () => {
    selectedItem.value = null;
};
```

### Maintenance Tasks

#### Adding New Metadata Items
1. **Update the XML file** (`data/metadata_std.xml`)
2. **Extract new data** and add to `metadataItems` array:
```javascript
{
    id: 'new_id',
    nameThai: 'ชื่อภาษาไทย',
    technicalName: 'technical_name',
    description: 'คำอธิบาย',
    format: 'รูปแบบข้อมูล',
    example: 'ตัวอย่าง',
    category: 'หมวดหมู่'
}
```

#### Updating Categories
Categories are automatically computed from the data:
```javascript
const categories = computed(() => {
    const cats = [...new Set(metadataItems.value.map(item => item.category))];
    return cats.sort();
});
```

#### Modifying Search Logic
To add new searchable fields, update the filter function:
```javascript
const matchesSearch = searchQuery.value === '' || 
    item.nameThai.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.technicalName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.newField.toLowerCase().includes(searchQuery.value.toLowerCase()); // Add new field
```

#### Styling Updates
The page uses a gradient theme with glassmorphism effects:
```css
.header-gradient { 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
}
.card-gradient { 
    background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.8) 100%); 
    backdrop-filter: blur(10px); 
}
```

#### Animation Customization
Page load animations are controlled by GSAP:
```javascript
onMounted(() => {
    // Fade in elements
    const fadeElements = document.querySelectorAll('.fade-in');
    gsap.fromTo(fadeElements, 
        { opacity: 0, y: 20 }, 
        { opacity: 1, y: 0, duration: 0.8, stagger: 0.1, ease: "power2.out" }
    );

    // Animate statistics cards
    gsap.fromTo('.stat-card', 
        { scale: 0.8, opacity: 0 }, 
        { scale: 1, opacity: 1, duration: 0.6, stagger: 0.1, delay: 0.5, ease: "back.out(1.7)" }
    );
});
```

### Performance Considerations
- **Virtual Scrolling**: For large datasets (>1000 items), consider implementing virtual scrolling
- **Debounced Search**: Add debouncing to search input for better performance
- **Lazy Loading**: Load images and heavy content on demand

### Accessibility Features
- **Keyboard Navigation**: Ensure all interactive elements are keyboard accessible
- **Screen Reader Support**: Use proper ARIA labels and semantic HTML
- **Color Contrast**: Maintain WCAG AA compliance
- **Focus Management**: Proper focus handling in modals

## Development Workflow

### 1. Setting Up Development Environment
No build tools required! Simply:
1. Open the HTML file in a modern browser
2. Use browser dev tools for debugging
3. Test across different devices and browsers

### 2. Making Changes
1. **Edit the HTML file** directly
2. **Refresh the browser** to see changes
3. **Test functionality** thoroughly
4. **Validate HTML** and check console for errors

### 3. Testing Checklist
- [ ] Page loads without errors
- [ ] All animations work smoothly
- [ ] Search and filter functions correctly
- [ ] Modal opens and closes properly
- [ ] Responsive design works on mobile
- [ ] Thai text renders correctly
- [ ] Performance is acceptable (60fps animations)

### 4. Version Control
Use Git for version control:
```bash
git add metadata-standard.html
git commit -m "feat: add new metadata field"
git push origin main
```

## Troubleshooting

### Common Issues

#### 1. CDN Loading Failures
**Problem**: External libraries fail to load
**Solution**: 
- Check internet connection
- Verify CDN URLs are correct and current
- Consider local fallbacks for critical libraries

#### 2. Thai Font Rendering Issues
**Problem**: Thai text displays incorrectly
**Solution**:
- Ensure Google Fonts link is correct
- Check font-family CSS is applied
- Verify browser supports the font

#### 3. Animation Performance Issues
**Problem**: Animations are choppy or slow
**Solution**:
- Use `transform` and `opacity` for animations
- Avoid animating layout properties
- Use `will-change` CSS property sparingly
- Test on lower-end devices

#### 4. Mobile Responsiveness Issues
**Problem**: Layout breaks on mobile devices
**Solution**:
- Use Tailwind responsive prefixes (`sm:`, `md:`, `lg:`)
- Test with browser dev tools device emulation
- Ensure touch targets are at least 44px

#### 5. Vue.js Reactivity Issues
**Problem**: Data updates don't reflect in UI
**Solution**:
- Use `ref()` or `reactive()` for reactive data
- Avoid direct array/object mutations
- Use Vue dev tools for debugging

### Debug Tools
- **Vue DevTools**: Browser extension for Vue debugging
- **Browser Dev Tools**: Network, Performance, and Console tabs
- **Lighthouse**: For performance and accessibility audits

## Deployment

### 1. Static Hosting
Since these are static HTML files, you can deploy to:
- **GitHub Pages**
- **Netlify**
- **Vercel**
- **AWS S3 + CloudFront**

### 2. Server Configuration
No special server configuration required. Ensure:
- **HTTPS**: Use SSL certificates
- **Compression**: Enable gzip/brotli compression
- **Caching**: Set appropriate cache headers for static assets

### 3. Performance Optimization
- **Minification**: Consider minifying HTML for production
- **CDN**: Use CDNs for better global performance
- **Preloading**: Preload critical fonts and resources

### 4. Monitoring
- **Error Tracking**: Implement error tracking (e.g., Sentry)
- **Analytics**: Add web analytics (e.g., Google Analytics)
- **Performance Monitoring**: Monitor Core Web Vitals

## Best Practices

### Code Organization
1. **Consistent Structure**: Follow the established HTML structure pattern
2. **Clear Naming**: Use descriptive variable and function names
3. **Comments**: Add comments for complex logic
4. **Separation of Concerns**: Keep styling, logic, and data separate

### Performance
1. **Optimize Images**: Use WebP format when possible
2. **Minimize Reflows**: Batch DOM updates
3. **Efficient Selectors**: Use specific CSS selectors
4. **Memory Management**: Clean up event listeners and observers

### Security
1. **Content Security Policy**: Implement CSP headers
2. **Input Validation**: Validate and sanitize user inputs
3. **XSS Prevention**: Use Vue's built-in XSS protection
4. **HTTPS Only**: Serve over HTTPS in production

### Accessibility
1. **Semantic HTML**: Use proper HTML elements
2. **ARIA Labels**: Add ARIA attributes where needed
3. **Keyboard Navigation**: Ensure full keyboard accessibility
4. **Color Contrast**: Maintain sufficient color contrast ratios

## Getting Help

### Resources
- **Vue.js Docs**: https://vuejs.org/guide/
- **Tailwind CSS Docs**: https://tailwindcss.com/docs
- **GSAP Docs**: https://greensock.com/docs/
- **D3.js Docs**: https://d3js.org/

### Community
- **Vue.js Discord**: https://discord.com/invite/vue
- **Stack Overflow**: Tag questions with relevant technology tags
- **GitHub Issues**: Report bugs and request features

### Contact
For project-specific questions, contact the development team or create an issue in the project repository.

---

*Last updated: $(date)*
*Version: 1.0*