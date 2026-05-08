# from base import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# time.sleep(2)

# try:
#     # Try to locate the profile icon (only appears when user is logged in)
#     profile_icon = driver.find_element(By.XPATH, "//img[contains(@src, 'profile')]")
#     print("✅ User is logged in, attempting to logout...")

#     # Hover to reveal the dropdown
#     actions = ActionChains(driver)
#     actions.move_to_element(profile_icon).perform()
#     time.sleep(1)

#     # Find and click logout option
#     logout_btn = driver.find_element(By.XPATH, "//ul[contains(@class, 'nav-profile-dropdown')]//p[text()='Logout']")
#     logout_btn.click()
#     print("✅ Logout clicked successfully.")

# except Exception as e:
#     print("✅ Logout Test Executes Successfully.")
#     print(" User is not logged in. Profile icon or logout button not found.")

# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_logout_functionality():
    """
    Tests the logout process. If a user is logged in, it logs them out. 
    If not logged in, the test passes.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Use find_elements to check for the profile icon without raising an error
        profile_icons = driver.find_elements(By.XPATH, "//img[contains(@src, 'profile')]")

        if len(profile_icons) > 0:
            print("✅ User appears to be logged in. Attempting to logout...")
            profile_icon = profile_icons[0]
            
            # Hover over the profile icon to reveal the dropdown
            actions = ActionChains(driver)
            actions.move_to_element(profile_icon).perform()

            # Find and click the logout button in the dropdown
            logout_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='Logout']"))
            )
            logout_btn.click()

            # Assertion: Verify logout was successful by checking for the "sign in" button's return
            wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'sign in')]")))
            print("✅ ASSERTION PASSED: User logged out successfully.")
        else:
            print("✅ User is not logged in. Test passes as there is no one to log out.")
            # Assertion: In a logged-out state, the "sign in" button should be visible
            assert len(driver.find_elements(By.XPATH, "//button[contains(text(), 'sign in')]")) > 0

    finally:
        driver.quit()