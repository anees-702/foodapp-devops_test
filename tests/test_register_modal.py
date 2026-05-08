# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# time.sleep(2)

# try:
#     # Step 1: Click the "sign in" button
#     sign_in_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]")
#     sign_in_btn.click()
#     print("✅ 'sign in' button clicked to open modal")
#     time.sleep(1)

#     # Step 2: Switch to Sign Up mode by clicking "Click here"
#     switch_to_signup = driver.find_element(By.XPATH, "//p[contains(text(), 'Create a new account')]/span")
#     switch_to_signup.click()
#     print("✅ Switched to Sign Up mode")
#     time.sleep(1)

#     # Step 3: Check if name input field is now visible
#     name_input = driver.find_element(By.NAME, "name")
#     assert name_input
#     print("✅ Register modal shows 'name' field")

# except Exception as e:
#     print("❌ Test failed:", str(e))

# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_register_modal_switch():
    """
    Tests the switch from the login modal to the sign-up (register) modal.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
        
        # Step 1: Open the login modal
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'sign in')]"))).click()
        print("✅ Login modal opened.")

        # Step 2: Click the link to switch to the Sign Up form
        switch_to_signup_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Click here')]"))
        )
        switch_to_signup_link.click()
        print("✅ Switched to Sign Up mode.")

        # Step 3: Wait for the 'name' input field, which is specific to the register form
        name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))

        # Assertion: Verify the 'name' field is now displayed
        assert name_input.is_displayed()
        print("✅ ASSERTION PASSED: Register modal correctly shows the 'name' field.")

    finally:
        driver.quit()