# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")

# links = driver.find_elements(By.TAG_NAME, "a")
# clicked = False
# for link in links:
#     text = link.text.strip().lower()
#     if "menu" in text:
#         link.click()
#         clicked = True
#         time.sleep(2)
#         break

# assert clicked
# print("✅ Navbar scroll to menu section works")
# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .base import get_driver

def test_navbar_scroll_to_menu():
    """
    Tests that clicking the 'Menu' link in the navigation bar scrolls the page down.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Get the scroll position before clicking. It should be 0 on a fresh page.
        scroll_pos_before = driver.execute_script("return window.pageYOffset;")

        # Find the 'Menu' link and click it
        menu_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(., 'MENU', 'menu'), 'menu')]"))
        )
        menu_link.click()

        # Wait a moment for the browser's smooth-scroll animation to complete
        time.sleep(1)

        # Get the scroll position after clicking
        scroll_pos_after = driver.execute_script("return window.pageYOffset;")

        # Assertion: The new scroll position must be greater than the original position.
        assert scroll_pos_after > scroll_pos_before
        print(f"✅ ASSERTION PASSED: Page scrolled from {scroll_pos_before}px to {scroll_pos_after}px.")

    finally:
        driver.quit()