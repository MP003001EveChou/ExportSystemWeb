from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p:
    
    browser = p.chromium.launch(channel="chrome")
    page = browser.new_page()
    #page.goto("http://playwright.dev")
    page.goto("http://www.google.com")
    print(page.title())
    browser.close()
browser.close()
