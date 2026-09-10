# SAMAR Portal Builder
import os
import json

BASE_DIR = r"C:\Users\HP\.gemini\antigravity\scratch\samar-laptop-portal"

def make_data_js():
    content = """// SAMAR Laptop Choice Portal - Laptop Database
// Rich catalog featuring Intel 13th & 14th Gen (i3, i5, i7), AMD Ryzen (3, 5, 7, 9) and Apple M3

const LAPTOPS_DATA = [
  // ==================== BUDGET ENTRY (Under ₹45,000) ====================
  {
    id: "lenovo-ideapad-slim-3-i3-13th",
    name: "Lenovo IdeaPad Slim 3 15",
    brand: "Lenovo",
    series: "IdeaPad",
    price: 36990,
    originalPrice: 53990,
    rating: 4.3,
    reviewsCount: 1420,
    image: "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i3",
      generation: "13th Gen",
      model: "Intel Core i3-1315U (6 Cores: 2P + 4E)",
      cores: 6,
      threads: 8,
      baseSpeed: "1.2 GHz",
      boostSpeed: "4.5 GHz"
    },
    ram: 8,
    ramType: "LPDDR5 4800MHz",
    ramExpandable: false,
    storage: 512,
    storageType: "NVMe M.2 SSD",
    gpu: {
      type: "Integrated",
      name: "Intel UHD Graphics",
      vram: "Shared"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "60Hz",
      panel: "IPS Anti-Glare",
      brightness: "300 nits"
    },
    battery: {
      capacity: "47 Wh",
      lifeHours: 7,
      fastCharging: "80% in 60 mins"
    },
    weight: 1.62,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["college", "office"],
    benchmarkScores: {
      singleCore: 1620,
      multiCore: 5300,
      gamingFPS: 32,
      productivityScore: 74
    },
    pros: [
      "Modern 13th Gen Intel processor with snappy daily responsiveness",
      "Very lightweight for a 15.6-inch laptop (1.62 kg)",
      "Comes with lifetime Microsoft Office 2021 pre-installed",
      "Physical privacy shutter on webcam"
    ],
    cons: [
      "RAM is soldered (cannot upgrade beyond 8GB)",
      "Not intended for heavy gaming or 4K video exports"
    ],
    samarVerdict: "The best overall entry-level choice under ₹40K for students and office workers wanting 13th Gen Intel reliability with zero lag for everyday multitasking."
  },
  {
    id: "asus-vivobook-go-15-ryzen-7520u",
    name: "ASUS Vivobook Go 15 (2024)",
    brand: "ASUS",
    series: "Vivobook",
    price: 38990,
    originalPrice: 56990,
    rating: 4.2,
    reviewsCount: 980,
    image: "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 5",
      generation: "7000 Series",
      model: "AMD Ryzen 5 7520U (4 Cores / 8 Threads)",
      cores: 4,
      threads: 8,
      baseSpeed: "2.8 GHz",
      boostSpeed: "4.3 GHz"
    },
    ram: 16,
    ramType: "LPDDR5 5500MHz",
    ramExpandable: false,
    storage: 512,
    storageType: "PCIe 3.0 NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "AMD Radeon 610M",
      vram: "Shared"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "60Hz",
      panel: "Anti-Glare LED",
      brightness: "250 nits"
    },
    battery: {
      capacity: "42 Wh",
      lifeHours: 8,
      fastCharging: "60% in 49 mins"
    },
    weight: 1.63,
    os: "Windows 11 Home",
    suitableFor: ["college", "office", "coding"],
    benchmarkScores: {
      singleCore: 1480,
      multiCore: 4900,
      gamingFPS: 30,
      productivityScore: 76
    },
    pros: [
      "Rare 16GB LPDDR5 RAM at under ₹40,000 price point",
      "180-degree lay-flat hinge design",
      "AI noise cancellation microphone for clean meetings/classes",
      "Excellent power efficiency and battery endurance"
    ],
    cons: [
      "Display brightness is 250 nits (best suited for indoors)",
      "Basic integrated Radeon graphics"
    ],
    samarVerdict: "Unbeatable budget multitasking king! Getting 16GB RAM at this price is a massive win for students learning web development or multitasking with 30+ browser tabs."
  },
  {
    id: "hp-15s-ryzen-5500u",
    name: "HP 15s-eq2144AU",
    brand: "HP",
    series: "15s",
    price: 41490,
    originalPrice: 54500,
    rating: 4.4,
    reviewsCount: 3200,
    image: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 5",
      generation: "5000 Series",
      model: "AMD Ryzen 5 5500U (6 Cores / 12 Threads)",
      cores: 6,
      threads: 12,
      baseSpeed: "2.1 GHz",
      boostSpeed: "4.0 GHz"
    },
    ram: 16,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe NVMe M.2 SSD",
    gpu: {
      type: "Integrated",
      name: "AMD Radeon Vega 7 Graphics",
      vram: "Shared"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "60Hz",
      panel: "Micro-Edge IPS",
      brightness: "250 nits"
    },
    battery: {
      capacity: "41 Wh",
      lifeHours: 7.5,
      fastCharging: "50% in 45 mins"
    },
    weight: 1.69,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["college", "office", "coding"],
    benchmarkScores: {
      singleCore: 1420,
      multiCore: 6100,
      gamingFPS: 38,
      productivityScore: 79
    },
    pros: [
      "Proven 6 Cores / 12 Threads processor with superior multi-threading",
      "16GB RAM upgradeable to 32GB in future",
      "Reliable HP after-sales service network across India",
      "Fast charging and very comfortable full-size keyboard"
    ],
    cons: [
      "No Type-C charging support",
      "Plastic chassis finish"
    ],
    samarVerdict: "The most trusted budget workhorse in India. The 6-core Ryzen 5 5500U punches way above its price class in compile times and spreadsheet processing."
  },
  {
    id: "acer-aspire-lite-i3-13th",
    name: "Acer Aspire Lite 15",
    brand: "Acer",
    series: "Aspire",
    price: 33990,
    originalPrice: 52990,
    rating: 4.1,
    reviewsCount: 740,
    image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i3",
      generation: "13th Gen",
      model: "Intel Core i3-1305U (5 Cores: 1P + 4E)",
      cores: 5,
      threads: 6,
      baseSpeed: "1.2 GHz",
      boostSpeed: "4.5 GHz"
    },
    ram: 8,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "Intel UHD Graphics",
      vram: "Shared"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "60Hz",
      panel: "Slim Bezel Anti-Glare",
      brightness: "250 nits"
    },
    battery: {
      capacity: "36 Wh",
      lifeHours: 5.5,
      fastCharging: "Standard"
    },
    weight: 1.59,
    os: "Windows 11 Home",
    suitableFor: ["college", "office"],
    benchmarkScores: {
      singleCore: 1540,
      multiCore: 4400,
      gamingFPS: 28,
      productivityScore: 70
    },
    pros: [
      "Extremely affordable entry price under ₹35,000",
      "Metal top cover gives premium hand-feel",
      "RAM slot is user-expandable up to 32GB"
    ],
    cons: [
      "Modest battery capacity (36Wh)",
      "Basic webcam and speakers"
    ],
    samarVerdict: "Solid pick if your budget is strictly capped around ₹35,000 and you need a modern 13th Gen Intel machine with future RAM upgradeability."
  },
  {
    id: "dell-vostro-14-i3-13th",
    name: "Dell Vostro 3430",
    brand: "Dell",
    series: "Vostro",
    price: 37990,
    originalPrice: 51990,
    rating: 4.2,
    reviewsCount: 810,
    image: "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i3",
      generation: "13th Gen",
      model: "Intel Core i3-1305U (5 Cores / 6 Threads)",
      cores: 5,
      threads: 6,
      baseSpeed: "1.2 GHz",
      boostSpeed: "4.5 GHz"
    },
    ram: 8,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "Intel UHD Graphics",
      vram: "Shared"
    },
    display: {
      size: "14.0 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "60Hz",
      panel: "WVA Display",
      brightness: "250 nits"
    },
    battery: {
      capacity: "41 Wh",
      lifeHours: 6.5,
      fastCharging: "ExpressCharge"
    },
    weight: 1.48,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["college", "office"],
    benchmarkScores: {
      singleCore: 1560,
      multiCore: 4500,
      gamingFPS: 29,
      productivityScore: 72
    },
    pros: [
      "Compact 14-inch form factor weighing just 1.48kg",
      "Dual RAM slots with upgrade path up to 32GB",
      "Dell hardware TPM 2.0 security chip for business privacy"
    ],
    cons: [
      "Screen viewing angles are modest",
      "Single channel 8GB out of box"
    ],
    samarVerdict: "Affordable and compact business-ready laptop with Dell durability and security, ideal for accounting, studies, and remote office work."
  },

  // ==================== MID-RANGE (₹45,000 - ₹65,000) ====================
  {
    id: "lenovo-ideapad-slim-5-i5-13th",
    name: "Lenovo IdeaPad Slim 5 14 (All-Metal)",
    brand: "Lenovo",
    series: "IdeaPad",
    price: 59990,
    originalPrice: 82990,
    rating: 4.6,
    reviewsCount: 1850,
    image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13500H (12 Cores: 4P + 8E / 16 Threads)",
      cores: 12,
      threads: 16,
      baseSpeed: "2.6 GHz",
      boostSpeed: "4.7 GHz"
    },
    ram: 16,
    ramType: "LPDDR5 5200MHz",
    ramExpandable: false,
    storage: 512,
    storageType: "PCIe Gen 4 NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "Intel Iris Xe Graphics (80EU)",
      vram: "Shared"
    },
    display: {
      size: "14.0 inch",
      resolution: "WUXGA (1920x1200) 16:10",
      refreshRate: "60Hz",
      panel: "OLED / 100% DCI-P3",
      brightness: "400 nits"
    },
    battery: {
      capacity: "56.6 Wh",
      lifeHours: 8.5,
      fastCharging: "Rapid Charge Boost (2hr in 15m)"
    },
    weight: 1.46,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["coding", "college", "office", "editing"],
    benchmarkScores: {
      singleCore: 1820,
      multiCore: 12400,
      gamingFPS: 45,
      productivityScore: 92
    },
    pros: [
      "High performance H-series 12-core i5-13500H (crushes compile benchmarks)",
      "Vibrant 100% DCI-P3 color gamut screen with 16:10 productivity aspect ratio",
      "Full aluminium chassis, military-grade MIL-STD-810H durability",
      "FHD IR webcam with Windows Hello Face unlock"
    ],
    cons: [
      "No dedicated graphics card for AAA games",
      "LPDDR5 RAM cannot be upgraded"
    ],
    samarVerdict: "SAMAR'S EDITORS CHOICE FOR CODING & STUDENTS! The 12-core i5-13500H crushes Docker containers and IDE compiles, while the 1.46kg metal body is effortless to carry."
  },
  {
    id: "asus-vivobook-16-i5-13th",
    name: "ASUS Vivobook 16X (2024)",
    brand: "ASUS",
    series: "Vivobook",
    price: 54990,
    originalPrice: 74990,
    rating: 4.4,
    reviewsCount: 1100,
    image: "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13420H (8 Cores: 4P + 4E / 12 Threads)",
      cores: 8,
      threads: 12,
      baseSpeed: "2.1 GHz",
      boostSpeed: "4.6 GHz"
    },
    ram: 16,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe 4.0 NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "Intel UHD Graphics",
      vram: "Shared"
    },
    display: {
      size: "16.0 inch",
      resolution: "WUXGA (1920x1200) 16:10",
      refreshRate: "60Hz",
      panel: "IPS Anti-Glare",
      brightness: "300 nits"
    },
    battery: {
      capacity: "50 Wh",
      lifeHours: 6.5,
      fastCharging: "65W Fast Charge"
    },
    weight: 1.88,
    os: "Windows 11 Home",
    suitableFor: ["coding", "office", "college"],
    benchmarkScores: {
      singleCore: 1710,
      multiCore: 9800,
      gamingFPS: 40,
      productivityScore: 84
    },
    pros: [
      "Spacious 16-inch 16:10 display allows seeing more lines of code",
      "Powerful H-series 13th Gen Intel processor",
      "ErgoSense keyboard with antimicrobial guard protection",
      "RAM slot is expandable up to 24GB"
    ],
    cons: [
      "Slightly heavier at 1.88kg due to 16-inch form factor",
      "Speakers are downward firing"
    ],
    samarVerdict: "Great pick for developers and spreadsheet specialists who love large screens without spending a fortune. Clean thermal profile and very comfortable typing experience."
  },
  {
    id: "dell-inspiron-3530-i5-13th",
    name: "Dell Inspiron 3530 (120Hz)",
    brand: "Dell",
    series: "Inspiron",
    price: 52990,
    originalPrice: 68990,
    rating: 4.3,
    reviewsCount: 1640,
    image: "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-1335U (10 Cores: 2P + 8E / 12 Threads)",
      cores: 10,
      threads: 12,
      baseSpeed: "1.3 GHz",
      boostSpeed: "4.6 GHz"
    },
    ram: 16,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "Intel Iris Xe Graphics",
      vram: "Shared"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "120Hz",
      panel: "WVA Anti-Glare",
      brightness: "250 nits"
    },
    battery: {
      capacity: "54 Wh",
      lifeHours: 7.5,
      fastCharging: "ExpressCharge (80% in 60 mins)"
    },
    weight: 1.65,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["office", "college", "coding"],
    benchmarkScores: {
      singleCore: 1680,
      multiCore: 8200,
      gamingFPS: 38,
      productivityScore: 82
    },
    pros: [
      "Smooth 120Hz refresh rate display in an office laptop",
      "Dell lift-hinge ergonomic design for cooler airflow and better typing angle",
      "Both RAM slots are dual-channel upgradable (up to 32GB)",
      "High reliability Dell build quality and after-sales support"
    ],
    cons: [
      "Plastic chassis on base model",
      "Display colors are 45% NTSC"
    ],
    samarVerdict: "A rock-solid corporate & student machine. The 120Hz refresh rate makes daily browsing and code scrolling ultra smooth, paired with easy RAM upgrades."
  },
  {
    id: "acer-swift-go-14-oled-i5-13th",
    name: "Acer Swift Go 14 OLED",
    brand: "Acer",
    series: "Swift",
    price: 62990,
    originalPrice: 79990,
    rating: 4.6,
    reviewsCount: 890,
    image: "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13500H (12 Cores / 16 Threads)",
      cores: 12,
      threads: 16,
      baseSpeed: "2.6 GHz",
      boostSpeed: "4.7 GHz"
    },
    ram: 16,
    ramType: "LPDDR5 4800MHz",
    ramExpandable: false,
    storage: 512,
    storageType: "PCIe Gen4 SSD",
    gpu: {
      type: "Integrated",
      name: "Intel Iris Xe Graphics",
      vram: "Shared"
    },
    display: {
      size: "14.0 inch",
      resolution: "2.8K OLED (2880x1800) 16:10",
      refreshRate: "90Hz",
      panel: "True Black 500 HDR OLED / 100% DCI-P3",
      brightness: "500 nits"
    },
    battery: {
      capacity: "65 Wh",
      lifeHours: 9.5,
      fastCharging: "100W USB-PD"
    },
    weight: 1.25,
    os: "Windows 11 Home",
    suitableFor: ["editing", "coding", "college", "office"],
    benchmarkScores: {
      singleCore: 1840,
      multiCore: 12500,
      gamingFPS: 46,
      productivityScore: 94
    },
    pros: [
      "Breathtaking 2.8K 90Hz OLED display (deep blacks, 100% DCI-P3)",
      "Featherlight at just 1.25kg - perfect for backpack commuters",
      "TwinAir dual fan cooling keeps high TDP 13500H cool",
      "Dual Thunderbolt 4 ports with 100W PD charging"
    ],
    cons: [
      "OLED uses slightly more battery when viewing white documents at max brightness",
      "No dedicated GPU"
    ],
    samarVerdict: "BEST DISPLAY UNDER ₹65K. If you do graphic design, content consumption, or programming on a laptop that you take everywhere, this 1.25kg OLED marvel is top tier."
  },

  // ==================== BUDGET & MID GAMING (₹60,000 - ₹85,000) ====================
  {
    id: "lenovo-loq-i5-13th-rtx3050",
    name: "Lenovo LOQ 15 (13th Gen HX)",
    brand: "Lenovo",
    series: "LOQ",
    price: 64990,
    originalPrice: 89990,
    rating: 4.5,
    reviewsCount: 2400,
    image: "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13450HX (10 Cores: 6P + 4E / 16 Threads)",
      cores: 10,
      threads: 16,
      baseSpeed: "2.4 GHz",
      boostSpeed: "4.6 GHz"
    },
    ram: 16,
    ramType: "DDR5 4800MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe Gen4 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 3050 (6GB)",
      vram: "6GB GDDR6",
      tgp: "95W TGP"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS G-SYNC 100% sRGB",
      brightness: "350 nits"
    },
    battery: {
      capacity: "60 Wh",
      lifeHours: 5,
      fastCharging: "Super Rapid Charge Pro"
    },
    weight: 2.38,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "editing", "ai"],
    benchmarkScores: {
      singleCore: 1780,
      multiCore: 14200,
      gamingFPS: 78,
      productivityScore: 91
    },
    pros: [
      "Desktop-grade 13450HX processor with undervolt support",
      "Full power 95W TGP RTX 3050 with generous 6GB VRAM (not 4GB)",
      "100% sRGB 144Hz 350-nit display (far better than washed out budget screens)",
      "Dual M.2 SSD slots and dual DDR5 RAM slots"
    ],
    cons: [
      "Bulkier gaming charger and chassis (2.38kg)",
      "Battery life under 4.5 hours on hybrid mode"
    ],
    samarVerdict: "SAMAR'S BEST VALUE GAMING & AI ENTRY MACHINE. The 6GB VRAM on the 95W RTX 3050 combined with 13450HX handles modern games, Premiere Pro timeline scrub, and local AI PyTorch models."
  },
  {
    id: "asus-tuf-a15-ryzen-7735hs-rtx4050",
    name: "ASUS TUF Gaming A15 (2024)",
    brand: "ASUS",
    series: "TUF",
    price: 76990,
    originalPrice: 104990,
    rating: 4.6,
    reviewsCount: 3100,
    image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 7",
      generation: "7000 Series",
      model: "AMD Ryzen 7 7735HS (8 Cores / 16 Threads)",
      cores: 8,
      threads: 16,
      baseSpeed: "3.2 GHz",
      boostSpeed: "4.75 GHz"
    },
    ram: 16,
    ramType: "DDR5 4800MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe 4.0 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4050",
      vram: "6GB GDDR6",
      tgp: "140W Max TGP with Dynamic Boost"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS Anti-Glare 100% sRGB",
      brightness: "300 nits"
    },
    battery: {
      capacity: "90 Wh",
      lifeHours: 8.5,
      fastCharging: "Fast charge 50% in 30 mins"
    },
    weight: 2.20,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "editing", "ai"],
    benchmarkScores: {
      singleCore: 1810,
      multiCore: 14800,
      gamingFPS: 110,
      productivityScore: 95
    },
    pros: [
      "Gigantic 90Wh battery delivers 8+ hours non-gaming battery life (unheard of in gaming laptops)",
      "Full 140W TGP RTX 4050 with DLSS 3 Frame Generation support",
      "Ryzen 7 7735HS runs cool and power efficient",
      "100% sRGB color accuracy for video editing work",
      "MIL-STD-810H military drop resistance"
    ],
    cons: [
      "Comes with 512GB SSD out of the box (2nd slot is free)",
      "Webcam is 720p"
    ],
    samarVerdict: "THE ALL-ROUND CHAMPION UNDER ₹80K. If you need both serious gaming/AI power (RTX 4050 140W) AND all-day battery life for college/travel, ASUS TUF A15 with 90Wh battery is unmatched."
  },
  {
    id: "acer-nitro-v15-i5-13th-rtx4050",
    name: "Acer Nitro V 15",
    brand: "Acer",
    series: "Nitro",
    price: 69990,
    originalPrice: 89990,
    rating: 4.3,
    reviewsCount: 1560,
    image: "https://images.unsplash.com/photo-1595327656903-2f54e37ce09b?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13420H (8 Cores / 12 Threads)",
      cores: 8,
      threads: 12,
      baseSpeed: "2.1 GHz",
      boostSpeed: "4.6 GHz"
    },
    ram: 16,
    ramType: "DDR5 5200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4050",
      vram: "6GB GDDR6",
      tgp: "75W TGP"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS Anti-Glare",
      brightness: "250 nits"
    },
    battery: {
      capacity: "57 Wh",
      lifeHours: 5,
      fastCharging: "135W AC Adapter"
    },
    weight: 2.11,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "ai"],
    benchmarkScores: {
      singleCore: 1720,
      multiCore: 10400,
      gamingFPS: 95,
      productivityScore: 88
    },
    pros: [
      "Most affordable route to an RTX 4050 with DLSS 3 (under ₹70,000)",
      "High speed DDR5 5200MHz RAM",
      "Thunderbolt 4 port included",
      "Lighter than traditional gaming laptops at 2.11kg"
    ],
    cons: [
      "Display is 45% NTSC color gamut",
      "75W TGP is lower than TUF 140W"
    ],
    samarVerdict: "Best budget gateway to RTX 4050. If your budget is strictly ₹70,000 and you must have DLSS 3 and Ada Lovelace architecture for gaming and CUDA machine learning."
  },
  {
    id: "lenovo-loq-i5-14th-rtx4050",
    name: "Lenovo LOQ 15 (14th Gen HX / 1TB SSD)",
    brand: "Lenovo",
    series: "LOQ",
    price: 81990,
    originalPrice: 106990,
    rating: 4.5,
    reviewsCount: 1720,
    image: "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "14th Gen",
      model: "Intel Core i5-14450HX (10 Cores: 6P + 4E / 16 Threads)",
      cores: 10,
      threads: 16,
      baseSpeed: "2.4 GHz",
      boostSpeed: "4.8 GHz"
    },
    ram: 16,
    ramType: "DDR5 4800MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe Gen4 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4050",
      vram: "6GB GDDR6",
      tgp: "105W TGP"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS 100% sRGB G-SYNC",
      brightness: "300 nits"
    },
    battery: {
      capacity: "60 Wh",
      lifeHours: 5,
      fastCharging: "Super Rapid Charge (0-80% in 30m)"
    },
    weight: 2.38,
    os: "Windows 11 Home + 3-month Xbox Game Pass",
    suitableFor: ["gaming", "coding", "ai", "editing"],
    benchmarkScores: {
      singleCore: 1890,
      multiCore: 15400,
      gamingFPS: 112,
      productivityScore: 94
    },
    pros: [
      "Latest 14th Gen Intel HX-series processor with overclocking headroom",
      "Huge 1TB Gen4 SSD out of the box - zero storage anxiety",
      "100% sRGB color gamut 144Hz screen with G-SYNC",
      "LA1 AI chip dynamically shifts power between CPU and GPU"
    ],
    cons: [
      "Battery life is modest due to power-hungry HX processor",
      "Chassis is plastic though very sturdy"
    ],
    samarVerdict: "SAMAR'S PICK FOR 14TH GEN INTEL VALUE. The i5-14450HX and 105W RTX 4050 with 1TB SSD handles every modern game at ultra settings with DLSS 3 and compiles large codebases in seconds."
  },

  // ==================== HIGH PERFORMANCE & CREATOR (₹85,000 - ₹1,25,000) ====================
  {
    id: "acer-predator-helios-neo-16-i7-14th",
    name: "Acer Predator Helios Neo 16 (14th Gen)",
    brand: "Acer",
    series: "Predator",
    price: 114990,
    originalPrice: 149990,
    rating: 4.7,
    reviewsCount: 1450,
    image: "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "14th Gen",
      model: "Intel Core i7-14700HX (20 Cores: 8P + 12E / 28 Threads)",
      cores: 20,
      threads: 28,
      baseSpeed: "2.1 GHz",
      boostSpeed: "5.5 GHz"
    },
    ram: 16,
    ramType: "DDR5 5600MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe Gen4 NVMe SSD (RAID 0 supported)",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4060",
      vram: "8GB GDDR6",
      tgp: "140W Max TGP"
    },
    display: {
      size: "16.0 inch",
      resolution: "WQXGA (2560x1600) 16:10",
      refreshRate: "165Hz",
      panel: "IPS 100% sRGB / 500 nits / G-SYNC",
      brightness: "500 nits"
    },
    battery: {
      capacity: "90 Wh",
      lifeHours: 5.5,
      fastCharging: "330W Adapter"
    },
    weight: 2.60,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "ai", "editing", "coding"],
    benchmarkScores: {
      singleCore: 2050,
      multiCore: 23500,
      gamingFPS: 145,
      productivityScore: 98
    },
    pros: [
      "MONSTROUS 20-Core / 28-Thread i7-14700HX CPU (destroys Cinebench)",
      "Gorgeous 2.5K 165Hz 500-nit display (100% sRGB, 16:10 ratio)",
      "Liquid metal thermal paste & 5th Gen AeroBlade 3D metal fans",
      "Full 140W TGP RTX 4060 with 8GB VRAM (ready for 1440p gaming & AI LLMs)"
    ],
    cons: [
      "Heavy at 2.6kg with a massive 330W power brick",
      "Fans get loud under maximum Turbo mode"
    ],
    samarVerdict: "THE ULTIMATE PERFORMANCE MONSTER UNDER ₹1.15L. A true 20-core 14th Gen i7 paired with 140W RTX 4060 and a radiant 500-nit 2.5K screen. Exceptional for AI training, Blender 3D, and esports."
  },
  {
    id: "hp-omen-16-ryzen-7840hs-rtx4060",
    name: "HP OMEN 16 (Ryzen 7)",
    brand: "HP",
    series: "OMEN",
    price: 104990,
    originalPrice: 132990,
    rating: 4.6,
    reviewsCount: 880,
    image: "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 7",
      generation: "7000 Series",
      model: "AMD Ryzen 7 7840HS (8 Cores / 16 Threads with AI Engine)",
      cores: 8,
      threads: 16,
      baseSpeed: "3.8 GHz",
      boostSpeed: "5.1 GHz"
    },
    ram: 16,
    ramType: "DDR5 5600MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe Gen4 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4060",
      vram: "8GB GDDR6",
      tgp: "140W TGP"
    },
    display: {
      size: "16.1 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "165Hz",
      panel: "IPS 100% sRGB / 7ms response",
      brightness: "300 nits"
    },
    battery: {
      capacity: "83 Wh",
      lifeHours: 7,
      fastCharging: "HP Fast Charge (50% in 30 mins)"
    },
    weight: 2.37,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "ai", "editing"],
    benchmarkScores: {
      singleCore: 1910,
      multiCore: 16800,
      gamingFPS: 138,
      productivityScore: 95
    },
    pros: [
      "Zen 4 Ryzen 7 7840HS includes Ryzen AI NPU engine for on-device AI",
      "Full 140W TGP RTX 4060 with 8GB VRAM",
      "Clean, minimalist design that fits nicely in professional workspaces",
      "Great 83Wh battery and Bang & Olufsen tuned audio"
    ],
    cons: [
      "Screen is 1080p rather than 1440p",
      "Trackpad could be slightly larger"
    ],
    samarVerdict: "Stealthy gaming & developer powerhouse. The Ryzen 7 7840HS is one of the most balanced chips ever made: exceptional sustained performance with cool thermals and great battery life."
  },
  {
    id: "lenovo-legion-slim-5-ryzen-7840hs",
    name: "Lenovo Legion Slim 5 16 Gen 8",
    brand: "Lenovo",
    series: "Legion",
    price: 108990,
    originalPrice: 139990,
    rating: 4.8,
    reviewsCount: 1980,
    image: "https://images.unsplash.com/photo-1593642634315-48f5414c3ad9?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 7",
      generation: "7000 Series",
      model: "AMD Ryzen 7 7840HS (8 Cores / 16 Threads)",
      cores: 8,
      threads: 16,
      baseSpeed: "3.8 GHz",
      boostSpeed: "5.1 GHz"
    },
    ram: 16,
    ramType: "DDR5 5600MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB M.2 2280 PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4060",
      vram: "8GB GDDR6",
      tgp: "140W TGP"
    },
    display: {
      size: "16.0 inch",
      resolution: "WQXGA (2560x1600) 16:10",
      refreshRate: "165Hz",
      panel: "IPS 100% sRGB / 350 nits / Dolby Vision",
      brightness: "350 nits"
    },
    battery: {
      capacity: "80 Wh",
      lifeHours: 7.5,
      fastCharging: "Super Rapid Charge (80Wh in 60m)"
    },
    weight: 2.30,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "ai", "editing"],
    benchmarkScores: {
      singleCore: 1920,
      multiCore: 17100,
      gamingFPS: 142,
      productivityScore: 97
    },
    pros: [
      "Renowned Legion TrueStrike keyboard - best laptop keyboard on the market",
      "Stunning 2.5K 16:10 screen ideal for reading code and crisp 1440p gaming",
      "ColdFront 5.0 cooling with whisper-quiet balanced mode",
      "Premium aluminium A-cover and stealth aesthetic"
    ],
    cons: [
      "Can get heavy with the power brick for daily commute",
      "Audio speakers are standard"
    ],
    samarVerdict: "SAMAR'S HIGHEST RATED LAPTOP. Legion build quality and the legendary TrueStrike keyboard make this the holy grail for programmers who game after work."
  },
  {
    id: "asus-rog-zephyrus-g14-2024",
    name: "ASUS ROG Zephyrus G14 (2024 OLED)",
    brand: "ASUS",
    series: "ROG Zephyrus",
    price: 144990,
    originalPrice: 179990,
    rating: 4.9,
    reviewsCount: 820,
    image: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 7",
      generation: "8000 Series",
      model: "AMD Ryzen 7 8845HS (Zen 4 + Ryzen AI NPU)",
      cores: 8,
      threads: 16,
      baseSpeed: "3.8 GHz",
      boostSpeed: "5.1 GHz"
    },
    ram: 16,
    ramType: "LPDDR5X 6400MHz",
    ramExpandable: false,
    storage: 1000,
    storageType: "1TB PCIe 4.0 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4060",
      vram: "8GB GDDR6",
      tgp: "90W TGP"
    },
    display: {
      size: "14.0 inch",
      resolution: "3K OLED (2880x1800) 16:10",
      refreshRate: "120Hz 0.2ms",
      panel: "ROG Nebula OLED / 100% DCI-P3 / G-SYNC",
      brightness: "500 nits"
    },
    battery: {
      capacity: "73 Wh",
      lifeHours: 9.5,
      fastCharging: "100W USB-C PD Fast Charge"
    },
    weight: 1.50,
    os: "Windows 11 Home",
    suitableFor: ["editing", "coding", "gaming", "ai", "college"],
    benchmarkScores: {
      singleCore: 1980,
      multiCore: 17400,
      gamingFPS: 125,
      productivityScore: 99
    },
    pros: [
      "Unbelievable CNC aluminium unibody build - the MacBook of Windows laptops",
      "Only 1.50kg yet packs an RTX 4060 and Ryzen 8000 AI CPU",
      "Class-leading 3K 120Hz OLED screen (0.2ms response, 100% DCI-P3)",
      "Best 6-speaker audio system on any Windows laptop",
      "9+ hours of real-world battery endurance"
    ],
    cons: [
      "Premium price tag",
      "Soldered LPDDR5X RAM"
    ],
    samarVerdict: "THE PINNACLE PORTABLE POWERHOUSE. If you have the budget and want zero compromises between portability (1.5kg), OLED screen beauty, gaming, and 9-hour battery life, this is perfection."
  },

  // ==================== ULTRA HIGH-END & FLAGSHIPS (₹1,30,000 - ₹2,20,000+) ====================
  {
    id: "lenovo-legion-pro-5i-i7-14th-rtx4070",
    name: "Lenovo Legion Pro 5i (14th Gen / 32GB RAM)",
    brand: "Lenovo",
    series: "Legion Pro",
    price: 169990,
    originalPrice: 204990,
    rating: 4.8,
    reviewsCount: 1120,
    image: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "14th Gen",
      model: "Intel Core i7-14700HX (20 Cores: 8P + 12E / 28 Threads)",
      cores: 20,
      threads: 28,
      baseSpeed: "2.1 GHz",
      boostSpeed: "5.5 GHz"
    },
    ram: 32,
    ramType: "DDR5 5600MHz (2x16GB)",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4070",
      vram: "8GB GDDR6",
      tgp: "140W Max TGP"
    },
    display: {
      size: "16.0 inch",
      resolution: "WQXGA (2560x1600) 16:10",
      refreshRate: "240Hz",
      panel: "IPS 500 nits / 100% sRGB / HDR 400",
      brightness: "500 nits"
    },
    battery: {
      capacity: "80 Wh",
      lifeHours: 5,
      fastCharging: "300W Slim Tip (Super Rapid Charge)"
    },
    weight: 2.50,
    os: "Windows 11 Home",
    suitableFor: ["ai", "gaming", "editing", "coding"],
    benchmarkScores: {
      singleCore: 2100,
      multiCore: 24200,
      gamingFPS: 175,
      productivityScore: 100
    },
    pros: [
      "32GB DDR5 5600MHz RAM pre-installed for heavy AI models & virtual machines",
      "Beastly 140W RTX 4070 GPU with 240Hz 2.5K competitive esports display",
      "Unrivaled 20-core i7-14700HX processor performance",
      "Lenovo AI Engine+ tuning for zero micro-stutters"
    ],
    cons: [
      "Large power brick",
      "Battery life under 5 hours when not plugged in"
    ],
    samarVerdict: "SUPREME WORKSTATION & GAMING TITAN. 32GB RAM + RTX 4070 + 20 Cores makes this an unstoppable machine for AI researchers, 3D Unreal Engine developers, and 240Hz competitive gamers."
  },
  {
    id: "asus-rog-strix-g16-i7-13th",
    name: "ASUS ROG Strix G16 (2024)",
    brand: "ASUS",
    series: "ROG Strix",
    price: 139990,
    originalPrice: 174990,
    rating: 4.7,
    reviewsCount: 930,
    image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "13th Gen",
      model: "Intel Core i7-13650HX (14 Cores / 24 Threads)",
      cores: 14,
      threads: 24,
      baseSpeed: "2.6 GHz",
      boostSpeed: "4.9 GHz"
    },
    ram: 16,
    ramType: "DDR5 4800MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe 4.0 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4060",
      vram: "8GB GDDR6",
      tgp: "140W TGP"
    },
    display: {
      size: "16.0 inch",
      resolution: "FHD+ (1920x1200) 16:10",
      refreshRate: "165Hz",
      panel: "ROG Nebula Display / 100% sRGB",
      brightness: "300 nits"
    },
    battery: {
      capacity: "90 Wh",
      lifeHours: 6.5,
      fastCharging: "Fast charge 50% in 30 mins"
    },
    weight: 2.50,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "ai", "editing"],
    benchmarkScores: {
      singleCore: 1940,
      multiCore: 18600,
      gamingFPS: 140,
      productivityScore: 96
    },
    pros: [
      "Tri-Fan technology with Conductonaut Extreme liquid metal cooling",
      "Huge 90Wh battery with USB Type-C 100W PD charging support",
      "Underglow RGB lightbar with per-key Aura Sync customization",
      "Dedicated MUX switch and NVIDIA Advanced Optimus"
    ],
    cons: [
      "Screen is FHD+ rather than QHD at this price bracket",
      "Chassis has gamer aesthetic which might not suit corporate offices"
    ],
    samarVerdict: "Legendary cooling capability! ROG Strix G16 runs full-tilt during long gaming tournaments or compiling marathon sessions without ever thermal throttling."
  },
  {
    id: "dell-xps-14-core-ultra-7",
    name: "Dell XPS 14 (9440) Ultra 7 / 32GB",
    brand: "Dell",
    series: "XPS",
    price: 184990,
    originalPrice: 219990,
    rating: 4.5,
    reviewsCount: 420,
    image: "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "14th Gen",
      model: "Intel Core Ultra 7 155H (16 Cores / 22 Threads + NPU)",
      cores: 16,
      threads: 22,
      baseSpeed: "1.4 GHz",
      boostSpeed: "4.8 GHz"
    },
    ram: 32,
    ramType: "LPDDR5X 7467MHz",
    ramExpandable: false,
    storage: 1000,
    storageType: "1TB PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4050",
      vram: "6GB GDDR6",
      tgp: "30W Whisper Quiet"
    },
    display: {
      size: "14.5 inch",
      resolution: "3.2K OLED (3200x2000) Touch",
      refreshRate: "120Hz Variable",
      panel: "InfinityEdge OLED / 100% DCI-P3",
      brightness: "400 nits"
    },
    battery: {
      capacity: "69.5 Wh",
      lifeHours: 10,
      fastCharging: "ExpressCharge"
    },
    weight: 1.68,
    os: "Windows 11 Home",
    suitableFor: ["office", "college", "editing", "coding", "ai"],
    benchmarkScores: {
      singleCore: 1950,
      multiCore: 15800,
      gamingFPS: 72,
      productivityScore: 97
    },
    pros: [
      "Futuristic seamless glass touch touchpad and zero-lattice keyboard",
      "Integrated Intel AI Boost NPU engine for on-device AI tasks",
      "Stunning 3.2K 120Hz Touch OLED panel",
      "32GB ultra-high-speed 7467MHz RAM"
    ],
    cons: [
      "Only USB Type-C / Thunderbolt ports (requires dongle for Type-A)",
      "Premium luxury pricing"
    ],
    samarVerdict: "The luxury executive ultrabook. Impeccable CNC aluminum craftsmanship, whisper quiet acoustics, cutting-edge Intel Core Ultra 7 AI silicon and 32GB RAM."
  },
  {
    id: "apple-macbook-air-m3-16gb",
    name: "Apple MacBook Air 13 (M3 Chip / 16GB)",
    brand: "Apple",
    series: "MacBook Air",
    price: 124900,
    originalPrice: 134900,
    rating: 4.9,
    reviewsCount: 4800,
    image: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Apple",
      tier: "M3",
      generation: "M3 Series",
      model: "Apple M3 (8-Core CPU / 10-Core GPU)",
      cores: 8,
      threads: 8,
      baseSpeed: "Dynamic",
      boostSpeed: "4.05 GHz"
    },
    ram: 16,
    ramType: "Unified Memory 100GB/s",
    ramExpandable: false,
    storage: 512,
    storageType: "Apple Superfast PCIe SSD",
    gpu: {
      type: "Integrated",
      name: "Apple 10-Core GPU (Hardware Ray Tracing)",
      vram: "Unified"
    },
    display: {
      size: "13.6 inch",
      resolution: "Liquid Retina (2560x1664)",
      refreshRate: "60Hz",
      panel: "True Tone IPS / P3 Wide Color",
      brightness: "500 nits"
    },
    battery: {
      capacity: "52.6 Wh",
      lifeHours: 16,
      fastCharging: "MagSafe 3 Fast Charging"
    },
    weight: 1.24,
    os: "macOS Sonoma (Sequoia ready)",
    suitableFor: ["college", "office", "coding", "editing"],
    benchmarkScores: {
      singleCore: 3100,
      multiCore: 12100,
      gamingFPS: 55,
      productivityScore: 99
    },
    pros: [
      "Astounding 15-18 hour real-world battery life (leave charger at home)",
      "Zero fan noise - completely silent fanless operation forever",
      "Single-core performance is fastest in class (instant app launches)",
      "Best trackpad, speaker array, and resale value in the laptop industry"
    ],
    cons: [
      "Not designed for Windows PC gaming (DirectX limitations)",
      "Memory & SSD cannot be upgraded after purchase"
    ],
    samarVerdict: "THE UNCONTESTED KING OF BATTERY LIFE & BUILD QUALITY. If you are a college student or developer working in iOS, web, or cloud, nothing touches the M3 MacBook Air for battery and portability."
  },
  {
    id: "hp-victus-15-i5-13th-rtx2050",
    name: "HP Victus 15 (13th Gen)",
    brand: "HP",
    series: "Victus",
    price: 58990,
    originalPrice: 76990,
    rating: 4.3,
    reviewsCount: 2100,
    image: "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i5",
      generation: "13th Gen",
      model: "Intel Core i5-13420H (8 Cores: 4P + 4E / 12 Threads)",
      cores: 8,
      threads: 12,
      baseSpeed: "2.1 GHz",
      boostSpeed: "4.6 GHz"
    },
    ram: 16,
    ramType: "DDR4 3200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "PCIe Gen4 NVMe SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 2050",
      vram: "4GB GDDR6",
      tgp: "50W TGP"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS Anti-Glare",
      brightness: "250 nits"
    },
    battery: {
      capacity: "52.5 Wh",
      lifeHours: 5.5,
      fastCharging: "HP Fast Charge (50% in 30 mins)"
    },
    weight: 2.29,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "college"],
    benchmarkScores: {
      singleCore: 1710,
      multiCore: 9900,
      gamingFPS: 62,
      productivityScore: 86
    },
    pros: [
      "Affordable entry into NVIDIA dedicated graphics under ₹60K",
      "Smooth 144Hz high refresh rate screen",
      "Clean understated design suitable for college lecture halls",
      "Upgrade-friendly dual RAM slots"
    ],
    cons: [
      "4GB VRAM limits maximum texture quality in modern AAA games",
      "Screen brightness is basic 250 nits"
    ],
    samarVerdict: "Solid entry-level gaming machine for casual gamers, engineering students using AutoCAD, and programmers who want dedicated GPU acceleration under ₹60K."
  },
  {
    id: "msi-thin-15-i7-13th-rtx4050",
    name: "MSI Thin 15 (13th Gen)",
    brand: "MSI",
    series: "Thin",
    price: 74990,
    originalPrice: 94990,
    rating: 4.2,
    reviewsCount: 760,
    image: "https://images.unsplash.com/photo-1595327656903-2f54e37ce09b?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "13th Gen",
      model: "Intel Core i7-13620H (10 Cores: 6P + 4E / 16 Threads)",
      cores: 10,
      threads: 16,
      baseSpeed: "2.4 GHz",
      boostSpeed: "4.9 GHz"
    },
    ram: 16,
    ramType: "DDR5 5200MHz",
    ramExpandable: true,
    storage: 512,
    storageType: "NVMe PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4050",
      vram: "6GB GDDR6",
      tgp: "45W TGP"
    },
    display: {
      size: "15.6 inch",
      resolution: "Full HD (1920x1080)",
      refreshRate: "144Hz",
      panel: "IPS-Level Matrix",
      brightness: "250 nits"
    },
    battery: {
      capacity: "52.4 Wh",
      lifeHours: 4.5,
      fastCharging: "120W Adapter"
    },
    weight: 1.86,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "coding", "editing"],
    benchmarkScores: {
      singleCore: 1830,
      multiCore: 13900,
      gamingFPS: 82,
      productivityScore: 89
    },
    pros: [
      "Genuine 13th Gen Core i7 under ₹75,000",
      "Very light for a gaming laptop at just 1.86kg",
      "Brushed hair-line aluminium aesthetics",
      "Fast DDR5 memory"
    ],
    cons: [
      "45W TGP limits RTX 4050 maximum potential",
      "Single fan cooling requires keeping vents clear"
    ],
    samarVerdict: "A lightweight compromise for those who want an Intel Core i7 processor and an RTX 4050 GPU in a sub-2kg chassis under ₹75,000."
  },
  {
    id: "acer-predator-helios-16-i7-13th-rtx4070",
    name: "Acer Predator Helios 16 (13th Gen / RTX 4070)",
    brand: "Acer",
    series: "Predator",
    price: 154990,
    originalPrice: 189990,
    rating: 4.7,
    reviewsCount: 680,
    image: "https://images.unsplash.com/photo-1544652478-6653e09f18a2?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "Intel",
      tier: "i7",
      generation: "13th Gen",
      model: "Intel Core i7-13700HX (16 Cores: 8P + 8E / 24 Threads)",
      cores: 16,
      threads: 24,
      baseSpeed: "2.1 GHz",
      boostSpeed: "5.0 GHz"
    },
    ram: 16,
    ramType: "DDR5 5600MHz",
    ramExpandable: true,
    storage: 1000,
    storageType: "1TB PCIe Gen4 SSD",
    gpu: {
      type: "Dedicated",
      name: "NVIDIA GeForce RTX 4070",
      vram: "8GB GDDR6",
      tgp: "140W Max TGP"
    },
    display: {
      size: "16.0 inch",
      resolution: "WQXGA (2560x1600) 16:10",
      refreshRate: "240Hz",
      panel: "IPS 500 nits / 100% DCI-P3 / G-SYNC",
      brightness: "500 nits"
    },
    battery: {
      capacity: "90 Wh",
      lifeHours: 5,
      fastCharging: "330W Adapter"
    },
    weight: 2.65,
    os: "Windows 11 Home",
    suitableFor: ["gaming", "ai", "editing", "coding"],
    benchmarkScores: {
      singleCore: 2010,
      multiCore: 21500,
      gamingFPS: 170,
      productivityScore: 99
    },
    pros: [
      "140W RTX 4070 delivers max FPS in Cyberpunk 2077 & Black Myth Wukong",
      "Gorgeous 240Hz 500-nit WQXGA screen with 100% DCI-P3 gamut",
      "Dual 5th Gen AeroBlade 3D fans with liquid metal cooling",
      "Full RGB per-key keyboard with mini-LED backlights"
    ],
    cons: [
      "Heavy carrying weight (2.65kg)",
      "Loud turbo cooling fan profile"
    ],
    samarVerdict: "Uncompromised enthusiast power. If your focus is maxed-out 1440p gaming or 3D animations with an RTX 4070 under ₹1.6L, this Predator is a beast."
  },
  {
    id: "hp-pavilion-plus-14-oled-ryzen-7840u",
    name: "HP Pavilion Plus 14 (OLED)",
    brand: "HP",
    series: "Pavilion Plus",
    price: 79990,
    originalPrice: 96990,
    rating: 4.6,
    reviewsCount: 710,
    image: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=60",
    processor: {
      brand: "AMD",
      tier: "Ryzen 7",
      generation: "7000 Series",
      model: "AMD Ryzen 7 7840U (8 Cores / 16 Threads + Ryzen AI)",
      cores: 8,
      threads: 16,
      baseSpeed: "3.3 GHz",
      boostSpeed: "5.1 GHz"
    },
    ram: 16,
    ramType: "LPDDR5X 6400MHz",
    ramExpandable: false,
    storage: 1000,
    storageType: "1TB PCIe Gen4 NVMe SSD",
    gpu: {
      type: "Integrated",
      name: "AMD Radeon 780M (Near GTX 1650 performance)",
      vram: "Shared"
    },
    display: {
      size: "14.0 inch",
      resolution: "2.8K OLED (2880x1800) 16:10",
      refreshRate: "120Hz VRR",
      panel: "IMAX Enhanced OLED / 100% DCI-P3 / 500 nits HDR",
      brightness: "500 nits"
    },
    battery: {
      capacity: "68 Wh",
      lifeHours: 11,
      fastCharging: "65W USB-C (50% in 30 mins)"
    },
    weight: 1.38,
    os: "Windows 11 Home + MS Office 2021",
    suitableFor: ["college", "coding", "editing", "office"],
    benchmarkScores: {
      singleCore: 1880,
      multiCore: 14600,
      gamingFPS: 58,
      productivityScore: 96
    },
    pros: [
      "Radeon 780M is the most powerful integrated GPU in existence - plays GTA V & Forza smoothly",
      "Spectacular 2.8K 120Hz IMAX Enhanced OLED display",
      "All-metal slim 1.38kg frame with 11-hour battery life",
      "Generous 1TB SSD & 16GB ultra-fast 6400MHz RAM"
    ],
    cons: [
      "Soldered RAM",
      "Glossy glass screen has reflections in bright sunlight"
    ],
    samarVerdict: "SAMAR'S ULTIMATE SLIM & POWERFUL RECOMMENDATION. The 7840U + Radeon 780M gives you gaming-class iGPU speeds in an ultra-portable 1.38kg shell with 11 hours of battery."
  }
];

const QUICK_PRESETS = [
  {
    title: "Best Student Budget (< ₹45K)",
    budget: 45000,
    purpose: "college",
    processor: "any",
    ram: "any",
    storage: "any",
    brand: "all"
  },
  {
    title: "Coding & Dev Machine (₹55K - ₹70K)",
    budget: 65000,
    purpose: "coding",
    processor: "intel-i5",
    ram: "16",
    storage: "512",
    brand: "all"
  },
  {
    title: "Affordable RTX 4050 Gaming (< ₹80K)",
    budget: 80000,
    purpose: "gaming",
    processor: "any",
    ram: "16",
    storage: "any",
    brand: "all"
  },
  {
    title: "AI, ML & 3D Workstation (₹1L - ₹1.5L)",
    budget: 130000,
    purpose: "ai",
    processor: "intel-i7",
    ram: "16",
    storage: "1000",
    brand: "all"
  },
  {
    title: "All-Day Battery Ultrabook (10+ hrs)",
    budget: 130000,
    purpose: "college",
    processor: "any",
    ram: "16",
    storage: "512",
    brand: "all"
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LAPTOPS_DATA, QUICK_PRESETS };
}
"""
    target = os.path.join(BASE_DIR, "data.js")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated data.js successfully.")


def make_app_js():
    content = r"""// SAMAR Laptop Choice Portal - Interactive Recommendation Engine & UI Logic

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
  selectedLaptop: null
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
    desc: "Dedicated RTX GPU (high TGP), 144Hz+ display, high thermal cooling"
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

// Calculate Samar Match Score (0 - 100)
function calculateSamarScore(laptop, filters) {
  let score = 50; // baseline
  const budget = filters.budget;
  const isFlexible = filters.isBudgetFlexible;
  const maxBudget = isFlexible ? budget * 1.05 : budget;

  // 1. Budget Suitability (up to 30 pts)
  if (laptop.price <= budget) {
    // Under budget: Reward getting great specs without wasting budget
    const budgetUtilization = laptop.price / budget;
    if (budgetUtilization >= 0.75 && budgetUtilization <= 1.0) {
      score += 30; // Sweet spot: utilizes budget fully for high specs
    } else if (budgetUtilization < 0.75) {
      score += 24; // Great savings
    }
  } else if (laptop.price <= maxBudget) {
    score += 18; // Slight stretch (+5%) but acceptable in flexible mode
  } else {
    // Far above budget
    return 0; // Exclude
  }

  // 2. Purpose Match (up to 30 pts)
  if (filters.purpose && filters.purpose !== 'all') {
    if (laptop.suitableFor.includes(filters.purpose)) {
      score += 25;
    } else {
      score -= 15;
    }

    // Specific purpose bonus logic
    if (filters.purpose === 'gaming') {
      if (laptop.gpu.type === 'Dedicated') {
        score += 10;
        if (laptop.gpu.name.includes('RTX 40') || laptop.gpu.name.includes('RTX 30')) score += 5;
      } else {
        score -= 25; // integrated graphics penalised heavily for gaming
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
    score += 15; // Neutral purpose
  }

  // 3. Processor Match (up to 15 pts)
  if (filters.processor !== 'any') {
    const pTier = laptop.processor.tier.toLowerCase();
    const pGen = laptop.processor.generation.toLowerCase();
    const pBrand = laptop.processor.brand.toLowerCase();

    if (filters.processor === 'intel-i3' && pBrand === 'intel' && pTier === 'i3') score += 15;
    else if (filters.processor === 'intel-i5' && pBrand === 'intel' && pTier === 'i5') score += 15;
    else if (filters.processor === 'intel-i7' && pBrand === 'intel' && pTier === 'i7') score += 15;
    else if (filters.processor === 'intel-13th' && pGen.includes('13th')) score += 15;
    else if (filters.processor === 'intel-14th' && pGen.includes('14th')) score += 15;
    else if (filters.processor === 'amd-ryzen-3' && pTier.includes('ryzen 3')) score += 15;
    else if (filters.processor === 'amd-ryzen-5' && pTier.includes('ryzen 5')) score += 15;
    else if (filters.processor === 'amd-ryzen-7' && pTier.includes('ryzen 7')) score += 15;
    else if (filters.processor === 'amd-ryzen-all' && pBrand === 'amd') score += 15;
    else if (filters.processor === 'apple-m' && pBrand === 'apple') score += 15;
    else score -= 15;
  }

  // 4. RAM Match (up to 10 pts)
  if (filters.ram !== 'any') {
    const reqRam = parseInt(filters.ram);
    if (laptop.ram === reqRam) score += 10;
    else if (laptop.ram > reqRam) score += 7; // more RAM is always welcomed
    else score -= 12; // less RAM than desired
  }

  // 5. Storage Match (up to 10 pts)
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

  // Rating & Review Bonus
  score += Math.round((laptop.rating - 4.0) * 10);

  // Clamp score between 10 and 99
  return Math.min(99, Math.max(10, score));
}

// Format currency in Indian Rupees ₹
function formatINR(amount) {
  return "₹" + amount.toLocaleString('en-IN');
}

// Format RAM string
function formatRAM(gb) {
  return `${gb} GB`;
}

// Format Storage string
function formatStorage(gb) {
  if (gb >= 1000) {
    return `${gb / 1000} TB SSD`;
  }
  return `${gb} GB SSD`;
}

// Filter laptops
function getFilteredAndScoredLaptops() {
  const maxBudget = state.isBudgetFlexible ? state.budget * 1.05 : state.budget;

  let results = LAPTOPS_DATA.map(laptop => {
    const score = calculateSamarScore(laptop, state);
    return {
      ...laptop,
      samarScore: score,
      isSlightStretch: laptop.price > state.budget && laptop.price <= maxBudget
    };
  });

  // Strict filters
  results = results.filter(laptop => {
    // Budget check
    if (laptop.price > maxBudget) return false;

    // Brand filter if explicitly selected
    if (state.brand !== 'all' && laptop.brand.toLowerCase() !== state.brand.toLowerCase()) {
      return false;
    }

    // Processor strict filter if explicitly chosen
    if (state.processor !== 'any') {
      const p = laptop.processor;
      if (state.processor === 'intel-i3' && !(p.brand === 'Intel' && p.tier === 'i3')) return false;
      if (state.processor === 'intel-i5' && !(p.brand === 'Intel' && p.tier === 'i5')) return false;
      if (state.processor === 'intel-i7' && !(p.brand === 'Intel' && p.tier === 'i7')) return false;
      if (state.processor === 'intel-13th' && !(p.brand === 'Intel' && p.generation.includes('13th'))) return false;
      if (state.processor === 'intel-14th' && !(p.brand === 'Intel' && p.generation.includes('14th'))) return false;
      if (state.processor === 'amd-ryzen-3' && !(p.brand === 'AMD' && p.tier.includes('3'))) return false;
      if (state.processor === 'amd-ryzen-5' && !(p.brand === 'AMD' && p.tier.includes('5'))) return false;
      if (state.processor === 'amd-ryzen-7' && !(p.brand === 'AMD' && p.tier.includes('7'))) return false;
      if (state.processor === 'amd-ryzen-all' && p.brand !== 'AMD') return false;
      if (state.processor === 'apple-m' && p.brand !== 'Apple') return false;
    }

    // RAM minimum filter
    if (state.ram !== 'any') {
      const minRam = parseInt(state.ram);
      if (laptop.ram < minRam) return false;
    }

    // Storage minimum filter
    if (state.storage !== 'any') {
      const minStorage = parseInt(state.storage);
      if (laptop.storage < minStorage) return false;
    }

    // Purpose filter (if selected and strict)
    if (state.purpose !== 'all') {
      if (!laptop.suitableFor.includes(state.purpose)) return false;
    }

    // Text search query
    if (state.searchQuery.trim()) {
      const q = state.searchQuery.toLowerCase();
      const matchName = laptop.name.toLowerCase().includes(q);
      const matchBrand = laptop.brand.toLowerCase().includes(q);
      const matchCPU = laptop.processor.model.toLowerCase().includes(q);
      const matchGPU = laptop.gpu.name.toLowerCase().includes(q);
      if (!matchName && !matchBrand && !matchCPU && !matchGPU) return false;
    }

    return true;
  });

  // Sorting
  results.sort((a, b) => {
    if (state.sortBy === 'samar-match') {
      return b.samarScore - a.samarScore;
    } else if (state.sortBy === 'price-low') {
      return a.price - b.price;
    } else if (state.sortBy === 'price-high') {
      return b.price - a.price;
    } else if (state.sortBy === 'rating') {
      return b.rating - a.rating;
    } else if (state.sortBy === 'cpu-power') {
      return b.benchmarkScores.multiCore - a.benchmarkScores.multiCore;
    } else if (state.sortBy === 'gaming-fps') {
      return b.benchmarkScores.gamingFPS - a.benchmarkScores.gamingFPS;
    }
    return 0;
  });

  return results;
}

// Render UI Components
function renderApp() {
  renderBudgetControls();
  renderPurposeCards();
  renderPresets();
  renderResults();
  renderCompareBar();
  lucide.createIcons();
}

// Budget Controls
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

// Purpose Cards
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

  // Attach click events
  container.querySelectorAll('.purpose-card').forEach(card => {
    card.addEventListener('click', () => {
      state.purpose = card.dataset.purpose;
      renderApp();
    });
  });
}

// Presets
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

// Synchronize Dropdowns & Radio Buttons with State
function updateFilterControls() {
  // Processor Select
  const procSelect = document.getElementById('processorSelect');
  if (procSelect) procSelect.value = state.processor;

  // RAM Select
  const ramSelect = document.getElementById('ramSelect');
  if (ramSelect) ramSelect.value = state.ram;

  // Storage Select
  const storageSelect = document.getElementById('storageSelect');
  if (storageSelect) storageSelect.value = state.storage;

  // Brand Select
  const brandSelect = document.getElementById('brandSelect');
  if (brandSelect) brandSelect.value = state.brand;

  // Search
  const searchInput = document.getElementById('searchInput');
  if (searchInput) searchInput.value = state.searchQuery;

  // Sort
  const sortSelect = document.getElementById('sortSelect');
  if (sortSelect) sortSelect.value = state.sortBy;
}

// Results Section
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
    spotlightBanner.classList.remove('hidden');
    spotlightBanner.innerHTML = `
      <div class="spotlight-card">
        <div class="spotlight-badge">
          <i data-lucide="crown"></i>
          <span>SAMAR'S #1 TOP RECOMMENDATION</span>
        </div>
        <div class="spotlight-body">
          <div class="spotlight-image-col">
            <img src="${topPick.image}" alt="${topPick.name}" class="spotlight-img" />
            <div class="score-pill">
              <span class="score-num">${topPick.samarScore}%</span>
              <span class="score-label">Samar Match</span>
            </div>
          </div>
          <div class="spotlight-info-col">
            <div class="spotlight-header">
              <div>
                <span class="brand-pill">${topPick.brand}</span>
                <h2 class="spotlight-title">${topPick.name}</h2>
              </div>
              <div class="spotlight-price-box">
                <div class="spotlight-price">${formatINR(topPick.price)}</div>
                <div class="spotlight-orig-price">${formatINR(topPick.originalPrice)}</div>
                <div class="discount-badge">${Math.round((1 - topPick.price / topPick.originalPrice) * 100)}% OFF</div>
              </div>
            </div>

            <div class="specs-pill-grid">
              <div class="spec-pill"><i data-lucide="cpu"></i><span>${topPick.processor.model}</span></div>
              <div class="spec-pill"><i data-lucide="circuit-board"></i><span>${formatRAM(topPick.ram)} ${topPick.ramType}</span></div>
              <div class="spec-pill"><i data-lucide="hard-drive"></i><span>${formatStorage(topPick.storage)}</span></div>
              <div class="spec-pill"><i data-lucide="monitor"></i><span>${topPick.display.size} ${topPick.display.panel} (${topPick.display.refreshRate})</span></div>
              <div class="spec-pill"><i data-lucide="zap"></i><span>${topPick.gpu.name} ${topPick.gpu.tgp ? `(${topPick.gpu.tgp})` : ''}</span></div>
              <div class="spec-pill"><i data-lucide="battery-charging"></i><span>${topPick.battery.lifeHours}h Battery (${topPick.weight} kg)</span></div>
            </div>

            <div class="samar-quote">
              <i data-lucide="quote" class="quote-icon"></i>
              <p><strong>Why Samar picked this for you:</strong> ${topPick.samarVerdict}</p>
            </div>

            <div class="spotlight-actions">
              <button class="btn btn-primary" onclick="openDetailsModal('${topPick.id}')">
                <i data-lucide="info"></i> View Full Specifications
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
    } else if (laptop.benchmarkScores.multiCore >= 15000) {
      badgeHtml = `<div class="card-badge badge-power"><i data-lucide="flame"></i> Performance Beast</div>`;
    } else if (laptop.battery.lifeHours >= 9) {
      badgeHtml = `<div class="card-badge badge-battery"><i data-lucide="battery-charging"></i> Marathon Battery</div>`;
    } else if (laptop.isSlightStretch) {
      badgeHtml = `<div class="card-badge badge-stretch"><i data-lucide="arrow-up-right"></i> Worth +5% Stretch</div>`;
    }

    return `
      <div class="laptop-card" id="card-${laptop.id}">
        ${badgeHtml}
        <div class="card-img-wrap">
          <img src="${laptop.image}" alt="${laptop.name}" class="card-img" loading="lazy" />
          <div class="card-score-badge">
            <span class="score-percent">${laptop.samarScore}%</span>
            <span class="score-tag">Match</span>
          </div>
        </div>

        <div class="card-content">
          <div class="card-meta">
            <span class="brand-tag">${laptop.brand}</span>
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
            <div class="spec-mini-item" title="Graphics">
              <i data-lucide="sparkles"></i>
              <span>${laptop.gpu.name}</span>
            </div>
            <div class="spec-mini-item" title="Display">
              <i data-lucide="monitor"></i>
              <span>${laptop.display.size} ${laptop.display.resolution.split('(')[0]} (${laptop.display.refreshRate})</span>
            </div>
          </div>

          <div class="card-verdict-snippet">
            <strong>Samar's Take:</strong> ${laptop.samarVerdict.length > 110 ? laptop.samarVerdict.slice(0, 110) + '...' : laptop.samarVerdict}
          </div>

          <div class="card-footer">
            <div class="card-price-wrap">
              <div class="card-price">${formatINR(laptop.price)}</div>
              <div class="card-orig-price">${formatINR(laptop.originalPrice)}</div>
            </div>
            <div class="card-btn-group">
              <button class="btn btn-sm btn-outline" onclick="openDetailsModal('${laptop.id}')" title="Details">
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

// Comparison Tray & Modal
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
            <img src="${l.image}" alt="${l.name}" />
            <span class="compare-thumb-name">${l.name.split(' ')[0]} ${l.name.split(' ')[1] || ''}</span>
            <button class="compare-thumb-remove" onclick="toggleCompare('${l.id}')">×</button>
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
            ${laptops.map(l => `
              <th>
                <div class="table-laptop-header">
                  <img src="${l.image}" alt="${l.name}" class="table-img" />
                  <h4>${l.name}</h4>
                  <div class="table-price">${formatINR(l.price)}</div>
                  <button class="btn btn-sm btn-primary" onclick="openDetailsModal('${l.id}')">View Details</button>
                </div>
              </th>
            `).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Samar Match Score</strong></td>
            ${laptops.map(l => `<td><span class="score-pill-sm">${calculateSamarScore(l, state)}% Match</span></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Processor</strong></td>
            ${laptops.map(l => `<td>${l.processor.model}<br><small class="text-muted">${l.processor.cores} Cores / ${l.processor.threads} Threads</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>RAM & Upgradability</strong></td>
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
            <td><strong>Display & Refresh</strong></td>
            ${laptops.map(l => `<td>${l.display.size} ${l.display.resolution}<br><small class="text-muted">${l.display.panel} | ${l.display.refreshRate}</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Battery & Weight</strong></td>
            ${laptops.map(l => `<td>${l.battery.lifeHours} hrs (${l.battery.capacity})<br><small class="text-muted">${l.weight} kg</small></td>`).join('')}
          </tr>
          <tr>
            <td><strong>Operating System</strong></td>
            ${laptops.map(l => `<td>${l.os}</td>`).join('')}
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

// Details Modal
function openDetailsModal(id) {
  const laptop = LAPTOPS_DATA.find(l => l.id === id);
  if (!laptop) return;

  const modal = document.getElementById('detailsModal');
  const content = document.getElementById('detailsModalContent');
  if (!modal || !content) return;

  const score = calculateSamarScore(laptop, state);

  content.innerHTML = `
    <div class="details-modal-grid">
      <div class="details-img-col">
        <img src="${laptop.image}" alt="${laptop.name}" class="details-img" />
        <div class="details-score-box">
          <div class="score-circle">
            <span class="score-circle-num">${score}%</span>
            <span class="score-circle-lbl">Samar Score</span>
          </div>
          <div class="score-explanation">
            <h4>Recommendation Strength</h4>
            <p>Calculated based on your budget of ${formatINR(state.budget)}, processor preference, and workflow requirements.</p>
          </div>
        </div>

        <div class="benchmarks-box">
          <h4>Performance Benchmarks</h4>
          <div class="benchmark-item">
            <div class="benchmark-meta">
              <span>Multi-Core CPU Power</span>
              <span>${laptop.benchmarkScores.multiCore} pts</span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill" style="width: ${Math.min(100, (laptop.benchmarkScores.multiCore / 25000) * 100)}%"></div></div>
          </div>
          <div class="benchmark-item">
            <div class="benchmark-meta">
              <span>Gaming & 3D Render FPS</span>
              <span>${laptop.benchmarkScores.gamingFPS} FPS</span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill bar-fill-gaming" style="width: ${Math.min(100, (laptop.benchmarkScores.gamingFPS / 180) * 100)}%"></div></div>
          </div>
          <div class="benchmark-item">
            <div class="benchmark-meta">
              <span>Productivity & Multitasking</span>
              <span>${laptop.benchmarkScores.productivityScore} / 100</span>
            </div>
            <div class="benchmark-bar"><div class="bar-fill bar-fill-productivity" style="width: ${laptop.benchmarkScores.productivityScore}%"></div></div>
          </div>
        </div>
      </div>

      <div class="details-info-col">
        <div class="details-header">
          <div>
            <span class="brand-pill">${laptop.brand}</span>
            <h2>${laptop.name}</h2>
          </div>
          <div class="details-pricing">
            <div class="details-price">${formatINR(laptop.price)}</div>
            <div class="details-orig">${formatINR(laptop.originalPrice)}</div>
          </div>
        </div>

        <div class="samar-analysis-box">
          <div class="analysis-tag"><i data-lucide="brain"></i> Samar's Deep Analysis</div>
          <p>${laptop.samarVerdict}</p>
        </div>

        <div class="details-tabs-content">
          <h3>Full Specifications</h3>
          <div class="spec-table-grid">
            <div class="spec-row"><span class="spec-k">Processor</span><span class="spec-v">${laptop.processor.model} (${laptop.processor.cores}C/${laptop.processor.threads}T, Up to ${laptop.processor.boostSpeed})</span></div>
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
          <button class="btn btn-primary" onclick="alert('This laptop is available at major electronics retailers and authorized brand stores in India.')">
            <i data-lucide="shopping-bag"></i> Check Local & Online Availability
          </button>
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

// Reset filters to default
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
  updateFilterControls();
  renderApp();
}

// Setup Event Listeners
function initEventListeners() {
  // Budget Slider
  const slider = document.getElementById('budgetSlider');
  const input = document.getElementById('budgetInput');
  const flexToggle = document.getElementById('flexBudgetToggle');

  if (slider) {
    slider.addEventListener('input', (e) => {
      state.budget = parseInt(e.target.value);
      renderBudgetControls();
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

  // Budget Quick Chips
  document.querySelectorAll('.budget-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      state.budget = parseInt(chip.dataset.budget);
      renderBudgetControls();
      renderResults();
    });
  });

  // Processor Dropdown
  const procSelect = document.getElementById('processorSelect');
  if (procSelect) {
    procSelect.addEventListener('change', (e) => {
      state.processor = e.target.value;
      renderResults();
    });
  }

  // RAM Dropdown
  const ramSelect = document.getElementById('ramSelect');
  if (ramSelect) {
    ramSelect.addEventListener('change', (e) => {
      state.ram = e.target.value;
      renderResults();
    });
  }

  // Storage Dropdown
  const storageSelect = document.getElementById('storageSelect');
  if (storageSelect) {
    storageSelect.addEventListener('change', (e) => {
      state.storage = e.target.value;
      renderResults();
    });
  }

  // Brand Dropdown
  const brandSelect = document.getElementById('brandSelect');
  if (brandSelect) {
    brandSelect.addEventListener('change', (e) => {
      state.brand = e.target.value;
      renderResults();
    });
  }

  // Search Input
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderResults();
    });
  }

  // Sort Dropdown
  const sortSelect = document.getElementById('sortSelect');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      renderResults();
    });
  }

  // Close Modals on overlay or escape
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

// Initial Boot
document.addEventListener('DOMContentLoaded', () => {
  initEventListeners();
  updateFilterControls();
  renderApp();
});
"""
    target = os.path.join(BASE_DIR, "app.js")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated app.js successfully.")


def make_styles_css():
    content = r"""/* SAMAR Laptop Choice Portal - Modern Futuristic Tech Theme */

:root {
  --bg-primary: #0a0d14;
  --bg-surface: #121826;
  --bg-surface-elevated: #1a2234;
  --bg-surface-hover: #222d42;
  --border-subtle: #232f48;
  --border-focus: #3b82f6;

  --accent-cyan: #06b6d4;
  --accent-blue: #3b82f6;
  --accent-purple: #8b5cf6;
  --accent-emerald: #10b981;
  --accent-amber: #f59e0b;
  --accent-rose: #f43f5e;

  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #64748b;

  --font-heading: 'Outfit', sans-serif;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-full: 9999px;

  --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
  --shadow-md: 0 8px 24px rgba(0,0,0,0.4);
  --shadow-lg: 0 16px 40px rgba(0,0,0,0.6);
  --shadow-glow: 0 0 25px rgba(59, 130, 246, 0.25);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-main);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Background ambient light effects */
.bg-glow-orb-1 {
  position: fixed;
  top: -100px;
  left: -100px;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(0, 0, 0, 0) 70%);
  pointer-events: none;
  z-index: 0;
}

.bg-glow-orb-2 {
  position: fixed;
  top: 30%;
  right: -150px;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, rgba(0, 0, 0, 0) 70%);
  pointer-events: none;
  z-index: 0;
}

.app-wrapper {
  position: relative;
  z-index: 1;
  max-width: 1380px;
  margin: 0 auto;
  padding: 0 24px 80px;
}

/* Header */
.portal-header {
  padding: 24px 0 20px;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 28px;
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-icon-box {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  box-shadow: 0 0 20px rgba(59, 130, 246, 0.4);
}

.brand-title {
  font-family: var(--font-heading);
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(120deg, #ffffff 40%, var(--accent-cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.brand-tagline {
  font-size: 13px;
  color: var(--text-muted);
}

.header-badges {
  display: flex;
  gap: 10px;
}

.pill-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: var(--radius-full);
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.25);
  color: #60a5fa;
}

/* Hero Title Section */
.hero-section {
  text-align: center;
  margin-bottom: 36px;
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 700;
  color: var(--accent-cyan);
  background: rgba(6, 182, 212, 0.1);
  border: 1px solid rgba(6, 182, 212, 0.25);
  padding: 4px 12px;
  border-radius: var(--radius-full);
  margin-bottom: 12px;
}

.hero-heading {
  font-family: var(--font-heading);
  font-size: 38px;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-bottom: 10px;
}

.hero-heading span {
  background: linear-gradient(135deg, #60a5fa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-sub {
  color: var(--text-muted);
  font-size: 16px;
  max-width: 680px;
  margin: 0 auto;
}

/* Quick Preset Strip */
.presets-strip {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 30px;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 12px 20px;
  overflow-x: auto;
}

.presets-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: var(--accent-amber);
  white-space: nowrap;
}

.preset-chips-wrap {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}

.preset-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-main);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}

.preset-chip:hover {
  background: var(--border-subtle);
  border-color: var(--accent-blue);
  color: #fff;
  transform: translateY(-1px);
}

/* Control Hub / Filters Section */
.control-hub {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 28px;
  margin-bottom: 36px;
  box-shadow: var(--shadow-md);
}

.hub-section-title {
  font-family: var(--font-heading);
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--text-main);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Purpose Grid */
.purpose-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 12px;
  margin-bottom: 28px;
}

.purpose-card {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
}

.purpose-card:hover {
  background: var(--bg-surface-hover);
  border-color: #3b82f6;
  transform: translateY(-2px);
}

.purpose-card.active {
  background: rgba(59, 130, 246, 0.12);
  border-color: #3b82f6;
  box-shadow: 0 0 20px rgba(59, 130, 246, 0.2);
}

.purpose-icon {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-cyan);
  margin-bottom: 10px;
}

.purpose-card.active .purpose-icon {
  background: var(--accent-blue);
  color: #fff;
}

.purpose-name {
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
}

.purpose-desc {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.35;
}

/* Secondary Filter Matrix */
.filter-matrix {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr 1fr 1fr;
  gap: 20px;
  align-items: start;
  padding-top: 20px;
  border-top: 1px solid var(--border-subtle);
}

@media (max-width: 1024px) {
  .filter-matrix {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .filter-matrix {
    grid-template-columns: 1fr;
  }
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter-label {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.budget-val-badge {
  font-family: var(--font-heading);
  font-size: 18px;
  font-weight: 800;
  color: #60a5fa;
}

/* Budget Slider & Input */
.budget-box {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.slider-custom {
  -webkit-appearance: none;
  width: 100%;
  height: 8px;
  border-radius: 4px;
  background: var(--border-subtle);
  outline: none;
}

.slider-custom::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: linear-gradient(135deg, #3b82f6, #06b6d4);
  cursor: pointer;
  box-shadow: 0 0 10px rgba(59, 130, 246, 0.6);
  border: 2px solid #ffffff;
}

.budget-sub-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.budget-num-input-wrap {
  display: flex;
  align-items: center;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 6px 10px;
  width: 130px;
}

.currency-sym {
  color: var(--text-muted);
  font-weight: 600;
  margin-right: 4px;
}

.budget-input-field {
  background: transparent;
  border: none;
  outline: none;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  width: 100%;
}

.flex-budget-label {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--text-muted);
  cursor: pointer;
}

.flex-budget-label input[type="checkbox"] {
  accent-color: var(--accent-blue);
  cursor: pointer;
}

/* Dropdowns & Selects */
.select-custom {
  width: 100%;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  color: #fff;
  font-size: 13px;
  font-weight: 500;
  outline: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.select-custom:focus {
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}

.select-custom option {
  background: var(--bg-surface-elevated);
  color: #fff;
}

/* Search and Sort Toolbar */
.toolbar-strip {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  gap: 16px;
  flex-wrap: wrap;
}

.search-box-wrap {
  position: relative;
  flex: 1;
  max-width: 450px;
}

.search-icon-inside {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  pointer-events: none;
}

.search-input-field {
  width: 100%;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 10px 16px 10px 42px;
  color: #fff;
  font-size: 14px;
  outline: none;
  transition: all 0.2s ease;
}

.search-input-field:focus {
  border-color: var(--accent-blue);
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
}

.toolbar-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.results-count-badge {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  padding: 8px 14px;
  border-radius: var(--radius-full);
}

.sort-dropdown-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sort-dropdown-wrap span {
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
}

/* Winner Spotlight Card */
.spotlight-section {
  margin-bottom: 36px;
}

.spotlight-section.hidden {
  display: none;
}

.spotlight-card {
  background: linear-gradient(135deg, rgba(26, 34, 52, 0.95), rgba(18, 24, 38, 0.95));
  border: 1px solid rgba(59, 130, 246, 0.4);
  border-radius: var(--radius-lg);
  padding: 28px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 35px rgba(59, 130, 246, 0.2);
}

.spotlight-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #000;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.5px;
  padding: 6px 16px;
  border-radius: var(--radius-full);
  margin-bottom: 20px;
}

.spotlight-body {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 32px;
  align-items: center;
}

@media (max-width: 900px) {
  .spotlight-body {
    grid-template-columns: 1fr;
  }
}

.spotlight-image-col {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  height: 240px;
  background: #0d1117;
}

.spotlight-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.score-pill {
  position: absolute;
  top: 14px;
  right: 14px;
  background: rgba(10, 13, 20, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(59, 130, 246, 0.5);
  border-radius: var(--radius-full);
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.score-num {
  font-family: var(--font-heading);
  font-size: 18px;
  font-weight: 800;
  color: #60a5fa;
}

.score-label {
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.spotlight-info-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.spotlight-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 12px;
}

.brand-pill {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--accent-cyan);
  background: rgba(6, 182, 212, 0.12);
  padding: 2px 8px;
  border-radius: 4px;
  margin-bottom: 6px;
}

.spotlight-title {
  font-family: var(--font-heading);
  font-size: 26px;
  font-weight: 800;
  line-height: 1.2;
}

.spotlight-price-box {
  text-align: right;
}

.spotlight-price {
  font-family: var(--font-heading);
  font-size: 28px;
  font-weight: 800;
  color: #10b981;
}

.spotlight-orig-price {
  font-size: 13px;
  color: var(--text-dim);
  text-decoration: line-through;
}

.discount-badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  color: #f59e0b;
  background: rgba(245, 158, 11, 0.15);
  padding: 2px 6px;
  border-radius: 4px;
}

.specs-pill-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 10px;
}

.spec-pill {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-sm);
  padding: 8px 12px;
  font-size: 12px;
  color: #cbd5e1;
}

.spec-pill i {
  color: var(--accent-cyan);
  flex-shrink: 0;
  width: 16px;
  height: 16px;
}

.samar-quote {
  background: rgba(59, 130, 246, 0.08);
  border-left: 3px solid var(--accent-blue);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 12px 16px;
  display: flex;
  gap: 10px;
  font-size: 13px;
  color: #e2e8f0;
}

.quote-icon {
  color: var(--accent-blue);
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}

.spotlight-actions {
  display: flex;
  gap: 12px;
  margin-top: 4px;
}

/* Laptops Grid */
.laptops-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.laptop-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.25s ease;
}

.laptop-card:hover {
  transform: translateY(-4px);
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: var(--shadow-lg);
}

.card-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 2;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-full);
  display: flex;
  align-items: center;
  gap: 5px;
  backdrop-filter: blur(8px);
}

.badge-winner {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #000;
}

.badge-value {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
}

.badge-power {
  background: linear-gradient(135deg, #ef4444, #dc2626);
  color: #fff;
}

.badge-battery {
  background: linear-gradient(135deg, #06b6d4, #0891b2);
  color: #fff;
}

.badge-stretch {
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  color: #fff;
}

.card-img-wrap {
  position: relative;
  height: 180px;
  background: #0d1117;
  overflow: hidden;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.laptop-card:hover .card-img {
  transform: scale(1.04);
}

.card-score-badge {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(10, 13, 20, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(59, 130, 246, 0.4);
  border-radius: var(--radius-full);
  padding: 4px 10px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.score-percent {
  font-family: var(--font-heading);
  font-size: 14px;
  font-weight: 800;
  color: #60a5fa;
}

.score-tag {
  font-size: 10px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.card-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.brand-tag {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--accent-cyan);
}

.rating-tag {
  display: flex;
  align-items: center;
  gap: 3px;
  font-size: 12px;
  font-weight: 600;
  color: #f1f5f9;
}

.star-icon {
  width: 14px;
  height: 14px;
  fill: #f59e0b;
  color: #f59e0b;
}

.reviews-count {
  font-size: 11px;
  color: var(--text-dim);
}

.card-title {
  font-family: var(--font-heading);
  font-size: 17px;
  font-weight: 700;
  margin-bottom: 14px;
  line-height: 1.3;
  min-height: 44px;
}

.specs-mini-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 14px;
}

.spec-mini-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: var(--text-muted);
  background: var(--bg-surface-elevated);
  padding: 6px 8px;
  border-radius: var(--radius-sm);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.spec-mini-item i {
  color: var(--accent-cyan);
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}

.card-verdict-snippet {
  font-size: 12px;
  color: #cbd5e1;
  background: rgba(255, 255, 255, 0.03);
  border-radius: var(--radius-sm);
  padding: 8px 10px;
  margin-bottom: 16px;
  line-height: 1.4;
  flex: 1;
}

.card-verdict-snippet strong {
  color: #60a5fa;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1px solid var(--border-subtle);
}

.card-price {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 800;
  color: #10b981;
}

.card-orig-price {
  font-size: 11px;
  color: var(--text-dim);
  text-decoration: line-through;
}

.card-btn-group {
  display: flex;
  gap: 6px;
}

/* General Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  padding: 9px 18px;
  border-radius: var(--radius-md);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: #fff;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
  transform: translateY(-1px);
}

.btn-secondary {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-main);
}

.btn-secondary:hover {
  background: var(--bg-surface-hover);
  border-color: #3b82f6;
}

.btn-secondary.active {
  background: rgba(59, 130, 246, 0.2);
  border-color: var(--accent-blue);
  color: #60a5fa;
}

.btn-outline {
  background: transparent;
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
}

.btn-outline:hover {
  border-color: var(--accent-blue);
  color: #fff;
}

.btn-ghost {
  background: transparent;
  color: var(--text-muted);
}

.btn-ghost:hover {
  color: #fff;
}

.btn-sm {
  padding: 6px 12px;
  font-size: 12px;
}

/* Empty State */
.empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: 60px 20px;
  background: var(--bg-surface);
  border: 1px dashed var(--border-subtle);
  border-radius: var(--radius-lg);
}

.empty-icon {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--bg-surface-elevated);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  color: var(--text-dim);
}

.empty-state h3 {
  font-size: 20px;
  margin-bottom: 8px;
}

.empty-state p {
  color: var(--text-muted);
  font-size: 14px;
  max-width: 440px;
  margin: 0 auto 20px;
}

/* Floating Compare Bar */
.compare-floating-bar {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(18, 24, 38, 0.95);
  backdrop-filter: blur(12px);
  border: 1px solid var(--accent-blue);
  border-radius: var(--radius-full);
  padding: 10px 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), 0 0 20px rgba(59, 130, 246, 0.3);
  z-index: 100;
  transition: all 0.3s ease;
}

.compare-floating-bar.hidden {
  opacity: 0;
  transform: translate(-50%, 50px);
  pointer-events: none;
}

.compare-bar-inner {
  display: flex;
  align-items: center;
  gap: 20px;
}

.compare-info {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
}

.compare-badge {
  background: var(--accent-blue);
  color: #fff;
  padding: 2px 8px;
  border-radius: var(--radius-full);
  font-size: 11px;
}

.compare-thumbnails {
  display: flex;
  gap: 8px;
}

.compare-thumb {
  display: flex;
  align-items: center;
  gap: 6px;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-full);
  padding: 4px 10px 4px 4px;
  font-size: 12px;
}

.compare-thumb img {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  object-fit: cover;
}

.compare-thumb-remove {
  background: none;
  border: none;
  color: var(--text-dim);
  cursor: pointer;
  font-size: 16px;
  padding: 0 2px;
}

.compare-thumb-remove:hover {
  color: var(--accent-rose);
}

.compare-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Modals */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  z-index: 200;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-backdrop.hidden {
  display: none;
}

.modal-container {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  max-width: 1050px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: var(--shadow-lg);
}

.modal-close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  z-index: 10;
  transition: all 0.2s ease;
}

.modal-close-btn:hover {
  color: #fff;
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.2);
}

/* Details Modal Interior */
.details-modal-grid {
  display: grid;
  grid-template-columns: 360px 1fr;
  gap: 32px;
  padding: 32px;
}

@media (max-width: 860px) {
  .details-modal-grid {
    grid-template-columns: 1fr;
  }
}

.details-img-col {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.details-img {
  width: 100%;
  height: 230px;
  border-radius: var(--radius-md);
  object-fit: cover;
  border: 1px solid var(--border-subtle);
}

.details-score-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.score-circle {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, rgba(30, 58, 138, 0.5) 100%);
  border: 2px solid #3b82f6;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.score-circle-num {
  font-family: var(--font-heading);
  font-size: 20px;
  font-weight: 800;
  color: #fff;
  line-height: 1;
}

.score-circle-lbl {
  font-size: 9px;
  color: #93c5fd;
  text-transform: uppercase;
  margin-top: 2px;
}

.score-explanation h4 {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 4px;
}

.score-explanation p {
  font-size: 11px;
  color: var(--text-muted);
  line-height: 1.4;
}

.benchmarks-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 16px;
}

.benchmarks-box h4 {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 14px;
  color: var(--accent-cyan);
}

.benchmark-item {
  margin-bottom: 12px;
}

.benchmark-meta {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  margin-bottom: 5px;
  color: var(--text-muted);
}

.benchmark-bar {
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-full);
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #3b82f6, #06b6d4);
  border-radius: var(--radius-full);
}

.bar-fill-gaming {
  background: linear-gradient(90deg, #8b5cf6, #ec4899);
}

.bar-fill-productivity {
  background: linear-gradient(90deg, #10b981, #3b82f6);
}

.details-info-col {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.details-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}

.details-header h2 {
  font-family: var(--font-heading);
  font-size: 24px;
  font-weight: 800;
}

.details-price {
  font-family: var(--font-heading);
  font-size: 26px;
  font-weight: 800;
  color: #10b981;
}

.details-orig {
  font-size: 13px;
  color: var(--text-dim);
  text-decoration: line-through;
  text-align: right;
}

.samar-analysis-box {
  background: rgba(59, 130, 246, 0.08);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: var(--radius-md);
  padding: 16px;
}

.analysis-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: #60a5fa;
  margin-bottom: 8px;
}

.samar-analysis-box p {
  font-size: 13px;
  color: #e2e8f0;
  line-height: 1.5;
}

.spec-table-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 14px 0 20px;
}

.spec-row {
  display: grid;
  grid-template-columns: 140px 1fr;
  padding: 8px 12px;
  background: var(--bg-surface-elevated);
  border-radius: var(--radius-sm);
  font-size: 13px;
}

.spec-k {
  color: var(--text-muted);
  font-weight: 600;
}

.spec-v {
  color: #f1f5f9;
}

.pros-cons-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 20px;
}

@media (max-width: 600px) {
  .pros-cons-grid {
    grid-template-columns: 1fr;
  }
}

.pros-box, .cons-box {
  background: var(--bg-surface-elevated);
  border-radius: var(--radius-md);
  padding: 16px;
}

.pros-box h4 {
  font-size: 13px;
  font-weight: 700;
  color: #10b981;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.cons-box h4 {
  font-size: 13px;
  font-weight: 700;
  color: #f43f5e;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.pros-box ul, .cons-box ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.pros-box li, .cons-box li {
  font-size: 12px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
  color: #cbd5e1;
}

.check-icon {
  color: #10b981;
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  margin-top: 2px;
}

.x-icon {
  color: #f43f5e;
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  margin-top: 2px;
}

.details-footer-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

/* Compare Table Modal */
.compare-table-container {
  padding: 32px;
  overflow-x: auto;
}

.compare-table {
  width: 100%;
  border-collapse: collapse;
}

.compare-table th, .compare-table td {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border-subtle);
  text-align: left;
  vertical-align: top;
  font-size: 13px;
}

.compare-table th {
  background: var(--bg-surface-elevated);
}

.table-laptop-header {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.table-img {
  width: 100%;
  height: 120px;
  object-fit: cover;
  border-radius: var(--radius-sm);
}

.table-price {
  font-family: var(--font-heading);
  font-size: 18px;
  font-weight: 800;
  color: #10b981;
}

.score-pill-sm {
  display: inline-block;
  background: rgba(59, 130, 246, 0.15);
  border: 1px solid rgba(59, 130, 246, 0.4);
  color: #60a5fa;
  font-weight: 700;
  font-size: 12px;
  padding: 4px 10px;
  border-radius: var(--radius-full);
}

/* Footer */
.portal-footer {
  text-align: center;
  margin-top: 60px;
  padding-top: 24px;
  border-top: 1px solid var(--border-subtle);
  color: var(--text-dim);
  font-size: 13px;
}

.portal-footer a {
  color: #60a5fa;
  text-decoration: none;
}
"""
    target = os.path.join(BASE_DIR, "styles.css")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated styles.css successfully.")


def make_index_html():
    content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SAMAR Laptop Choice Portal | Smart AI Laptop Advisor</title>
  <meta name="description" content="Find the perfect laptop within your budget, storage, RAM, and processor needs with SAMAR Laptop Choice Portal." />
  
  <!-- Google Fonts: Outfit & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800;900&display=swap" rel="stylesheet" />

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <!-- Ambient background lighting orbs -->
  <div class="bg-glow-orb-1"></div>
  <div class="bg-glow-orb-2"></div>

  <div class="app-wrapper">
    <!-- Header -->
    <header class="portal-header">
      <div class="brand-wrapper">
        <div class="brand-icon-box">
          <i data-lucide="laptop"></i>
        </div>
        <div>
          <h1 class="brand-title">SAMAR Laptop Portal</h1>
          <p class="brand-tagline">Smart Advisory &amp; Machine Analysis for Laptop Recommendations</p>
        </div>
      </div>

      <div class="header-badges">
        <span class="pill-tag"><i data-lucide="cpu"></i> Intel 13th &amp; 14th Gen</span>
        <span class="pill-tag"><i data-lucide="zap"></i> AMD Ryzen Series</span>
        <span class="pill-tag"><i data-lucide="sparkles"></i> AI Match Engine</span>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-tag"><i data-lucide="compass"></i> Personalized Tech Advisory</div>
      <h2 class="hero-heading">Find the <span>Best Laptop</span> for Your Exact Needs</h2>
      <p class="hero-sub">Enter your budget, desired RAM, storage, processor generation, and intended purpose. SAMAR will calculate the ultimate match with zero guesswork.</p>
    </section>

    <!-- Quick Presets -->
    <div class="presets-strip">
      <div class="presets-label"><i data-lucide="sparkles"></i> Quick Picks:</div>
      <div class="preset-chips-wrap" id="presetChips">
        <!-- Injected by JavaScript -->
      </div>
    </div>

    <!-- Main Control Hub -->
    <section class="control-hub">
      <div class="hub-section-title">
        <i data-lucide="crosshair"></i> 1. Select Your Primary Purpose
      </div>
      <div class="purpose-grid" id="purposeGrid">
        <!-- Injected by JavaScript -->
      </div>

      <div class="filter-matrix">
        <!-- Budget Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>2. Max Budget</span>
            <span class="budget-val-badge" id="budgetDisplay">₹90,000</span>
          </div>
          <div class="budget-box">
            <input type="range" id="budgetSlider" class="slider-custom" min="30000" max="220000" step="2000" value="90000" />
            <div class="budget-sub-row">
              <div class="budget-num-input-wrap">
                <span class="currency-sym">₹</span>
                <input type="number" id="budgetInput" class="budget-input-field" min="30000" max="250000" step="1000" value="90000" />
              </div>
              <label class="flex-budget-label" title="Allows suggesting a laptop that costs up to 5% more if it offers a massive generational jump">
                <input type="checkbox" id="flexBudgetToggle" checked />
                <span>+5% value stretch</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Processor Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>3. Processor Choice</span>
          </div>
          <select id="processorSelect" class="select-custom">
            <option value="any">⚡ Any Recommended Processor</option>
            <optgroup label="Intel Processors">
              <option value="intel-i3">Intel Core i3 (13th &amp; 14th Gen)</option>
              <option value="intel-i5">Intel Core i5 (13th &amp; 14th Gen)</option>
              <option value="intel-i7">Intel Core i7 (13th &amp; 14th Gen)</option>
              <option value="intel-13th">Intel 13th Gen Raptor Lake</option>
              <option value="intel-14th">Intel 14th Gen / Core Ultra</option>
            </optgroup>
            <optgroup label="AMD Ryzen Processors">
              <option value="amd-ryzen-3">AMD Ryzen 3 Series</option>
              <option value="amd-ryzen-5">AMD Ryzen 5 Series (5500U, 7520U)</option>
              <option value="amd-ryzen-7">AMD Ryzen 7 Series (7735HS, 7840HS, 8845HS)</option>
              <option value="amd-ryzen-all">All AMD Ryzen Models</option>
            </optgroup>
            <optgroup label="Apple Silicon">
              <option value="apple-m">Apple M2 / M3 Series</option>
            </optgroup>
          </select>
        </div>

        <!-- RAM Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>4. Minimum RAM</span>
          </div>
          <select id="ramSelect" class="select-custom">
            <option value="any">Any RAM Size</option>
            <option value="8">8 GB RAM</option>
            <option value="16">16 GB RAM (Recommended)</option>
            <option value="24">24 GB RAM</option>
            <option value="32">32 GB RAM (Pro / AI)</option>
          </select>
        </div>

        <!-- Storage Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>5. Storage Size</span>
          </div>
          <select id="storageSelect" class="select-custom">
            <option value="any">Any Storage Capacity</option>
            <option value="256">256 GB SSD</option>
            <option value="512">512 GB NVMe SSD</option>
            <option value="1000">1 TB NVMe SSD</option>
            <option value="2000">2 TB NVMe SSD</option>
          </select>
        </div>

        <!-- Brand Filter -->
        <div class="filter-group">
          <div class="filter-label">
            <span>6. Preferred Brand</span>
          </div>
          <select id="brandSelect" class="select-custom">
            <option value="all">🏢 All Trusted Brands</option>
            <option value="Lenovo">Lenovo (LOQ, Legion, IdeaPad)</option>
            <option value="ASUS">ASUS (Vivobook, TUF, ROG)</option>
            <option value="HP">HP (Victus, Pavilion, OMEN, 15s)</option>
            <option value="Dell">Dell (Inspiron, Vostro, XPS)</option>
            <option value="Acer">Acer (Aspire, Nitro, Predator, Swift)</option>
            <option value="Apple">Apple (MacBook Air, MacBook Pro)</option>
            <option value="MSI">MSI (Thin, Katana, Modern)</option>
          </select>
        </div>
      </div>
    </section>

    <!-- Winner Spotlight Banner (SAMAR Top Recommendation) -->
    <div id="spotlightSection" class="spotlight-section">
      <!-- Injected by JavaScript -->
    </div>

    <!-- Toolbar: Search, Count & Sort -->
    <div class="toolbar-strip">
      <div class="search-box-wrap">
        <i data-lucide="search" class="search-icon-inside"></i>
        <input type="text" id="searchInput" class="search-input-field" placeholder="Search by model, specs (e.g. LOQ, RTX 4060, OLED, 14700HX)..." />
      </div>

      <div class="toolbar-right">
        <div class="results-count-badge" id="resultsCountBadge">Loading laptops...</div>
        <div class="sort-dropdown-wrap">
          <span>Sort By:</span>
          <select id="sortSelect" class="select-custom" style="width: 190px;">
            <option value="samar-match">🌟 Samar Match Score</option>
            <option value="price-low">💰 Price: Low to High</option>
            <option value="price-high">💎 Price: High to Low</option>
            <option value="rating">⭐ Customer Rating</option>
            <option value="cpu-power">🚀 CPU Benchmark Power</option>
            <option value="gaming-fps">🎮 Gaming FPS (3D Power)</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Laptops Grid -->
    <div class="laptops-grid" id="laptopsGrid">
      <!-- Injected by JavaScript -->
    </div>

    <!-- Floating Comparison Bar -->
    <div id="compareFloatingBar" class="compare-floating-bar hidden">
      <!-- Injected by JavaScript -->
    </div>

    <!-- Full Details Modal -->
    <div id="detailsModal" class="modal-backdrop hidden">
      <div class="modal-container">
        <button class="modal-close-btn" onclick="closeDetailsModal()">&times;</button>
        <div id="detailsModalContent">
          <!-- Injected by JavaScript -->
        </div>
      </div>
    </div>

    <!-- Compare Side-by-Side Modal -->
    <div id="compareModal" class="modal-backdrop hidden">
      <div class="modal-container" style="max-width: 1150px;">
        <button class="modal-close-btn" onclick="closeCompareModal()">&times;</button>
        <div id="compareModalContent">
          <!-- Injected by JavaScript -->
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="portal-footer">
      <p>SAMAR Laptop Choice Portal &bull; Crafted with intelligent recommendation weighting for Intel 13th/14th Gen and AMD Ryzen laptops.</p>
    </footer>
  </div>

  <script src="data.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""
    target = os.path.join(BASE_DIR, "index.html")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated index.html successfully.")

def make_readme():
    content = r"""# SAMAR Laptop Choice Portal

A modern, responsive web application for finding the best laptop based on budget, storage, RAM, processor generation, brand, and user purpose.

## Features Included

- **Portal Name**: **SAMAR Laptop Choice Portal** (with SAMAR branding and custom advisory logic).
- **Comprehensive Processors**:
  - Intel Core i3 (13th & 14th Gen)
  - Intel Core i5 (13th & 14th Gen, e.g. 13420H, 13500H, 14450HX)
  - Intel Core i7 (13th & 14th Gen, e.g. 13650HX, 13700HX, 14700HX, Core Ultra 7)
  - AMD Ryzen (Ryzen 3, Ryzen 5 5500U/7520U, Ryzen 7 7735HS/7840HS/8845HS)
  - Apple M3 Series
- **Purpose Selection**:
  - Coding & Software Development
  - Gaming & Esports
  - Video Editing & 3D Design
  - College & Everyday Use
  - AI, Machine Learning & Data Science
  - Business & Office
- **Budget Control**: Live slider & numeric INR (₹) input with flexible +5% value stretch option.
- **RAM & Storage Filters**: 8GB, 16GB, 24GB, 32GB RAM; 256GB, 512GB, 1TB, 2TB SSD.
- **Brand Filter**: All Brands, Lenovo, ASUS, HP, Dell, Acer, Apple, MSI.
- **Samar Match Score (0 - 100%)**: Weighted purpose matching, spec scoring, and budget optimization.
- **Winner Spotlight**: Displays SAMAR's #1 recommendation prominently.
- **Side-by-Side Comparison**: Compare up to 3 laptops with full spec tables.
- **Full Specification Modal**: Complete hardware breakdown, benchmark charts (Single-Core, Multi-Core, Gaming FPS, Productivity), pros & cons.

## How to Run

1. Open `index.html` directly in any web browser (Chrome, Edge, Firefox).
   OR
2. Run a lightweight local server:
   ```bash
   python -m http.server 8080
   ```
   Then navigate to `http://localhost:8080` in your web browser.
"""
    target = os.path.join(BASE_DIR, "README.md")
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated README.md successfully.")

make_index_html()
make_readme()
