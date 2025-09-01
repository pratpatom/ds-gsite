# Thailand Data Standards Portal

A collection of powerful single-page HTML applications for displaying and managing Thailand government data standards. Built with modern web technologies for optimal performance and user experience.

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd ds-gsite
   ```

2. **Open any HTML file in a browser**
   ```bash
   # No build process required!
   open metadata-standard.html
   ```

3. **Start developing**
   - Edit HTML files directly
   - Refresh browser to see changes
   - Use browser dev tools for debugging

## 📁 Project Structure

```
ds-gsite/
├── metadata-standard.html         # Metadata standards viewer
├── DEVELOPER-GUIDE.md            # Comprehensive developer guide
├── AGENTS.md                     # Project specifications
├── data/
│   ├── metadata_std.xml         # Source data for metadata standards
│   └── [other data files]
├── docs/
│   ├── PAGE-CREATION-TEMPLATE.md # Template for new pages
│   ├── QUICK-REFERENCE.md        # Common maintenance tasks
│   └── [other documentation]
├── assets/
│   ├── images/
│   └── fonts/
└── README.md                     # This file
```

## 🎯 Current Pages

### metadata-standard.html
Interactive viewer for Thailand government metadata standards.

**Features:**
- ✅ Real-time search across all fields
- ✅ Category-based filtering
- ✅ Interactive statistics dashboard
- ✅ Detailed modal views
- ✅ Responsive design
- ✅ Smooth animations
- ✅ Thai language support

**Data Source:** `data/metadata_std.xml`

**Tech Stack:** Vue.js 3 + Tailwind CSS + GSAP + D3.js

## 🛠 Technology Stack

- **Vue.js 3** - Reactive UI framework with Composition API
- **Tailwind CSS** - Utility-first CSS framework
- **GSAP** - High-performance animations
- **D3.js** - Data manipulation and visualization
- **Google Fonts** - Thai language typography

All dependencies are loaded via CDN - no build tools required!

## 📚 Documentation

### For New Developers
- 📖 **[DEVELOPER-GUIDE.md](DEVELOPER-GUIDE.md)** - Complete guide to the project
- 🎯 **[QUICK-REFERENCE.md](docs/QUICK-REFERENCE.md)** - Common maintenance tasks
- 📋 **[PAGE-CREATION-TEMPLATE.md](docs/PAGE-CREATION-TEMPLATE.md)** - Template for new pages

### Project Specifications
- 📋 **[AGENTS.md](AGENTS.md)** - Architecture patterns and standards

## 🔧 Development Workflow

### Making Changes
1. **Edit HTML files** directly in your favorite editor
2. **Test in browser** - refresh to see changes
3. **Use browser dev tools** for debugging
4. **Test across devices** using browser dev tools
5. **Commit changes** with descriptive messages

### Adding New Pages
1. **Follow the template** in `docs/PAGE-CREATION-TEMPLATE.md`
2. **Use consistent patterns** from existing pages
3. **Update documentation** as needed
4. **Test thoroughly** before deployment

### Common Tasks

#### Adding Data to metadata-standard.html
```javascript
// Add to metadataItems array
{
    id: '16',
    nameThai: 'ชื่อรายการใหม่',
    technicalName: 'new_technical_name',
    description: 'คำอธิบายรายละเอียด',
    format: 'รูปแบบข้อมูล',
    example: 'ตัวอย่าง',
    category: 'หมวดหมู่'
}
```

#### Updating Search Fields
```javascript
// Modify filteredMetadata computed property
const matchesSearch = searchQuery.value === '' || 
    item.nameThai.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.technicalName.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    item.newField.toLowerCase().includes(searchQuery.value.toLowerCase()); // New field
```

#### Customizing Animations
```javascript
// Adjust GSAP animations in onMounted()
gsap.fromTo('.fade-in', 
    { opacity: 0, y: 20 }, 
    { opacity: 1, y: 0, duration: 0.8, stagger: 0.1 }
);
```

## 🎨 Design Principles

### Visual Design
- **Gradient themes** with glassmorphism effects
- **Consistent color scheme** using Tailwind's palette
- **Thai typography** with Noto Sans Thai font
- **Responsive layout** with mobile-first approach

### User Experience
- **Smooth animations** for all interactions
- **Real-time feedback** for search and filters
- **Accessible design** with keyboard navigation
- **Performance optimization** for smooth 60fps

### Code Organization
- **Single-file applications** for simplicity
- **Vue 3 Composition API** for reactive data
- **Computed properties** for derived data
- **GSAP timelines** for coordinated animations

## 🚀 Deployment

### Static Hosting Options
- **GitHub Pages** - Free hosting for public repos
- **Netlify** - Easy drag-and-drop deployment
- **Vercel** - Automatic deployments from Git
- **AWS S3 + CloudFront** - Scalable hosting

### Production Checklist
- [ ] Test all functionality
- [ ] Validate HTML markup
- [ ] Check mobile responsiveness
- [ ] Verify CDN links work
- [ ] Test loading performance
- [ ] Enable compression and caching

## 🐛 Troubleshooting

### Common Issues

#### Page Won't Load
- Check browser console for errors
- Verify CDN links are accessible
- Ensure proper HTML structure

#### Animations Are Choppy
- Use `transform` and `opacity` for animations
- Avoid animating layout properties
- Test on lower-end devices

#### Thai Text Not Displaying
- Verify Google Fonts link is working
- Check font-family CSS is applied
- Test with different browsers

### Getting Help
- Check the **[DEVELOPER-GUIDE.md](DEVELOPER-GUIDE.md)** for detailed solutions
- Use browser dev tools for debugging
- Search existing issues before creating new ones

## 🤝 Contributing

### Guidelines
1. **Follow existing patterns** from current pages
2. **Test thoroughly** before submitting
3. **Update documentation** for new features
4. **Use descriptive commit messages**

### Code Style
- Use **consistent indentation** (2 spaces)
- Follow **Vue.js best practices**
- Use **Tailwind utilities** over custom CSS
- Write **clear, descriptive variable names**

### Commit Message Format
```
feat: add new visualization component
fix: resolve mobile layout issue
docs: update developer guide
style: improve color contrast
refactor: optimize search performance
```

## 📄 License

[Add license information here]

## 📞 Contact

[Add contact information here]

---

**Built with ❤️ for Thailand's digital government initiatives**

*Last updated: December 2024*