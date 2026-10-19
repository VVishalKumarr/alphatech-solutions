import sys, os, asyncio
from playwright.async_api import async_playwright

FPS = 30
T = 8
out = sys.argv[1]
only = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else list(range(FPS * T))
os.makedirs(out, exist_ok=True)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--use-gl=swiftshader", "--enable-unsafe-swiftshader"])
        pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        await pg.goto("file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "scene.html")))
        cv = await pg.query_selector("canvas")
        for i in only:
            await pg.evaluate(f"renderFrame({i},{FPS})")
            await cv.screenshot(path=f"{out}/f{i:04d}.png")
        await b.close()

asyncio.run(main())
