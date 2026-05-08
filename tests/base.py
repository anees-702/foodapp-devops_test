# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# def get_driver():
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--window-size=1920,1080')

#     service = Service(ChromeDriverManager().install())
#     return webdriver.Chrome(service=service, options=options)


# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    """
    Configures and returns a Selenium WebDriver for Chrome.

    This function sets up the Chrome browser to run in a "headless" mode,
    which is essential for automated tests in environments like Docker and Jenkins
    where there is no graphical user interface.
    """
    # Create an instance of ChromeOptions
    options = Options()

    # Add arguments for running in a headless/CI environment
    options.add_argument("--headless")
    options.add_argument("--no-sandbox") # Required for running as root in Docker
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage") # Prevents browser crashes in Docker

    # Initialize the Chrome WebDriver with the specified options.
    # Selenium will automatically find the ChromeDriver in the system's PATH
    # which we installed in the Dockerfile. No managers are needed.
    driver = webdriver.Chrome(options=options)
    
    return driver
