import asyncio
import time
import urllib.parse
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch() #(headless=False, slow_mo=100)
        page = await browser.new_page()
        #page.set_viewport_size({"width": 1440, "height": 960})
        searchTerm = urllib.parse.quote_plus("best lipstick")
        print(searchTerm)
        openUrl = "https://www.ulta.com/ulta/a/_/Ntt-"+ searchTerm +"/Nty-1?Dy=1&ciSelector=searchResults"
        await page.goto(openUrl)
        time.sleep(5)
        #await page.screenshot(path='example.png', full_page=True)
        content = await page.content()
        with open("Output.html", "w") as html_file:
            html_file.write(content)
        await browser.close()

asyncio.run(main())