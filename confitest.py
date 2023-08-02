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

        # Create a Service object
        chrome_service = Service(executable_path=chrome_driver_path)

        # Launch ChromeDriver using the Service object
        driver = webdriver.Chrome(service=chrome_service)
        request.cls.driver = driver
        # yield
        # driver.quit()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
