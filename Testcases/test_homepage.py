from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pageobjects.Homepage import Homepage
from Pageobjects.Loginpage import Loginpage
from Testcases.test_base import Basetest
from Configurations.config import Testdata
from Testcases.confitest import init_driver
import allure
import allure_pytest
from allure_commons.types import AttachmentType


class Test_homepage(Basetest):
    @allure.description("Testing Hompage Title")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Home_page_title(self):
        self.Homepage = Loginpage(self.driver)
        title = self.Homepage.get_title(Testdata.HOMEPAGE_TITLE)
        print(title)
        sleep(2)
        if self.driver.title == "DataHub":
            allure.attach(self.driver.get_screenshot_as_png(), name="Datahub title is present",
                          attachment_type=AttachmentType.PNG)
            assert True, "Datahub title is present"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Datahub title is absent",
                          attachment_type=AttachmentType.PNG)
            assert False, "Datahub title is absent"

    @allure.description("Testing Participants Tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_participants_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_visible(Homepage.PARTICIPANT_TAB)
        print(bool)
        homepage.do_click(Homepage.PARTICIPANT_TAB)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Participants tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participants tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Participants tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Participants tab is invisible"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Dashboard Tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Dashboard_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_visible(Homepage.DASHBOARD_TAB)
        print(bool)
        homepage.do_click(Homepage.DASHBOARD_TAB)
        sleep(6)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_dashboard":
            allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Dashboard tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Dashboard tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Dashboard tab is invisible"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Datasets Tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Datasets_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_visible(Homepage.DATASETS_TAB)
        print(bool)
        homepage.do_click(Homepage.DATASETS_TAB)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_datasets":
            allure.attach(self.driver.get_screenshot_as_png(), name="Datasets tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Datasets tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Datasets tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Datasets tab is invisible"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Connectors Tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Connectors_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_visible(Homepage.CONNECTORS_TAB)
        print(bool)
        homepage.do_click(Homepage.CONNECTORS_TAB)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/connectors":
            allure.attach(self.driver.get_screenshot_as_png(), name="Connectors tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Connectors tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Connectors tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Connectors tab is invisible"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Settings tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_settings_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_visible(Homepage.SETTINGS_BUTTON)
        print(bool)
        homepage.do_click(Homepage.SETTINGS_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/1":
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Settings tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Settings tab is invisible"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing sign_out Icon")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_out_button(self):
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
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        bool = homepage.is_enabled(Homepage.SIGN_OUT_BUTTON)
        print(bool)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_datasets":
            allure.attach(self.driver.get_screenshot_as_png(), name="Sign out button is present",
                          attachment_type=AttachmentType.PNG)
            assert True, "Sign out button is present"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Sign out button is absent",
                          attachment_type=AttachmentType.PNG)
            assert False, "Sign out button is absent"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing get_started button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_started_button(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        homepage.do_click(Homepage.HOME_BUTTON)
        sleep(3)
        homepage.do_click(Homepage.GET_STARTED_BUTTON_1)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home/get-started":
            allure.attach(self.driver.get_screenshot_as_png(), name="Get_started button is clickable",
                          attachment_type=AttachmentType.PNG)
            assert True, "Get_started button is clickable"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Get_started button is not clickable",
                          attachment_type=AttachmentType.PNG)
            assert False, "Get_started button is not clickable"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    #
    @allure.description("Testing view_all_datasets Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_all_datasets_button(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        homepage.do_click(Homepage.HOME_BUTTON)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,1000);")
        sleep(2)
        homepage.do_click(Homepage.VIEW_ALL_DATASETS_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(3)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home/datasets":
            allure.attach(self.driver.get_screenshot_as_png(), name="View all datasets is clickable",
                          attachment_type=AttachmentType.PNG)
            assert True, "View all datasets is clickable"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="View all datasets is not clickable",
                          attachment_type=AttachmentType.PNG)
            assert False, "View all datasets is not clickable"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing view_all_costeward Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_all_costeward_button(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        homepage.do_click(Homepage.HOME_BUTTON)
        self.driver.execute_script("window.scrollBy(0,2000);")
        sleep(2)
        homepage.do_click(Homepage.VIEW_ALL_CO_STEWARDS_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home/costeward":
            allure.attach(self.driver.get_screenshot_as_png(), name="View_all_costeward Button is clickable",
                          attachment_type=AttachmentType.PNG)
            assert True, "View_all_costeward Button is clickable"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="View_all_costeward Button is not clickable",
                          attachment_type=AttachmentType.PNG)
            assert False, "View_all_costeward Button is not clickable"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing view_all_participants Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_view_all_participants_button(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        homepage.do_click(Homepage.HOME_BUTTON)
        sleep(2)
        homepage.do_scroll_down(Homepage.VIEW_ALL_PARTICIPANTS_BUTTON)
        self.driver.execute_script("window.scrollBy(0,2500);")
        sleep(2)
        homepage.do_click(Homepage.VIEW_ALL_PARTICIPANTS_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="View_all_participants Button is clickable",
                          attachment_type=AttachmentType.PNG)
            assert True, "View_all_participants Button is clickable"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="View_all_participants Button is not clickable",
                          attachment_type=AttachmentType.PNG)
            assert False, "View_all_participants Button is not clickable"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing get_started_button2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_started_button2(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.loginpage.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        homepage = Homepage(self.driver)
        homepage.do_click(Homepage.HOME_BUTTON)
        self.driver.execute_script("window.scrollBy(0,3800);")
        sleep(2)
        homepage.do_click(Homepage.GET_STARTED_BUTTON_2)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home/get-started":
            allure.attach(self.driver.get_screenshot_as_png(), name="Get_started button is clickable",
                          attachment_type=AttachmentType.PNG)
            assert True, "Get_started button is clickable"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Get_started button is not clickable",
                          attachment_type=AttachmentType.PNG)
            assert False, "Get_started button is not clickable"
        homepage.do_click(Homepage.SIGN_OUT_BUTTON)
        print("Completed")



#             #
# # """ignoreexceptions="""
# #
