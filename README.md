# Alpha Tech Solutions — website

One-page website for Alpha Tech Solutions, electrical contractors near Vijayanagar Metro Station, Bengaluru.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The whole site: markup, styles and scripts in one file |
| `hero.mp4` | Hero background loop (1920×1080, 8 s, seamless, no audio) |
| `poster.jpg` | First frame of the loop, shown before the video plays |
| `video/scene.html` | The canvas scene the hero loop is rendered from |
| `video/render.py` | Renders `scene.html` to PNG frames with Playwright |

## Hosting

It's a static site with no build step. Upload the three root files to any static host
(GitHub Pages, Netlify, Vercel, Cloudflare Pages) and `index.html` is the home page.

For GitHub Pages: Settings → Pages → Deploy from a branch → `main` / root.
Pages on the free plan needs the repository to be public.

Fonts load from Google Fonts; everything else is self-contained.

## Re-rendering the hero video

```bash
pip install playwright && playwright install chromium
cd video
python3 render.py frames            # writes frames/f0000.png … f0239.png
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -preset slow -crf 21 \
  -pix_fmt yuv420p -movflags +faststart -an ../hero.mp4
ffmpeg -i frames/f0000.png -q:v 3 ../poster.jpg
```

Every motion in `scene.html` repeats on an 8-second period, so frame 240 equals frame 0 and the loop has no seam.

## Business details used

- Address: No: 174/8, 1st Floor, 15th Main, Balaji Complex, Near Vijayanagar Metro Station, Vijayanagar, Bengaluru, Karnataka 560040
- Phone: +91 99022 56817
- Email: alphatech2solutions@gmail.com
- Hours: Open 24 hours, every day
