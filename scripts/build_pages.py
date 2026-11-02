#!/usr/bin/env python3
"""Build each area page (<key>/index.html) from templates/area.html + pages.json.

Shared styling and the logo are taken from the hand-built UBC page so every page
matches it. Run after editing pages.json or the template:  python3 scripts/build_pages.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read()


def main():
    ubc = rd("ubc/index.html")
    css = ubc[ubc.index("<style>") + 7:ubc.index("</style>")]
    logo = ubc[ubc.index('<svg class="logo"'):ubc.index("</svg>") + 6]
    tpl = rd("templates/area.html").replace("/*UBC_CSS*/", css).replace("<!--LOGO-->", logo)
    reg = json.loads(rd("registry.json"))["areas"]
    pages = json.loads(rd("pages.json"))
    for key, p in pages["pages"].items():
        area = reg[key]
        segs = dict(pages["_segments"]); segs.update(p.get("segments", {}))
        cfg = {"key": key, "name": area["name"], "segs": segs}
        photo = p.get("photo")
        rep = {
            "%%NAME%%": area["name"].replace("&", "&amp;"),
            "%%FULLNAME%%": area["full_name"].replace("&", "&amp;"),
            "%%H1%%": p["h1"], "%%LEDE%%": p["lede"], "%%DESC%%": p["desc"],
            "%%OGDESC%%": p.get("ogdesc", p["lede"].split(". Updated")[0] + "."),
            "%%OGIMAGE%%": f'<meta property="og:image" content="https://stats.ericcoulombe.com/{photo["src"]}">\n' if photo else "",
            "%%HEROCLASS%%": "" if photo else " nophoto",
            "%%HEROPHOTO%%": f'<figure class="hero-photo" aria-hidden="true"><img alt="" src="../{photo["src"]}" style="object-position:{photo.get("pos", "center 60%")}"></figure><div class="hero-shade" aria-hidden="true"></div>\n  ' if photo else "",
            "%%HEROCREDIT%%": f'<p class="hero-credit">{photo["credit"]}</p>' if photo and photo.get("credit") else "",
            "%%NOTE%%": f'<p>{p["note"]}</p>\n    ' if p.get("note") else "",
            "%%CFG%%": json.dumps(cfg, ensure_ascii=False),
            "%%CANON%%": area.get("host_url") or f"https://stats.ericcoulombe.com/{key}/",
        }
        html = tpl
        for k, v in rep.items():
            html = html.replace(k, v)
        assert "%%" not in html, key
        os.makedirs(os.path.join(ROOT, key), exist_ok=True)
        with open(os.path.join(ROOT, key, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("built", key)


if __name__ == "__main__":
    main()
