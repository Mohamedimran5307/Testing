from time import sleep

import pytest
import allure

from Configurations.config import Testdata
from Pageobjects.Loginpage import Loginpage
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest

from allure_commons.types import AttachmentType


class Test_login(Basetest):

    @allure.description("Testing Homepage Title")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Home_page_title(self):
        self.Homepage = Loginpage(self.driver)
        title = self.Homepage.get_title(Testdata.HOMEPAGE_TITLE)
        print(title)

        if self.driver.title == "DataHub":
            allure.attach(self.driver.get_screenshot_as_png(), name="Valid Homepage",
                          attachment_type=AttachmentType.PNG)
            assert True, "Valid Homepagee"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Invalid Homepage",
                          attachment_type=AttachmentType.PNG)
            assert False, "Invalid Homepage"
        print("Completed")

    @allure.description("Testing Log in functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_as_admin(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
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
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_datasets":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Login is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Login is failed"
        print("Completed")

