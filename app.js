// SAMAR Laptop Choice Portal - Interactive Recommendation Engine & UI Logic

// State Management
const state = {
  budget: 90000,
  isBudgetFlexible: true,
  purpose: 'all',
  processor: 'any',
  ram: 'any',
  storage: 'any',
  brand: 'all',
  searchQuery: '',
  sortBy: 'samar-match',
  compareList: [],
  selectedLaptop: null,
  studentDiscount: false,
  bankOffer: 'none',
  exchangeValue: 0
};

// Purpose configuration
const PURPOSE_CONFIG = {
  coding: {
    label: "Coding & Dev",
    icon: "code",
    desc: "Fast compile, multi-core CPU, 16GB+ RAM, comfortable keyboard"
  },
  gaming: {
    label: "Gaming & Esports",
    icon: "gamepad-2",
    desc: "Dedicated RTX GPU, 144Hz+ display, high GTA 5 & AAA FPS"
  },
  editing: {
    label: "Video & 3D Design",
    icon: "film",
    desc: "100% sRGB/DCI-P3 OLED/IPS, dedicated VRAM, fast export speeds"
  },
  college: {
    label: "College & Daily Use",
    icon: "graduation-cap",
    desc: "Lightweight (<1.7kg), all-day battery (7+ hrs), reliable build"
  },
  ai: {
    label: "AI, ML & Data Science",
    icon: "brain-circuit",
    desc: "16-32GB RAM, NVIDIA CUDA Tensor cores, heavy multi-threading"
  },
  office: {
    label: "Business & Office",
    icon: "briefcase",
    desc: "Snappy multitasking, web meetings, MS Office, high reliability"
  }
};

// Calculate Deal & Discounts
function calculateDiscounts(basePrice) {
  let studentSavings = 0;
  let bankSavings = 0;
  let exchangeSavings = state.exchangeValue || 0;

  if (state.studentDiscount) {
    studentSavings = Math.min(7000, Math.round(basePrice * 0.07));
  }

  if (state.bankOffer === 'hdfc') {
    bankSavings = Math.min(4000, Math.round(basePrice * 0.10));
  } else if (state.bankOffer === 'icici') {
    bankSavings = Math.min(5000, Math.round(basePrice * 0.10));
  } else if (state.bankOffer === 'sbi') {
    bankSavings = Math.min(3500, Math.round(basePrice * 0.10));
  } else if (state.bankOffer === 'axis') {
    bankSavings = Math.min(3000, Math.round(basePrice * 0.10));
  } else if (state.bankOffer === 'instant10') {
    bankSavings = Math.min(5000, Math.round(basePrice * 0.10));
  }

  const totalSavings = studentSavings + bankSavings + exchangeSavings;
  const effectivePrice = Math.max(12000, basePrice - totalSavings);

  return {
    basePrice,
    totalSavings,
    effectivePrice,
    studentSavings,
    bankSavings,
    exchangeSavings,
    hasDiscounts: totalSavings > 0
  };
}

// Calculate Samar Match Score (0 - 100)
function calculateSamarScore(laptop, filters) {
  let score = 50;
  const dealInfo = calculateDiscounts(laptop.price);
  const evaluationPrice = dealInfo.hasDiscounts ? dealInfo.effectivePrice : laptop.price;

  const budget = filters.budget;
  const isFlexible = filters.isBudgetFlexible;
  const maxBudget = isFlexible ? budget * 1.05 : budget;

  // 1. Budget Suitability
  if (evaluationPrice <= budget) {
    const budgetUtilization = evaluationPrice / budget;
    if (budgetUtilization >= 0.75 && budgetUtilization <= 1.0) {
      score += 30;
    } else if (budgetUtilization < 0.75) {
      score += 24;
    }
  } else if (evaluationPrice <= maxBudget) {
    score += 18;
  } else {
    return 0;
  }

  // 2. Purpose Match
  if (filters.purpose && filters.purpose !== 'all') {
    if (laptop.suitableFor.includes(filters.purpose)) {
      score += 25;
    } else {
      score -= 15;
    }

    if (filters.purpose === 'gaming') {
      if (laptop.gpu.type === 'Dedicated') {
        score += 10;
        if (laptop.benchmarkScores && laptop.benchmarkScores.gta5FPS >= 100) score += 8;
      } else {
        score -= 25;
      }
    } else if (filters.purpose === 'college') {
      if (laptop.battery.lifeHours >= 7.5) score += 8;
      if (laptop.weight <= 1.6) score += 7;
      if (laptop.weight > 2.3) score -= 8;
    } else if (filters.purpose === 'coding') {
      if (laptop.ram >= 16) score += 8;
      if (laptop.processor.cores >= 8) score += 7;
    } else if (filters.purpose === 'ai') {
      if (laptop.gpu.type === 'Dedicated' && laptop.gpu.name.includes('NVIDIA')) score += 10;
      if (laptop.ram >= 16) score += 5;
    } else if (filters.purpose === 'editing') {
      if (laptop.display.panel.includes('100%') || laptop.display.panel.includes('OLED')) score += 8;
      if (laptop.gpu.type === 'Dedicated') score += 7;
    }
  } else {
    score += 15;
  }

  // 3. Processor Match
  if (filters.processor !== 'any') {
    const pTier = laptop.processor.tier.toLowerCase();
    const pGen = laptop.processor.generation.toLowerCase();
    const pBrand = laptop.processor.brand.toLowerCase();

    if (filters.processor === 'intel-i3' && pBrand === 'intel' && pTier === 'i3') score += 15;
    else if (filters.processor === 'intel-i5' && pBrand === 'intel' && pTier === 'i5') score += 15;
    else if (filters.processor === 'intel-i7' && pBrand === 'intel' && pTier === 'i7') score += 15;
    else if (filters.processor === 'intel-11th' && pGen.includes('11th')) score += 15;
    else if (filters.processor === 'intel-12th' && pGen.includes('12th')) score += 15;
    else if (filters.processor === 'intel-13th' && pGen.includes('13th')) score += 15;
    else if (filters.processor === 'intel-14th' && (pGen.includes('14th') || pGen.includes('ultra'))) score += 15;
    else if (filters.processor === 'amd-ryzen-3' && pTier.includes('ryzen 3')) score += 15;
    else if (filters.processor === 'amd-ryzen-5' && pTier.includes('ryzen 5')) score += 15;
    else if (filters.processor === 'amd-ryzen-7' && pTier.includes('ryzen 7')) score += 15;
    else if (filters.processor === 'amd-ryzen-all' && pBrand === 'amd') score += 15;
    else if (filters.processor === 'apple-m' && pBrand === 'apple') score += 15;
    else score -= 15;
  }

  // 4. RAM Match
  if (filters.ram !== 'any') {
    const reqRam = parseInt(filters.ram);
    if (laptop.ram === reqRam) score += 10;
    else if (laptop.ram > reqRam) score += 7;
    else score -= 12;
  }

  // 5. Storage Match
  if (filters.storage !== 'any') {
    const reqStorage = parseInt(filters.storage);
    if (laptop.storage >= reqStorage) score += 10;
    else score -= 10;
  }

  // 6. Brand Match
  if (filters.brand !== 'all') {
    if (laptop.brand.toLowerCase() === filters.brand.toLowerCase()) score += 10;
    else score -= 20;
  }

  score += Math.round((laptop.rating - 4.0) * 10);
  return Math.min(99, Math.max(10, score));
}

function formatINR(amount) {
  return "₹" + amount.toLocaleString('en-IN');
}

function formatRAM(gb) {
  return `${gb} GB`;
}

function formatStorage(gb) {
  if (gb >= 1000) {
    return `${gb / 1000} TB SSD`;
  }
  return `${gb} GB SSD`;
}

function getFilteredAndScoredLaptops() {
  const maxBudget = state.isBudgetFlexible ? state.budget * 1.05 : state.budget;

  let results = LAPTOPS_DATA.map(laptop => {
    const score = calculateSamarScore(laptop, state);
    const dealInfo = calculateDiscounts(laptop.price);
    const checkPrice = dealInfo.hasDiscounts ? dealInfo.effectivePrice : laptop.price;

    return {
      ...laptop,
      samarScore: score,
      dealInfo: dealInfo,
      isSlightStretch: checkPrice > state.budget && checkPrice <= maxBudget
    };
  });

  results = results.filter(laptop => {
    const checkPrice = laptop.dealInfo.hasDiscounts ? laptop.dealInfo.effectivePrice : laptop.price;
    if (checkPrice > maxBudget) return false;

    if (state.brand !== 'all' && laptop.brand.toLowerCase() !== state.brand.toLowerCase()) {
      return false;
    }

    if (state.processor !== 'any') {
      const p = laptop.processor;
      if (state.processor === 'intel-i3' && !(p.brand === 'Intel' && p.tier === 'i3')) return false;
      if (state.processor === 'intel-i5' && !(p.brand === 'Intel' && p.tier === 'i5')) return false;
      if (state.processor === 'intel-i7' && !(p.brand === 'Intel' && p.tier === 'i7')) return false;
      if (state.processor === 'intel-11th' && !(p.brand === 'Intel' && p.generation.includes('11th'))) return false;
      if (state.processor === 'intel-12th' && !(p.brand === 'Intel' && p.generation.includes('12th'))) return false;
      if (state.processor === 'intel-13th' && !(p.brand === 'Intel' && p.generation.includes('13th'))) return false;
      if (state.processor === 'intel-14th' && !(p.brand === 'Intel' && (p.generation.includes('14th') || p.generation.includes('Ultra')))) return false;
      if (state.processor === 'amd-ryzen-3' && !(p.brand === 'AMD' && p.tier.includes('3'))) return false;
      if (state.processor === 'amd-ryzen-5' && !(p.brand === 'AMD' && p.tier.includes('5'))) return false;
      if (state.processor === 'amd-ryzen-7' && !(p.brand === 'AMD' && p.tier.includes('7'))) return false;
      if (state.processor === 'amd-ryzen-all' && p.brand !== 'AMD') return false;
      if (state.processor === 'apple-m' && p.brand !== 'Apple') return false;
    }

    if (state.ram !== 'any') {
      const minRam = parseInt(state.ram);
      if (laptop.ram < minRam) return false;
    }

    if (state.storage !== 'any') {
      const minStorage = parseInt(state.storage);
      if (laptop.storage < minStorage) return false;
    }

    if (state.purpose !== 'all') {
      if (!laptop.suitableFor.includes(state.purpose)) return false;
    }

    if (state.searchQuery.trim()) {
      const q = state.searchQuery.toLowerCase();
      const matchName = laptop.name.toLowerCase().includes(q);
      const matchBrand = laptop.brand.toLowerCase().includes(q);
      const matchCPU = laptop.processor.model.toLowerCase().includes(q);
      const matchGPU = laptop.gpu.name.toLowerCase().includes(q);
      const matchGen = laptop.processor.generation.toLowerCase().includes(q);
      if (!matchName && !matchBrand && !matchCPU && !matchGPU && !matchGen) return false;
    }

    return true;
  });

  results.sort((a, b) => {
    if (state.sortBy === 'samar-match') {
      return b.samarScore - a.samarScore;
    } else if (state.sortBy === 'gta-fps') {
      const fpsA = (a.benchmarkScores && a.benchmarkScores.gta5FPS) || 0;
      const fpsB = (b.benchmarkScores && b.benchmarkScores.gta5FPS) || 0;
      return fpsB - fpsA;
    } else if (state.sortBy === 'price-low') {
      const pA = a.dealInfo.hasDiscounts ? a.dealInfo.effectivePrice : a.price;
      const pB = b.dealInfo.hasDiscounts ? b.dealInfo.effectivePrice : b.price;
      return pA - pB;
    } else if (state.sortBy === 'price-high') {
      const pA = a.dealInfo.hasDiscounts ? a.dealInfo.effectivePrice : a.price;
      const pB = b.dealInfo.hasDiscounts ? b.dealInfo.effectivePrice : b.price;
      return pB - pA;
    } else if (state.sortBy === 'rating') {
      return b.rating - a.rating;
    } else if (state.sortBy === 'cpu-power') {
      return b.benchmarkScores.multiCore - a.benchmarkScores.multiCore;
    }
    return 0;
  });

  return results;
}

function renderApp() {
  renderBudgetControls();
  renderPurposeCards();
  renderPresets();
  renderDiscountBar();
  renderResults();
  renderCompareBar();
  lucide.createIcons();
}

function renderDiscountBar() {
  const toggle = document.getElementById('studentDiscountToggle');
  const bankSelect = document.getElementById('bankOfferSelect');
  const exchangeSelect = document.getElementById('exchangeSelect');
  const savingsPill = document.getElementById('globalSavingsPill');
  const savingsVal = document.getElementById('globalSavingsVal');
  const studentTile = document.getElementById('studentTile');

  if (toggle) toggle.checked = state.studentDiscount;
  if (bankSelect) bankSelect.value = state.bankOffer;
  if (exchangeSelect) exchangeSelect.value = state.exchangeValue;

  if (studentTile) {
    if (state.studentDiscount) studentTile.classList.add('active');
    else studentTile.classList.remove('active');
  }

  const rep = calculateDiscounts(state.budget);
  if (savingsPill && savingsVal) {
    if (rep.hasDiscounts) {
      savingsPill.classList.add('has-savings');
      savingsVal.textContent = `Save up to ${formatINR(rep.totalSavings)} Off`;
    } else {
      savingsPill.classList.remove('has-savings');
      savingsVal.textContent = 'No offers applied';
    }
  }
}

function renderBudgetControls() {
  const slider = document.getElementById('budgetSlider');
  const input = document.getElementById('budgetInput');
  const display = document.getElementById('budgetDisplay');
  const stretchCheck = document.getElementById('flexBudgetToggle');

  if (slider) slider.value = state.budget;
  if (input) input.value = state.budget;
  if (display) display.textContent = formatINR(state.budget);
  if (stretchCheck) stretchCheck.checked = state.isBudgetFlexible;
}

function renderPurposeCards() {
  const container = document.getElementById('purposeGrid');
  if (!container) return;

  container.innerHTML = `
    <div class="purpose-card ${state.purpose === 'all' ? 'active' : ''}" data-purpose="all">
      <div class="purpose-icon"><i data-lucide="sparkles"></i></div>
      <div class="purpose-name">All Purposes</div>
      <div class="purpose-desc">Show best balanced laptops for any general workflow</div>
    </div>
    ${Object.entries(PURPOSE_CONFIG).map(([key, item]) => `
      <div class="purpose-card ${state.purpose === key ? 'active' : ''}" data-purpose="${key}">
        <div class="purpose-icon"><i data-lucide="${item.icon}"></i></div>
        <div class="purpose-name">${item.label}</div>
        <div class="purpose-desc">${item.desc}</div>
      </div>
    `).join('')}
  `;

  container.querySelectorAll('.purpose-card').forEach(card => {
    card.addEventListener('click', () => {
      state.purpose = card.dataset.purpose;
      renderApp();
    });
  });
}

function renderPresets() {
  const container = document.getElementById('presetChips');
  if (!container) return;

  container.innerHTML = QUICK_PRESETS.map((preset, idx) => `
    <button class="preset-chip" data-idx="${idx}">
      <i data-lucide="zap"></i>
      <span>${preset.title}</span>
    </button>
  `).join('');

  container.querySelectorAll('.preset-chip').forEach(btn => {
    btn.addEventListener('click', () => {
      const preset = QUICK_PRESETS[btn.dataset.idx];
      state.budget = preset.budget;
      state.purpose = preset.purpose;
      state.processor = preset.processor;
      state.ram = preset.ram;
      state.storage = preset.storage;
      state.brand = preset.brand;
      updateFilterControls();
      renderApp();
    });
  });
}

function updateFilterControls() {
  const procSelect = document.getElementById('processorSelect');
  if (procSelect) procSelect.value = state.processor;

  const ramSelect = document.getElementById('ramSelect');
  if (ramSelect) ramSelect.value = state.ram;

  const storageSelect = document.getElementById('storageSelect');
  if (storageSelect) storageSelect.value = state.storage;

  const brandSelect = document.getElementById('brandSelect');
  if (brandSelect) brandSelect.value = state.brand;

  const searchInput = document.getElementById('searchInput');
  if (searchInput) searchInput.value = state.searchQuery;

  const sortSelect = document.getElementById('sortSelect');
  if (sortSelect) sortSelect.value = state.sortBy;
}

function renderResults() {
  const resultsContainer = document.getElementById('laptopsGrid');
  const countBadge = document.getElementById('resultsCountBadge');
  const spotlightBanner = document.getElementById('spotlightSection');

  if (!resultsContainer) return;

  const results = getFilteredAndScoredLaptops();
  if (countBadge) countBadge.textContent = `${results.length} Laptops Found`;

  if (results.length === 0) {
    spotlightBanner.innerHTML = '';
    spotlightBanner.classList.add('hidden');
    resultsContainer.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon"><i data-lucide="search-x"></i></div>
        <h3>No laptops match your exact criteria</h3>
        <p>Try increasing your budget slightly or switching Processor/RAM to 'Any' to discover options.</p>
        <button class="btn btn-primary" onclick="resetFilters()">
          <i data-lucide="rotate-ccw"></i> Reset Filters
        </button>
      </div>
    `;
    return;
  }

  // Top Recommendation (Winner Spotlight)
  const topPick = results[0];
  if (topPick && spotlightBanner) {
    const deal = topPick.dealInfo;
    const priceDisplay = deal.hasDiscounts ? `
      <div class="spotlight-deal-row">
        <span class="deal-badge-pill">🔥 Effective Deal Price</span>
        <div class="spotlight-price deal-highlight">${formatINR(deal.effectivePrice)}</div>
        <div class="regular-strike">Reg: ${formatINR(topPick.price)}</div>
        <span class="savings-tag">You Save ${formatINR(deal.totalSavings)}</span>
      </div>
    ` : `
      <div class="spotlight-price">${formatINR(topPick.price)}</div>
      <div class="spotlight-orig-price">${formatINR(topPick.originalPrice)}</div>
      <div class="discount-badge">${Math.round((1 - topPick.price / topPick.originalPrice) * 100)}% OFF</div>
    `;

    spotlightBanner.classList.remove('hidden');
    spotlightBanner.innerHTML = `
      <div class="spotlight-card">
        <div class="spotlight-badge">
          <i data-lucide="crown"></i>
          <span>SAMAR'S #1 TOP RECOMMENDATION</span>
        </div>
        <div class="spotlight-body">
          <div class="spotlight-image-col">
            <img src="${topPick.image}" alt="${topPick.name}" class="spotlight-img" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60';" />
            <div class="score-pill">
              <span class="score-num">${topPick.samarScore}%</span>
              <span class="score-label">Samar Match</span>
            </div>
            <div class="spotlight-gta-badge">
              <i data-lucide="gamepad-2"></i> GTA 5: <strong>${topPick.benchmarkScores.gta5FPS} FPS</strong>
            </div>
          </div>
          <div class="spotlight-info-col">
            <div class="spotlight-header">
              <div>
                <span class="brand-pill">${topPick.brand} &bull; ${topPick.processor.generation}</span>
                <h2 class="spotlight-title">${topPick.name}</h2>
              </div>
              <div class="spotlight-price-box">
                ${priceDisplay}
              </div>
            </div>

            <div class="specs-pill-grid">
              <div class="spec-pill"><i data-lucide="cpu"></i><span>${topPick.processor.model}</span></div>
              <div class="spec-pill"><i data-lucide="circuit-board"></i><span>${formatRAM(topPick.ram)} ${topPick.ramType}</span></div>
              <div class="spec-pill"><i data-lucide="hard-drive"></i><span>${formatStorage(topPick.storage)}</span></div>
              <div class="spec-pill gta-spec-pill"><i data-lucide="gamepad-2"></i><span><strong>GTA 5: ${topPick.benchmarkScores.gta5FPS} FPS</strong> (${topPick.benchmarkScores.gta5Settings})</span></div>
              <div class="spec-pill"><i data-lucide="zap"></i><span>${topPick.gpu.name} ${topPick.gpu.tgp ? `(${topPick.gpu.tgp})` : ''}</span></div>
              <div class="spec-pill"><i data-lucide="battery-charging"></i><span>${topPick.battery.lifeHours}h Battery (${topPick.weight} kg)</span></div>
            </div>

            <!-- Quick Direct Store Buy Buttons -->
            <div class="store-links-strip">
              <span class="store-label"><i data-lucide="shopping-bag"></i> Direct Store Links:</span>
              <div class="store-buttons-wrap">
                <a href="${topPick.buyLinks.amazon}" target="_blank" rel="noopener noreferrer" class="store-link-btn store-amazon">
                  <span class="store-icon-tag">a</span> Buy on Amazon
                </a>
                <a href="${topPick.buyLinks.flipkart}" target="_blank" rel="noopener noreferrer" class="store-link-btn store-flipkart">
                  <span class="store-icon-tag">fk</span> Buy on Flipkart
                </a>
                <a href="${topPick.buyLinks.brandStore}" target="_blank" rel="noopener noreferrer" class="store-link-btn store-brand">
                  <i data-lucide="shield-check"></i> ${topPick.buyLinks.brandStoreName}
                </a>
              </div>
            </div>

            <div class="samar-quote">
              <i data-lucide="quote" class="quote-icon"></i>
              <p><strong>Why Samar picked this for you:</strong> ${topPick.samarVerdict}</p>
            </div>

            <div class="spotlight-actions">
              <button class="btn btn-primary" onclick="openDetailsModal('${topPick.id}')">
                <i data-lucide="info"></i> View Full Specs &amp; Discount Calculator
              </button>
              <button class="btn ${isCompared(topPick.id) ? 'btn-secondary active' : 'btn-secondary'}" onclick="toggleCompare('${topPick.id}')">
                <i data-lucide="${isCompared(topPick.id) ? 'check' : 'layers'}"></i>
                ${isCompared(topPick.id) ? 'Added to Compare' : 'Add to Compare'}
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  // Render Grid Cards
  resultsContainer.innerHTML = results.map((laptop, index) => {
    let badgeHtml = '';
    if (index === 0) {
      badgeHtml = `<div class="card-badge badge-winner"><i data-lucide="award"></i> Best Overall</div>`;
    } else if (laptop.price <= state.budget * 0.75 && laptop.samarScore >= 75) {
      badgeHtml = `<div class="card-badge badge-value"><i data-lucide="badge-percent"></i> Best Value King</div>`;
    } else if (laptop.benchmarkScores && laptop.benchmarkScores.gta5FPS >= 130) {
      badgeHtml = `<div class="card-badge badge-power"><i data-lucide="flame"></i> GTA 5: 130+ FPS</div>`;
    } else if (laptop.battery.lifeHours >= 9) {
      badgeHtml = `<div class="card-badge badge-battery"><i data-lucide="battery-charging"></i> Marathon Battery</div>`;
    } else if (laptop.isSlightStretch) {
      badgeHtml = `<div class="card-badge badge-stretch"><i data-lucide="arrow-up-right"></i> Worth +5% Stretch</div>`;
    }

    const gtaFps = (laptop.benchmarkScores && laptop.benchmarkScores.gta5FPS) || 'N/A';
    const deal = laptop.dealInfo;

    const cardPriceHtml = deal.hasDiscounts ? `
      <div class="card-price-wrap">
        <div class="effective-deal-line">
          <span class="card-price deal-green">${formatINR(deal.effectivePrice)}</span>
          <span class="card-deal-save-badge">Save ${formatINR(deal.totalSavings)}</span>
        </div>
        <div class="card-orig-price">MSRP: ${formatINR(laptop.price)}</div>
      </div>
    ` : `
      <div class="card-price-wrap">
        <div class="card-price">${formatINR(laptop.price)}</div>
        <div class="card-orig-price">${formatINR(laptop.originalPrice)}</div>
      </div>
    `;

    return `
      <div class="laptop-card" id="card-${laptop.id}">
        ${badgeHtml}
        <div class="card-img-wrap">
          <img src="${laptop.image}" alt="${laptop.name}" class="card-img" loading="lazy" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60';" />
          <div class="card-score-badge">
            <span class="score-percent">${laptop.samarScore}%</span>
            <span class="score-tag">Match</span>
          </div>
          <div class="card-gta-floating">
            <i data-lucide="gamepad-2"></i> ${gtaFps} FPS
          </div>
        </div>

        <div class="card-content">
          <div class="card-meta">
            <span class="brand-tag">${laptop.brand} &bull; ${laptop.processor.generation}</span>
            <div class="rating-tag">
              <i data-lucide="star" class="star-icon"></i>
              <span>${laptop.rating}</span>
              <span class="reviews-count">(${laptop.reviewsCount})</span>
            </div>
          </div>

          <h3 class="card-title" title="${laptop.name}">${laptop.name}</h3>

          <div class="specs-mini-grid">
            <div class="spec-mini-item" title="Processor">
              <i data-lucide="cpu"></i>
              <span>${laptop.processor.model.split('(')[0]}</span>
            </div>
            <div class="spec-mini-item" title="RAM & Storage">
              <i data-lucide="layers"></i>
              <span>${formatRAM(laptop.ram)} | ${formatStorage(laptop.storage)}</span>
            </div>
            <div class="spec-mini-item gta-highlight" title="GTA 5 Performance">
              <i data-lucide="gamepad-2"></i>
              <span>GTA 5: <strong>${gtaFps} FPS</strong></span>
            </div>
            <div class="spec-mini-item" title="Graphics">
              <i data-lucide="sparkles"></i>
              <span>${laptop.gpu.name}</span>
            </div>
          </div>

          <!-- Quick Store Action Pills -->
          <div class="card-store-strip">
            <a href="${laptop.buyLinks.amazon}" target="_blank" rel="noopener noreferrer" class="mini-store-link amz-link" title="Search on Amazon India">
              <span>a</span> Amazon
            </a>
            <a href="${laptop.buyLinks.flipkart}" target="_blank" rel="noopener noreferrer" class="mini-store-link fk-link" title="Search on Flipkart">
              <span>fk</span> Flipkart
            </a>
            <a href="${laptop.buyLinks.brandStore}" target="_blank" rel="noopener noreferrer" class="mini-store-link brand-link" title="${laptop.buyLinks.brandStoreName}">
              <i data-lucide="external-link"></i> ${laptop.brand} Store
            </a>
          </div>

          <div class="card-verdict-snippet">
            <strong>Samar:</strong> ${laptop.samarVerdict.length > 95 ? laptop.samarVerdict.slice(0, 95) + '...' : laptop.samarVerdict}
          </div>

          <div class="card-footer">
            ${cardPriceHtml}
            <div class="card-btn-group">
              <button class="btn btn-sm btn-outline" onclick="openDetailsModal('${laptop.id}')" title="Details & Offers">
                Specs
              </button>
              <button class="btn btn-sm ${isCompared(laptop.id) ? 'btn-secondary active' : 'btn-secondary'}" onclick="toggleCompare('${laptop.id}')" title="Compare">
                <i data-lucide="${isCompared(laptop.id) ? 'check' : 'plus'}"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function isCompared(id) {
  return state.compareList.includes(id);
}

function toggleCompare(id) {
  if (state.compareList.includes(id)) {
    state.compareList = state.compareList.filter(item => item !== id);
  } else {
    if (state.compareList.length >= 3) {
      alert("You can compare up to 3 laptops simultaneously.");
      return;
    }
    state.compareList.push(id);
  }
  renderApp();
}

function clearCompare() {
  state.compareList = [];
  renderApp();
}

function renderCompareBar() {
  const bar = document.getElementById('compareFloatingBar');
  if (!bar) return;

  if (state.compareList.length === 0) {
    bar.classList.add('hidden');
    return;
  }

  bar.classList.remove('hidden');
  const laptops = LAPTOPS_DATA.filter(l => state.compareList.includes(l.id));

  bar.innerHTML = `
    <div class="compare-bar-inner">
      <div class="compare-info">
        <span class="compare-badge">${laptops.length}/3</span>
        <span>Laptops selected to compare</span>
      </div>
      <div class="compare-thumbnails">
        ${laptops.map(l => `
          <div class="compare-thumb">
            <img src="${l.image}" alt="${l.name}" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60';" />
            <span class="compare-thumb-name">${l.name.split(' ')[0]} ${l.name.split(' ')[1] || ''}</span>
            <button class="compare-thumb-remove" onclick="toggleCompare('${l.id}')">&times;</button>
          </div>
        `).join('')}
      </div>
      <div class="compare-actions">
        <button class="btn btn-primary" onclick="openCompareModal()">
          <i data-lucide="columns-3"></i> Compare Side-by-Side
        </button>
        <button class="btn btn-ghost" onclick="clearCompare()">
          Clear
        </button>
      </div>
    </div>
  `;
}

function openCompareModal() {
  const modal = document.getElementById('compareModal');
  const content = document.getElementById('compareModalContent');
  if (!modal || !content) return;

  const laptops = LAPTOPS_DATA.filter(l => state.compareList.includes(l.id));
  if (laptops.length === 0) return;

  content.innerHTML = `
    <div class="compare-table-container">
      <table class="compare-table">
        <thead>
          <tr>
            <th>Specification</th>
            ${laptops.map(l => {
              const deal = calculateDiscounts(l.price);
              return `
              <th>
                <div class="table-laptop-header">
                  <img src="${l.image}" alt="${l.name}" class="table-img" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60';" />
                  <h4>${l.name}</h4>
                  <div class="table-price">
                    ${deal.hasDiscounts ? `${formatINR(deal.effectivePrice)} <small class="text-dim"><del>${formatINR(l.price)}</del></small>` : formatINR(l.price)}
                  </div>
                  <div class="table-store-links">
                    <a href="${l.buyLinks.amazon}" target="_blank" rel="noopener noreferrer" class="mini-store-link amz-link">Amazon</a>
                    <a href="${l.buyLinks.flipkart}" target="_blank" rel="noopener noreferrer" class="mini-store-link fk-link">Flipkart</a>
                  </div>
                  <button class="btn btn-sm btn-primary" onclick="openDetailsModal('${l.id}')">Full Specs &amp; Offers</button>
                </div>
              </th>
            `}).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Samar Match Score</strong></td>
            ${laptops.map(l => `<td><span class="score-pill-sm">${calculateSamarScore(l, state)}% Match</span></td>`).join('')}
          </tr>
          <tr class="highlight-row">
            <td><strong>🎮 GTA 5 FPS Benchmark</strong></td>
            ${laptops.map(l => `<td class="gta-cell"><strong class="gta-fps-text">${l.benchmarkScores.gta5FPS} FPS</strong><br><small class="text-muted">${l.benchmarkScores.gta5Settings}</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Processor &amp; Generation</strong></td>
            ${laptops.map(l => `<td><strong>${l.processor.generation}</strong><br>${l.processor.model}<br><small class="text-muted">${l.processor.cores} Cores / ${l.processor.threads} Threads</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>RAM &amp; Expandability</strong></td>
            ${laptops.map(l => `<td>${formatRAM(l.ram)} ${l.ramType}<br><small class="text-muted">${l.ramExpandable ? '✅ Upgradable' : '🔒 Soldered'}</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Storage</strong></td>
            ${laptops.map(l => `<td>${formatStorage(l.storage)}<br><small class="text-muted">${l.storageType}</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Graphics (GPU)</strong></td>
            ${laptops.map(l => `<td>${l.gpu.name}<br><small class="text-muted">${l.gpu.vram} ${l.gpu.tgp ? `(${l.gpu.tgp})` : ''}</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Direct Official Store</strong></td>
            ${laptops.map(l => `<td><a href="${l.buyLinks.brandStore}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline"><i data-lucide="external-link"></i> ${l.buyLinks.brandStoreName}</a></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Battery &amp; Weight</strong></td>
            ${laptops.map(l => `<td>${l.battery.lifeHours} hrs (${l.battery.capacity})<br><small class="text-muted">${l.weight} kg</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Samar Verdict</strong></td>
            ${laptops.map(l => `<td><em>${l.samarVerdict}</em></td>`).join('')}
          </tr>
        </tbody>
      </table>
    </div>
  `;

  modal.classList.remove('hidden');
  lucide.createIcons();
}

function closeCompareModal() {
  const modal = document.getElementById('compareModal');
  if (modal) modal.classList.add('hidden');
}

function openDetailsModal(id) {
  const laptop = LAPTOPS_DATA.find(l => l.id === id);
  if (!laptop) return;

  const modal = document.getElementById('detailsModal');
  const content = document.getElementById('detailsModalContent');
  if (!modal || !content) return;

  const score = calculateSamarScore(laptop, state);
  const deal = calculateDiscounts(laptop.price);

  content.innerHTML = `
    <div class="details-modal-grid">
      <div class="details-img-col">
        <img src="${laptop.image}" alt="${laptop.name}" class="details-img" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60';" />
        
        <div class="details-score-box">
          <div class="score-circle">
            <span class="score-circle-num">${score}%</span>
            <span class="score-circle-lbl">Samar Score</span>
          </div>
          <div class="score-explanation">
            <h4>Recommendation Strength</h4>
            <p>Calculated for your budget of ${formatINR(state.budget)}, processor preference, and workflow requirements.</p>
          </div>
        </div>

        <!-- Real Gaming Benchmarks -->
        <div class="benchmarks-box">
          <h4>🎮 Real Gaming &amp; Performance Benchmarks</h4>
          
          <div class="benchmark-item gta-bench-item">
            <div class="benchmark-meta">
              <span><strong>GTA 5 Benchmark FPS:</strong></span>
              <span class="gta-highlight-val"><strong>${laptop.benchmarkScores.gta5FPS} FPS</strong></span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill bar-fill-gta" style="width: ${Math.min(100, (laptop.benchmarkScores.gta5FPS / 200) * 100)}%"></div></div>
            <small class="text-dim">Tested at ${laptop.benchmarkScores.gta5Settings}</small>
          </div>

          <div class="benchmark-item">
            <div class="benchmark-meta">
              <span>Multi-Core CPU Power</span>
              <span>${laptop.benchmarkScores.multiCore} pts</span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill" style="width: ${Math.min(100, (laptop.benchmarkScores.multiCore / 25000) * 100)}%"></div></div>
          </div>

          <div class="benchmark-item">
            <div class="benchmark-meta">
              <span>Overall 3D / Esports FPS</span>
              <span>${laptop.benchmarkScores.gamingFPS} FPS</span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill bar-fill-gaming" style="width: ${Math.min(100, (laptop.benchmarkScores.gamingFPS / 180) * 100)}%"></div></div>
          </div>
        </div>

        <!-- Store Purchase Links Box -->
        <div class="modal-stores-box">
          <h4><i data-lucide="shopping-bag"></i> Where to Buy at Lowest Price</h4>
          <div class="modal-store-list">
            <a href="${laptop.buyLinks.amazon}" target="_blank" rel="noopener noreferrer" class="modal-store-card store-card-amz">
              <div class="store-card-info">
                <strong>Amazon India</strong>
                <span>Fast Prime delivery, No-Cost EMI &amp; bank discounts</span>
              </div>
              <span class="btn-store-visit">Check Deal <i data-lucide="arrow-up-right"></i></span>
            </a>

            <a href="${laptop.buyLinks.flipkart}" target="_blank" rel="noopener noreferrer" class="modal-store-card store-card-fk">
              <div class="store-card-info">
                <strong>Flipkart India</strong>
                <span>SuperCoins, exchange trade-in &amp; brand warranty</span>
              </div>
              <span class="btn-store-visit">Check Deal <i data-lucide="arrow-up-right"></i></span>
            </a>

            <a href="${laptop.buyLinks.brandStore}" target="_blank" rel="noopener noreferrer" class="modal-store-card store-card-brand">
              <div class="store-card-info">
                <strong>${laptop.buyLinks.brandStoreName}</strong>
                <span>100% Genuine, Student UNiDAYS offers &amp; custom upgrades</span>
              </div>
              <span class="btn-store-visit">Visit Store <i data-lucide="arrow-up-right"></i></span>
            </a>
          </div>
        </div>
      </div>

      <div class="details-info-col">
        <div class="details-header">
          <div>
            <span class="brand-pill">${laptop.brand} &bull; ${laptop.processor.generation}</span>
            <h2>${laptop.name}</h2>
          </div>
          <div class="details-pricing">
            ${deal.hasDiscounts ? `
              <div class="deal-tag-sub">Effective Deal Price</div>
              <div class="details-price deal-green">${formatINR(deal.effectivePrice)}</div>
              <div class="details-orig">MSRP: ${formatINR(laptop.price)}</div>
            ` : `
              <div class="details-price">${formatINR(laptop.price)}</div>
              <div class="details-orig">${formatINR(laptop.originalPrice)}</div>
            `}
          </div>
        </div>

        <!-- Interactive Discount Breakdown Simulator for this Laptop -->
        <div class="modal-deal-calc-card">
          <div class="deal-calc-title">
            <i data-lucide="calculator"></i>
            <span>Interactive Deal Breakdown (This Laptop)</span>
          </div>
          <div class="deal-calc-breakdown">
            <div class="calc-line"><span>Regular Store Price:</span><span>${formatINR(laptop.price)}</span></div>
            ${deal.studentSavings > 0 ? `<div class="calc-line green"><span>🎓 Student Education Discount (7%):</span><span>- ${formatINR(deal.studentSavings)}</span></div>` : ''}
            ${deal.bankSavings > 0 ? `<div class="calc-line green"><span>💳 Credit Card Bank Offer:</span><span>- ${formatINR(deal.bankSavings)}</span></div>` : ''}
            ${deal.exchangeSavings > 0 ? `<div class="calc-line green"><span>🔄 Old Laptop Trade-in Value:</span><span>- ${formatINR(deal.exchangeSavings)}</span></div>` : ''}
            <div class="calc-line total">
              <span><strong>Final Effective Payable:</strong></span>
              <span class="total-effective">${formatINR(deal.effectivePrice)}</span>
            </div>
          </div>
          ${!deal.hasDiscounts ? `
            <small class="deal-hint">Tip: Toggle the Student or Bank Card offers in the Deal Calculator bar above to activate instant savings!</small>
          ` : `
            <small class="deal-hint deal-active-hint">✅ Extra ${formatINR(deal.totalSavings)} savings applied from your active selections!</small>
          `}
        </div>

        <div class="samar-analysis-box">
          <div class="analysis-tag"><i data-lucide="brain"></i> Samar's Deep Analysis</div>
          <p>${laptop.samarVerdict}</p>
        </div>

        <div class="details-tabs-content">
          <h3>Full Specifications</h3>
          <div class="spec-table-grid">
            <div class="spec-row"><span class="spec-k">Processor</span><span class="spec-v">${laptop.processor.model} (${laptop.processor.generation}, ${laptop.processor.cores}C/${laptop.processor.threads}T, Up to ${laptop.processor.boostSpeed})</span></div>
            <div class="spec-row gta-row"><span class="spec-k">GTA 5 Performance</span><span class="spec-v"><strong>${laptop.benchmarkScores.gta5FPS} FPS</strong> (${laptop.benchmarkScores.gta5Settings})</span></div>
            <div class="spec-row"><span class="spec-k">RAM Memory</span><span class="spec-v">${formatRAM(laptop.ram)} ${laptop.ramType} (${laptop.ramExpandable ? 'Expandable slot available' : 'Soldered'})</span></div>
            <div class="spec-row"><span class="spec-k">Storage Drive</span><span class="spec-v">${formatStorage(laptop.storage)} (${laptop.storageType})</span></div>
            <div class="spec-row"><span class="spec-k">Graphics Card</span><span class="spec-v">${laptop.gpu.name} (${laptop.gpu.vram} ${laptop.gpu.tgp ? `• ${laptop.gpu.tgp}` : ''})</span></div>
            <div class="spec-row"><span class="spec-k">Display Screen</span><span class="spec-v">${laptop.display.size}, ${laptop.display.resolution}, ${laptop.display.panel}, ${laptop.display.brightness}, ${laptop.display.refreshRate}</span></div>
            <div class="spec-row"><span class="spec-k">Battery Life</span><span class="spec-v">${laptop.battery.capacity} (Up to ${laptop.battery.lifeHours} hours, ${laptop.battery.fastCharging})</span></div>
            <div class="spec-row"><span class="spec-k">Chassis Weight</span><span class="spec-v">${laptop.weight} kg</span></div>
            <div class="spec-row"><span class="spec-k">Operating System</span><span class="spec-v">${laptop.os}</span></div>
          </div>

          <div class="pros-cons-grid">
            <div class="pros-box">
              <h4><i data-lucide="thumbs-up"></i> Key Advantages</h4>
              <ul>
                ${laptop.pros.map(pro => `<li><i data-lucide="check" class="check-icon"></i> ${pro}</li>`).join('')}
              </ul>
            </div>
            <div class="cons-box">
              <h4><i data-lucide="thumbs-down"></i> Potential Trade-offs</h4>
              <ul>
                ${laptop.cons.map(con => `<li><i data-lucide="x" class="x-icon"></i> ${con}</li>`).join('')}
              </ul>
            </div>
          </div>
        </div>

        <div class="details-footer-actions">
          <button class="btn btn-secondary" onclick="toggleCompare('${laptop.id}'); closeDetailsModal();">
            <i data-lucide="${isCompared(laptop.id) ? 'check' : 'layers'}"></i>
            ${isCompared(laptop.id) ? 'Remove from Compare' : 'Add to Compare'}
          </button>
          <a href="${laptop.buyLinks.amazon}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i data-lucide="shopping-cart"></i> Buy on Amazon
          </a>
          <a href="${laptop.buyLinks.brandStore}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
            <i data-lucide="shield-check"></i> Official Store
          </a>
        </div>
      </div>
    </div>
  `;

  modal.classList.remove('hidden');
  lucide.createIcons();
}

function closeDetailsModal() {
  const modal = document.getElementById('detailsModal');
  if (modal) modal.classList.add('hidden');
}

function resetFilters() {
  state.budget = 90000;
  state.isBudgetFlexible = true;
  state.purpose = 'all';
  state.processor = 'any';
  state.ram = 'any';
  state.storage = 'any';
  state.brand = 'all';
  state.searchQuery = '';
  state.sortBy = 'samar-match';
  state.studentDiscount = false;
  state.bankOffer = 'none';
  state.exchangeValue = 0;
  updateFilterControls();
  renderApp();
}

function initEventListeners() {
  const slider = document.getElementById('budgetSlider');
  const input = document.getElementById('budgetInput');
  const flexToggle = document.getElementById('flexBudgetToggle');

  if (slider) {
    slider.addEventListener('input', (e) => {
      state.budget = parseInt(e.target.value);
      renderBudgetControls();
      renderDiscountBar();
      renderResults();
      renderCompareBar();
    });
  }

  if (input) {
    input.addEventListener('change', (e) => {
      let val = parseInt(e.target.value) || 30000;
      val = Math.max(30000, Math.min(250000, val));
      state.budget = val;
      renderBudgetControls();
      renderDiscountBar();
      renderResults();
      renderCompareBar();
    });
  }

  if (flexToggle) {
    flexToggle.addEventListener('change', (e) => {
      state.isBudgetFlexible = e.target.checked;
      renderResults();
    });
  }

  // Discount Calculator Listeners
  const studentToggle = document.getElementById('studentDiscountToggle');
  if (studentToggle) {
    studentToggle.addEventListener('change', (e) => {
      state.studentDiscount = e.target.checked;
      renderApp();
    });
  }

  const bankSelect = document.getElementById('bankOfferSelect');
  if (bankSelect) {
    bankSelect.addEventListener('change', (e) => {
      state.bankOffer = e.target.value;
      renderApp();
    });
  }

  const exchangeSelect = document.getElementById('exchangeSelect');
  if (exchangeSelect) {
    exchangeSelect.addEventListener('change', (e) => {
      state.exchangeValue = parseInt(e.target.value) || 0;
      renderApp();
    });
  }

  const procSelect = document.getElementById('processorSelect');
  if (procSelect) {
    procSelect.addEventListener('change', (e) => {
      state.processor = e.target.value;
      renderResults();
    });
  }

  const ramSelect = document.getElementById('ramSelect');
  if (ramSelect) {
    ramSelect.addEventListener('change', (e) => {
      state.ram = e.target.value;
      renderResults();
    });
  }

  const storageSelect = document.getElementById('storageSelect');
  if (storageSelect) {
    storageSelect.addEventListener('change', (e) => {
      state.storage = e.target.value;
      renderResults();
    });
  }

  const brandSelect = document.getElementById('brandSelect');
  if (brandSelect) {
    brandSelect.addEventListener('change', (e) => {
      state.brand = e.target.value;
      renderResults();
    });
  }

  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderResults();
    });
  }

  const sortSelect = document.getElementById('sortSelect');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      renderResults();
    });
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDetailsModal();
      closeCompareModal();
    }
  });

  const detailsModal = document.getElementById('detailsModal');
  if (detailsModal) {
    detailsModal.addEventListener('click', (e) => {
      if (e.target === detailsModal) closeDetailsModal();
    });
  }

  const compareModal = document.getElementById('compareModal');
  if (compareModal) {
    compareModal.addEventListener('click', (e) => {
      if (e.target === compareModal) closeCompareModal();
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initEventListeners();
  updateFilterControls();
  renderApp();
});
