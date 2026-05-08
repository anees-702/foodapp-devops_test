# from base import get_driver
# from selenium.webdriver.common.by import By
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# time.sleep(2)

# food_items = driver.find_elements(By.CLASS_NAME, "food-item")
# assert len(food_items) > 0
# print(f"✅ {len(food_items)} food items rendered on menu")
# driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Use a relative import to get the driver from the 'base.py' file
from .base import get_driver

def test_menu_items_are_rendered():
    """
    Tests that the homepage loads and displays at least one food item.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        # Wait for at least one element with the class 'food-item' to be present
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item")))
        
        # Get all the food items
        food_items = driver.find_elements(By.CLASS_NAME, "food-item")

        # Assertion: Check that the number of food items is greater than zero
        assert len(food_items) > 0
        print(f"✅ ASSERTION PASSED: {len(food_items)} food items rendered on menu.")

    finally:
        driver.quit()