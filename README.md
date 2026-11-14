# stats.ericcoulombe.com

Neighbourhood market statistics pages for ericcoulombe.com, built from public
Greater Vancouver REALTORS® Stats Centre share links.

- `registry.json`: the areas and the GVR share link behind each chart.
- `scripts/update.py`: downloads and checks the data; writes `data/<area>.json`.
- `.github/workflows/update.yml`: runs the update daily; publishes only when
  GVR has new data; opens a "needs attention" issue (emailed to the owner) on
  any problem, and closes it once a run is clean.
- `<area>/index.html`: each area's page; `index.html`: the stats hub.
- Add `?embed=1` to any page to embed it on ericcoulombe.com (hides the logo
  bar and reports its height to the host page).

Photos: Unsplash, see `assets/img/CREDITS.md`.

Also hosted here: `spinning-wheel/index.html`, the Spinning Wheel Calculator
(embedded on ericcoulombe.com/spinning-wheel.html with `?embed=1`;
scenario links use `#s=appr_rate_ltv_term_reinvest_rentPct_years_downturn`; engine assumptions match one-house-fifteen-years.html).

Also hosted here: `reports/<report>/index.html`, client-facing reports (see `reports/README.md`).
