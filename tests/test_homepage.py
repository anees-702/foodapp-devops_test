# from base import get_driver

# driver = get_driver()
# driver.get("http://16.171.54.54:3000")
# assert "Small Bite" in driver.title  # Adjust this if needed
# print("✅ Homepage loaded successfully")
# driver.quit()

import os
# Use a relative import to get the driver from the 'base.py' file in the same directory
from .base import get_driver

def test_homepage_title():
    """
    Tests if the homepage loads and has the expected title.
    """
    # Get the base URL from the environment variable
    base_url = os.getenv("TEST_URL", "http://localhost:3000")
    driver = get_driver()

    try:
        # Navigate to the homepage
        driver.get(base_url)
        
        # Assertion: Check if the expected text is in the browser title
        expected_title = "Small Bite"
        assert expected_title in driver.title
        print(f"✅ ASSERTION PASSED: Homepage loaded with title '{driver.title}'.")
        
    finally:
        # Teardown: Always close the browser
        driver.quit()