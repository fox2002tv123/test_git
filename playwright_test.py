'''
Author: bob
Date: 2022-04-15 16:32:31
LastEditors: bob
LastEditTime: 2022-04-15 16:40:45
FilePath: \test_git\test_git\playwright_test.py
Description: 

Copyright (c) 2022 by bob, All Rights Reserved. 
'''
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://whatsmyuseragent.org/')
            # await page.screenshot(path=f'example-{browser_type.name}.png')
            # await browser.close()

asyncio.run(main())