# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'sign in')]")
# login_button.click()
# time.sleep(1)

# email_field = driver.find_element(By.NAME, "email")
# password_field = driver.find_element(By.NAME, "password")

# assert email_field and password_field
# print("✅ Login modal opened with fields")
# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_login_modal_opens_with_fields():
    """
    Tests that the login modal opens correctly and displays the email and password fields.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()
    
    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Wait for the 'sign in' button to be clickable and click it
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'sign in')]"))
        )
        login_button.click()
        
        # Wait for the email and password fields to be present in the modal
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        # Assertion: Check that both fields are displayed
        assert email_field.is_displayed() and password_field.is_displayed()
        print("✅ ASSERTION PASSED: Login modal opened with required fields.")

    finally:
        driver.quit()