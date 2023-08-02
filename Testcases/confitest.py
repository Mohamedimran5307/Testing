from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from Configurations.config import Testdata


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    driver = None
    if request.param == "chrome":
        # Path to the ChromeDriver executable
        chrome_driver_path = Testdata.CHROME_EXECUTABLE_PATH

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (necessary for headless on macOS)
        chrome_options.add_argument("--window-size=1920x1080")  # Set window size (necessary for headless on macOS)

        # Launch ChromeDriver with headless mode
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        # # Create a Service object
        # chrome_service = Service(executable_path=chrome_driver_path)
        #
        # # Launch ChromeDriver using the Service object
        # driver = webdriver.Chrome(service=chrome_service)
        request.cls.driver = driver
        # yield
        # driver.quit()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
