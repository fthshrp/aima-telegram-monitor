from playwright.sync_api import sync_playwright

URL = "https://contactenos.aima.gov.pt/tracking/a0be286b-92af-4b8c-a6c8-4f46d7331abe"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
    )

    print("AIMA sayfası açılıyor...")

    try:
        response = page.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("HTTP status:", response.status if response else "unknown")
        print("Final URL:", page.url)
        print("Title:", page.title())

        page.wait_for_timeout(10000)

        text = page.locator("body").inner_text()

        print("Sayfa metni:")
        print(text[:5000])

    except Exception as e:
        print("AIMA erişim hatası:", repr(e))
        raise

    finally:
        browser.close()
