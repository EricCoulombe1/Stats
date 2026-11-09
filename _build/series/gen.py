# Generates the investing series strip, one variant per page (current page marked, no JS needed).
import html
PAGES=[
 ("investing.html","Start Here","What owning one house is like"),
 ("investment-properties-northern-bc.html","Leverage, Explained","The numbers behind a mortgage"),
 ("one-house-fifteen-years.html","One House, Fifteen Years","One house, held for 15 years"),
 ("spinning-wheel.html","The Spinning Wheel","Recycling equity, with the rules"),
 ("fort-st-john-investor-brief.html","Fort St. John","Why this town, and the risks"),
 ("investmentproperties.html","Current Opportunities","Properties on the market now"),
 ("our-portfolio.html","Our Portfolio","Our own rentals, by the numbers"),
]
CSS="""<style>
#ec-series{--r:#B7202E;--ink:#1F2124;--body:#45484D;--mut:#5E6166;--ln:#E2E2DF;background:#fff;border-top:1px solid var(--ln);border-bottom:1px solid var(--ln);font-family:'Engel Voelkers Text','Helvetica Neue',Arial,sans-serif;color:var(--body)}
#ec-series *{box-sizing:border-box}
#ec-series .ecs-w{max-width:1120px;margin:0 auto;padding:36px 16px 32px}
#ec-series .ecs-top{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:8px 24px;margin:0 0 16px}
#ec-series .ecs-k{margin:0;font-size:12px !important;line-height:1.4 !important;letter-spacing:.1em;text-transform:uppercase;font-weight:700;color:var(--r)}
#ec-series .ecs-nx{margin:0;font-size:15px !important;line-height:1.4 !important}
#ec-series .ecs-nx a{color:var(--r);font-weight:600;text-decoration:none}
#ec-series .ecs-nx a:hover{text-decoration:underline}
#ec-series ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(138px,1fr));gap:0 16px}
#ec-series li{margin:0;padding:0;border-top:2px solid var(--ln);list-style:none}
#ec-series li::before,#ec-series li::marker{content:none}
#ec-series li a,#ec-series li .ecs-here{display:block;padding:12px 0 14px;text-decoration:none;color:inherit}
#ec-series .ecs-n{display:block;font-family:'Engel Voelkers Head',Georgia,serif;font-size:13px !important;line-height:1.2 !important;color:var(--mut);margin:0 0 4px}
#ec-series .ecs-t{display:block;font-size:15px !important;line-height:1.3 !important;font-weight:600;color:var(--ink)}
#ec-series .ecs-d{display:block;font-size:13px !important;line-height:1.4 !important;color:var(--mut);margin-top:4px}
#ec-series li a:hover .ecs-t{color:var(--r)}
#ec-series li[aria-current]{border-top-color:var(--r)}
#ec-series li[aria-current] .ecs-n{color:var(--r)}
#ec-series .ecs-you{font-size:11px !important;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--r);margin-left:6px;font-family:'Engel Voelkers Text','Helvetica Neue',Arial,sans-serif}
@media(max-width:640px){#ec-series .ecs-w{padding:28px 16px 24px}#ec-series ol{grid-template-columns:1fr}#ec-series li a,#ec-series li .ecs-here{display:grid;grid-template-columns:28px 1fr;column-gap:8px;padding:10px 0}#ec-series .ecs-n{grid-row:1/3;margin:2px 0 0}#ec-series .ecs-d{margin-top:2px}#ec-series li{border-top-width:1px}#ec-series li[aria-current]{border-top-width:2px}}
</style>"""
def strip(cur):
    i=[p[0] for p in PAGES].index(cur)
    items=[]
    for k,(href,t,d) in enumerate(PAGES):
        inner=f'<span class="ecs-n">{k+1:02d}</span><span class="ecs-t">{html.escape(t)}</span><span class="ecs-d">{html.escape(d)}</span>'
        if k==i:
            inner=inner.replace('</span><span class="ecs-d">','<span class="ecs-you">You&rsquo;re here</span></span><span class="ecs-d">',1)
            items.append(f'<li aria-current="page"><span class="ecs-here">{inner}</span></li>')
        else:
            items.append(f'<li><a href="{href}">{inner}</a></li>')
    if i<len(PAGES)-1:
        n=PAGES[i+1]; nx=f'Next: <a href="{n[0]}">{html.escape(n[1])} &rarr;</a>'
    else:
        nx='Want the full reports? <a href="request-reports.html">Ask for them &rarr;</a>'
    return (f'<!-- EC investing series strip v1.0 (2026-11-08). Same block on every investing page; only the current item differs. Source: stats repo _build/series/gen.py -->\n'
            f'{CSS}\n<nav id="ec-series" aria-label="The investing series"><div class="ecs-w"><div class="ecs-top"><p class="ecs-k">The investing series &middot; {i+1} of {len(PAGES)}</p><p class="ecs-nx">{nx}</p></div><ol>{"".join(items)}</ol></div></nav>\n<!-- /EC investing series strip -->\n')
for href,_,_ in PAGES:
    open(href.replace('.html','')+'.strip.html','w').write(strip(href))
# preview page
pv='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Series strip preview</title><link rel="stylesheet" href="https://stats.ericcoulombe.com/assets/fonts/ev-fonts.css"></head><body style="margin:0">'
pv+=''.join('<div style="height:24px;background:#F4F4F2"></div>'+strip(h) for h,_,_ in [PAGES[0],PAGES[3],PAGES[6]])+'</body></html>'
open('preview.html','w').write(pv)
