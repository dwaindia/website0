with open('about-us.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Revert #page-tabs to standard anchor links with black bg & theme hover
nav_start = c.find('<nav id="page-tabs"')
nav_end = c.find('</nav>', nav_start) + len('</nav>')

reverted_nav = '''<nav id="page-tabs" class="sticky top-16 md:top-20 z-40 bg-white/95 backdrop-blur-md border-b border-border shadow-sm py-3 px-4 sm:px-6 md:px-8" aria-label="Section navigation">
    <div class="max-w-content mx-auto">
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 md:gap-4">
        
        <!-- Tab 1: Problem -->
        <a href="#problem"
           class="inline-flex items-center justify-center gap-2.5 sm:gap-3.5 px-4 sm:px-6 md:px-8 py-3.5 sm:py-4 border border-black bg-black hover:bg-accent hover:border-accent text-white hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm">
          <svg class="w-4 h-4 text-white group-hover:text-white transition-colors shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="10"/>
            <line x1="12" y1="8" x2="12" y2="12"/>
            <line x1="12" y1="16" x2="12.01" y2="16"/>
          </svg>
          <span>Problem</span>
        </a>

        <!-- Tab 2: Plan -->
        <a href="#plan"
           class="inline-flex items-center justify-center gap-2.5 sm:gap-3.5 px-4 sm:px-6 md:px-8 py-3.5 sm:py-4 border border-black bg-black hover:bg-accent hover:border-accent text-white hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm">
          <svg class="w-4 h-4 text-white group-hover:text-white transition-colors shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
          <span>Plan</span>
        </a>

        <!-- Tab 3: People -->
        <a href="#people"
           class="inline-flex items-center justify-center gap-2.5 sm:gap-3.5 px-4 sm:px-6 md:px-8 py-3.5 sm:py-4 border border-black bg-black hover:bg-accent hover:border-accent text-white hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm">
          <svg class="w-4 h-4 text-white group-hover:text-white transition-colors shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
            <circle cx="9" cy="7" r="4"/>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
          </svg>
          <span>People</span>
        </a>

        <!-- Tab 4: Credentials -->
        <a href="#credentials"
           class="inline-flex items-center justify-center gap-2.5 sm:gap-3.5 px-4 sm:px-6 md:px-8 py-3.5 sm:py-4 border border-black bg-black hover:bg-accent hover:border-accent text-white hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm">
          <svg class="w-4 h-4 text-white group-hover:text-white transition-colors shrink-0" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            <polyline points="9 12 11 14 15 10"/>
          </svg>
          <span>Credentials</span>
        </a>

      </div>
    </div>
  </nav>'''

c = c[:nav_start] + reverted_nav + c[nav_end:]

# 2. Revert main content to single problem card
main_start = c.find('</nav>') + len('</nav>')
main_end = c.find('</main>', main_start)

single_problem_section = '''

  <!-- ═══════════════════════════════
       SOCIOECONOMIC CHALLENGES & MAJOR PROBLEM HIGHLIGHTS
       Horizontal 2-Column Card (Border Gray-300, Black on Hover)
  ═══════════════════════════════ -->
  <section id="problem" class="scroll-mt-32 md:scroll-mt-36 py-12 sm:py-16 md:py-20 bg-offwhite border-b border-border" aria-label="Socioeconomic Challenges in Rural Rayalaseema">
    <div class="max-w-content mx-auto px-4 sm:px-6 md:px-8">
      
      <!-- Full section width horizontal card (Left Image: 2-2.jpg, Right Content) -->
      <div class="border border-gray-300 hover:border-black transition-colors duration-300 bg-white flex flex-col lg:flex-row overflow-hidden group shadow-sm">
        
        <!-- Left Column: Image 2-2.jpg -->
        <div class="w-full lg:w-1/2 relative overflow-hidden bg-gray-100 min-h-[300px] sm:min-h-[380px] lg:min-h-full">
          <img src="2-2.jpg"
               alt="Socioeconomic challenges and agrarian crisis in rural Rayalaseema"
               class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
               loading="lazy" />
        </div>

        <!-- Right Column: Heading, Description, Link, and Major Problem Highlight Buttons -->
        <div class="w-full lg:w-1/2 p-6 sm:p-8 md:p-10 lg:p-12 flex flex-col justify-between">
          <div>
            <!-- Heading -->
            <h2 class="font-heading font-bold text-2xl sm:text-3xl text-primary leading-tight mb-4 tracking-tight">
              Structural Marginalization and Agrarian Crisis: Socioeconomic Challenges in Rural Rayalaseema
            </h2>

            <!-- Description -->
            <p class="font-sans text-secondary text-sm sm:text-base leading-relaxed mb-6 text-justify">
              In the semi-arid Rayalaseema belt of Andhra Pradesh, deep-seated caste inequities, landlessness, and chronic drought cycles trap rural Dalit families in acute economic distress. Without access to formal banking or irrigation safety nets, marginalized households face severe crop losses, financial stagnation, and seasonal distress migration.
            </p>

            <!-- Link: Opens Right-Side Popup Drawer -->
            <div class="mb-8">
              <button type="button"
                      id="open-problem-drawer"
                      class="inline-flex items-center gap-2 font-heading font-bold text-xs sm:text-sm tracking-wider uppercase text-primary hover:text-accent border-b-2 border-primary hover:border-accent pb-1 transition-colors cursor-pointer group/link">
                <span>Read Complete Context &amp; Analysis</span>
                <svg class="w-4 h-4 transform group-hover/link:translate-x-1 transition-transform" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Below: Buttons with icons for major highlights of the problem -->
          <div class="pt-5 border-t border-gray-200">
            <p class="font-heading font-bold text-xs uppercase tracking-wider text-secondary mb-3.5">
              Highlights of Major Problems
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              <!-- Button 1 -->
              <button type="button" data-highlight-index="0" class="problem-highlight-btn text-left p-3 border border-gray-300 hover:border-black transition-colors duration-200 bg-white flex items-center gap-2.5 rounded-none cursor-pointer group/btn">
                <div class="w-7 h-7 shrink-0 rounded-none bg-offwhite flex items-center justify-center text-primary group-hover/btn:bg-primary group-hover/btn:text-white transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
                </div>
                <span class="font-heading font-semibold text-xs text-primary leading-tight">Systemic Socioeconomic Exclusion</span>
              </button>

              <!-- Button 2 -->
              <button type="button" data-highlight-index="1" class="problem-highlight-btn text-left p-3 border border-gray-300 hover:border-black transition-colors duration-200 bg-white flex items-center gap-2.5 rounded-none cursor-pointer group/btn">
                <div class="w-7 h-7 shrink-0 rounded-none bg-offwhite flex items-center justify-center text-primary group-hover/btn:bg-primary group-hover/btn:text-white transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/><circle cx="12" cy="12" r="4"/></svg>
                </div>
                <span class="font-heading font-semibold text-xs text-primary leading-tight">Agrarian Instability &amp; Climate</span>
              </button>

              <!-- Button 3 -->
              <button type="button" data-highlight-index="2" class="problem-highlight-btn text-left p-3 border border-gray-300 hover:border-black transition-colors duration-200 bg-white flex items-center gap-2.5 rounded-none cursor-pointer group/btn">
                <div class="w-7 h-7 shrink-0 rounded-none bg-offwhite flex items-center justify-center text-primary group-hover/btn:bg-primary group-hover/btn:text-white transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="0"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>
                </div>
                <span class="font-heading font-semibold text-xs text-primary leading-tight">Female Enterprise Stagnation</span>
              </button>

              <!-- Button 4 -->
              <button type="button" data-highlight-index="3" class="problem-highlight-btn text-left p-3 border border-gray-300 hover:border-black transition-colors duration-200 bg-white flex items-center gap-2.5 rounded-none cursor-pointer group/btn">
                <div class="w-7 h-7 shrink-0 rounded-none bg-offwhite flex items-center justify-center text-primary group-hover/btn:bg-primary group-hover/btn:text-white transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                </div>
                <span class="font-heading font-semibold text-xs text-primary leading-tight">Education Access &amp; Dropouts</span>
              </button>

              <!-- Button 5 -->
              <button type="button" data-highlight-index="4" class="problem-highlight-btn sm:col-span-2 text-left p-3 border border-gray-300 hover:border-black transition-colors duration-200 bg-white flex items-center gap-2.5 rounded-none cursor-pointer group/btn">
                <div class="w-7 h-7 shrink-0 rounded-none bg-offwhite flex items-center justify-center text-primary group-hover/btn:bg-primary group-hover/btn:text-white transition-colors">
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 010 8h-1M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
                </div>
                <span class="font-heading font-semibold text-xs text-primary leading-tight">Nutritional Insecurity &amp; Crisis Vulnerability</span>
              </button>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
'''

c = c[:main_start] + single_problem_section + '\n' + c[main_end:]

# 3. Revert drawers to single problem drawer
drawers_start = c.find('<!-- ═══════════════════════════════\n     RIGHT-SIDE DRAWERS')
drawers_end = c.find('<!-- ═══════════════════════════════\n     PRIVACY POLICY MODAL')

single_drawer = '''<!-- ═══════════════════════════════
     RIGHT-SIDE PROBLEM OVERVIEW POPUP (DRAWER)
═══════════════════════════════ -->
<div id="problem-drawer-overlay"
     class="fixed inset-0 z-[75] bg-black/60 opacity-0 pointer-events-none transition-opacity duration-300"
     aria-hidden="true"></div>

<aside id="problem-drawer"
       class="fixed top-0 right-0 z-[80] h-full w-full max-w-2xl bg-white shadow-2xl flex flex-col transform translate-x-full transition-transform duration-300 ease-in-out will-change-transform overflow-hidden"
       role="dialog"
       aria-modal="true"
       aria-labelledby="problem-drawer-title">
  
  <!-- Drawer Header -->
  <div class="p-6 sm:p-7 border-b border-border bg-offwhite flex items-center justify-between gap-4 shrink-0">
    <div>
      <span class="inline-block text-[11px] font-heading font-bold uppercase tracking-wider text-accent mb-1">
        Context &amp; Analysis
      </span>
      <h3 id="problem-drawer-title" class="font-heading font-bold text-base sm:text-lg text-primary leading-snug">
        Socioeconomic Challenges in Rural Rayalaseema
      </h3>
    </div>
    <button id="close-problem-drawer"
            type="button"
            aria-label="Close drawer"
            class="w-9 h-9 flex items-center justify-center border border-border hover:border-black text-secondary hover:text-primary transition-colors cursor-pointer shrink-0 rounded-none bg-white">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </button>
  </div>

  <!-- Drawer Scrollable Content -->
  <div id="problem-drawer-body" class="p-6 sm:p-8 md:p-10 overflow-y-auto space-y-8 flex-grow">
    
    <!-- Main Title -->
    <div class="border-b border-border pb-4">
      <h3 class="font-heading font-bold text-xl sm:text-2xl text-primary leading-snug">
        Structural Marginalization and Agrarian Crisis: Socioeconomic Challenges in Rural Rayalaseema
      </h3>
    </div>

    <!-- Historical Context -->
    <div class="space-y-3">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 bg-accent inline-block"></span>
        <h4 class="font-heading font-bold text-base sm:text-lg text-primary uppercase tracking-wide">
          Historical Context
        </h4>
      </div>
      <p class="font-sans text-secondary text-sm sm:text-base leading-relaxed text-justify">
        Historically, rural Dalit and oppressed communities across Andhra Pradesh have endured deep-seated caste-based inequities, social exclusion, and systemic poverty that severely restricted their economic mobility. For generations, limited access to land ownership, formal credit, and higher education forced these down-trodden populations into low-wage, unorganized agricultural labor. Women in these marginalized households faced compound structural barriers, lacking independent asset ownership, business management skills, or formal financial representation. Furthermore, high illiteracy rates and lack of primary school support reinforced intergenerational poverty cycles across successive generations. Without organized community institutions or formal welfare safety nets, marginalized families remained vulnerable to systemic economic exploitation and debt traps. These historical inequities created a persistent socioeconomic divide that voluntary initiatives continue working to dismantle.
      </p>
    </div>

    <!-- Regional Context -->
    <div class="space-y-3">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 bg-accent inline-block"></span>
        <h4 class="font-heading font-bold text-base sm:text-lg text-primary uppercase tracking-wide">
          Regional Context
        </h4>
      </div>
      <p class="font-sans text-secondary text-sm sm:text-base leading-relaxed text-justify">
        Regionally, DWA’s target populations live in the semi-arid Rayalaseema belt of Kurnool District, Andhra Pradesh—specifically across Sirivella Block, Bandi Atmakur Mandal, and surrounding rural Panchayats. Rayalaseema is defined by severe climatic vulnerability, recurring drought cycles, and El Niño-induced monsoon failures that disrupt subsistence agriculture. Because local village economies depend heavily on rain-fed farming and daily-wage agricultural labor, water scarcity triggers severe agrarian distress, crop loss, and household income collapse. During dry seasons and winter months, landless Dalit families, single mothers, and widowed heads of households face extreme economic vulnerability, often forced into seasonal distress migration to urban centers in search of basic livelihood work.
      </p>
    </div>

    <!-- Highlights of Major Problems -->
    <div class="space-y-4 pt-4 border-t border-border">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 bg-accent inline-block"></span>
        <h4 class="font-heading font-bold text-base sm:text-lg text-primary uppercase tracking-wide">
          Highlights of Major Problems
        </h4>
      </div>
      <div class="space-y-3">
        
        <!-- Highlight 0 -->
        <div id="drawer-highlight-0" class="drawer-hl-item p-4 border border-border bg-offwhite transition-all duration-300">
          <h5 class="font-heading font-bold text-sm text-primary mb-1 flex items-center gap-2">
            <span class="w-1.5 h-1.5 bg-primary inline-block"></span>
            Systemic Socioeconomic Exclusion
          </h5>
          <p class="font-sans text-secondary text-xs sm:text-sm leading-relaxed">
            High reliance on unorganized daily-wage labor, absence of land assets, and persistent socio-cultural barriers for Dalit and Below Poverty Line (BPL) families.
          </p>
        </div>

        <!-- Highlight 1 -->
        <div id="drawer-highlight-1" class="drawer-hl-item p-4 border border-border bg-offwhite transition-all duration-300">
          <h5 class="font-heading font-bold text-sm text-primary mb-1 flex items-center gap-2">
            <span class="w-1.5 h-1.5 bg-primary inline-block"></span>
            Agrarian Instability &amp; Climate Vulnerability
          </h5>
          <p class="font-sans text-secondary text-xs sm:text-sm leading-relaxed">
            Chronic drought cycles, groundwater depletion, and El Niño weather patterns causing recurring crop failures and distress migration.
          </p>
        </div>

        <!-- Highlight 2 -->
        <div id="drawer-highlight-2" class="drawer-hl-item p-4 border border-border bg-offwhite transition-all duration-300">
          <h5 class="font-heading font-bold text-sm text-primary mb-1 flex items-center gap-2">
            <span class="w-1.5 h-1.5 bg-primary inline-block"></span>
            Female Enterprise Stagnation &amp; Financial Gaps
          </h5>
          <p class="font-sans text-secondary text-xs sm:text-sm leading-relaxed">
            Over 98% of rural women's businesses remain trapped at micro-scale due to a lack of credit access, informal record-keeping, and low digital banking adoption.
          </p>
        </div>

        <!-- Highlight 3 -->
        <div id="drawer-highlight-3" class="drawer-hl-item p-4 border border-border bg-offwhite transition-all duration-300">
          <h5 class="font-heading font-bold text-sm text-primary mb-1 flex items-center gap-2">
            <span class="w-1.5 h-1.5 bg-primary inline-block"></span>
            Primary Education Access &amp; Dropout Risks
          </h5>
          <p class="font-sans text-secondary text-xs sm:text-sm leading-relaxed">
            Financial hardship, lack of basic school supplies, and migration-induced family movement forcing underprivileged children out of government primary schools.
          </p>
        </div>

        <!-- Highlight 4 -->
        <div id="drawer-highlight-4" class="drawer-hl-item p-4 border border-border bg-offwhite transition-all duration-300">
          <h5 class="font-heading font-bold text-sm text-primary mb-1 flex items-center gap-2">
            <span class="w-1.5 h-1.5 bg-primary inline-block"></span>
            Nutritional Insecurity &amp; Crisis Vulnerability
          </h5>
          <p class="font-sans text-secondary text-xs sm:text-sm leading-relaxed">
            Lack of emergency food safety nets during seasonal agricultural downturns, winter distress, and economic shocks.
          </p>
        </div>

      </div>
    </div>

  </div>

  <!-- Drawer Footer -->
  <div class="p-4 sm:p-5 border-t border-border bg-offwhite shrink-0 flex items-center justify-between">
    <span class="text-xs text-secondary font-sans font-medium">Dalit Welfare Association &bull; Kurnool District</span>
    <button type="button" id="close-problem-drawer-footer" class="px-5 py-2.5 bg-primary hover:bg-accent text-white hover:text-primary font-heading font-bold text-xs uppercase tracking-wider transition-colors cursor-pointer rounded-none">
      Close
    </button>
  </div>

</aside>
'''

c = c[:drawers_start] + single_drawer + '\n' + c[drawers_end:]

# 4. Revert JavaScript to single drawer handler
js_start = c.find('/* ── Tab Switching & Right-Side Drawers ── */')
js_end = c.find('</script>\n</body>')
if js_end == -1:
    js_end = c.rfind('</script>')

single_js = '''/* ── Problem Overview Right-Side Drawer ── */
  const problemDrawer = document.getElementById('problem-drawer');
  const problemOverlay = document.getElementById('problem-drawer-overlay');
  const openDrawerBtn = document.getElementById('open-problem-drawer');
  const closeDrawerBtn = document.getElementById('close-problem-drawer');
  const closeDrawerFooter = document.getElementById('close-problem-drawer-footer');
  const highlightBtns = document.querySelectorAll('.problem-highlight-btn');

  function openProblemDrawer(targetIndex = null) {
    if (!problemDrawer || !problemOverlay) return;
    problemDrawer.classList.remove('translate-x-full');
    problemOverlay.classList.remove('opacity-0', 'pointer-events-none');
    document.body.style.overflow = 'hidden';

    if (targetIndex !== null) {
      const targetEl = document.getElementById('drawer-highlight-' + targetIndex);
      if (targetEl) {
        setTimeout(() => {
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          targetEl.classList.add('border-accent', 'bg-accent/10');
          setTimeout(() => {
            targetEl.classList.remove('border-accent', 'bg-accent/10');
          }, 2000);
        }, 320);
      }
    }
  }

  function closeProblemDrawer() {
    if (!problemDrawer || !problemOverlay) return;
    problemDrawer.classList.add('translate-x-full');
    problemOverlay.classList.add('opacity-0', 'pointer-events-none');
    document.body.style.overflow = '';
  }

  if (openDrawerBtn) openDrawerBtn.addEventListener('click', () => openProblemDrawer());
  if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeProblemDrawer);
  if (closeDrawerFooter) closeDrawerFooter.addEventListener('click', closeProblemDrawer);
  if (problemOverlay) problemOverlay.addEventListener('click', closeProblemDrawer);

  highlightBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const idx = btn.getAttribute('data-highlight-index');
      openProblemDrawer(idx);
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && problemDrawer && !problemDrawer.classList.contains('translate-x-full')) {
      closeProblemDrawer();
    }
  });'''

c = c[:js_start] + single_js + '\n' + c[js_end:]

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('about-us.html reverted successfully!')
