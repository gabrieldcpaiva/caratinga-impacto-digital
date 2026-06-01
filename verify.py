import os
import re
from playwright.sync_api import sync_playwright

def verify_frontend():
    # Ensure verification directories exist
    os.makedirs('/home/jules/verification/screenshots', exist_ok=True)
    os.makedirs('/home/jules/verification/videos', exist_ok=True)

    with sync_playwright() as p:
        # Launch browser and create a context for recording video
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir='/home/jules/verification/videos',
            record_video_size={'width': 1280, 'height': 720}
        )
        page = context.new_page()

        # Load the modified HTML file locally
        page.goto('file:///app/solucao/index.html')

        # Wait for the calculator section to load
        page.wait_for_selector('#calculadora')
        page.locator('#calculadora').scroll_into_view_if_needed()

        # Submit empty to trigger validation
        page.click('button:has-text("Simular Resultado")')
        page.wait_for_timeout(500) # Give it a moment for UI to update

        # Take a screenshot showing the error state
        screenshot_path = '/home/jules/verification/screenshots/solucao_error_state.png'
        page.screenshot(path=screenshot_path)

        # Assert the error is visible
        error_element = page.locator('#revenue-error')
        assert error_element.is_visible(), "Error message should be visible"
        assert "Por favor, insira um valor válido" in error_element.inner_text(), "Error message text is wrong"

        # Now input a valid number
        page.fill('#revenue', '2000')
        page.click('button:has-text("Simular Resultado")')
        page.wait_for_timeout(500)

        # Take a screenshot showing the success state
        success_screenshot_path = '/home/jules/verification/screenshots/solucao_success_state.png'
        page.screenshot(path=success_screenshot_path)

        # Assert error is hidden and result is visible
        assert not error_element.is_visible(), "Error message should be hidden"
        result_box = page.locator('#result-box')
        assert result_box.is_visible(), "Result box should be visible"

        # Close context and browser to finalize video recording
        context.close()
        browser.close()

if __name__ == "__main__":
    verify_frontend()
    print("Frontend verification completed successfully.")
