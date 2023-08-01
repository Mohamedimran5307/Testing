from time import sleep

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations.config import Testdata
from Pageobjects.Loginpage import Loginpage
from Pageobjects.SettingsPage import SettingsPage
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest
from Pageobjects.AddParticipant_page import Participant_page


class Test_Settings_page(Basetest):

    @allure.description("Testing Account Settings Page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_account_settings_page(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.FIRST_NAME_FIELD)
        self.settings_page.do_select_all(SettingsPage.FIRST_NAME_FIELD)
        self.settings_page.do_clear(SettingsPage.FIRST_NAME_FIELD)
        sleep(2)
        self.settings_page.do_sendkeys(SettingsPage.FIRST_NAME_FIELD, Testdata.ACCOUNT_FIRST_NAME)
        self.settings_page.do_click(SettingsPage.LAST_NAME_FIELD)
        self.settings_page.do_select_all(SettingsPage.LAST_NAME_FIELD)
        self.settings_page.do_clear(SettingsPage.LAST_NAME_FIELD)
        sleep(2)
        self.settings_page.do_sendkeys(SettingsPage.LAST_NAME_FIELD, Testdata.ACCOUNT_LAST_NAME)
        self.settings_page.do_click(SettingsPage.CONTACT_NUMBER_FIELD)
        for i in range(10):
            self.settings_page.do_clear(SettingsPage.CONTACT_NUMBER_FIELD)
        sleep(2)
        self.settings_page.do_sendkeys(SettingsPage.CONTACT_NUMBER_FIELD, Testdata.ACCOUNT_CONTACT_NUMBER)
        sleep(1)
        self.settings_page.do_click(SettingsPage.SUBMIT_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/1":
            allure.attach(self.driver.get_screenshot_as_png(), name="Updating account details is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Updating account details is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Updating account details is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Updating account details is failed"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)
        print("jbds")

    @allure.description("Testing Cancel Button in account settings is Visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Cancel_Button_Account_Settings(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CANCEL_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_datasets":
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel Button in account settings is Visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Cancel Button in account settings is Visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel Button in account settings is Visible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Cancel Button in account settings is Visible"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)

    #
    @allure.description("Testing Organization Setting Page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_organization_settings_page(self):
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
        sleep(3)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_SETTINGS_TAB)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_NAME_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_NAME_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_NAME_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_NAME_FIELD, Testdata.UPDATE_ORGANIZATION_NAME)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_EMAIL_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_EMAIL_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_EMAIL_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_EMAIL_FIELD, Testdata.UPDATE_ORGANIZATION_MAIL_ID)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_WEBSITE_LINK_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_WEBSITE_LINK_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_WEBSITE_LINK_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_WEBSITE_LINK_FIELD,
                                       Testdata.UPDATE_ORGANIZATION_WEBSITE_LINK)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_CONTACTNUMBER_FIELD)
        for i in range(10):
            self.settings_page.do_clear(SettingsPage.ORGANIZATION_CONTACTNUMBER_FIELD)
        sleep(1)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_CONTACTNUMBER_FIELD,
                                       Testdata.UPDATE_ORGANIZATION_CONTACT_NUMBER)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_ADDRESS_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_ADDRESS_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_ADDRESS_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_ADDRESS_FIELD, Testdata.ORGANIZATION_ADDRESS)
        sleep(2)
        self.settings_page.do_click(SettingsPage.COUNTRY_FIELD)
        self.settings_page.do_click(SettingsPage.SELECT_COUNTRY)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_PINCODE_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_PINCODE_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_PINCODE_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_PINCODE_FIELD, Testdata.UPDATE_ORGANIZATION_PINCODE)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_DESCRIPTION_FIELD)
        self.settings_page.do_select_all(SettingsPage.ORGANIZATION_DESCRIPTION_FIELD)
        self.settings_page.do_clear(SettingsPage.ORGANIZATION_DESCRIPTION_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ORGANIZATION_DESCRIPTION_FIELD,
                                       Testdata.UPDATE_ORGANIZATION_DESCRIPTION)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,400);")
        sleep(2)
        self.settings_page.do_sendkeys_ORG_LOGO()
        sleep(2)
        self.settings_page.do_click(SettingsPage.DONE_BUTTON_LOGO)
        sleep(2)
        self.settings_page.do_click(SettingsPage.CANCEL_LOGO_BUTTON)
        sleep(1)
        self.settings_page.do_sendkeys_ORG_LOGO()
        sleep(2)
        self.settings_page.do_click(SettingsPage.DONE_BUTTON_LOGO)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.ORGANIZATION_SUBMIT_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/2":
            allure.attach(self.driver.get_screenshot_as_png(), name="Updating organizational details is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Updating organizational details is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Updating organizational details is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Updating organizational details is failed"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)

    @allure.description("Testing Policy Settings Page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_policy_settings_page(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.POLICY_TAB)
        self.settings_page.do_click(SettingsPage.ADD_NEW_POLICY)
        self.settings_page.do_click(SettingsPage.POLICY_NAME_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.POLICY_NAME_FIELD, Testdata.POLICY_NAME)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.POLICY_DESCRIPTION)
        self.settings_page.do_sendkeys(SettingsPage.POLICY_DESCRIPTION, Testdata.POLICY_DESCRIPTION)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_sendkeys_POLICIES()
        sleep(2)
        self.settings_page.do_click(SettingsPage.ADD_POLICY)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/3":
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding Policy is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Adding Policy is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding Policy is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Adding Policy is successful"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)

    @allure.description("Updating Policy")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_policy(self):
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
        sleep(3)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.POLICY_TAB)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_NAME_FIELD)
        self.settings_page.do_select_all(SettingsPage.UPDATE_POLICY_NAME_FIELD)
        self.settings_page.do_clear(SettingsPage.UPDATE_POLICY_NAME_FIELD)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_sendkeys(SettingsPage.UPDATE_POLICY_NAME_FIELD, Testdata.UPDATE_POLICY_NAME)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DESCRIPTION_FIELD)
        self.settings_page.do_select_all(SettingsPage.UPDATE_POLICY_DESCRIPTION_FIELD)
        self.settings_page.do_clear(SettingsPage.UPDATE_POLICY_DESCRIPTION_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.UPDATE_POLICY_DESCRIPTION_FIELD, Testdata.UPDATE_POLICY_DESCRIPTION)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        # # self.settings_page.do_click(SettingsPage.UPDATE_CLOSE_BUTTON)
        # # sleep(2)
        # self.settings_page.do_sendkeys_UPDATE_POLICIES()
        # sleep(5)
        print("IMRAN")
        self.settings_page.do_click(SettingsPage.UPDATE_SAVE_BUTTON)
        sleep(2)
        # self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_BUTTON)
        # self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_BUTTON_2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/3":
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings button is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, ""
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings button is invisible",
                          attachment_type=AttachmentType.PNG)

    @allure.description("Testing Delete Policy")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Delete_Policy(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.POLICY_TAB)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_ICON)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_POPPER)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/3":
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Policy is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Deleting Policy is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Policy is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Deleting Policy is failed"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)

    @allure.description("Testing Delete Policy Button2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Delete_Policy_Button2(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.POLICY_TAB)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,900);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_BUTTON2)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_POLICY_DELETE_POPPER2)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/3":
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Policy is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Deleting Policy is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Policy is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, "Deleting Policy is failed"
        self.settings_page.do_click(SettingsPage.SIGN_OUT_BUTTON)

    @allure.description("Adding Categories")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_adding_category(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
        self.settings_page.do_click(SettingsPage.ADD_NEW_CATEGORY)
        self.settings_page.do_click(SettingsPage.CATEGORY_NAME_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.CATEGORY_NAME_FIELD, Testdata.CATEGORY_NAME)
        self.settings_page.do_click(SettingsPage.CATEGORY_DESCRIPTION_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.CATEGORY_DESCRIPTION_FIELD, Testdata.POLICY_DESCRIPTION)
        self.settings_page.do_click(SettingsPage.ADD_CATEGORY_BUTTON)
        self.driver.execute_script("window.scrollBy(0,700);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding Categories is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Adding Categories is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to add categories",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to add categories"

    @allure.description("Adding sub categories")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_adding_sub_category(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_ACCORDION)
        self.settings_page.do_click(SettingsPage.ADD_SUB_CATEGORY_NAME_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.ADD_SUB_CATEGORY_NAME_FIELD, Testdata.ADD_SUB_CATEGORY_NAME)
        self.settings_page.do_click(SettingsPage.ADD_SUB_CATEGORY_ICON)
        self.driver.execute_script("window.scrollBy(0,700);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        sleep(2)
        # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_EDIT_ICON)
        # self.settings_page.do_click(SettingsPage.EDIT_CATEGORY_NAME_FIELD)
        # self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_BUTTON)
        # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_BUTTON_2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding Subcategory is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Adding Subcategory is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to add sub-categories",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to add sub-categories"

    @allure.description("Updating Category Name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Updating_Category_Name(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_ACCORDION)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_EDIT_ICON)
        sleep(2)
        self.settings_page.do_click(SettingsPage.EDIT_CATEGORY_NAME_FIELD)
        self.settings_page.do_select_all(SettingsPage.EDIT_CATEGORY_NAME_FIELD)
        self.settings_page.do_clear(SettingsPage.EDIT_CATEGORY_NAME_FIELD)
        sleep(2)
        self.settings_page.do_sendkeys(SettingsPage.EDIT_CATEGORY_NAME_FIELD, Testdata.UPDATE_CATGEORY_NAME_FIELD)
        self.driver.execute_script("window.scrollBy(0,400);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_NAME_BUTTON)
        self.driver.execute_script("window.scrollBy(0,700);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
            allure.attach(self.driver.get_screenshot_as_png(), name="Updating Category Name is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Updating Category Name is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to Updating Category Name",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to Updating Category Name"

    @allure.description("Delete Icon Category ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Delete_Icon_Category(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_ICON)
        # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_ACCORDION3)
        # sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_POPPER_BUTTON_2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Category is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Deleting Category is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to Delete Category",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to Delete Category"
    #

    @allure.description("Delete Button Category ")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Delete_Button_Category(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
        sleep(2)
        # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_ICON)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_ACCORDION3)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.DELETE_CATEGORY_BUTTON)
        sleep(2)
        self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_POPPER_BUTTON_2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.CATEGORY_SUBMIT_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting Category is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Deleting Category is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to Delete Category",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to Delete Category"
    # @allure.description("Cancel Button in Category ")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_Cancel_Button_Category(self):
    #     self.loginpage = Loginpage(self.driver)
    #     sleep(3)
    #     self.driver.execute_script("window.localStorage.clear();")
    #     sleep(3)
    #     self.driver.execute_script("window.location.reload(true);")
    #     sleep(2)
    #     self.driver.maximize_window()
    #     self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
    #     self.loginpage.do_click(Loginpage.USERNAME_FIELD)
    #     self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
    #     self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
    #     sleep(2)
    #     self.loginpage.do_click(Loginpage.ENTER_OTP)
    #     self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
    #     self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
    #     sleep(5)
    #     self.settings_page = SettingsPage(self.driver)
    #     self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
    #     self.settings_page.do_click(SettingsPage.CATEGORY_TAB)
    #     sleep(2)
    #     self.driver.execute_script("window.scrollBy(0,500);")
    #     sleep(2)
    #     self.settings_page.do_click(SettingsPage.CANCEL_BUTTON_CATEGORY)
    #     sleep(2)
    #     if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/new_datasets":
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Cancel Button is visible",
    #                       attachment_type=AttachmentType.PNG)
    #         assert True, "Cancel Button is visible"
    #     else:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Cancel Button is invisible",
    #                       attachment_type=AttachmentType.PNG)
    #         assert False, "Cancel Button is invisible"

    @allure.description("Adding Datapoint_category")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_adding_datapoint_category(self):
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
        sleep(5)
        self.settings_page = SettingsPage(self.driver)
        self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
        self.settings_page.do_click(SettingsPage.DATAPOINT_TAB)
        self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_NAME_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.DATAPOINT_CATEGORY_NAME_FIELD, Testdata.DATAPOINT_CATEGORY_NAME)
        self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_DESCRIPTION_FIELD)
        self.settings_page.do_sendkeys(SettingsPage.DATAPOINT_CATEGORY_DESCRIPTION_FIELD,
                                       Testdata.DATAPOINT_CATEGORY_DESCRIPTION)
        self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_ADD_BUTTON)
        self.driver.execute_script("window.scrollBy(0,900);")
        sleep(2)
        self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_SUBMIT_BUTTON)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/5":
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings button is visible",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Settings button is invisible",
                          attachment_type=AttachmentType.PNG)

    # @allure.description("Adding Datapoint Attributes")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_Adding_Datapoint_Attributes(self):
    #     self.loginpage = Loginpage(self.driver)
    #     sleep(2)
    #     self.driver.execute_script("window.localStorage.clear();")
    #     self.driver.maximize_window()
    #     self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
    #     self.loginpage.do_click(Loginpage.USERNAME_FIELD)
    #     self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
    #     self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
    #     sleep(2)
    #     self.loginpage.do_click(Loginpage.ENTER_OTP)
    #     self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
    #     self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
    #     sleep(5)
    #     self.settings_page = SettingsPage(self.driver)
    #     self.settings_page.do_click(SettingsPage.SETTINGS_BUTTON)
    #     self.settings_page.do_click(SettingsPage.DATAPOINT_TAB)
    #     sleep(2)
    #     self.driver.execute_script("window.scrollBy(0,700);")
    #     sleep(2)
    #     self.settings_page.do_click(SettingsPage.UPDATE_DATAPOINT_CATEGORY)
    #     sleep(2)
    #     self.driver.execute_script("window.scrollBy(0,300);")
    #     sleep(2)
    #     # self.settings_page.do_click(SettingsPage.ADD_DATAPOINT_ATTRIBUTE_NAME_FIELD)
    #     # sleep(2)
    #     self.settings_page.do_click_ADD_DATAPOINT_ATTRIBUTE_NAME_FIELD()
    #     sleep(2)
    #     # self.settings_page.do_sendkeys(SettingsPage.ADD_DATAPOINT_ATTRIBUTE_NAME_FIELD, Testdata.ADD_DATAPOINT_ATTRIBUTES)
    #     # sleep(2)
    #     # self.settings_page.do_click(SettingsPage.ADD_DATAPOINT_ATTRIBUTE_ICON)
    #     # sleep(2)
    #     # self.driver.execute_script("window.scrollBy(0,500);")
    #     # sleep(2)
    #     # self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_SUBMIT_BUTTON)
    #     # self.settings_page.do_click(SettingsPage.UPDATE_DATAPOINT_CATEGORY_EDIT_BUTTON)
    #     # self.settings_page.do_click(SettingsPage.EDIT_DATAPOINT_CATEGORY_NAME_FIELD)
    #     # self.settings_page.do_select_all(SettingsPage.EDIT_DATAPOINT_CATEGORY_NAME_FIELD)
    #     # self.settings_page.do_clear(SettingsPage.EDIT_DATAPOINT_CATEGORY_NAME_FIELD)
    #     # self.settings_page.do_sendkeys(SettingsPage.EDIT_DATAPOINT_CATEGORY_NAME_FIELD,Testdata.UPDATED_DATAPOINT_CATEGORY_NAME)
    #     # self.settings_page.do_click(SettingsPage.UPDATE_DATAPOINT_CATEGORY_NAME_BUTTON)
    #     # self.settings_page.do_click(SettingsPage.DATAPOINT_CATEGORY_SUBMIT_BUTTON)
    #     # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_BUTTON)
    #     # self.settings_page.do_click(SettingsPage.UPDATE_CATEGORY_DELETE_BUTTON_2)
    #     if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/settings/4":
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Adding Datapoint Attributes is successful",
    #                       attachment_type=AttachmentType.PNG)
    #         assert True,"Adding Datapoint Attributes is successful"
    #     else:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Failed to add Datapoint Attributes ",
    #                       attachment_type=AttachmentType.PNG)
    #         assert False,"Failed to add Datapoint Attributes"
