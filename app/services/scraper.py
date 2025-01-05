from playwright.async_api import async_playwright

async def scrape_content(url: str) -> str:
    url=str(url)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector("body")
        content = await page.content()
        await browser.close()
        return content
