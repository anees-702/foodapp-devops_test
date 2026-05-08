# from base import get_driver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")

# try:
#     wait = WebDriverWait(driver, 30)  # Increased timeout

#     # Ensure food item image loads
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-image")))
#     print("✅ Food items loaded")

#     # Check if item is already in cart
#     try:
#         green_icon = driver.find_element(By.CSS_SELECTOR, ".food-item-count .add-remove")
#         print("⚠️ Item already in cart, skipping add")
#         print(f"Green icon src: {green_icon.get_attribute('src')[:50]}...")  # Debug src
#     except:
#         # Click white 'add' icon
#         add_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".food-item:first-child .add.add-remove")))
#         driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
#         driver.execute_script("arguments[0].click();", add_btn)
#         print("✅ Item added to cart")

#         # Confirm green icon (reliable locator)
#         green_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".food-item-count .add-remove")))
#         print("✅ Green '+' icon appeared")
#         print(f"Green icon src: {green_icon.get_attribute('src')[:50]}...")  # Debug src

#     # Navigate to cart page
#     driver.get("http://16.171.54.54:3000/cart")

#     # Confirm cart page loads
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))
#     print("✅ Cart page loaded")

#     # Check cart items
#     cart_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-items-title")))
#     assert len(cart_items) > 0, "❌ No items found in cart"
#     print(f"✅ Cart displays {len(cart_items)} item(s)")

# except Exception as e:
#     print("❌ Test failed")
#     print("Error:", str(e))
   

# finally:
#     driver.quit()

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import get_driver

def test_cart_shows_added_item():
    """
    Adds an item to the cart from the homepage and verifies it appears on the cart page.
    """
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()
    
    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-image")))

        first_item = driver.find_element(By.CSS_SELECTOR, ".food-item")

        # Add item to cart if it's not already there
        try:
            first_item.find_element(By.CLASS_NAME, "food-item-count")
        except:
            add_button = first_item.find_element(By.CSS_SELECTOR, ".add.add-remove")
            driver.execute_script("arguments[0].click();", add_button)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "food-item-count")))
        
        # Navigate to the cart page
        cart_url = f"{base_url}/cart"
        driver.get(cart_url)

        # Wait for the main cart container to load to ensure we are on the right page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart")))

        # **ACTION REQUIRED**: Verify this locator is correct for your app.
        # Right-click an item in your cart and "Inspect" to find the right class name.
        cart_item_locator = (By.CLASS_NAME, 'cart-items-title') 
        
        # Wait until at least one item with the specified locator appears on the page
        wait.until(EC.presence_of_element_located(cart_item_locator))

        # Assertion: Verify that there is at least one item listed in the cart
        cart_items = driver.find_elements(*cart_item_locator)
        assert len(cart_items) > 0, "Cart is empty, but it should contain at least one item."
        print(f"✅ ASSERTION PASSED: Cart displays {len(cart_items)} item(s).")

    finally:
        driver.quit()