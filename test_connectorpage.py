from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from Pageobjects.Connectorpage import Connectorspage
from Pageobjects.Homepage import Homepage
from Pageobjects.Loginpage import Loginpage
from Testcases.test_base import Basetest
from Configurations.config import Testdata
from Testcases.confitest import init_driver
from selenium import webdriver

from time import sleep

import pytest
import allure
from allure_commons.types import AttachmentType

from Configurations.config import Testdata
from Pageobjects.Loginpage import Loginpage
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest


class Test_add_connector(Basetest):

    @allure.description("Testing Adding Connector")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_connector(self):
        self.loginpage = Loginpage(self.driver)
        sleep(2)
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.connectors_page = Connectorspage(self.driver)
        self.connectors_page.do_click(Connectorspage.CONNECTOR_BUTTON)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.ADD_CONNECTOR_BUTTON)
        self.connectors_page.do_click(Connectorspage.CONNECTOR_NAME_FIELD)
        self.connectors_page.do_sendkeys(Connectorspage.CONNECTOR_NAME_FIELD, Testdata.CONNECTOR_NAME)
        self.connectors_page.do_click(Connectorspage.CONNECTOR_DESCRIPTION_FIELD)
        self.connectors_page.do_sendkeys(Connectorspage.CONNECTOR_DESCRIPTION_FIELD, Testdata.CONNECTOR_DESCRIPTION)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.connectors_page.do_click(Connectorspage.SELECT_ORGANIZATION_DROPDOWN)
        self.connectors_page.do_click(Connectorspage.SELECT_ORGANIZATION_1)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_DROPDOWN)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_1)
        self.connectors_page.do_click(Connectorspage.SELECT_FILE_DROPDOWN)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_FILE)
        self.connectors_page.do_click(Connectorspage.ADD_BUTTON)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.connectors_page.do_clickable_Checkbox_Connectors()
        sleep(3)
        self.connectors_page.do_scroll_up(Connectorspage.CONNECTOR_NAME_FIELD)
        # self.driver.execute_script("window.scrollBy(0,-3000);")
        self.connectors_page.do_click(Connectorspage.SELECT_ORGANIZATION_DROPDOWN)
        self.connectors_page.do_click(Connectorspage.SELECT_ORGANIZATION_2)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_DROPDOWN)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_2)
        self.connectors_page.do_click(Connectorspage.SELECT_FILE_DROPDOWN)
        self.connectors_page.do_click(Connectorspage.SELECT_DATASET_FILE)
        self.connectors_page.do_click(Connectorspage.ADD_BUTTON)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,1100);")
        sleep(2)
        self.connectors_page.do_clickable_Checkbox_Connectors_2()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,-300);")
        sleep(2)
        self.connectors_page.do_click(Connectorspage.JOIN_BY_ICON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,600);")
        self.connectors_page.do_click(Connectorspage.LEFT_JOIN_FIELD)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.SELECT_ANY_COLUMN_LEFT)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.RIGHT_JOIN_FIELD)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.SELECT_ANY_COLUMN_RIGHT)
        sleep(2)
        self.connectors_page.do_click(Connectorspage.JOIN_TYPE_ICON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.connectors_page.do_click(Connectorspage.APPLY_BUTTON)
        print("IMRAN")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,1300);")
        sleep(2)
        self.connectors_page.do_click(Connectorspage.DOWNLOAD_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        self.connectors_page.do_click(Connectorspage.SAVE_CONNECTOR_BUTTON)
        sleep(3)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/connectors":
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating connector is successfully",
                          attachment_type=AttachmentType.PNG)
            assert True, "Creating connector is successfully"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating connector is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Creating connector is failed"
