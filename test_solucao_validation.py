import os
from playwright.sync_api import sync_playwright

def test_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Create output directories if they don't exist
        os.makedirs('/home/jules/verification/screenshots', exist_ok=True)
        os.makedirs('/home/jules/verification/videos', exist_ok=True)

        context = browser.new_context(record_video_dir="/home/jules/verification/videos")
        page = context.new_page()

        # Load the local HTML file
        page.goto('file:///app/solucao/index.html')

        # Wait for the calculator section
        page.wait_for_selector('#calculadora')

        # Click the simulate button without entering a value
        page.click('button:has-text("Simular Resultado")')

        # Verify the error message appears
        error_msg = page.locator('#revenue-error')
        page.wait_for_selector('#revenue-error', state='visible')
        print(f"Error message text: '{error_msg.inner_text()}'")

        # Capture screenshot of the error state
        page.screenshot(path='/home/jules/verification/screenshots/solucao_validation_error.png')

        # Enter a valid value
        page.fill('#revenue', '1000')
        page.click('button:has-text("Simular Resultado")')

        # Verify the error message disappears and result appears
        page.wait_for_selector('#result-box', state='visible')
        result_text = page.locator('#taxResult').inner_text()
        print(f"Result text: '{result_text}'")
        print(f"Error message text (should be empty): '{error_msg.inner_text()}'")

        # Capture screenshot of the success state
        page.screenshot(path='/home/jules/verification/screenshots/solucao_validation_success.png')

        context.close()
        browser.close()

        print("Playwright test completed successfully.")

if __name__ == "__main__":
    test_validation()
