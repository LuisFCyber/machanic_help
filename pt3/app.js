// DOM Elements
const carListEl = document.getElementById('car-list');
const welcomeStateEl = document.getElementById('welcome-state');
const carDetailStateEl = document.getElementById('car-detail-state');
const carImageEl = document.getElementById('car-image');
const carTitleEl = document.getElementById('car-title');
const carDescriptionEl = document.getElementById('car-description');
const categoryFiltersEl = document.getElementById('category-filters');
const partsGridEl = document.getElementById('parts-grid');
const searchInput = document.getElementById('search-input');
const noResultsEl = document.getElementById('no-results');

// State
let selectedCarId = null;
let selectedCategory = 'Todas';
let searchQuery = '';

// Initialize
function init() {
    renderCarList();
    setupEventListeners();
}

const carSearchInput = document.getElementById('car-search-input');

// Render the sidebar car list grouped by brand
function renderCarList(filterText = '') {
    const sidebarMenu = document.getElementById('sidebar-menu');
    sidebarMenu.innerHTML = '';
    
    // Get unique brands
    const brands = [...new Set(window.database.map(c => c.brand))];
    const normalizedFilter = filterText.toLowerCase().trim();
    
    brands.forEach(brand => {
        const brandCars = window.database.filter(c => c.brand === brand && c.name.toLowerCase().includes(normalizedFilter));
        
        if (normalizedFilter !== '' && brandCars.length === 0) return;

        const brandGroup = document.createElement('div');
        brandGroup.className = 'brand-group';
        
        const brandLabel = document.createElement('div');
        brandLabel.className = 'menu-label';
        
        const isSelectedBrand = brandCars.some(c => c.id === selectedCarId);
        const shouldBeOpen = normalizedFilter !== '' || isSelectedBrand;
        
        if (!shouldBeOpen) {
            brandLabel.classList.add('collapsed');
        }

        brandLabel.innerHTML = `<span>${brand}</span> <i class="fa-solid fa-chevron-down"></i>`;
        
        const ul = document.createElement('ul');
        ul.className = `car-list ${shouldBeOpen ? '' : 'collapsed'}`;
        
        brandLabel.addEventListener('click', () => {
            brandLabel.classList.toggle('collapsed');
            ul.classList.toggle('collapsed');
        });

        brandCars.forEach(car => {
            const li = document.createElement('li');
            li.className = `car-item ${selectedCarId === car.id ? 'active' : ''}`;
            li.innerHTML = `
                <i class="fa-solid fa-car-side"></i>
                <span>${car.name}</span>
            `;
            li.addEventListener('click', () => selectCar(car.id));
            ul.appendChild(li);
        });
        
        brandGroup.appendChild(brandLabel);
        brandGroup.appendChild(ul);
        sidebarMenu.appendChild(brandGroup);
    });

    if (sidebarMenu.innerHTML === '') {
        sidebarMenu.innerHTML = '<p style="color:var(--text-tertiary); font-size:12px; text-align:center; margin-top: 20px;">Nenhum veículo encontrado.</p>';
    }
}

// Select a car and show its details
function selectCar(carId) {
    selectedCarId = carId;
    selectedCategory = 'Todas'; // Reset category filter
    searchQuery = ''; // Reset search
    searchInput.value = '';
    
    renderCarList(); // Update active class
    
    const car = window.database.find(c => c.id === carId);
    if (!car) return;

    // Update UI
    welcomeStateEl.classList.add('hidden');
    carDetailStateEl.classList.remove('hidden');
    
    carImageEl.src = car.image;
    carTitleEl.textContent = car.name;
    carDescriptionEl.textContent = car.description;

    renderCategoryFilters(car);
    renderPartsGrid();
}

// Render Category Filters
function renderCategoryFilters(car) {
    categoryFiltersEl.innerHTML = '';
    
    // Get unique categories
    const categories = ['Todas', ...new Set(car.parts.map(p => p.category))];
    
    categories.forEach(category => {
        const btn = document.createElement('button');
        btn.className = `filter-btn ${selectedCategory === category ? 'active' : ''}`;
        btn.textContent = category;
        btn.addEventListener('click', () => {
            selectedCategory = category;
            
            // Update active class on buttons
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            renderPartsGrid();
        });
        categoryFiltersEl.appendChild(btn);
    });
}

// Render Parts Grid based on filters
function renderPartsGrid() {
    partsGridEl.innerHTML = '';
    const car = window.database.find(c => c.id === selectedCarId);
    if (!car) return;

    let filteredParts = car.parts;

    // Apply category filter
    if (selectedCategory !== 'Todas') {
        filteredParts = filteredParts.filter(p => p.category === selectedCategory);
    }

    // Apply search filter
    if (searchQuery) {
        const query = searchQuery.toLowerCase();
        filteredParts = filteredParts.filter(p => 
            p.name.toLowerCase().includes(query) || 
            p.originalCode.toLowerCase().includes(query) ||
            p.compatibles.some(c => c.code.toLowerCase().includes(query) || c.brand.toLowerCase().includes(query))
        );
    }

    if (filteredParts.length === 0) {
        partsGridEl.classList.add('hidden');
        noResultsEl.classList.remove('hidden');
        return;
    }

    partsGridEl.classList.remove('hidden');
    noResultsEl.classList.add('hidden');

    filteredParts.forEach(part => {
        const card = document.createElement('div');
        card.className = 'part-card';
        
        const compatiblesHTML = part.compatibles.map(comp => `
            <div class="compat-item">
                <span class="compat-brand">${comp.brand}</span>
                <span class="compat-code">${comp.code}</span>
            </div>
        `).join('');

        const compatibleCarsHTML = part.compatibleCars && part.compatibleCars.length > 0 ? `
            <div class="discreet-compat">
                <i class="fa-solid fa-car-on"></i> Serve também em: <span>${part.compatibleCars.join(', ')}</span>
            </div>
        ` : '';

        card.innerHTML = `
            <div class="part-header">
                <div>
                    <h3 class="part-title">${part.name}</h3>
                    <span class="part-category">${part.category}</span>
                </div>
                <i class="fa-solid fa-gear" style="color: var(--text-tertiary); opacity: 0.5; font-size: 20px;"></i>
            </div>
            
            <div class="original-code">
                <span class="code-label">Código Original da Montadora</span>
                <span class="code-value">${part.originalCode}</span>
            </div>
            
            ${compatibleCarsHTML}

            <div class="cross-reference">
                <h4><i class="fa-solid fa-code-compare"></i> Marcas Compatíveis</h4>
                <div class="compat-list">
                    ${compatiblesHTML}
                </div>
            </div>
        `;
        
        partsGridEl.appendChild(card);
    });
}

// Event Listeners
function setupEventListeners() {
    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value;
        if (selectedCarId) {
            renderPartsGrid();
        }
    });

    carSearchInput.addEventListener('input', (e) => {
        renderCarList(e.target.value);
    });
}

// Run
init();
