from time import sleep

import pytest
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
from Pageobjects.Basepage import Basepage
from Configurations.config import Testdata
from Pageobjects.Loginpage import Loginpage
from Testcases.confitest import init_driver
from Testcases.test_base import Basetest
from Pageobjects.AddParticipant_page import Participant_page


class Test_add_participant(Basetest):

    @allure.description("Testing Admin Adding Participant")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Admin_adding_participant(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_CARD_BUTTON)
        sleep(1)
        self.participant_page.do_click(Participant_page.ORGANIZATION_NAME_FIELD)
        sleep(2)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_NAME_FIELD, Testdata.ORGANIZATION_NAME)
        sleep(1)
        self.participant_page.do_click(Participant_page.ORGANIZATION_EMAIL_ID_FIELD)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_EMAIL_ID_FIELD, Testdata.ORGANIZATION_EMAIL_ID)
        sleep(2)
        self.participant_page.do_click(Participant_page.ORGANIZATION_WEBSITE_LINK)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_WEBSITE_LINK,
                                          Testdata.ORGANIZATION_WEBSITE_LINK)
        self.participant_page.do_click(Participant_page.ORGANIZATION_ADDRESS)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_ADDRESS, Testdata.ORGANIZATION_ADDRESS)
        self.participant_page.do_click(Participant_page.COUNTRY_DROP_DOWN)
        sleep(1)
        self.participant_page.do_click(Participant_page.SELECT_COUNTRY)
        self.participant_page.do_click(Participant_page.PINCODE_FIELD)
        self.participant_page.do_sendkeys(Participant_page.PINCODE_FIELD, Testdata.PINCODE)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.participant_page.do_click(Participant_page.FIRST_NAME_FIELD)
        self.participant_page.do_sendkeys(Participant_page.FIRST_NAME_FIELD, Testdata.FIRST_NAME)
        self.participant_page.do_click(Participant_page.LAST_NAME_FIELD)
        self.participant_page.do_sendkeys(Participant_page.LAST_NAME_FIELD, Testdata.LAST_NAME)
        self.participant_page.do_click(Participant_page.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD,
                                          Testdata.ORGANIZATION_ROOT_USER_EMAIL_ID_2)
        self.participant_page.do_click(Participant_page.ORGANIZATION_CONTACT_NUMBER)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_CONTACT_NUMBER, Testdata.CONTACT_NUMBER)
        sleep(3)
        self.participant_page.do_click(Participant_page.SUBMIT_BUTTON)
        sleep(10)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Participant is added by admin",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participant is successfully added by admin"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to add Participant by admin",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to add Participant by admin"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Admin Adding Participant to Co-steward")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Admin_adding_participant_to_costeward(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_CARD_BUTTON)
        sleep(1)
        self.participant_page.do_click(Participant_page.ORGANIZATION_NAME_FIELD)
        sleep(2)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_NAME_FIELD, Testdata.ORGANIZATION_NAME)
        sleep(1)
        self.participant_page.do_click(Participant_page.ORGANIZATION_EMAIL_ID_FIELD)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_EMAIL_ID_FIELD,
                                          Testdata.ORGANIZATION_EMAIL_ID_2)
        sleep(2)
        self.participant_page.do_click(Participant_page.ORGANIZATION_WEBSITE_LINK)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_WEBSITE_LINK,
                                          Testdata.ORGANIZATION_WEBSITE_LINK)
        self.participant_page.do_click(Participant_page.ORGANIZATION_ADDRESS)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_ADDRESS, Testdata.ORGANIZATION_ADDRESS)
        self.participant_page.do_click(Participant_page.COUNTRY_DROP_DOWN)
        sleep(1)
        self.participant_page.do_click(Participant_page.SELECT_COUNTRY)
        self.participant_page.do_click(Participant_page.PINCODE_FIELD)
        self.participant_page.do_sendkeys(Participant_page.PINCODE_FIELD, Testdata.PINCODE)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.participant_page.do_click(Participant_page.FIRST_NAME_FIELD)
        self.participant_page.do_sendkeys(Participant_page.FIRST_NAME_FIELD, Testdata.FIRST_NAME)
        self.participant_page.do_click(Participant_page.LAST_NAME_FIELD)
        self.participant_page.do_sendkeys(Participant_page.LAST_NAME_FIELD, Testdata.LAST_NAME)
        self.participant_page.do_click(Participant_page.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD,
                                          Testdata.ORGANIZATION_ROOT_USER_EMAIL_ID)
        self.participant_page.do_click(Participant_page.ORGANIZATION_CONTACT_NUMBER)
        self.participant_page.do_sendkeys(Participant_page.ORGANIZATION_CONTACT_NUMBER, Testdata.CONTACT_NUMBER)
        sleep(2)
        self.participant_page.do_click_costeward_checkbox()
        sleep(2)
        self.participant_page.do_click(Participant_page.SUBMIT_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.COSTEWARD_TAB)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        print("Done")

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Costeward is added by admin",
                          attachment_type=AttachmentType.PNG)
            assert True, "Costeward is successfully added by admin"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to add Costeward by admin",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to add Costeward by admin"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Selecting Costeward while participant registration tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Selecting_Costeward_while_participant_registration(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.REGISTER_TAB)
        sleep(2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_NAME_FIELD)
        sleep(2)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_NAME_FIELD, Testdata.ORGANIZATION_NAME)
        sleep(1)
        self.loginpage.do_click(Loginpage.ORGANIZATION_EMAIL_ID_FIELD)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_EMAIL_ID_FIELD, Testdata.ORGANIZATION_EMAIL_ID)
        sleep(2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_WEBSITE_LINK)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_WEBSITE_LINK,
                                   Testdata.ORGANIZATION_WEBSITE_LINK)
        self.loginpage.do_click(Loginpage.ORGANIZATION_ADDRESS)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_ADDRESS, Testdata.ORGANIZATION_ADDRESS)
        self.loginpage.do_click(Loginpage.COUNTRY_DROP_DOWN)
        sleep(1)
        self.loginpage.do_click(Loginpage.SELECT_COUNTRY)
        self.loginpage.do_click(Loginpage.PINCODE_FIELD)
        self.loginpage.do_sendkeys(Loginpage.PINCODE_FIELD, Testdata.PINCODE)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.loginpage.do_click(Loginpage.FIRST_NAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.FIRST_NAME_FIELD, Testdata.FIRST_NAME)
        self.loginpage.do_click(Loginpage.LAST_NAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.LAST_NAME_FIELD, Testdata.LAST_NAME)
        self.loginpage.do_click(Loginpage.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD,
                                   Testdata.ORGANIZATION_ROOT_USER_EMAIL_ID_2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_CONTACT_NUMBER)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_CONTACT_NUMBER, Testdata.CONTACT_NUMBER)
        sleep(3)
        self.loginpage.do_click(Loginpage.SELECT_COSTEWARD_DROP_DOWN)
        sleep(2)
        self.loginpage.do_click(Loginpage.SELECT_COSTEWARD)
        sleep(3)
        self.loginpage.do_click(Loginpage.SUBMIT_BUTTON)
        sleep(5)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home":
            allure.attach(self.driver.get_screenshot_as_png(), name="Selecting Costeward while participant "
                                                                    "registration is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, "Selecting Costeward while participant registration is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to Selecting Costeward while participant "
                                                                    "registration",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to Selecting Costeward while participant registration"
        print("Completed")

    @allure.description("Testing Participant Registration tab")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_participant_registration(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.REGISTER_TAB)
        sleep(2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_NAME_FIELD)
        sleep(2)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_NAME_FIELD, Testdata.ORGANIZATION_NAME)
        sleep(1)
        self.loginpage.do_click(Loginpage.ORGANIZATION_EMAIL_ID_FIELD)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_EMAIL_ID_FIELD, Testdata.ORGANIZATION_EMAIL_ID)
        sleep(2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_WEBSITE_LINK)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_WEBSITE_LINK,
                                   Testdata.ORGANIZATION_WEBSITE_LINK)
        self.loginpage.do_click(Loginpage.ORGANIZATION_ADDRESS)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_ADDRESS, Testdata.ORGANIZATION_ADDRESS)
        self.loginpage.do_click(Loginpage.COUNTRY_DROP_DOWN)
        sleep(1)
        self.loginpage.do_click(Loginpage.SELECT_COUNTRY)
        self.loginpage.do_click(Loginpage.PINCODE_FIELD)
        self.loginpage.do_sendkeys(Loginpage.PINCODE_FIELD, Testdata.PINCODE)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,500);")
        sleep(2)
        self.loginpage.do_click(Loginpage.FIRST_NAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.FIRST_NAME_FIELD, Testdata.FIRST_NAME)
        self.loginpage.do_click(Loginpage.LAST_NAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.LAST_NAME_FIELD, Testdata.LAST_NAME)
        self.loginpage.do_click(Loginpage.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD,
                                   Testdata.ORGANIZATION_ROOT_USER_EMAIL_ID_2)
        self.loginpage.do_click(Loginpage.ORGANIZATION_CONTACT_NUMBER)
        self.loginpage.do_sendkeys(Loginpage.ORGANIZATION_CONTACT_NUMBER, Testdata.CONTACT_NUMBER)
        sleep(3)
        self.loginpage.do_click(Loginpage.SUBMIT_BUTTON)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/home":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Participant is registered",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participant is successfully registered"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to registered Participant",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to registered Participant"
        print("Completed")

    @allure.description("Testing cancel button")
    @allure.severity(allure.severity_level.NORMAL)
    def test_Cancel_button(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.REGISTER_TAB)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,700);")
        sleep(2)
        self.loginpage.do_click(Loginpage.CANCEL_BUTTON)
        sleep(2)
        if self.driver.current_url == "https://datahubethstage.farmstack.co/home":
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel button is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Cancel button is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel button is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Cancel button is invisible"

    @allure.description("Testing Approving participant request by admin")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Approving_Participant_Request_Button(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.NEW_PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        self.participant_page.do_click(Participant_page.APPROVE_BUTTON)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Participant request is approved by "
                                                                    "admin",
                          attachment_type=AttachmentType.PNG)
            assert True, "Successfully Participant request is approved by admin"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to approve Participant request by admin",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to approve participant request by admin"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Rejecting participant request by admin")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Rejecting_Participant_Request_Button(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.NEW_PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        self.participant_page.do_click(Participant_page.REJECT_BUTTON)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Successfully Participant request is rejected by "
                                                                    "admin",
                          attachment_type=AttachmentType.PNG)
            assert True, "Successfully Participant request is rejected by admin"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to rejected Participant request by admin",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to rejected participant request by admin"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Back button in New participant request")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Back_Button_in_New_Participant_Request(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.NEW_PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_REQUEST)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        self.participant_page.do_click(Participant_page.BACK_BUTTON)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Back button is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Back button is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Back button is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Back button is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Participant load more button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Participant_tab(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(3)
        self.participant_page.do_click(Participant_page.PARTICIPANT_LOAD_MORE)
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant load more button is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participant load more button is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant load more button is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Participant load more button is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing New Participant Request load more button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_New_participant_request_tab(self):
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
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(3)
        self.participant_page.do_click_LOAD_MORE()
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="New Participant Request Tab is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "New Participant Request Tab is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="New Participant Request Tab is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "New Participant Request Tab is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Costeward tab load more is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Costeward_tab(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.COSTEWARD_TAB)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        self.participant_page.do_click(Participant_page.COSTEWARD_LOAD_MORE_BUTTON)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,-800);")
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Costeward load more button is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Costeward load more button is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Costeward load more button is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Costeward load more button is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Costeward list view is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Costeward_List_View(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.COSTEWARD_TAB)
        sleep(3)
        self.participant_page.do_click(Participant_page.COSTEWARD_LIST_VIEW_BUTTON)
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Costeward list view is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Costeward list view is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Costeward list view is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Costeward list view is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing participant list view is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Participant_List_View(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(3)
        self.participant_page.do_click(Participant_page.PARTICIPATE_LIST_VIEW_BUTTON)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant list view is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Participant list view is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Participant list view is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Participant list view is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing New participant request list view is visible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_New_Participant_Request_List_View(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.NEW_PARTICIPANT_REQUEST)
        sleep(3)
        self.participant_page.do_click(Participant_page.NEW_PARTICIPANT_REQUEST_LIST_VIEW_BUTTON)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,200);")
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="New participant request list view is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "New participant request list view is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="New participant request list view is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "New participant request list view is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Inviting participant is successful")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Invite_Participant(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(3)
        self.participant_page.do_click(Participant_page.INVITE_PARTICIPANT_BUTTON)
        sleep(3)
        self.participant_page.do_click(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD)
        sleep(2)
        self.participant_page.do_sendkeys(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD,
                                          Testdata.INVITE_PARTICIPANT_EMAIL_ID)
        sleep(2)
        self.participant_page.do_enter(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD)
        sleep(2)
        self.participant_page.do_click(Participant_page.ADD_INVITE_NOTE)
        self.participant_page.do_sendkeys(Participant_page.ADD_INVITE_NOTE, Testdata.ADD_INVITE_NOTE_TEXT)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.participant_page.do_click(Participant_page.INVITE_SUBMIT_BUTTON)
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants/invite":
            allure.attach(self.driver.get_screenshot_as_png(), name="Invite sent successfully",
                          attachment_type=AttachmentType.PNG)
            assert True, "Invite sent successfully"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed to sent invite",
                          attachment_type=AttachmentType.PNG)
            assert False, "Failed to sent invite"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")

    @allure.description("Testing Cancel participant invitation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Cancel_Participant_Invite(self):
        self.loginpage = Loginpage(self.driver)
        sleep(3)
        self.driver.execute_script("window.localStorage.clear();")
        sleep(3)
        self.driver.execute_script("window.location.reload(true);")
        sleep(2)
        self.driver.maximize_window()
        self.loginpage.do_click(Loginpage.LOGIN_AS_ADMIN_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.USERNAME_FIELD)
        self.loginpage.do_sendkeys(Loginpage.USERNAME_FIELD, Testdata.USER_NAME)
        self.loginpage.do_click(Loginpage.SEND_OTP_BUTTON)
        sleep(2)
        self.loginpage.do_click(Loginpage.ENTER_OTP)
        self.loginpage.do_sendkeys(Loginpage.ENTER_OTP, Testdata.OTP)
        self.loginpage.do_click(Loginpage.VERIFY_OTP_BUTTON)
        sleep(2)
        self.participant_page = Participant_page(self.driver)
        self.driver.maximize_window()
        self.participant_page.do_click(Participant_page.PARTICIPANTS_BUTTON)
        sleep(2)
        self.participant_page.do_click(Participant_page.PARTICIPANT_BUTTON)
        sleep(3)
        self.participant_page.do_click(Participant_page.INVITE_PARTICIPANT_BUTTON)
        sleep(3)
        self.participant_page.do_click(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD)
        sleep(2)
        self.participant_page.do_sendkeys(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD,
                                          Testdata.INVITE_PARTICIPANT_EMAIL_ID)
        sleep(2)
        self.participant_page.do_enter(Participant_page.INVITE_PARTICIPANT_EMAIL_FIELD)
        sleep(2)
        self.participant_page.do_click(Participant_page.ADD_INVITE_NOTE)
        self.participant_page.do_sendkeys(Participant_page.ADD_INVITE_NOTE, Testdata.ADD_INVITE_NOTE_TEXT)
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,300);")
        sleep(2)
        self.participant_page.do_click(Participant_page.INVITE_CANCEL_BUTTON)
        sleep(3)

        if self.driver.current_url == "https://datahubethstage.farmstack.co/datahub/participants":
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel participant invitation is visible",
                          attachment_type=AttachmentType.PNG)
            assert True, "Cancel participant invitation is visible"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Cancel participant invitation is invisible",
                          attachment_type=AttachmentType.PNG)
            assert False, "Cancel participant invitation is invisible"

        self.participant_page.do_click(Participant_page.SIGN_OUT_BUTTON)
        print("Completed")
