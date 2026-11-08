"""Build the code blocks pasted into each ericcoulombe.com stats page (myRealPage HTML widget).
Output: _build/host-widgets.json. Re-paste a page's block after changing its intro or photo."""
import json,re,html,sys
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
OUT={}
p=json.load(open('pages.json'))['pages']; reg=json.load(open('registry.json'))['areas']
slug={'ubc':'ubc-market-stats.html','point-grey':'point-grey-market-stats.html','dunbar':'dunbar-mackenzie-heights-market-stats.html','kerrisdale':'kerrisdale-market-stats.html','arbutus':'arbutus-market-stats.html','kitsilano':'kitsilano-market-stats.html','fairview':'fairview-market-stats.html','downtown':'downtown-peninsula-market-stats.html'}
cover={'point-grey':'detached homes and apartments (condos) in Greater Vancouver REALTORS&reg; sub-area &ldquo;Point Grey&rdquo;. Point Grey has too few townhouse sales to chart reliably',
'dunbar':'detached homes in the Greater Vancouver REALTORS&reg; sub-areas &ldquo;Dunbar&rdquo; and &ldquo;MacKenzie Heights&rdquo;, shown separately. MacKenzie Heights is a small area with relatively few sales, so its numbers can move more from month to month',
'kerrisdale':'detached homes, apartments (condos) and townhouses in Greater Vancouver REALTORS&reg; sub-area &ldquo;Kerrisdale&rdquo;',
'arbutus':'detached homes in Greater Vancouver REALTORS&reg; sub-area &ldquo;Arbutus&rdquo;, which reports figures for detached homes only',
'kitsilano':'detached homes, apartments (condos) and townhouses in Greater Vancouver REALTORS&reg; sub-area &ldquo;Kitsilano&rdquo;',
'fairview':'apartments (condos) and townhouses in Greater Vancouver REALTORS&reg; sub-area &ldquo;Fairview VW&rdquo;. Detached homes are rare in Fairview and are not shown',
'downtown':'apartments (condos) in the Greater Vancouver REALTORS&reg; sub-areas &ldquo;Downtown VW&rdquo;, &ldquo;Yaletown&rdquo;, &ldquo;Coal Harbour&rdquo; and &ldquo;West End VW&rdquo;, shown side by side'}
short={'ubc':'UBC','point-grey':'Point Grey','dunbar':'Dunbar &amp; MacKenzie Heights','kerrisdale':'Kerrisdale','arbutus':'Arbutus','kitsilano':'Kitsilano','fairview':'Fairview','downtown':'Downtown Peninsula'}
order=['ubc','point-grey','dunbar','kerrisdale','arbutus','kitsilano','fairview','downtown']
def ent(s): return s.replace('·','&middot;').replace('®','&reg;').replace("’","&rsquo;").replace("'","&rsquo;").replace('ö','&ouml;').replace('é','&eacute;')
STYLE="""<link rel="stylesheet" href="https://stats.ericcoulombe.com/assets/fonts/ev-fonts.css">
<style>
.ech{position:relative;overflow:hidden;background:#2e2f32;color:#f3f3f2;font-family:"Engel Voelkers Text","Helvetica Neue",Arial,sans-serif}
.ech img{position:absolute;inset:0;width:100%;height:100%;max-width:none;object-fit:cover;display:block}
.ech .sh{position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,20,23,.86) 0%,rgba(18,20,23,.66) 45%,rgba(18,20,23,.22) 100%),linear-gradient(0deg,rgba(18,20,23,.55) 0%,rgba(18,20,23,0) 40%)}
.ech .in{position:relative;max-width:1120px;margin:0 auto;padding:56px 16px 64px;min-height:360px;box-sizing:border-box;display:grid;align-content:end;gap:12px}
.ech .eb{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:#c9cacc;font-weight:600}
.ech h1{font-family:"Engel Voelkers Head",Georgia,serif!important;font-weight:800!important;font-size:clamp(40px,7vw,76px)!important;line-height:.95!important;text-transform:none!important;margin:0;letter-spacing:-.01em;color:#f3f3f2;text-wrap:balance}
.ech h1 span{box-shadow:inset 0 -.12em 0 #b7202e;font-size:inherit!important;line-height:inherit!important;font-family:inherit!important;font-weight:inherit!important;letter-spacing:inherit!important;color:inherit!important}
.ech p{margin:0;font-size:17px;line-height:1.55;color:#c9cacc;max-width:58ch}
.ech p b{color:#f3f3f2;font-weight:600}
.ech .cr{position:absolute;right:16px;bottom:10px;margin:0;font-size:11px;color:rgba(243,243,242,.78);max-width:none}
.ech .cr a{color:inherit}
@media(max-width:640px){.ech .sh{background:linear-gradient(0deg,rgba(18,20,23,.88) 0%,rgba(18,20,23,.62) 60%,rgba(18,20,23,.4) 100%)}.ech .in{padding:40px 16px 48px}.ech p{font-size:16px}}
.ecb{max-width:1120px;margin:0 auto;padding:8px 16px 48px;font-family:"Engel Voelkers Text","Helvetica Neue",Arial,sans-serif;font-size:16px;line-height:1.6;color:#45484D;display:grid;gap:18px}
.ecb .bt{display:flex;flex-wrap:wrap;gap:12px;margin:0}
.ecb .bt a{display:inline-block;text-decoration:none;font-weight:600;padding:12px 20px;border-radius:2px}
.ecb details{border-top:1px solid #e1e5e8;padding-top:10px;max-width:72ch}
.ecb summary{cursor:pointer;font-weight:600;color:#1F2124}
.ecb details p{margin:8px 0 0}
.ecb .nb{margin:0;font-size:15px}
.ecb .nb a{color:#B7202E}
</style>"""
SCRIPT="""<script>(function(){var f=document.getElementById('ec-stats');window.addEventListener('message',function(e){if(e.origin!=='https://stats.ericcoulombe.com')return;var d=e.data;if(d&&d.type==='ec-stats-height'&&d.h>200){f.style.height=d.h+'px';f.style.minHeight='0';}});})();</script>"""
def links(cur, label='More neighbourhood stats:'):
    return f'<p class="nb"><strong style="color:#1F2124">{label}</strong> '+' &middot; '.join(f'<a href="{slug[k]}">{short[k]}</a>' for k in order if k!=cur)+(' &middot; <a href="neighbourhood-market-stats.html">All neighbourhoods</a>' if cur else '')+'</p>'
def hero(k):
    a=p[k]; ph=a.get('photo'); nm=short[k]
    h1=a['h1']
    img=f'<img src="https://stats.ericcoulombe.com/{ph["src"]}" alt="" style="object-position:{ph.get("pos","center 60%")}">' if ph else ''
    cr=f'<p class="cr">{ent(ph["credit"])}</p>' if ph and ph.get('credit') else ''
    return f'<section class="ech">{img}<div class="sh"></div><div class="in"><div class="eb">Market Insight &middot; {ent(reg[k]["full_name"]).replace("&amp;","&").replace("&","&amp;").replace("&amp;reg;","&reg;")}</div><h1>{h1} <span>Market</span></h1><p>{ent(a["lede"])}</p></div>{cr}</section>'
for k in order[1:]:
    nm=short[k]; subj=html.unescape(nm).replace(' ','%20').replace('&','%26')
    t=f"""{STYLE}
{hero(k)}
<iframe id="ec-stats" src="https://stats.ericcoulombe.com/{k}/?embed=1&bare=1" title="{html.unescape(nm)} market statistics, updated monthly" scrolling="no" style="display:block;width:100%;border:0;min-height:1400px;background:#f4f4f3"></iframe>
<section class="ecb"><p class="bt"><a href="tel:16047648620" style="background:#B7202E;color:#fff">Call Eric &middot; 604-764-8620</a><a href="mailto:eric@ericcoulombe.com?subject={subj}%20market%20question" style="border:1px solid #1F2124;color:#1F2124;padding:11px 20px">Email Eric &rarr;</a></p><details><summary>What these numbers cover</summary><p>These figures cover {cover[k]}. They come from Greater Vancouver REALTORS&reg; and refresh automatically each month. Market statistics describe the whole neighbourhood, not any one home; for what they mean for a specific property, give me a call.</p></details>{links(k)}</section>
{SCRIPT}"""
    OUT[k]=t
hubhero='<section class="ech"><div class="sh" style="background:radial-gradient(120% 140% at 100% 0%,#3a3c40 0%,#26272a 55%,#1d1e21 100%)"></div><div class="in" style="min-height:300px"><div class="eb">Market Insight</div><h1>Neighbourhood <span>Stats</span></h1><p>How prices, demand and selling speed are moving in the Vancouver neighbourhoods I work in. Each page updates monthly from Greater Vancouver REALTORS&reg; data.</p></div></section>'
hub=f"""{STYLE}
{hubhero}
<iframe id="ec-stats" src="https://stats.ericcoulombe.com/?embed=1&bare=1" title="Vancouver neighbourhood market statistics" scrolling="no" style="display:block;width:100%;border:0;min-height:900px;background:#f4f4f3"></iframe>
<section class="ecb"><p class="bt"><a href="tel:16047648620" style="background:#B7202E;color:#fff">Call Eric &middot; 604-764-8620</a></p><details><summary>About these numbers</summary><p>Each neighbourhood page tracks benchmark prices, how quickly listings are selling, how long homes take to get an accepted offer and how much negotiating room buyers have, using Greater Vancouver REALTORS&reg; data for Vancouver&rsquo;s Westside and Downtown. Market statistics describe whole neighbourhoods, not any one home.</p></details>{links(None,'Neighbourhoods:')}</section>
{SCRIPT}"""
OUT['hub']=hub

# UBC (hand-built stats page; copy kept here so its ericcoulombe.com block matches the others)
ubc_hero='<section class="ech"><img src="https://stats.ericcoulombe.com/assets/img/ec-ubc-campus-skyline.jpg" alt="" style="object-position:center 78%"><div class="sh"></div><div class="in"><div class="eb">Market Insight &middot; UBC / University Endowment Lands</div><h1>UBC <span>Market</span></h1><p>Where UBC condo and townhouse values are heading, how fast homes are selling, and how leasehold compares with the rest of the Westside. Updated monthly from Greater Vancouver REALTORS&reg; data.</p></div><p class="cr">UBC campus &middot; Photo: <a href="https://unsplash.com/photos/cwYMwz3WAMs" target="_blank" rel="noopener">Billy Xue / Unsplash</a></p></section>'
OUT['ubc']=f"""{STYLE}
{ubc_hero}
<iframe id="ec-stats" src="https://stats.ericcoulombe.com/ubc/?embed=1&bare=1" title="UBC market statistics, updated monthly" scrolling="no" style="display:block;width:100%;border:0;min-height:1600px;background:#f4f4f3"></iframe>
<section class="ecb"><p class="bt"><a href="tel:16047648620" style="background:#B7202E;color:#fff">Call Eric &middot; 604-764-8620</a><a href="mailto:eric@ericcoulombe.com?subject=UBC%20market%20question" style="border:1px solid #1F2124;color:#1F2124;padding:11px 20px">Email Eric &rarr;</a><a href="ubc-utopianlifestyle.html" style="border:1px solid #1F2124;color:#1F2124;padding:11px 20px">Buying &amp; selling at UBC &rarr;</a></p><details><summary>What these numbers cover</summary><p>These figures cover condos and townhouses in the University Endowment Lands and UBC neighbourhoods (Greater Vancouver REALTORS&reg; sub-area &ldquo;University VW&rdquo;), plus a comparison of UBC&rsquo;s prepaid leasehold condos with freehold condos across Vancouver West on a price-per-square-foot basis. They come from Greater Vancouver REALTORS&reg; and refresh automatically each month. Market statistics describe the whole neighbourhood, not any one home; if you&rsquo;re weighing a purchase or sale at UBC, including buying for a student, give me a call.</p></details>{links('ubc')}</section>
{SCRIPT}"""

json.dump(OUT,open('_build/host-widgets.json','w'))
print('ok')
