# EC Website Ops Register - ericcoulombe.com

**Version:** v1.5 · **Created:** 2026-11-02 · **Updated:** 2026-11-08 (late evening) · **Prepared by:** Claude for Eric Coulombe
**Status:** Working draft. Eric approves decisions; Claude runs the upkeep.

---

## 0. How this system works (read this first)

This register is the **one root document** for ericcoulombe.com. If it isn't here, it isn't tracked.

- **What it holds:** every page and how often it gets refreshed, every recurring check, every technical/AI-search setting, open decisions, Eric's short to-do list, and a change log.
- **Where it lives:** 30 Business - Shared Operations / 03 Personal Brand / Website - ericcoulombe.com / Working - Drafts and AI. Always open the **highest version number**. Older versions stay as history; nothing is overwritten.
- **Who does what:**
  - **Claude** runs the checks, drafts the updates, makes approved site edits, and keeps this register current.
  - **Eric** reads one short message a month and answers at most **three asks**. That is the whole job.
- **How it stays whole (no fracturing):**
  1. Every Claude session that edits the site logs the change here (section 7) and updates the page's row (section 2).
  2. The **monthly website review (20th)** reconciles this register against the live site. If any session forgot to log something, the gap is caught within a month.
  3. All recurring site work is listed in section 1. New recurring work gets added there, not created as a stray task.
- **The standard:** no page shows stale figures, no "updated" stamp older than its cadence, no visible gaps that make the site look neglected.

---

## 1. The heartbeat: scheduled checks

| When | Task | What it does | What Eric gets |
|---|---|---|---|
| 5th, monthly | Market Insight: monthly 20-second update draft | Pulls new GVR board data and rates, drafts the hub's monthly update and lists stale figures elsewhere | Phone message with the draft; reply "approve" |
| 12th, monthly | Monthly stats check-in | Checks the stats.ericcoulombe.com data pipeline and drafts the UBC 20-second line | Phone message: "all checks passed" or what needs attention |
| 12th Jan/Apr/Jul/Oct | Split Market: quarterly update prep | Research pack for the next edition of the flagship report | Phone message with the pack and decisions needed |
| **20th, monthly** | **Website monthly review** | Freshness of every page against section 2, AI-search and technical checks (section 3), llms.txt vs. sitemap, lead inbox, time-sensitive phrases (section 4), health of the other three tasks, then saves a new register version if anything changed | **One** phone message: status line plus up to 3 asks |
| 20th Jan/Apr/Jul/Oct (same task) | Quarterly deep review | Adds: page-by-page content review, AI-visibility spot checks, competitor scan | Included in the same message |
| 20th January (same task) | Annual review | Adds: years-in-business wording, rent-cap and rule changes, bio, testimonials, photo refresh, cadence reset | Included in the same message |

Other recurring tasks that touch the business but not the site (net worth, resource watchlist) are not tracked here.

---

## 2. Page inventory and refresh cadence

Freshness signal = what a visitor sees that proves the page is current. Last verified = last date Claude checked the live page.

| Page | Purpose | Cadence | Freshness signal | Last verified | Next due |
|---|---|---|---|---|---|
| / (home) | Front door, both arms | Figures monthly (with 20-sec update); full review quarterly | Split Market card figures | 2026-11-08 (strategy card now The Spinning Wheel) | 2026-11-05 (figures) |
| /market-insight.html | Market hub | Monthly (5th) | "Updated Oct. 30, 2026" | 2026-11-08 (Spinning Wheel link) | 2026-11-05 |
| /vancouver-market-report.html | The Split Market, flagship | Quarterly, after each Bank of Canada decision | "Updated Oct. 28, 2026" | 2026-11-02 | Jan 2027 |
| /ubc-market-stats.html | UBC stats (live charts) | Data daily (automated); text check monthly (12th) | Chart data month | 2026-11-02 | 2026-11-12 |
| /neighbourhood-market-stats.html | Neighbourhood stats hub | Same as above | Chart data month | 2026-11-03 | 2026-11-12 |
| /point-grey-, /dunbar-mackenzie-heights-, /kerrisdale-, /arbutus-, /kitsilano-, /fairview-, /downtown-peninsula-market-stats.html | Seven neighbourhood stats pages (live since 2026-11-02, linked from the hub; hidden menu items under Market Reports > Neighbourhood Stats since 2026-11-04, so they're in the sitemap) | Same as UBC stats | Chart data month | 2026-11-04 | 2026-11-12 |
| /ubc-utopianlifestyle.html | UBC homes guide | Fact check twice a year (leasehold, levies, rents, schools) | None yet; add "Reviewed [month year]" | 2026-11-02 | 2027-05 |
| /ubc-and-musqueam-leasehold-houses.html | Leasehold houses | Twice a year | None yet | 2026-11-02 | 2027-05 |
| /buy-a-ubc-condo-for-your-student.html | Parents landing page | Twice a year; rents annually | None yet | 2026-11-02 | 2027-05 |
| /investing.html | Investing series part 1, "Start Here" in the menu (v2.10, FAQ added 2026-11-03) | Quarterly fact check; FAQ answers must match the page's model figures | None yet | 2026-11-08 (series strip added) | 2027-01 |
| /investment-properties-northern-bc.html | Series part 2, "Leverage, Explained" | Quarterly | None yet | 2026-11-08 (series strip added) | 2027-01 |
| /one-house-fifteen-years.html | Series part 3, long-run case study (C$565K reference house) | Annual (numbers); must match the Spinning Wheel engine | None yet | 2026-11-08 (series strip added; "The honest part" renamed "The hard test") | 2027-01 |
| **/spinning-wheel.html** | **Series part 4, The Spinning Wheel (new 2026-11-08).** Replaces the Flywheel and Income vs Growth pages. Calculator embedded from stats.ericcoulombe.com/spinning-wheel/?embed=1. Block source: Stats repo `_build/spinning-wheel-page.html` | Annual (numbers), plus whenever the engine or rates assumptions change; figures must match the calculator and One House page | "November 2026" in header; "Part 4 of 7" | 2026-11-08 (series strip added; header now Part 4 of 7) | 2027-01 |
| /fort-st-john-investor-brief.html | Series part 5, FSJ brief (v2.4, FAQ added 2026-11-03) | Quarterly; rent cap each January; FAQ answers must match the page's figures | "October 2026" in header | 2026-11-08 (series strip added) | 2027-01 |
| /investmentproperties.html | Series part 6, "Current Opportunities": hand-built listing cards (snapshot Oct 31, 2026) | Monthly (listings current) | "Snapshot as of" date | 2026-11-08 (Kitimat Baxter card removed, two FSJ cards left; series strip added) | 2026-11-20. To be rebuilt as custom listing showcases (next project) |
| **/our-portfolio.html** | **Series part 7, "Our Portfolio" (new 2026-11-08).** Kitimat townhouse and 8419 81 St (Fort St. John) stories: typical-month cash flow, running costs explained, IRR to date and over 10 years. Block source: Stats repo `_build/our-portfolio-page.html`; models `pf/irr.py`, `pf/model.py` | Annual refresh each November with a full year of statements; 8420 can be added after mid-2027 | "Average month, Jan 1 to Oct 22, 2026"; IRR table | 2026-11-08 | 2027-11 |
| /request-reports.html | Report request form | With any report rename | Form options | 2026-11-08 (option renamed to "The Spinning Wheel Report: 15-year model and all scenarios") | 2027-01 |
| ~~/real-estate-flywheel.html~~, ~~/real-estate-income-vs-growth.html~~ | **Deleted 2026-11-08**; both redirect to /spinning-wheel.html | - | - | 2026-11-08 | - |
| /mylistings.html, /active-listings-eric.html | Eric's listings | Monthly (status correct) | Listings feed | 2026-11-02 | 2026-11-20 |
| /recip.html, /map-search.html | MLS search | Automated feed; check monthly it loads | Feed | 2026-11-02 | 2026-11-20 |
| /officelistings.html | Office listings | **Decision D2** | Feed | 2026-11-02 | - |
| /buying.html, /selling.html, /home-evaluation.html, /mortgage-calculator.html | Service pages | Twice a year | None | 2026-11-02 | 2027-05 |
| /about.html, /testimonials.html, /contact.html | Trust pages | Twice a year; testimonials as received | None | 2026-11-02 | 2027-05 |
| /blog.html (181 auto-posts) | Auto listing posts | **Decision D1** | Post dates | 2026-11-02 | - |

**Investing series and menu (since 2026-11-08):** Investment Properties > Start Here, Leverage Explained, One House Fifteen Years, The Spinning Wheel, Fort St. John, Current Opportunities, Our Portfolio (seven pages). Every one of the seven carries the same series strip ("The investing series · N of 7", current page marked, Next link) just above its "Where to next" section; on Start Here it sits above "Go deeper". Strip source: Stats repo `_build/series/gen.py` (one variant per page). If a page is added, renamed or reordered, regenerate the strip and replace it on all seven pages in the same session. Footer labels match ("Start here", "Leverage, explained"). The hidden Income vs Growth menu item was deleted 2026-11-08. Planned later: custom listing showcases, Work with Eric.

---

## 3. Technical and AI-search settings

| Item | Status (2026-11-08) | Owner | Next action |
|---|---|---|---|
| **Live vs Staging** | Edits saved in Live mode (new editor, Site Settings, Advanced) go live immediately. "Save page as" also publishes the copy immediately. Staging plus Publish exists for page edits | Claude | **Rule: build new pages and larger edits on Staging, verify, then publish.** On 2026-11-08 the Spinning Wheel and Our Portfolio work was saved in Live mode (unlinked until checked), because several edits since 2026-11-03 were made on Live only and publishing an outdated Staging copy could undo them. **Before the next Staging build, compare Staging with Live and resync it** |
| Page redirects | Site Settings > Advanced > Page Redirects. 13 mappings on 2026-11-08, incl. real-estate-flywheel.html, real-estate-income-vs-growth.html, spinning-wheel-calculator.html, flywheel, income and wheel, all to spinning-wheel.html. Redirects apply only when the old page no longer exists | Claude | Check monthly that each target is live |
| robots.txt | Allows all AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended); lists sitemap. myRealPage-managed | Claude checks monthly | Leave managed. Override route exists (upload "custom-robots.txt" to root My WebDrive) but it replaces their version, so only use if a real need arises |
| Sitemap | Index of 3. page-sitemap.xml lists only pages in the menu, **including hidden menu items** (Site Settings > Menu > item > "Hide in menu" on, "Hide in sitemap" off). **41 URLs on 2026-11-08**, incl. /spinning-wheel.html and /our-portfolio.html; the two deleted pages are out. "Last updated" dates: **not supported** (Jose/IT, 2026-11-04) | Claude | **Rule: every new page gets a menu item (hidden if it shouldn't show in the navigation) or it won't be in the sitemap.** Monthly review checks. |
| llms.txt | **v1.3 live (2026-11-08)** at https://ericcoulombe.com/llms.txt: investing section in series order, incl. The Spinning Wheel and Our Portfolio. Claude can upload it directly: Private Office classic view > Web Drive: Images & Files > My WebDrive root > "Upload file(s) here..."; a file with the same name replaces the old one in place | Claude | Must be updated whenever a page is added, renamed or removed. Source copy: Stats repo `_build/llms.txt` |
| Titles, meta descriptions, canonical, social tags | Present on every key page checked. /spinning-wheel.html title "The Spinning Wheel: Refinance and Redeploy Rental Equity \| Eric Coulombe". Calculator canonical now ericcoulombe.com/spinning-wheel.html | Claude checks monthly | None |
| Agent schema | **Enriched block live 2026-11-03** (site-wide head, appended after existing code; verified valid on home, About, UBC pages). Auto block still present and shares the same id | Claude | Add "image" when the new headshot exists. Note: Site Settings > Email & Contact > Business Name is blank (optional fill) |
| Breadcrumb schema | All pages except home | - | None |
| FAQ schema | UBC homes, UBC parents, **investing hub (7 Qs) and FSJ brief (6 Qs) live 2026-11-03**, each with matching FAQPage markup | Claude | When a page's model figures change, update its FAQ answers in the same edit. Source copy: "EC Website FAQ Blocks" in this folder |
| Wording rule: never "honest" | Removed from the investing hub 2026-11-03 and from One House 2026-11-08 ("The hard test"). All seven investing pages and the calculator checked clean 2026-11-08 | Claude | Monthly review searches the site for it |
| Visible "Updated"/"Reviewed" dates | Market hub and report show dates; guides and investing pages don't (Spinning Wheel shows "November 2026") | Claude | Add a real "Reviewed [Month YYYY]" line to each guide when it gets its scheduled review (section 2). No static dateModified schema: it would go stale between updates |
| Stats charts readable by AI | Numbers sit inside embedded frames; AI tools can't read them | Claude | Add short text summary of headline figures; refresh monthly with the 12th check-in. The Spinning Wheel page states its key figures in text, so the embedded calculator isn't the only source |
| Image alt text | Checked 2026-11-03: the 8 "missing" home images are decorative hero slides with alt="" inside an aria-hidden block, which is correct. v1.0 audit overcounted | Claude | None |
| Headshot / photo in schema | No current headshot (old one retired) | **Eric** | New AI headshot (in progress); Claude adds it to schema and About |
| Google Search Console | Not connected | **Eric** (2 min) + Claude | Eric verifies ownership; Claude submits sitemap and watches indexing |
| Bing Webmaster Tools | Not connected (feeds Copilot) | **Eric** + Claude | Import from Search Console once that's done |
| Google Business Profile | Unknown | **Eric** | Confirm it exists and is claimed; Claude reviews it |
| Name/phone consistency off-site | Not yet checked (REW, LinkedIn, E&V profile, Facebook) | Claude | Quarterly deep review |
| Stats data pipeline (GitHub) | Daily job; checked monthly. The Stats repo also hosts the Spinning Wheel Calculator (`spinning-wheel/`) and page-block sources (`_build/`) | Claude | 12th check-in |
| Lead pipeline | myRealPage Leads: 79 potential leads, 6 unseen (2026-11-03). Zapier not connected. Lofty (E&V account) already receives some myRealPage leads (source "myrealpage.com"), most likely by parsing notification emails | **Eric** (2 min) | Check Lofty > Settings > Lead Settings > Lead Capture: myRealPage listed, Auto-Import on, ownership Personal. If gaps remain, connect Zapier ("New or Updated Lead" and "New Market Insight Signup" triggers to Lofty) |

---

## 4. Time-sensitive wording watchlist

Phrases that go stale on their own. The monthly review searches the live site for each.

| Phrase / figure | Where | Rule |
|---|---|---|
| Years in business | Bio, schema, decks | Prefer "licensed since 2003" (never goes stale). Any "23 years" gets bumped each January |
| BC rent-increase cap (2.3% for 2026, 2.2% for 2027) | FSJ brief, investing pages, decks | Check each fall/January when the province announces |
| "Almost 7 years" in Fort St. John | FSJ brief, deck | Review each January |
| Bank of Canada rate, mortgage rates | Market hub, report, investing pages | Monthly with the 20-second update |
| Any "Updated" stamp | Hub, report | Must be within its cadence (section 2) |
| Copyright year in footer | All pages | Check each January |
| The word "honest" (Eric's rule: never used) | All pages, reports, decks | Flag any instance |
| FAQ answers on investing hub and FSJ brief (C$137k start, C$1,025/mo, 7.3% cap, 18%/12%/7.7% returns, 250+ Izon doors, 7–9 financed properties) | /investing.html, /fort-st-john-investor-brief.html | Must match the figures in the body of the same page |
| Our Portfolio figures (Kitimat +C$887/mo, FSJ +C$692/mo; IRR table 39%/35% Kitimat, 5%/14-17% FSJ, 26%/22-25% combined; running costs about 30% of rent net of the furnished extras, 35% with re-renting fees) | /our-portfolio.html, link library, decks | From PM statements and `pf/irr.py`. Refresh together each November. Never mention BC Assessment values. Keep lender names, the private loan, account numbers, ownership structure, tax and tenants off the page; show 8419 as a simplified 20%-down, 30-year, 3.99% purchase; show the best performer only as an anonymous line |
| Spinning Wheel figures (C$152,125 start; C$1.50M vs C$1.14M reinvesting; +C$362K; C$1,073K vs C$925K spending; 16.5% vs 14.3%; stress-test table; "November 2026") | /spinning-wheel.html, calculator, One House page | All come from one engine (Stats repo, C$565K reference house). If the engine or its assumptions change, regenerate every page's figures in the same session |

---

## 5. Eric's short list (only things Claude can't do)

Kept to the few items that need you. The monthly message never asks for more than three.

1. **Check Lofty Lead Capture settings** (2 min): myRealPage listed, Auto-Import on, lead ownership Personal. Eric: "Lofty later" (2026-11-08).
2. **Get the new headshot** (AI headshot service, in progress).
3. When ready: **Google Search Console** ownership check (Claude walks you through it, about 2 minutes).
4. Confirm whether you have a **Google Business Profile**.

Done: support email sent 2026-11-02; Private Office sign-in 2026-11-03; follow-up to Jose sent 2026-11-03 and answered 2026-11-04; Spinning Wheel page approved and deletion of the two old pages approved 2026-11-08; Terrace and Baxter listings deleted by Eric 2026-11-08; Market Insight declined 2026-11-08; llms.txt v1.3 uploaded by Claude 2026-11-08.

---

## 6. Open decisions

| # | Decision | Claude's recommendation (opinion) | Status |
|---|---|---|---|
| D1 | Blog: 181 thin auto-posts (new listing / sold) are hidden from the menu but still in the sitemap. Revive with real posts, keep as is, or remove auto-posts from the sitemap? | Keep auto-posts out of sight, start a modest real cadence (one useful post a month, drafted by Claude from the monthly data), and decide in the strategy session you wanted | Open |
| D2 | /officelistings.html is still live and in the sitemap although the Office Listings menu item was dropped | Leave it live (harmless) unless you want it unpublished | Open |
| D3 | Separate investing website vs. keep everything on ericcoulombe.com | One domain: AI and search authority concentrate on one site. Other domains can redirect to sections | Open |
| D4 | llms.txt | Done: live at the domain root 2026-11-03; v1.3 (with The Spinning Wheel and Our Portfolio) live 2026-11-08, uploaded by Claude through My WebDrive | Closed |
| D5 | Market Insight Package ($20/mo add-on: branded seller mini-CMA reports and sign-up page) | Was: 3-month trial if no extra fees and auto-approval | **Closed 2026-11-08: declined.** Eric: market insight is already well covered by the site's hub, report and stats pages, and by emailers he'll send later from Lofty or myRealPage |
| D6 | Neighbourhood stats pages in the sitemap | Done 2026-11-04: added as hidden menu items, no visible change | Closed |
| D7 | Investing section structure (series order, names, Spinning Wheel page replacing Flywheel and Income vs Growth) | Done 2026-11-08, approved by Eric | Closed |
| D8 | One "get the report" path on the Spinning Wheel page: the embedded calculator still has its own email button besides the page's request-reports card | Make the calculator's embed-mode button link to request-reports.html, keeping the scenario summary in the form's message | Open (Claude to propose) |

---

## 7. Change log

Newest first. One line per change to the site, its settings or this system.

- **2026-11-08** - Register v1.5 saved (this file).
- **2026-11-08** - /investmentproperties.html: removed the Kitimat 201-110 Baxter Avenue card (MLS R3174601; Eric deleted the listing), its footnote sentence, and changed "all three" to "both" in the stress-test line. Two Fort St. John cards remain (R3176945, R3164408). Verified live. The 3-column grid now leaves one empty column; the page is due to be rebuilt as custom listing showcases.
- **2026-11-08** - /one-house-fifteen-years.html: section label "The honest part" renamed "The hard test". Sweep of all seven investing pages: no "honest" left.
- **2026-11-08** - Series strip added to all seven investing pages (above "Where to next"; on Start Here above "Go deeper"), from Stats repo `_build/series/` (commit a745b50). Spinning Wheel header "Part 4 of 5" changed to "Part 4 of 7". Verified live on all seven: one strip each, right page marked, correct Next link, no overflow on a 390px phone.
- **2026-11-08** - Menu: hidden "Income vs Growth" item deleted (Eric approved). Saved; verified the live navigation ends at Our Portfolio.
- **2026-11-08** - llms.txt v1.3 uploaded to root My WebDrive (replaced v1.1; v1.2 had never gone live). Adds Our Portfolio; The Spinning Wheel is now listed too. Verified live at /llms.txt.
- **2026-11-08** - Menu: visible "Our Portfolio" item added after Current Opportunities. Verified in the live navigation and in page-sitemap.xml (41 URLs).
- **2026-11-08** - New page /our-portfolio.html (created with "Save page as" from The Spinning Wheel on Live, not shown in the menu until checked; block replaced with `_build/our-portfolio-page.html`). Title "Our Portfolio: Our Own Rentals, by the Numbers | Eric Coulombe"; description and canonical set; E&V brand fonts. Sections: Kitimat, Fort St. John 8419 (least flattering, picked on purpose), running costs explained (all-inclusive furnished rent; regular costs about 30% of net rent), IRR to date and 10-year forecast, series links, sources and disclosure. Verified desktop and mobile.
- **2026-11-08** - Finding: 8419's running costs, 12 months Nov 2025-Oct 2026 from Izon's Buildium statements: furnished extras (utilities, internet, housekeeping, supplies) C$7,002 (10.7% of collected rent); regular costs excluding placement fees 29.5% of the remaining rent, 34.9% with two placements. Vacancy about 11% this year. Confirms the models' 30% assumption; the risk at 8419 is turnover, not running costs.
- **2026-11-08** - Deleted /real-estate-flywheel.html and /real-estate-income-vs-growth.html (Eric approved). Page Redirects updated: real-estate-flywheel.html, real-estate-income-vs-growth.html, spinning-wheel-calculator.html, flywheel, income and wheel all go to spinning-wheel.html. Verified: each old address lands on /spinning-wheel.html; page-sitemap.xml 40 URLs, old pages out.
- **2026-11-08** - llms.txt v1.2 prepared and sent to Eric for upload (not yet live).
- **2026-11-08** - Link updates (Live, verified): home strategy card (title, description, aria labels), investing hub (Flywheel card and links; Income vs Growth card now "The Spinning Wheel Calculator" to #sw-calc; rules link to #sw-rules), Leverage ("See the 15-year comparison"; Go deeper card), One House (income link to #sw-income), FSJ brief (Go deeper card; Flywheel comparison sentence reworded), Market Insight (link and list item). Full-site sweep: no links left to the old pages.
- **2026-11-08** - /request-reports.html form option renamed: "Portfolio model: Flywheel and Income vs Growth" is now "The Spinning Wheel Report: 15-year model and all scenarios".
- **2026-11-08** - Menu: "The Real Estate Flywheel" item repointed to The Spinning Wheel (spinning-wheel.html) and moved after One House; Income vs Growth hidden in menu and sitemap. Saved and verified live.
- **2026-11-08** - New page /spinning-wheel.html (created with "Save page as" from One House, block replaced with `_build/spinning-wheel-page.html`; saved in Live mode). Sections: summary, calculator, where the money comes from, income vs growth, stress tests (reinvesting/spending toggle), operating rules, friction and risk, who it suits, series links, sources and disclosure. Anchors: #sw-calc, #sw-money, #sw-income, #sw-stress, #sw-rules.
- **2026-11-08** - Calculator (stats.ericcoulombe.com/spinning-wheel) canonical and "Copy a link to this scenario" now point to ericcoulombe.com/spinning-wheel.html; teaser widget source updated.
- **2026-11-08** - Menu relabel and reorder: "How It Works" now "Start Here", "Fort St. John Investor Brief" now "Fort St. John"; One House moved after Leverage. Site-wide footer (Advanced > custom body content): "How I invest" now "Start here", "Leverage basics" now "Leverage, explained". Verified live.
- **2026-11-04** - Jose replied (two emails): sitemap includes only menu pages; lastmod dates not supported; Market Insight has no extra board fees and requests can auto-approve.
- **2026-11-04** - Menu: added seven hidden child items under Market Reports > Neighbourhood Stats (Point Grey, Dunbar & MacKenzie Heights, Kerrisdale, Arbutus, Kitsilano, Fairview, Downtown Condo Stats), each "Hide in menu" on, "Hide in sitemap" off. Saved. Verified: page-sitemap.xml now 35 URLs incl. all seven; none appear in the live navigation.
- **2026-11-03** - FAQ sections published: /investing.html v2.10 (7 questions, before the closing call to action) and /fort-st-john-investor-brief.html v2.4 (6 questions, before "Where to next"). Each has visible Q&A plus FAQPage JSON-LD; every answer restates figures already on its page. Same edit removed "honest" from the investing hub (3 instances). Built on Staging, verified, then published (only these two pages were in the queue); verified live.
- **2026-11-03** - llms.txt v1.1 uploaded (overwrites v1.0): adds the seven neighbourhood stats pages. Verified live.
- **2026-11-03** - Found: seven neighbourhood stats pages (created 2026-11-02 in another session) were not in the register or llms.txt, and aren't in the sitemap because they aren't in the menu. Register and llms.txt updated; sitemap question added to the Jose draft.
- **2026-11-03** - Site-wide structured data (RealEstateAgent + Person + WebSite, Appendix B) appended to Site Settings > Advanced > Custom head content and saved; verified live and valid on /, /about.html, /ubc-utopianlifestyle.html. Original head code unchanged (reversible via Open History).
- **2026-11-03** - llms.txt uploaded to root My WebDrive; verified served at https://ericcoulombe.com/llms.txt (200, text/plain, accents intact).
- **2026-11-03** - Jose (myRealPage support) replied: sold data already enabled; Market Insight is a separate $20/mo add-on; custom robots.txt via Web-Drive upload; llms.txt and sitemap dates referred to IT. Follow-up reply drafted, then sent by Eric.
- **2026-11-03** - Findings: Lofty already receives some myRealPage leads; Zapier not connected; 79 potential / 6 unseen leads in Private Office; home hero alt-text "gap" was a false positive.
- **2026-11-02** - Register created (v1.0). Baseline AI-search audit run on the live site (Appendix A). Schema enrichment block drafted (Appendix B). myRealPage support email drafted in Gmail. Monthly website review scheduled for the 20th.
- **2026-11-02** - (from earlier sessions) UBC Market Stats page launched under Market Reports; seven neighbourhood stats pages and hub built; UBC pages and Musqueam page search bar replaced with a button; links to stats page added from UBC page and Market Insight hub.

---

## 8. Proposed entries for the website decisions file

Per the Drive README, the decisions file lives in the project's main folder and only Eric approves entries. Proposed, not yet approved:

- 2026-11-02 - Stay on myRealPage; AI-search readiness doesn't require a platform change.
- 2026-11-02 - Adopt this register as the single tracking document for the website, with a monthly review on the 20th.
- 2026-11-02 - Approve all recommended AI-search optimizations (schema enrichment, Article/FAQ schema, visible dates, stats text summaries, alt text, Search Console and Bing).
- 2026-11-03 - FAQ sections on the investing hub and FSJ brief approved and published.
- 2026-11-04 - Pages that shouldn't show in the navigation get hidden menu items so they stay in the sitemap.
- 2026-11-08 - Investing section is one numbered series (Start Here, Leverage Explained, One House Fifteen Years, The Spinning Wheel, Fort St. John), all on the same C$565K reference house and one model engine; The Spinning Wheel replaces the Flywheel and Income vs Growth pages.
- 2026-11-08 - Our Portfolio added as part 7 of the series: Kitimat and 8419 only (8420 after a full year; best performer as an anonymous line); IRR to date and forecast is the headline metric; no BC Assessment mentions.
- 2026-11-08 - All seven investing pages carry one shared series strip; changes to the series are made to all seven at once.
- 2026-11-08 - Market Insight add-on declined; market content stays on Eric's own pages and future emailers.
- 2026-11-08 - Current Opportunities to be rebuilt as custom listing showcases (next project).

---

## Appendix A - Baseline AI-search audit (2026-11-02, live site)

**Bottom line (opinion):** myRealPage is good enough for AI search, and the site is ahead of most agent sites. The limits are content depth and off-site signals, not the platform.

Facts checked on the live site:
- AI crawlers allowed in robots.txt; content is in the page HTML (readable without scripts).
- Sitemap present and includes the new pages; no "last updated" dates (confirmed not supported, 2026-11-04).
- Titles, meta descriptions, canonical tags and social-share tags present on key pages.
- Schema: RealEstateAgent (auto) on every page, breadcrumbs on all inner pages, FAQ on both UBC buyer pages. Agent node lacks name, photo, areaServed and specialties.
- llms.txt missing. Alt text flagged on 8 of 32 home images (later found to be correct decorative markup).

What myRealPage allows: site-wide and per-page custom head code (any schema), per-page meta tags, clean URLs, root-level files via the root My WebDrive folder (confirmed 2026-11-03), and hidden menu items that still feed the sitemap (confirmed 2026-11-04).

Priorities, highest value first:
1. Enrich agent schema (name, photo, service area, specialties, brokerage, licensed since 2003).
2. Make stats figures readable (short text summary under the charts).
3. Visible byline and "Updated" date on reports; FAQ blocks on investing pages.
4. Off-site signals: Google Business Profile, reviews, consistent name/phone everywhere. Industry reporting (HousingWire, 2026) puts only about 8% of agents in AI answers so far.
5. Search Console and Bing Webmaster Tools.
6. Keep everything on one domain.

Sources: myRealPage help (custom head content), myRealPage blog (AI search, 2026), Layer3 Labs AI search playbook, HousingWire on answer-engine optimization, Web Tonic SEO for real estate 2026.

---

## Appendix B - Site-wide schema enrichment (installed 2026-11-03)

Goes in Private Office > Website settings > Custom content in the head section. It shares the auto agent's id (https://ericcoulombe.com/#contact), so search engines merge it with the existing block rather than seeing a second agent. Add the headshot as "image" once it exists.

Covers: name; Person node for Eric (Real Estate Advisor, licensed since 2003, Engel & Völkers Vancouver, Kerrisdale office address, Facebook and LinkedIn); service areas (UBC, Point Grey, Dunbar and MacKenzie Heights, Kerrisdale, Arbutus, Kitsilano, Fairview, Downtown, Vancouver, Fort St. John); specialties (Westside homes and condos, UBC leasehold, Musqueam leasehold, UBC condo for a student, small multi-family income property, Northern BC cash flow, Fort St. John, leveraged portfolio planning); WebSite node. No Alberta references, per the site rule.

Full code is saved alongside this register as "EC Website Schema - Sitewide JSON-LD".
