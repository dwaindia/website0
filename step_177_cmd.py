python3 -c "
import re

# ══════════════════════════════════════════
# 2. UPDATE PROGRAMS.HTML
# ══════════════════════════════════════════
with open('programs.html', 'r') as fp:
    p_content = fp.read()

PROGRAMS_TAB_MENU = '''  <!-- ═══════════════════════════════
       STICKY SECTION TABS MENU (Problem, Plan, People, Credentials)
  ═══════════════════════════════ -->
  <nav id=\"page-tabs\" class=\"sticky top-16 md:top-20 z-40 bg-white/95 backdrop-blur-md border-b border-border shadow-sm py-3 px-4 sm:px-6 md:px-8\" aria-label=\"Section navigation\">
    <div class=\"max-w-content mx-auto\">
      <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 md:gap-4\">
        
        <!-- Tab 1: Problem -->
        <a href=\"#problem\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-primary shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <circle cx=\"12\" cy=\"12\" r=\"10\"/>
            <line x1=\"12\" y1=\"8\" x2=\"12\" y2=\"12\"/>
            <line x1=\"12\" y1=\"16\" x2=\"12.01\" y2=\"16\"/>
          </svg>
          <span>Problem</span>
        </a>

        <!-- Tab 2: Plan -->
        <a href=\"#plan\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-primary shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/>
            <polyline points=\"14 2 14 8 20 8\"/>
            <line x1=\"16\" y1=\"13\" x2=\"8\" y2=\"13\"/>
            <line x1=\"16\" y1=\"17\" x2=\"8\" y2=\"17\"/>
            <polyline points=\"10 9 9 9 8 9\"/>
          </svg>
          <span>Plan</span>
        </a>

        <!-- Tab 3: People -->
        <a href=\"#people\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-primary shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2\"/>
            <circle cx=\"9\" cy=\"7\" r=\"4\"/>
            <path d=\"M23 21v-2a4 4 0 0 0-3-3.87\"/>
            <path d=\"M16 3.13a4 4 0 0 1 0 7.75\"/>
          </svg>
          <span>People</span>
        </a>

        <!-- Tab 4: Credentials -->
        <a href=\"#credentials\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-primary shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z\"/>
            <polyline points=\"9 12 11 14 15 10\"/>
          </svg>
          <span>Credentials</span>
        </a>

      </div>
    </div>
  </nav>
'''

p_content = p_content.replace('</section>\n\n  <!-- Program 1: Women\'s Banking -->\n  <section id=\"womens-banking\" class=\"py-16 md:py-20 border-b border-border\">',
                              '</section>\n\n' + PROGRAMS_TAB_MENU + '\n  <!-- Program 1: Women\'s Banking (Problem) -->\n  <section id=\"problem\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 border-b border-border\"><div id=\"womens-banking\"></div>')

p_content = p_content.replace('<!-- Program 2: Education -->\n  <section id=\"education\" class=\"py-16 md:py-20 bg-offwhite border-b border-border\">',
                              '<!-- Program 2: Education (Plan) -->\n  <section id=\"plan\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 bg-offwhite border-b border-border\"><div id=\"education\"></div>')

p_content = p_content.replace('<!-- Program 3: Emergency Relief -->\n  <section id=\"relief\" class=\"py-16 md:py-20 border-b border-border\">',
                              '<!-- Program 3: Emergency Relief (People) -->\n  <section id=\"people\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 border-b border-border\"><div id=\"relief\"></div>')

p_content = p_content.replace('<!-- CTA -->\n  <section class=\"py-16 md:py-20 bg-navy text-white text-center\">',
                              '<!-- Funding & Credentials (CTA) -->\n  <section id=\"credentials\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 bg-navy text-white text-center\">')

with open('programs.html', 'w') as fp:
    fp.write(p_content)

print('Updated programs.html successfully!')


# ══════════════════════════════════════════
# 3. UPDATE ACCOUNTABILITY.HTML
# ══════════════════════════════════════════
with open('accountability.html', 'r') as fp:
    a_content = fp.read()

ACCOUNTABILITY_TAB_MENU = '''  <!-- ═══════════════════════════════
       STICKY SECTION TABS MENU (Problem, Plan, People, Credentials)
  ═══════════════════════════════ -->
  <nav id=\"page-tabs\" class=\"sticky top-16 md:top-20 z-40 bg-white/95 backdrop-blur-md border-b border-border shadow-sm py-3 px-4 sm:px-6 md:px-8\" aria-label=\"Section navigation\">
    <div class=\"max-w-content mx-auto\">
      <div class=\"grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 md:gap-4\">
        
        <!-- Tab 1: Problem -->
        <a href=\"#problem\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-accent group-hover:text-white transition-colors shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <circle cx=\"12\" cy=\"12\" r=\"10\"/>
            <line x1=\"12\" y1=\"8\" x2=\"12\" y2=\"12\"/>
            <line x1=\"12\" y1=\"16\" x2=\"12.01\" y2=\"16\"/>
          </svg>
          <span>Problem</span>
        </a>

        <!-- Tab 2: Plan -->
        <a href=\"#plan\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-accent group-hover:text-white transition-colors shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z\"/>
            <polyline points=\"14 2 14 8 20 8\"/>
            <line x1=\"16\" y1=\"13\" x2=\"8\" y2=\"13\"/>
            <line x1=\"16\" y1=\"17\" x2=\"8\" y2=\"17\"/>
            <polyline points=\"10 9 9 9 8 9\"/>
          </svg>
          <span>Plan</span>
        </a>

        <!-- Tab 3: People -->
        <a href=\"#people\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-accent group-hover:text-white transition-colors shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2\"/>
            <circle cx=\"9\" cy=\"7\" r=\"4\"/>
            <path d=\"M23 21v-2a4 4 0 0 0-3-3.87\"/>
            <path d=\"M16 3.13a4 4 0 0 1 0 7.75\"/>
          </svg>
          <span>People</span>
        </a>

        <!-- Tab 4: Credentials -->
        <a href=\"#credentials\"
           class=\"inline-flex items-center justify-center gap-2 sm:gap-2.5 px-3 py-2.5 sm:py-3 border border-gray-300 hover:bg-accent hover:border-accent text-primary hover:text-white transition-all duration-200 rounded-none text-xs sm:text-sm font-heading font-semibold uppercase tracking-wider group cursor-pointer shadow-sm\">
          <svg class=\"w-4 h-4 text-accent group-hover:text-white transition-colors shrink-0\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">
            <path d=\"M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z\"/>
            <polyline points=\"9 12 11 14 15 10\"/>
          </svg>
          <span>Credentials</span>
        </a>

      </div>
    </div>
  </nav>
'''

a_content = a_content.replace('</section>\n\n  <!-- Legal Identifiers -->\n  <section class=\"py-16 md:py-20 border-b border-border\">',
                              '</section>\n\n' + ACCOUNTABILITY_TAB_MENU + '\n  <!-- Legal Identifiers (Problem) -->\n  <section id=\"problem\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 border-b border-border\">')

a_content = a_content.replace('<!-- Financial Statements -->\n  <section id=\"financials\" class=\"py-16 md:py-20 bg-offwhite border-b border-border\">',
                              '<!-- Financial Statements (Plan) -->\n  <section id=\"plan\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 bg-offwhite border-b border-border\"><div id=\"financials\"></div>')

a_content = a_content.replace('<!-- FCRA Banking -->\n  <section class=\"py-16 md:py-20 border-b border-border\">',
                              '<!-- FCRA Banking (People / Governance) -->\n  <section id=\"people\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 border-b border-border\">')

a_content = a_content.replace('<!-- Third-party verification -->\n  <section class=\"py-16 md:py-20 bg-offwhite\">',
                              '<!-- Third-Party Credentials -->\n  <section id=\"credentials\" class=\"scroll-mt-32 md:scroll-mt-36 py-16 md:py-20 bg-offwhite\">')

with open('accountability.html', 'w') as fp:
    fp.write(a_content)

print('Updated accountability.html successfully!')
"