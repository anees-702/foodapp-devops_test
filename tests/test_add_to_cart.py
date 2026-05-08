# from base import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")

# try:
#     wait = WebDriverWait(driver, 20)

#     # Ensure at least one food item image has loaded
#     wait.until(
#         EC.presence_of_element_located((By.CLASS_NAME, "food-item-image"))
#     )
#     print("✅ Food items loaded")
#     time.sleep(1)  # Wait for icons to render

#     # Check if item is already in cart (green icon or counter present)
#     try:
#         green_icon = driver.find_element(By.CSS_SELECTOR, ".food-item-count .add-remove[src*='add_icon_green']")
#         print("⚠️ Item already in cart, skipping add")
#     except:
#         # Find and click the white 'add' icon using class
#         add_icon_white = wait.until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".add.add-remove"))
#         )
#         driver.execute_script("arguments[0].scrollIntoView(true);", add_icon_white)
#         driver.execute_script("arguments[0].click();", add_icon_white)
#         print("✅ Clicked 'Add to Cart' ")
        
#         green_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".food-item-count .add-remove")))
#         print("✅ Green '+' icon appeared")

#         # Wait for the green add icon to confirm the item was added
        

# except Exception as e:
#     print("❌ Test failed during Add to Cart process")
#     print("Error:", str(e))
#     driver.save_screenshot("error_screenshot.png")
#     with open("page_source.html", "w", encoding="utf-8") as f:
#         f.write(driver.page_source)
#     print("Screenshot and page source saved for debugging")

# finally:
#     driver.quit()

# Import your 'get_driver' function from the base file
# NEW, CORRECT LINE
from .base import get_driver

# Import Selenium libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os # Import os to get the environment variable

# This is the test function that pytest will discover and run
def test_add_item_to_cart():
    """
    Tests the functionality of adding a food item to the cart.
    """
    # Get the TEST_URL from the environment variable set in the docker run command
    base_url = os.getenv("TEST_URL", "http://localhost:3000")

    # Setup the driver for this specific test
    driver = get_driver()
    
    try:
        # Navigate to the website
        driver.get(base_url)

        # Use WebDriverWait for robust testing
        wait = WebDriverWait(driver, 20)

        # Ensure at least one food item image has loaded before proceeding
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "food-item-image"))
        )
        print("✅ Food items loaded")
        time.sleep(1) # Small pause for UI rendering

        # Find and click the white 'add' icon
        # This assumes you want to test adding a new item
        add_icon_white = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add.add-remove"))
        )
        
        # Use JavaScript to safely scroll and click the element
        driver.execute_script("arguments[0].scrollIntoView(true);", add_icon_white)
        driver.execute_script("arguments[0].click();", add_icon_white)
        print("✅ Clicked 'Add to Cart'")

        # Wait for the green add icon or the counter to confirm the item was added
        item_counter = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "food-item-count"))
        )
        print("✅ Item counter appeared")

        # Assertion: Check if the counter's text is '1' or greater
        assert int(item_counter.text) > 0
        print("✅ ASSERTION PASSED: Cart count is greater than 0.")

    finally:
        # Teardown: Always close the browser to clean up resources
        driver.quit()