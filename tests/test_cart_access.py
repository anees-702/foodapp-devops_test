import os
# Use a relative import to get the driver from the 'base.py' file in the same directory
from .base import get_driver

def test_cart_page_access():
    """
    Tests if the cart page URL can be accessed directly.
    """
    # Get the base URL from the environment variable set in the docker run command
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()
    
    try:
        # Navigate to the cart page
        cart_url = f"{base_url}/cart"
        driver.get(cart_url)
        
        # Assertion: Check if the URL contains "cart"
        assert "cart" in driver.current_url.lower()
        print("✅ ASSERTION PASSED: Cart page accessed successfully.")
        
    finally:
        # Teardown: Always close the browser to clean up resources
        driver.quit()