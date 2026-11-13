#!/usr/bin/env python3
"""Download header photos listed in assets/img/_incoming.json, resize to 2000px wide, save to assets/img/.

_incoming.json: [{"file": "ec-cambie-qe-park-view.jpg", "url": "https://upload.wikimedia.org/..."}]
Runs in GitHub Actions (the build sandbox can't reach Wikimedia). Existing files are skipped.
"""
import io, json, os, sys, time, urllib.request
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
items = json.load(open(os.path.join(IMG, "_incoming.json")))
ok = True
for it in items:
    out = os.path.join(IMG, it["file"])
    if os.path.exists(out):
        print("skip", it["file"]); continue
    req = urllib.request.Request(it["url"], headers={"User-Agent": "stats-photo-fetch/1.0 (https://stats.ericcoulombe.com)"})
    for attempt in range(3):
        try:
            data = urllib.request.urlopen(req, timeout=120).read(); break
        except Exception as e:
            print("retry", it["file"], e); time.sleep(10)
    else:
        ok = False; continue
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")
    if im.width > 2000:
        im = im.resize((2000, round(im.height * 2000 / im.width)), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    print("saved", it["file"], im.size, os.path.getsize(out) // 1024, "KB")
sys.exit(0 if ok else 1)
