<!-- Design System -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>DLV THONG LO 20 | Resident Dashboard</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&amp;family=Inter:wght@400;500;600&amp;family=Prompt:wght@300;400;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "on-secondary-fixed": "#291806",
              "tertiary-fixed": "#ffdbcd",
              "on-surface-variant": "#43474c",
              "error-container": "#ffdad6",
              "surface": "#fafaeb",
              "surface-tint": "#50606f",
              "surface-container-low": "#f4f5e6",
              "on-primary-container": "#fdfcff",
              "primary-fixed-dim": "#b8c8da",
              "tertiary": "#914723",
              "surface-container": "#efefe0",
              "tertiary-fixed-dim": "#ffb596",
              "outline-variant": "#c4c7cc",
              "error": "#ba1a1a",
              "on-tertiary-fixed": "#360f00",
              "on-primary": "#ffffff",
              "on-secondary": "#ffffff",
              "on-error-container": "#93000a",
              "inverse-surface": "#2f3128",
              "on-background": "#1b1c14",
              "on-tertiary-fixed-variant": "#76320f",
              "surface-variant": "#e3e3d5",
              "secondary-container": "#fedcbe",
              "primary-container": "#667686",
              "outline": "#74777c",
              "on-tertiary": "#ffffff",
              "secondary-fixed-dim": "#e1c1a4",
              "on-primary-fixed": "#0d1d2a",
              "surface-bright": "#fafaeb",
              "surface-container-highest": "#e3e3d5",
              "surface-dim": "#dbdbcd",
              "inverse-primary": "#b8c8da",
              "surface-container-lowest": "#ffffff",
              "background": "#fafaeb",
              "secondary": "#725a42",
              "on-secondary-container": "#796048",
              "primary": "#4e5e6d",
              "tertiary-container": "#b05e38",
              "on-tertiary-container": "#fffbff",
              "on-secondary-fixed-variant": "#59422c",
              "on-surface": "#1b1c14",
              "on-error": "#ffffff",
              "secondary-fixed": "#fedcbe",
              "inverse-on-surface": "#f1f2e3",
              "surface-container-high": "#e9e9db",
              "on-primary-fixed-variant": "#394857",
              "primary-fixed": "#d4e4f6"
            },
            fontFamily: {
              "headline": ["Manrope", "Prompt", "sans-serif"],
              "body": ["Inter", "Prompt", "sans-serif"],
              "label": ["Inter", "Prompt", "sans-serif"]
            },
            borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      body {
        background-color: #fafaeb;
        -webkit-font-smoothing: antialiased;
      }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="font-body text-on-surface">
<!-- TopAppBar -->
<header class="bg-[#fafaeb] dark:bg-slate-900 text-[#4e5e6d] dark:text-slate-300 docked full-width top-0 sticky z-40">
<div class="flex justify-between items-center w-full px-6 py-4 max-w-7xl mx-auto">
<button class="hover:bg-[#f4f5e6] dark:hover:bg-slate-800 transition-colors p-2 rounded-full flex items-center justify-center">
<span class="material-symbols-outlined">menu</span>
</button>
<h1 class="font-['Manrope'] font-bold tracking-wider text-[#725a42] dark:text-[#fedcbe] text-lg font-extrabold uppercase tracking-[0.05em] text-[#4e5e6d] dark:text-slate-200">
                DLV THONG LO 20
            </h1>
<button class="font-['Manrope'] font-bold tracking-wider text-[#725a42] dark:text-[#fedcbe] hover:bg-[#f4f5e6] dark:hover:bg-slate-800 transition-colors px-3 py-1 rounded-lg text-sm">
                EN/TH
            </button>
</div>
<div class="bg-[#e3e3d5] dark:bg-slate-800 h-[1px] w-full"></div>
</header>
<main class="max-w-7xl mx-auto px-6 pt-8 pb-32 space-y-10">
<!-- Welcome Section (Editorial Asymmetry) -->
<section class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end">
<div class="lg:col-span-8">
<p class="font-headline text-secondary text-lg mb-2 tracking-wide font-medium">Sawasdee, Resident</p>
<h2 class="font-headline text-4xl md:text-5xl font-extrabold text-primary leading-tight">
                    Welcome back to your <br/> Sanctuary in Thong Lo.
                </h2>
</div>
<div class="lg:col-span-4 hidden lg:block">
<div class="p-6 bg-surface-container-low rounded-2xl border-l-4 border-secondary">
<p class="text-sm font-label text-on-surface-variant uppercase tracking-widest mb-1">Building Status</p>
<p class="text-on-surface font-semibold">Elevators Operating normally. Concierge on duty until 10 PM.</p>
</div>
</div>
</section>
<!-- Main Dashboard Content -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
<!-- CAM Fee Tracker Card -->
<div class="lg:col-span-2 bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)] flex flex-col justify-between min-h-[320px] relative overflow-hidden">
<div class="relative z-10">
<div class="flex justify-between items-start mb-8">
<div>
<span class="bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider">
                                Outstanding Balance
                            </span>
<h3 class="font-headline text-2xl text-secondary mt-4 font-bold">Common Area Maintenance (CAM) Fee</h3>
</div>
<div class="text-right">
<p class="text-primary font-headline text-sm font-bold uppercase tracking-widest">Rate</p>
<p class="text-xl font-bold text-on-surface">59 <span class="text-sm font-medium">THB/sqm</span></p>
</div>
</div>
<div class="mt-auto">
<div class="flex items-baseline gap-2">
<span class="text-5xl font-extrabold text-primary tracking-tighter">4,248.00</span>
<span class="text-xl font-bold text-primary-container">THB</span>
</div>
<p class="text-on-surface-variant mt-2 font-medium">Due Date: 05 September 2024</p>
</div>
</div>
<!-- Abstract Decorative Background -->
<div class="absolute -right-20 -bottom-20 w-64 h-64 bg-surface-container-high rounded-full opacity-50 blur-3xl"></div>
</div>
<!-- Quick-Pay Section -->
<div class="bg-primary rounded-[2rem] p-8 text-on-primary shadow-xl flex flex-col justify-between">
<div>
<h3 class="font-headline text-2xl font-bold mb-2">Quick-Pay</h3>
<p class="text-primary-fixed-dim leading-relaxed mb-6">Instantly pay your monthly dues via PromptPay secure gateway.</p>
</div>
<div class="space-y-4">
<button class="w-full bg-secondary-container text-on-secondary-container py-5 rounded-xl font-bold text-lg flex items-center justify-center gap-3 transition-transform active:scale-95">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">qr_code_2</span>
                        Generate PromptPay QR
                    </button>
<button class="w-full bg-white/10 hover:bg-white/20 text-white py-4 rounded-xl font-semibold text-sm transition-colors border border-white/20">
                        View Payment History
                    </button>
</div>
</div>
<!-- Juristic Announcements (High Legibility for Seniors) -->
<div class="lg:col-span-3 bg-surface-container-low rounded-[2rem] p-8">
<div class="flex items-center justify-between mb-8 border-b border-outline-variant/20 pb-4">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary text-3xl">campaign</span>
<h3 class="font-headline text-2xl font-extrabold text-primary">Juristic Announcements</h3>
</div>
<a class="text-secondary font-bold text-sm border-b-2 border-secondary pb-1" href="#">View All News</a>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- News Item 1 -->
<div class="bg-surface-container-lowest p-6 rounded-2xl flex gap-6 items-start hover:shadow-md transition-shadow">
<div class="flex-shrink-0 w-16 h-16 bg-secondary-container rounded-xl flex flex-col items-center justify-center text-secondary">
<span class="text-xl font-bold">28</span>
<span class="text-[10px] font-bold uppercase">Aug</span>
</div>
<div class="flex-1">
<h4 class="font-headline text-lg font-bold text-on-surface leading-snug mb-2">Annual Fire Drill and Building Safety Inspection</h4>
<p class="text-on-surface-variant text-base leading-relaxed">Residents are advised that the annual fire drill will take place from 10:00 AM to 12:00 PM.</p>
</div>
</div>
<!-- News Item 2 -->
<div class="bg-surface-container-lowest p-6 rounded-2xl flex gap-6 items-start hover:shadow-md transition-shadow">
<div class="flex-shrink-0 w-16 h-16 bg-surface-container-highest rounded-xl flex flex-col items-center justify-center text-on-surface-variant">
<span class="text-xl font-bold">25</span>
<span class="text-[10px] font-bold uppercase">Aug</span>
</div>
<div class="flex-1">
<h4 class="font-headline text-lg font-bold text-on-surface leading-snug mb-2">Swimming Pool Maintenance Schedule</h4>
<p class="text-on-surface-variant text-base leading-relaxed">The main lap pool will be closed for quarterly chemical treatment this Saturday morning.</p>
</div>
</div>
</div>
</div>
<!-- Bento Card: Parcel Status (Contextual Highlight) -->
<div class="bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)]">
<div class="flex justify-between items-start mb-6">
<h3 class="font-headline text-xl font-bold text-secondary">Parcel Waiting</h3>
<span class="material-symbols-outlined text-primary text-3xl">package_2</span>
</div>
<div class="flex items-center gap-4 p-4 bg-secondary-fixed rounded-2xl">
<span class="text-3xl font-extrabold text-on-secondary-fixed">2</span>
<div>
<p class="font-bold text-on-secondary-fixed text-sm">Packages arrived</p>
<p class="text-on-secondary-fixed-variant text-xs">Awaiting collection at Lobby A</p>
</div>
</div>
</div>
<!-- Bento Card: Contact Concierge -->
<div class="bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)]">
<h3 class="font-headline text-xl font-bold text-secondary mb-4">Support</h3>
<div class="space-y-3">
<a class="flex items-center gap-4 p-4 hover:bg-surface-container-low rounded-2xl transition-colors" href="tel:021234567">
<span class="material-symbols-outlined text-primary">phone_in_talk</span>
<span class="font-medium">Call Concierge</span>
</a>
<div class="flex items-center gap-4 p-4 hover:bg-surface-container-low rounded-2xl transition-colors cursor-pointer">
<span class="material-symbols-outlined text-primary">chat_bubble</span>
<span class="font-medium">Juristic Chat</span>
</div>
</div>
</div>
<!-- Decorative Visual Element -->
<div class="relative rounded-[2rem] overflow-hidden group">
<img alt="Thong Lo Skyline" class="w-full h-full object-cover grayscale opacity-80 group-hover:grayscale-0 transition-all duration-700" data-alt="Modern architectural detail of a luxury condominium facade in Bangkok with warm sunset reflections and greenery" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBA-jfmurSjaq8fHBZrgeyKwPVYonGEDtDPqAZ1dJWdvIUMACkXFpiE272M-m_TSBmsokFcrR4aP1IEZ8tc5pFAmfiIlsqoYsFfY5tBd24ZJeHqZh9kv0mTqawqYHFRLBVBPPf03Y4cEm2yjmXI_wfwgtxP14MryfjEuspDdK8vvnuPjRGdZy6DptWQBXnwkoU-ZB_psIT9TZhO5zE3oMy-Ev1qRzWBUpnSLjzyGelRjEceYHUp-_twiGtIEkcApBaeJ6zXxmKlUcQ"/>
<div class="absolute inset-0 bg-gradient-to-t from-primary/80 to-transparent flex items-end p-8">
<p class="text-white font-headline font-bold text-lg">Experience Excellence at Thong Lo 20.</p>
</div>
</div>
</div>
</main>
<!-- BottomNavBar -->
<nav class="bg-white/80 dark:bg-slate-900/80 backdrop-blur-md text-[#4e5e6d] dark:text-slate-200 docked full-width bottom-0 rounded-t-3xl shadow-[0_-8px_24px_rgba(78,94,109,0.08)] fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3">
<!-- Home (Active) -->
<a class="flex flex-col items-center justify-center bg-[#fedcbe] dark:bg-[#725a42] text-[#725a42] dark:text-[#fedcbe] rounded-xl px-4 py-1 Active: scale-95 transition-transform duration-150" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">home</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Home</span>
</a>
<!-- Payments -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">payments</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Payments</span>
</a>
<!-- News -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">campaign</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">News</span>
</a>
<!-- Profile -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">person</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Profile</span>
</a>
</nav>
</body></html>

<!-- Resident Dashboard -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>DLV THONG LO 20 | Resident Dashboard</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&amp;family=Inter:wght@400;500;600&amp;family=Prompt:wght@300;400;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "on-secondary-fixed": "#291806",
              "tertiary-fixed": "#ffdbcd",
              "on-surface-variant": "#43474c",
              "error-container": "#ffdad6",
              "surface": "#fafaeb",
              "surface-tint": "#50606f",
              "surface-container-low": "#f4f5e6",
              "on-primary-container": "#fdfcff",
              "primary-fixed-dim": "#b8c8da",
              "tertiary": "#914723",
              "surface-container": "#efefe0",
              "tertiary-fixed-dim": "#ffb596",
              "outline-variant": "#c4c7cc",
              "error": "#ba1a1a",
              "on-tertiary-fixed": "#360f00",
              "on-primary": "#ffffff",
              "on-secondary": "#ffffff",
              "on-error-container": "#93000a",
              "inverse-surface": "#2f3128",
              "on-background": "#1b1c14",
              "on-tertiary-fixed-variant": "#76320f",
              "surface-variant": "#e3e3d5",
              "secondary-container": "#fedcbe",
              "primary-container": "#667686",
              "outline": "#74777c",
              "on-tertiary": "#ffffff",
              "secondary-fixed-dim": "#e1c1a4",
              "on-primary-fixed": "#0d1d2a",
              "surface-bright": "#fafaeb",
              "surface-container-highest": "#e3e3d5",
              "surface-dim": "#dbdbcd",
              "inverse-primary": "#b8c8da",
              "surface-container-lowest": "#ffffff",
              "background": "#fafaeb",
              "secondary": "#725a42",
              "on-secondary-container": "#796048",
              "primary": "#4e5e6d",
              "tertiary-container": "#b05e38",
              "on-tertiary-container": "#fffbff",
              "on-secondary-fixed-variant": "#59422c",
              "on-surface": "#1b1c14",
              "on-error": "#ffffff",
              "secondary-fixed": "#fedcbe",
              "inverse-on-surface": "#f1f2e3",
              "surface-container-high": "#e9e9db",
              "on-primary-fixed-variant": "#394857",
              "primary-fixed": "#d4e4f6"
            },
            fontFamily: {
              "headline": ["Manrope", "Prompt", "sans-serif"],
              "body": ["Inter", "Prompt", "sans-serif"],
              "label": ["Inter", "Prompt", "sans-serif"]
            },
            borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      body {
        background-color: #fafaeb;
        -webkit-font-smoothing: antialiased;
      }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
</head>
<body class="font-body text-on-surface">
<!-- TopAppBar -->
<header class="bg-[#fafaeb] dark:bg-slate-900 text-[#4e5e6d] dark:text-slate-300 docked full-width top-0 sticky z-40">
<div class="flex justify-between items-center w-full px-6 py-4 max-w-7xl mx-auto">
<button class="hover:bg-[#f4f5e6] dark:hover:bg-slate-800 transition-colors p-2 rounded-full flex items-center justify-center">
<span class="material-symbols-outlined">menu</span>
</button>
<h1 class="font-['Manrope'] font-bold tracking-wider text-[#725a42] dark:text-[#fedcbe] text-lg font-extrabold uppercase tracking-[0.05em] text-[#4e5e6d] dark:text-slate-200">
                DLV THONG LO 20
            </h1>
<button class="font-['Manrope'] font-bold tracking-wider text-[#725a42] dark:text-[#fedcbe] hover:bg-[#f4f5e6] dark:hover:bg-slate-800 transition-colors px-3 py-1 rounded-lg text-sm">
                EN/TH
            </button>
</div>
<div class="bg-[#e3e3d5] dark:bg-slate-800 h-[1px] w-full"></div>
</header>
<main class="max-w-7xl mx-auto px-6 pt-8 pb-32 space-y-10">
<!-- Welcome Section (Editorial Asymmetry) -->
<section class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end">
<div class="lg:col-span-8">
<p class="font-headline text-secondary text-lg mb-2 tracking-wide font-medium">Sawasdee, Resident</p>
<h2 class="font-headline text-4xl md:text-5xl font-extrabold text-primary leading-tight">Welcome back to your <br/> Sanctuary / ยินดีต้อนรับกลับสู่ที่พักของคุณ</h2>
</div>
<div class="lg:col-span-4 hidden lg:block">
<div class="p-6 bg-surface-container-low rounded-2xl border-l-4 border-secondary">
<p class="text-sm font-label text-on-surface-variant uppercase tracking-widest mb-1">Building Status</p>
<p class="text-on-surface font-semibold">Elevators Operating normally. Concierge on duty until 10 PM.</p>
</div>
</div>
</section>
<!-- Main Dashboard Content -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
<!-- CAM Fee Tracker Card -->
<div class="lg:col-span-2 bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)] flex flex-col justify-between min-h-[320px] relative overflow-hidden">
<div class="relative z-10">
<div class="flex justify-between items-start mb-8">
<div>
<span class="bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider">
                                Outstanding Balance
                            </span>
<h3 class="font-headline text-2xl text-secondary mt-4 font-bold">Common Area Maintenance (CAM) Fee / ค่าส่วนกลาง</h3>
</div>
<div class="text-right">
<p class="text-primary font-headline text-sm font-bold uppercase tracking-widest">Rate</p>
<p class="text-xl font-bold text-on-surface">59 <span class="text-sm font-medium">THB/sqm</span></p>
</div>
</div>
<div class="mt-auto">
<div class="flex items-baseline gap-2">
<span class="text-5xl font-extrabold text-primary tracking-tighter">4,248.00</span>
<span class="text-xl font-bold text-primary-container">THB</span>
</div>
<p class="text-on-surface-variant mt-2 font-medium">Due Date: 05 September 2024</p>
</div>
</div>
<!-- Abstract Decorative Background -->
<div class="absolute -right-20 -bottom-20 w-64 h-64 bg-surface-container-high rounded-full opacity-50 blur-3xl"></div>
</div>
<!-- Quick-Pay Section -->
<div class="bg-primary rounded-[2rem] p-8 text-on-primary shadow-xl flex flex-col justify-between">
<div>
<h3 class="font-headline text-2xl font-bold mb-2">Quick-Pay / ชำระเงินด่วน</h3>
<p class="text-primary-fixed-dim leading-relaxed mb-6">Instantly pay your monthly dues via PromptPay secure gateway.</p>
</div>
<div class="space-y-4">
<button class="w-full bg-secondary-container text-on-secondary-container py-5 rounded-xl font-bold text-lg flex items-center justify-center gap-3 transition-transform active:scale-95">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">qr_code_2</span>
                        Generate PromptPay QR
                    </button>
<button class="w-full bg-white/10 hover:bg-white/20 text-white py-4 rounded-xl font-semibold text-sm transition-colors border border-white/20">
                        View Payment History
                    </button>
</div>
</div>
<!-- Juristic Announcements (High Legibility for Seniors) -->
<div class="lg:col-span-3 bg-surface-container-low rounded-[2rem] p-8">
<div class="flex items-center justify-between mb-8 border-b border-outline-variant/20 pb-4">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary text-3xl">campaign</span>
<h3 class="font-headline text-2xl font-extrabold text-primary">Juristic Announcements / ประกาศจากนิติบุคคล</h3>
</div>
<a class="text-secondary font-bold text-sm border-b-2 border-secondary pb-1" href="#">View All News</a>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
<!-- News Item 1 -->
<div class="bg-surface-container-lowest p-6 rounded-2xl flex gap-6 items-start hover:shadow-md transition-shadow">
<div class="flex-shrink-0 w-16 h-16 bg-secondary-container rounded-xl flex flex-col items-center justify-center text-secondary">
<span class="text-xl font-bold">28</span>
<span class="text-[10px] font-bold uppercase">Aug</span>
</div>
<div class="flex-1">
<h4 class="font-headline text-lg font-bold text-on-surface leading-snug mb-2">Annual Fire Drill and Building Safety Inspection</h4>
<p class="text-on-surface-variant text-base leading-relaxed">Residents are advised that the annual fire drill will take place from 10:00 AM to 12:00 PM.</p>
</div>
</div>
<!-- News Item 2 -->
<div class="bg-surface-container-lowest p-6 rounded-2xl flex gap-6 items-start hover:shadow-md transition-shadow">
<div class="flex-shrink-0 w-16 h-16 bg-surface-container-highest rounded-xl flex flex-col items-center justify-center text-on-surface-variant">
<span class="text-xl font-bold">25</span>
<span class="text-[10px] font-bold uppercase">Aug</span>
</div>
<div class="flex-1">
<h4 class="font-headline text-lg font-bold text-on-surface leading-snug mb-2">Swimming Pool Maintenance Schedule</h4>
<p class="text-on-surface-variant text-base leading-relaxed">The main lap pool will be closed for quarterly chemical treatment this Saturday morning.</p>
</div>
</div>
</div>
</div>
<!-- Bento Card: Parcel Status (Contextual Highlight) -->
<div class="bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)]">
<div class="flex justify-between items-start mb-6">
<h3 class="font-headline text-xl font-bold text-secondary">Parcel Waiting / พัสดุรอรับ</h3>
<span class="material-symbols-outlined text-primary text-3xl">package_2</span>
</div>
<div class="flex items-center gap-4 p-4 bg-secondary-fixed rounded-2xl">
<span class="text-3xl font-extrabold text-on-secondary-fixed">2</span>
<div>
<p class="font-bold text-on-secondary-fixed text-sm">Packages arrived</p>
<p class="text-on-secondary-fixed-variant text-xs">Awaiting collection at Lobby A</p>
</div>
</div>
</div>
<!-- Bento Card: Contact Concierge -->
<div class="bg-surface-container-lowest rounded-[2rem] p-8 shadow-[0_8px_24px_rgba(78,94,109,0.08)]">
<h3 class="font-headline text-xl font-bold text-secondary mb-4">Support / ความช่วยเหลือ</h3>
<div class="space-y-3">
<a class="flex items-center gap-4 p-4 hover:bg-surface-container-low rounded-2xl transition-colors" href="tel:021234567">
<span class="material-symbols-outlined text-primary">phone_in_talk</span>
<span class="font-medium">Call Concierge</span>
</a>
<div class="flex items-center gap-4 p-4 hover:bg-surface-container-low rounded-2xl transition-colors cursor-pointer">
<span class="material-symbols-outlined text-primary">chat_bubble</span>
<span class="font-medium">Juristic Chat</span>
</div>
</div>
</div>
<!-- Decorative Visual Element -->
<div class="relative rounded-[2rem] overflow-hidden group">
<img alt="Thong Lo Skyline" class="w-full h-full object-cover grayscale opacity-80 group-hover:grayscale-0 transition-all duration-700" data-alt="Modern architectural detail of a luxury condominium facade in Bangkok with warm sunset reflections and greenery" src="https://lh3.googleusercontent.com/aida-public/AB6AXuBA-jfmurSjaq8fHBZrgeyKwPVYonGEDtDPqAZ1dJWdvIUMACkXFpiE272M-m_TSBmsokFcrR4aP1IEZ8tc5pFAmfiIlsqoYsFfY5tBd24ZJeHqZh9kv0mTqawqYHFRLBVBPPf03Y4cEm2yjmXI_wfwgtxP14MryfjEuspDdK8vvnuPjRGdZy6DptWQBXnwkoU-ZB_psIT9TZhO5zE3oMy-Ev1qRzWBUpnSLjzyGelRjEceYHUp-_twiGtIEkcApBaeJ6zXxmKlUcQ"/>
<div class="absolute inset-0 bg-gradient-to-t from-primary/80 to-transparent flex items-end p-8">
<p class="text-white font-headline font-bold text-lg">Experience Excellence at Thong Lo 20.</p>
</div>
</div>
</div>
</main>
<!-- BottomNavBar -->
<nav class="bg-white/80 dark:bg-slate-900/80 backdrop-blur-md text-[#4e5e6d] dark:text-slate-200 docked full-width bottom-0 rounded-t-3xl shadow-[0_-8px_24px_rgba(78,94,109,0.08)] fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3">
<!-- Home (Active) -->
<a class="flex flex-col items-center justify-center bg-[#fedcbe] dark:bg-[#725a42] text-[#725a42] dark:text-[#fedcbe] rounded-xl px-4 py-1 Active: scale-95 transition-transform duration-150" href="#">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">home</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Home</span>
</a>
<!-- Payments -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">payments</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Payments</span>
</a>
<!-- News -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">campaign</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">News</span>
</a>
<!-- Profile -->
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-4 py-1 hover:text-[#4e5e6d] dark:hover:text-white transition-colors" href="#">
<span class="material-symbols-outlined">person</span>
<span class="font-['Inter'] text-[12px] font-medium tracking-normal">Profile</span>
</a>
</nav>
</body></html>

<!-- Bilingual Resident Dashboard -->
<!DOCTYPE html>

<html lang="th"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;700;800&amp;family=Inter:wght@400;500;600&amp;family=Prompt:wght@300;400;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "background": "#fafaeb",
              "on-secondary-fixed": "#291806",
              "surface-variant": "#e3e3d5",
              "surface-container": "#efefe0",
              "on-tertiary-fixed-variant": "#76320f",
              "on-tertiary-container": "#fffbff",
              "on-error-container": "#93000a",
              "tertiary": "#914723",
              "error-container": "#ffdad6",
              "inverse-primary": "#b8c8da",
              "tertiary-fixed": "#ffdbcd",
              "on-surface": "#1b1c14",
              "surface-container-high": "#e9e9db",
              "surface-dim": "#dbdbcd",
              "surface-container-lowest": "#ffffff",
              "on-background": "#1b1c14",
              "inverse-on-surface": "#f1f2e3",
              "primary": "#4e5e6d",
              "surface-container-highest": "#e3e3d5",
              "on-secondary-fixed-variant": "#59422c",
              "on-secondary-container": "#796048",
              "inverse-surface": "#2f3128",
              "secondary-container": "#fedcbe",
              "surface-tint": "#50606f",
              "on-tertiary": "#ffffff",
              "surface-container-low": "#f4f5e6",
              "secondary-fixed": "#fedcbe",
              "on-error": "#ffffff",
              "on-primary-container": "#fdfcff",
              "outline": "#74777c",
              "primary-container": "#667686",
              "on-primary-fixed": "#0d1d2a",
              "tertiary-container": "#b05e38",
              "primary-fixed-dim": "#b8c8da",
              "on-tertiary-fixed": "#360f00",
              "tertiary-fixed-dim": "#ffb596",
              "on-secondary": "#ffffff",
              "on-primary-fixed-variant": "#394857",
              "secondary": "#725a42",
              "primary-fixed": "#d4e4f6",
              "error": "#ba1a1a",
              "on-surface-variant": "#43474c",
              "surface-bright": "#fafaeb",
              "outline-variant": "#c4c7cc",
              "on-primary": "#ffffff",
              "surface": "#fafaeb",
              "secondary-fixed-dim": "#e1c1a4"
            },
            fontFamily: {
              "headline": ["Manrope", "Prompt"],
              "body": ["Inter", "Prompt"],
              "label": ["Inter", "Prompt"]
            },
            borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      .glass-effect {
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
      }
      body {
        background-color: #fafaeb;
        color: #1b1c14;
      }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="font-body antialiased min-h-screen pb-32">
<!-- Top Navigation -->
<header class="flex justify-between items-center w-full px-6 py-4 fixed top-0 z-50 bg-[#e3e3d5] dark:bg-slate-800 no-border">
<div class="flex items-center gap-4">
<button class="text-[#4e5e6d] dark:text-slate-300 hover:bg-[#ffffff]/50 transition-colors p-2 rounded-full">
<span class="material-symbols-outlined" data-icon="arrow_back">arrow_back</span>
</button>
<h1 class="font-headline font-bold tracking-wider text-sm text-[#4e5e6d] dark:text-slate-300">DLV THONG LO 20</h1>
</div>
<div class="text-[#4e5e6d] dark:text-slate-300 font-headline font-bold text-xs tracking-widest cursor-pointer">
            TH/EN
        </div>
</header>
<main class="pt-24 px-6 max-w-2xl mx-auto">
<!-- Editorial Header Section -->
<section class="mb-10">
<p class="font-label text-secondary text-xs font-semibold tracking-[0.2em] mb-2">MANAGEMENT FEE</p>
<h2 class="font-headline text-3xl font-extrabold text-on-surface leading-tight">
                Payment Detail / <br/>
<span class="font-light text-secondary">รายละเอียดการชำระเงิน</span>
</h2>
</section>
<!-- Asymmetric Payment Info Bento -->
<div class="grid grid-cols-1 md:grid-cols-5 gap-6 mb-8">
<!-- Amount Card -->
<div class="md:col-span-3 bg-surface-container-lowest p-8 rounded-xl shadow-[0_8px_24px_rgba(78,94,109,0.04)] flex flex-col justify-between min-h-[180px]">
<div>
<span class="text-on-surface-variant text-sm font-medium">CAM Fee (Outstanding)</span>
<div class="mt-4 flex items-baseline gap-2">
<span class="font-headline text-4xl font-extrabold text-primary tracking-tighter">4,248.00</span>
<span class="text-secondary font-bold text-lg">THB</span>
</div>
</div>
<div class="pt-4 mt-4 border-t border-surface-variant/30">
<p class="text-xs text-on-surface-variant leading-relaxed">Due Date: 31 Oct 2023</p>
</div>
</div>
<!-- Resident Info Card -->
<div class="md:col-span-2 bg-surface-container-low p-6 rounded-xl flex flex-col justify-center">
<div class="space-y-4">
<div>
<p class="text-[10px] uppercase tracking-widest text-secondary font-bold mb-1">Unit</p>
<p class="font-headline text-xl font-bold text-on-surface">20/145</p>
</div>
<div>
<p class="text-[10px] uppercase tracking-widest text-secondary font-bold mb-1">Resident</p>
<p class="font-body text-sm font-medium text-on-surface">Mr. Somchai Sukhumvit</p>
</div>
</div>
</div>
</div>
<!-- PromptPay Action Section -->
<div class="space-y-6">
<button class="w-full bg-primary hover:bg-primary-container text-on-primary py-5 rounded-xl font-headline font-bold text-lg shadow-lg transition-all active:scale-[0.98] flex items-center justify-center gap-3">
<span class="material-symbols-outlined" data-icon="qr_code_2">qr_code_2</span>
                Generate PromptPay QR / สร้าง QR พร้อมเพย์
            </button>
<!-- PromptPay Visual Placeholder (Simulating the state after generation) -->
<div class="bg-surface-container-lowest p-10 rounded-2xl shadow-[0_12px_40px_rgba(78,94,109,0.06)] border border-surface-variant/20 flex flex-col items-center">
<div class="w-full max-w-[200px] mb-8">
<!-- PromptPay Brand Logo Placeholder -->
<div class="flex items-center justify-center gap-2 mb-6">
<div class="h-8 w-24 bg-primary/10 rounded-lg flex items-center justify-center">
<span class="text-[10px] font-black text-primary tracking-tighter">PromptPay</span>
</div>
<div class="h-8 px-3 bg-secondary-container rounded-lg flex items-center justify-center">
<span class="text-[10px] font-bold text-on-secondary-container">พร้อมเพย์</span>
</div>
</div>
<!-- QR Code Frame -->
<div class="aspect-square w-full bg-white p-4 border-4 border-primary/5 rounded-2xl flex items-center justify-center relative overflow-hidden group">
<div class="w-full h-full border border-dashed border-outline-variant/50 rounded-lg flex flex-col items-center justify-center text-center px-4">
<span class="material-symbols-outlined text-4xl text-outline-variant mb-2" data-icon="qr_code_scanner">qr_code_scanner</span>
<p class="text-[10px] text-outline-variant font-medium">QR Preview<br/>Will appear here</p>
</div>
<!-- Glassy Overlay for generated state simulation -->
<div class="absolute inset-0 bg-white/40 backdrop-blur-[2px] flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity">
<span class="text-xs font-bold text-primary">Previewing...</span>
</div>
</div>
</div>
<div class="w-full space-y-3">
<button class="w-full bg-surface-container-high hover:bg-surface-variant text-primary py-4 rounded-xl font-body font-semibold text-sm transition-colors flex items-center justify-center gap-2">
<span class="material-symbols-outlined text-lg" data-icon="download">download</span>
                        Save QR to Gallery / บันทึก QR ลงอัลบั้ม
                    </button>
<p class="text-center text-[10px] text-on-surface-variant px-12 leading-normal">
                        Verify the amount and recipient name before completing the transfer. This QR code is valid for 24 hours.
                    </p>
</div>
</div>
</div>
<!-- Secondary Information Cards -->
<div class="mt-12 grid grid-cols-1 gap-4">
<div class="bg-surface-container-low/50 p-6 rounded-xl flex items-center gap-4">
<div class="h-10 w-10 bg-secondary-container rounded-full flex items-center justify-center text-secondary">
<span class="material-symbols-outlined" data-icon="security">security</span>
</div>
<div>
<h4 class="text-sm font-bold text-on-surface">Secure Transaction</h4>
<p class="text-xs text-on-surface-variant">Encrypted through Bank of Thailand standards</p>
</div>
</div>
</div>
</main>
<!-- Bottom Navigation Shell -->
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3 bg-[#ffffff]/80 dark:bg-slate-950/80 backdrop-blur-xl shadow-[0_-8px_24px_rgba(78,94,109,0.08)] rounded-t-[2rem]">
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-all" href="#">
<span class="material-symbols-outlined mb-1" data-icon="home">home</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Home</span>
</a>
<a class="flex flex-col items-center justify-center bg-[#4e5e6d] dark:bg-slate-700 text-white dark:text-slate-100 rounded-2xl px-5 py-1.5 transition-all scale-95" href="#">
<span class="material-symbols-outlined mb-1" data-icon="payments" data-weight="fill" style="font-variation-settings: 'FILL' 1;">payments</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Payments</span>
</a>
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-all" href="#">
<span class="material-symbols-outlined mb-1" data-icon="newspaper">newspaper</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">News</span>
</a>
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-all" href="#">
<span class="material-symbols-outlined mb-1" data-icon="person">person</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Profile</span>
</a>
</nav>
</body></html>

<!-- PromptPay QR Payment / ชำระเงินพร้อมเพย์ -->
<!DOCTYPE html>

<html class="light" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&amp;family=Inter:wght@400;500;600&amp;family=Prompt:wght@400;500;600&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "background": "#fafaeb",
              "on-secondary-fixed": "#291806",
              "surface-variant": "#e3e3d5",
              "surface-container": "#efefe0",
              "on-tertiary-fixed-variant": "#76320f",
              "on-tertiary-container": "#fffbff",
              "on-error-container": "#93000a",
              "tertiary": "#914723",
              "error-container": "#ffdad6",
              "inverse-primary": "#b8c8da",
              "tertiary-fixed": "#ffdbcd",
              "on-surface": "#1b1c14",
              "surface-container-high": "#e9e9db",
              "surface-dim": "#dbdbcd",
              "surface-container-lowest": "#ffffff",
              "on-background": "#1b1c14",
              "inverse-on-surface": "#f1f2e3",
              "primary": "#4e5e6d",
              "surface-container-highest": "#e3e3d5",
              "on-secondary-fixed-variant": "#59422c",
              "on-secondary-container": "#796048",
              "inverse-surface": "#2f3128",
              "secondary-container": "#fedcbe",
              "surface-tint": "#50606f",
              "on-tertiary": "#ffffff",
              "surface-container-low": "#f4f5e6",
              "secondary-fixed": "#fedcbe",
              "on-error": "#ffffff",
              "on-primary-container": "#fdfcff",
              "outline": "#74777c",
              "primary-container": "#667686",
              "on-primary-fixed": "#0d1d2a",
              "tertiary-container": "#b05e38",
              "primary-fixed-dim": "#b8c8da",
              "on-tertiary-fixed": "#360f00",
              "tertiary-fixed-dim": "#ffb596",
              "on-secondary": "#ffffff",
              "on-primary-fixed-variant": "#394857",
              "secondary": "#725a42",
              "primary-fixed": "#d4e4f6",
              "error": "#ba1a1a",
              "on-surface-variant": "#43474c",
              "surface-bright": "#fafaeb",
              "outline-variant": "#c4c7cc",
              "on-primary": "#ffffff",
              "surface": "#fafaeb",
              "secondary-fixed-dim": "#e1c1a4"
            },
            fontFamily: {
              "headline": ["Manrope", "Prompt", "sans-serif"],
              "body": ["Inter", "Prompt", "sans-serif"],
              "label": ["Inter", "Prompt", "sans-serif"]
            },
            borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
          },
        },
      }
    </script>
<style>
      .material-symbols-outlined {
        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
      }
      body { background-color: #fafaeb; color: #1b1c14; -webkit-font-smoothing: antialiased; }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="font-body">
<!-- TopAppBar -->
<header class="flex justify-between items-center w-full px-6 py-4 fixed top-0 z-50 bg-[#f4f5e6] dark:bg-slate-900">
<div class="flex items-center gap-4">
<span class="material-symbols-outlined text-[#4e5e6d] dark:text-slate-300 cursor-pointer" data-icon="menu">menu</span>
<h1 class="text-lg font-extrabold text-[#725a42] dark:text-[#fedcbe] tracking-[0.02em] font-headline">DLV THONG LO 20</h1>
</div>
<div class="flex items-center gap-4">
<span class="font-headline font-bold tracking-wider text-sm text-[#4e5e6d] dark:text-slate-300 cursor-pointer hover:bg-[#ffffff]/50 transition-colors px-2 py-1 rounded">TH/EN</span>
</div>
</header>
<main class="pt-24 pb-32 px-6 max-w-5xl mx-auto">
<!-- Hero Section / Header -->
<section class="mb-10">
<h2 class="text-3xl md:text-4xl font-headline font-extrabold text-secondary tracking-tight mb-2">Juristic News / ข่าวสารจากนิติบุคคล</h2>
<p class="text-on-surface-variant text-lg font-body leading-relaxed max-w-2xl">
                Stay updated with the latest announcements, maintenance schedules, and community events from DLV Thong Lo 20 management.
            </p>
</section>
<!-- Featured News Card (Asymmetric Layout) -->
<section class="mb-12">
<div class="bg-surface-container-lowest rounded-[2rem] overflow-hidden shadow-[0_8px_24px_rgba(78,94,109,0.04)] border border-outline-variant/10 group flex flex-col md:flex-row">
<div class="md:w-1/2 h-64 md:h-auto overflow-hidden">
<img class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" data-alt="Modern high-end residential lobby with elegant wooden panels, warm lighting, and a concierge desk in a luxury apartment building" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCgnQ_mtxnf3PCNecclZQuoOz41si_ORP0RCNpnSsEfPjtm8pw1Fv4Tr8lQh8JGhKQ2QWqsfPTZF24FEKAeE1FKHjxm-vFiV3uyiwl1cw39WXS49CeSP2wEP7Kwez2RW7PggHm3f-FXOYS_Yrn_1rLm1243tYcmT3vpic4yfC9dFFopfN-zvXTx_gjcr1CjORnM-vAsIOXkqxCTYCBihjp1DOFUSP_zR2SvQ7rXF22A8xFq0yrMeWTrLFqDhn_IPBMxLnAfm5Fv0x4"/>
</div>
<div class="p-8 md:w-1/2 flex flex-col justify-center bg-surface-container-low">
<span class="inline-block px-3 py-1 mb-4 text-[11px] font-bold tracking-widest uppercase bg-secondary-container text-on-secondary-container rounded-full w-fit">IMPORTANT</span>
<h3 class="text-2xl font-headline font-bold text-on-background mb-3 leading-tight">Annual Fire Drill / ซ้อมดับเพลิงประจำปี</h3>
<div class="flex items-center gap-2 text-primary font-medium mb-4">
<span class="material-symbols-outlined text-sm" data-icon="calendar_today">calendar_today</span>
<span class="text-sm">August 28, 2024</span>
</div>
<p class="text-on-surface-variant mb-6 leading-relaxed">
                        Notice to all residents regarding the upcoming annual safety drill. Participation is highly encouraged for the safety of our community. 
                        ขอแจ้งให้ท่านเจ้าของร่วมและผู้พักอาศัยทุกท่านทราบถึงการซ้อมแผนป้องกันอัคคีภัยประจำปี
                    </p>
<button class="bg-primary text-on-primary px-6 py-3 rounded-xl font-medium w-fit hover:opacity-90 transition-opacity">
                        Read Full Notice
                    </button>
</div>
</div>
</section>
<!-- News Grid -->
<section class="grid grid-cols-1 md:grid-cols-2 gap-8">
<!-- News Card 2 -->
<div class="bg-surface-container-low p-8 rounded-[2rem] hover:bg-surface-container-high transition-all duration-300">
<div class="flex flex-col gap-4">
<div class="flex justify-between items-start">
<div class="flex items-center gap-2 text-primary font-medium">
<span class="material-symbols-outlined text-sm" data-icon="event">event</span>
<span class="text-sm">August 22, 2024</span>
</div>
<span class="px-3 py-1 text-[10px] font-bold tracking-widest uppercase bg-surface-variant text-on-surface-variant rounded-full">MAINTENANCE</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-background leading-snug">Water Pump Maintenance / ซ่อมบำรุงปั๊มน้ำ</h3>
<p class="text-on-surface-variant leading-relaxed">
                        Scheduled maintenance of the main water supply system on the 5th floor. Temporary water outage may occur.
                        การดำเนินการบำรุงรักษาปั๊มน้ำหลักบริเวณชั้น 5 อาจมีผลทำให้ความดันน้ำลดลงชั่วคราว
                    </p>
<div class="mt-4 pt-4 border-t border-outline-variant/20">
<a class="text-secondary font-bold flex items-center gap-1 hover:gap-2 transition-all" href="#">
                            View Details <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span>
</a>
</div>
</div>
</div>
<!-- News Card 3 -->
<div class="bg-surface-container-low p-8 rounded-[2rem] hover:bg-surface-container-high transition-all duration-300">
<div class="flex flex-col gap-4">
<div class="flex justify-between items-start">
<div class="flex items-center gap-2 text-primary font-medium">
<span class="material-symbols-outlined text-sm" data-icon="security">security</span>
<span class="text-sm">August 15, 2024</span>
</div>
<span class="px-3 py-1 text-[10px] font-bold tracking-widest uppercase bg-secondary-container text-on-secondary-container rounded-full">SECURITY</span>
</div>
<h3 class="text-xl font-headline font-bold text-on-background leading-snug">New Security Protocol / มาตรการความปลอดภัยใหม่</h3>
<p class="text-on-surface-variant leading-relaxed">
                        Updating entry requirements for visitors and delivery personnel to enhance resident safety.
                        ยกระดับความปลอดภัยในการตรวจสอบผู้เข้าติดต่อและพนักงานส่งของ เพื่อความเป็นส่วนตัวและความปลอดภัยสูงสุด
                    </p>
<div class="mt-4 pt-4 border-t border-outline-variant/20">
<a class="text-secondary font-bold flex items-center gap-1 hover:gap-2 transition-all" href="#">
                            View Details <span class="material-symbols-outlined text-sm" data-icon="arrow_forward">arrow_forward</span>
</a>
</div>
</div>
</div>
<!-- News Card 4 (Bento Style) -->
<div class="bg-surface-container-low p-8 rounded-[2rem] hover:bg-surface-container-high transition-all duration-300 md:col-span-2 flex flex-col md:flex-row gap-8 items-center">
<div class="bg-surface-container-lowest p-6 rounded-2xl shadow-sm w-full md:w-1/3 text-center border border-outline-variant/10">
<span class="material-symbols-outlined text-4xl text-secondary mb-2" data-icon="notifications_active">notifications_active</span>
<h4 class="font-headline font-bold text-on-background">Notification Settings</h4>
<p class="text-sm text-on-surface-variant mt-2">Personalize how you receive news updates.</p>
</div>
<div class="w-full md:w-2/3">
<h3 class="text-xl font-headline font-bold text-on-background mb-2">Subscribe to News via Email</h3>
<p class="text-on-surface-variant mb-4">Never miss an important building update. Receive all announcements directly in your inbox.</p>
<div class="flex flex-col sm:flex-row gap-2">
<input class="flex-grow bg-background border-none ring-1 ring-outline-variant/30 rounded-xl px-4 py-3 focus:ring-primary focus:ring-2" placeholder="resident@dlv-thonglo.com" type="email"/>
<button class="bg-primary text-on-primary px-6 py-3 rounded-xl font-medium whitespace-nowrap">Subscribe Now</button>
</div>
</div>
</div>
</section>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3 bg-[#ffffff]/80 dark:bg-slate-950/80 backdrop-blur-xl rounded-t-[2rem] shadow-[0_-8px_24px_rgba(78,94,109,0.08)]">
<div class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-colors cursor-pointer group">
<span class="material-symbols-outlined group-active:scale-95 transition-transform" data-icon="home">home</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Home</span>
</div>
<div class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-colors cursor-pointer group">
<span class="material-symbols-outlined group-active:scale-95 transition-transform" data-icon="payments">payments</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Payments</span>
</div>
<!-- Active Tab: News -->
<div class="flex flex-col items-center justify-center bg-[#4e5e6d] dark:bg-slate-700 text-white dark:text-slate-100 rounded-2xl px-5 py-1.5 transition-all cursor-pointer">
<span class="material-symbols-outlined" data-icon="newspaper" style="font-variation-settings: 'FILL' 1;">newspaper</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">News</span>
</div>
<div class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 px-5 py-1.5 hover:text-[#725a42] transition-colors cursor-pointer group">
<span class="material-symbols-outlined group-active:scale-95 transition-transform" data-icon="person">person</span>
<span class="font-['Inter'] text-[11px] font-medium tracking-tight">Profile</span>
</div>
</nav>
</body></html>

<!-- Juristic News / ข่าวสารจากนิติบุคคล -->
<!DOCTYPE html>

<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&amp;family=Inter:wght@400;500;600&amp;family=Prompt:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            colors: {
              "on-secondary-fixed": "#291806",
              "surface-tint": "#50606f",
              "surface": "#fafaeb",
              "on-surface-variant": "#43474c",
              "error-container": "#ffdad6",
              "surface-container-low": "#f4f5e6",
              "on-primary-container": "#fdfcff",
              "tertiary-fixed": "#ffdbcd",
              "tertiary": "#914723",
              "primary-fixed-dim": "#b8c8da",
              "outline-variant": "#c4c7cc",
              "tertiary-fixed-dim": "#ffb596",
              "surface-container": "#efefe0",
              "on-error-container": "#93000a",
              "inverse-surface": "#2f3128",
              "error": "#ba1a1a",
              "on-tertiary-fixed": "#360f00",
              "on-secondary": "#ffffff",
              "on-primary": "#ffffff",
              "surface-variant": "#e3e3d5",
              "on-tertiary-fixed-variant": "#76320f",
              "on-background": "#1b1c14",
              "secondary-container": "#fedcbe",
              "on-primary-fixed": "#0d1d2a",
              "primary-container": "#667686",
              "outline": "#74777c",
              "on-tertiary": "#ffffff",
              "secondary-fixed-dim": "#e1c1a4",
              "surface-container-highest": "#e3e3d5",
              "surface-bright": "#fafaeb",
              "surface-dim": "#dbdbcd",
              "surface-container-lowest": "#ffffff",
              "inverse-primary": "#b8c8da",
              "background": "#fafaeb",
              "on-secondary-container": "#796048",
              "tertiary-container": "#b05e38",
              "primary": "#4e5e6d",
              "on-tertiary-container": "#fffbff",
              "on-secondary-fixed-variant": "#59422c",
              "secondary": "#725a42",
              "secondary-fixed": "#fedcbe",
              "on-surface": "#1b1c14",
              "on-error": "#ffffff",
              "primary-fixed": "#d4e4f6",
              "inverse-on-surface": "#f1f2e3",
              "surface-container-high": "#e9e9db",
              "on-primary-fixed-variant": "#394857"
            },
            fontFamily: {
              "headline": ["Manrope", "Prompt", "sans-serif"],
              "body": ["Inter", "Prompt", "sans-serif"],
              "label": ["Inter", "Prompt", "sans-serif"]
            },
            borderRadius: {"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"},
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: #fafaeb;
            font-family: 'Inter', 'Prompt', sans-serif;
        }
        .bento-card {
            transition: transform 0.2s ease;
        }
        .bento-card:active {
            transform: scale(0.98);
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-surface text-on-surface min-h-screen pb-32">
<!-- TopAppBar -->
<header class="bg-[#f4f5e6] flex items-center justify-between px-6 py-4 w-full sticky top-0 z-50">
<div class="flex items-center gap-4">
<button class="text-[#4e5e6d] hover:opacity-80 transition-opacity">
<span class="material-symbols-outlined" data-icon="arrow_back">arrow_back</span>
</button>
<h1 class="font-headline font-bold text-xl tracking-wide text-[#4e5e6d]">Payment History</h1>
</div>
<button class="text-[#4e5e6d] hover:opacity-80 transition-opacity">
<span class="material-symbols-outlined" data-icon="translate">translate</span>
</button>
</header>
<main class="px-6 pt-6 space-y-8">
<!-- Thai Headline Anchor -->
<section class="space-y-1">
<h2 class="font-headline font-extrabold text-3xl text-secondary leading-tight">ประวัติการชำระเงิน</h2>
<p class="font-body text-on-surface-variant text-sm opacity-80">View and manage all your building transactions.</p>
</section>
<!-- Filter Rail: Glassmorphism effect -->
<div class="flex space-x-2 overflow-x-auto pb-2 scrollbar-hide">
<button class="flex-none px-6 py-2.5 bg-primary text-on-primary rounded-full font-label text-sm font-semibold shadow-sm">
                All / ทั้งหมด
            </button>
<button class="flex-none px-6 py-2.5 bg-surface-container-high text-primary rounded-full font-label text-sm font-medium hover:bg-surface-variant transition-colors">
                CAM Fee / ค่าส่วนกลาง
            </button>
<button class="flex-none px-6 py-2.5 bg-surface-container-high text-primary rounded-full font-label text-sm font-medium hover:bg-surface-variant transition-colors">
                Utilities / สาธารณูปโภค
            </button>
</div>
<!-- At-a-Glance Summary Bento Grid -->
<div class="grid grid-cols-2 gap-4">
<div class="col-span-2 bg-gradient-to-br from-primary to-primary-container p-6 rounded-[24px] text-on-primary shadow-lg">
<div class="flex justify-between items-start mb-4">
<span class="font-label text-xs uppercase tracking-widest opacity-80">Total Paid 2024</span>
<span class="material-symbols-outlined" data-icon="account_balance_wallet">account_balance_wallet</span>
</div>
<div class="font-headline font-bold text-4xl mb-1">9,846.00 <span class="text-xl">THB</span></div>
<div class="font-body text-sm opacity-90">Total of 4 transactions cleared</div>
</div>
</div>
<!-- Transaction List: Asymmetric & Editorial Layout -->
<div class="space-y-6">
<h3 class="font-headline font-bold text-lg text-secondary px-1">Recent Transactions</h3>
<div class="space-y-4">
<!-- Card 1 -->
<div class="bento-card group relative bg-surface-container-lowest p-5 rounded-[24px] shadow-[0_4px_12px_rgba(78,94,109,0.04)] hover:shadow-md transition-all">
<div class="flex justify-between items-start">
<div class="space-y-1">
<span class="font-label text-[10px] uppercase font-bold tracking-tighter text-secondary opacity-60">CAM Fee / ค่าส่วนกลาง</span>
<h4 class="font-headline font-bold text-on-surface text-lg">September 2024 CAM Fee</h4>
<p class="font-body text-sm text-on-surface-variant">Date: 05 Sep 2024</p>
</div>
<div class="bg-secondary-container text-on-secondary-container px-3 py-1 rounded-full text-[10px] font-bold">
                            Paid / ชำระแล้ว
                        </div>
</div>
<div class="mt-6 flex justify-between items-end border-t border-surface-container-low pt-4">
<div class="font-headline font-extrabold text-2xl text-primary">4,248.00 <span class="text-sm font-normal">THB</span></div>
<button class="flex items-center gap-1 text-secondary font-label text-sm font-bold">
                            Receipt <span class="material-symbols-outlined text-sm" data-icon="download">download</span>
</button>
</div>
</div>
<!-- Card 2 -->
<div class="bento-card group relative bg-surface-container-lowest p-5 rounded-[24px] shadow-[0_4px_12px_rgba(78,94,109,0.04)] hover:shadow-md transition-all">
<div class="flex justify-between items-start">
<div class="space-y-1">
<span class="font-label text-[10px] uppercase font-bold tracking-tighter text-secondary opacity-60">CAM Fee / ค่าส่วนกลาง</span>
<h4 class="font-headline font-bold text-on-surface text-lg">August 2024 CAM Fee</h4>
<p class="font-body text-sm text-on-surface-variant">Date: 05 Aug 2024</p>
</div>
<div class="bg-secondary-container text-on-secondary-container px-3 py-1 rounded-full text-[10px] font-bold">
                            Paid / ชำระแล้ว
                        </div>
</div>
<div class="mt-6 flex justify-between items-end border-t border-surface-container-low pt-4">
<div class="font-headline font-extrabold text-2xl text-primary">4,248.00 <span class="text-sm font-normal">THB</span></div>
<button class="flex items-center gap-1 text-secondary font-label text-sm font-bold">
                            Receipt <span class="material-symbols-outlined text-sm" data-icon="download">download</span>
</button>
</div>
</div>
<!-- Card 3 & 4: Smaller grid pattern for variety -->
<div class="grid grid-cols-1 gap-4">
<!-- Card 3 -->
<div class="bento-card bg-surface-container-low p-5 rounded-[24px] flex justify-between items-center">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-2xl bg-surface-container-highest flex items-center justify-center text-primary">
<span class="material-symbols-outlined" data-icon="water_drop">water_drop</span>
</div>
<div>
<h4 class="font-headline font-bold text-on-surface text-base">Water Bill - 20/145</h4>
<p class="font-body text-xs text-on-surface-variant">20 Aug 2024</p>
</div>
</div>
<div class="text-right">
<div class="font-headline font-bold text-primary">350.00</div>
<div class="text-[10px] font-bold text-secondary">PAID</div>
</div>
</div>
<!-- Card 4 -->
<div class="bento-card bg-surface-container-low p-5 rounded-[24px] flex justify-between items-center">
<div class="flex items-center gap-4">
<div class="w-12 h-12 rounded-2xl bg-surface-container-highest flex items-center justify-center text-primary">
<span class="material-symbols-outlined" data-icon="directions_car">directions_car</span>
</div>
<div>
<h4 class="font-headline font-bold text-on-surface text-base">Parking Fee / ค่าที่จอดรถ</h4>
<p class="font-body text-xs text-on-surface-variant">10 Aug 2024</p>
</div>
</div>
<div class="text-right">
<div class="font-headline font-bold text-primary">1,000.00</div>
<div class="text-[10px] font-bold text-secondary">PAID</div>
</div>
</div>
</div>
</div>
</div>
<!-- Support Section -->
<section class="mt-8 mb-12 bg-secondary-container/30 p-6 rounded-[32px] border border-secondary/10 text-center">
<h5 class="font-headline font-bold text-secondary mb-2">Need help with payments?</h5>
<p class="font-body text-sm text-on-surface-variant mb-4 px-4">Our concierge is available 24/7 for any billing inquiries.</p>
<button class="bg-secondary text-on-secondary px-8 py-3 rounded-full font-label font-bold text-sm shadow-sm hover:opacity-90 active:scale-95 transition-all">
                Contact Office
            </button>
</section>
</main>
<!-- BottomNavBar -->
<nav class="fixed bottom-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3 bg-[#fafaeb]/80 dark:bg-slate-900/80 backdrop-blur-md shadow-[0_-8px_24px_rgba(78,94,109,0.08)] rounded-t-[32px]">
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 p-2 hover:bg-[#f4f5e6] dark:hover:bg-slate-800 rounded-2xl transition-all duration-300 ease-in-out" href="#">
<span class="material-symbols-outlined" data-icon="home">home</span>
<span class="font-['Inter'] text-[10px] font-medium tracking-tight">Home</span>
</a>
<a class="flex flex-col items-center justify-center bg-[#4e5e6d] text-white rounded-2xl p-2 px-4 transition-all duration-300 ease-in-out" href="#">
<span class="material-symbols-outlined" data-icon="account_balance_wallet" style="font-variation-settings: 'FILL' 1;">account_balance_wallet</span>
<span class="font-['Inter'] text-[10px] font-medium tracking-tight">Payments</span>
</a>
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 p-2 hover:bg-[#f4f5e6] dark:hover:bg-slate-800 rounded-2xl transition-all duration-300 ease-in-out" href="#">
<span class="material-symbols-outlined" data-icon="dry_cleaning">dry_cleaning</span>
<span class="font-['Inter'] text-[10px] font-medium tracking-tight">Services</span>
</a>
<a class="flex flex-col items-center justify-center text-[#43474c] dark:text-slate-400 p-2 hover:bg-[#f4f5e6] dark:hover:bg-slate-800 rounded-2xl transition-all duration-300 ease-in-out" href="#">
<span class="material-symbols-outlined" data-icon="person">person</span>
<span class="font-['Inter'] text-[10px] font-medium tracking-tight">Profile</span>
</a>
</nav>
</body></html>