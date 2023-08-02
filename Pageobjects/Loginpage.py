from time import sleep

from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage
from Pageobjects.Homepage import Homepage

"""By locators"""


class Loginpage(Basepage):
    REGISTER_TAB = (By.ID,"navbar-register")
    LOGIN_AS_ADMIN_BUTTON = (By.ID, "navbar-login")
    USERNAME_FIELD = (By.ID, "email_id_for_login")
    SEND_OTP_BUTTON = (By.ID, "send-otp-btn")
    ENTER_OTP = (By.ID, "email_id_for_login")
    VERIFY_OTP_BUTTON = (By.ID, "send-otp-btn")
    SIGNOUT_BUTTON = (By.ID,"navbar-signout")

    ORGANIZATION_NAME_FIELD = (By.ID, "organisation-name-id")
    ORGANIZATION_EMAIL_ID_FIELD = (By.ID, "add-participant-mail-id")
    ORGANIZATION_WEBSITE_LINK = (By.ID, "add-participant-website-link")
    ORGANIZATION_ADDRESS = (By.ID, "add-participant-organisation-address")
    COUNTRY_DROP_DOWN = (By.ID, "country-in-add-participants")
    SELECT_COUNTRY = (By.ID, "country-[object Object]103")
    PINCODE_FIELD = (By.ID, "add-participant-pin-code")
    FIRST_NAME_FIELD = (By.ID, "add-participant-first-name")
    LAST_NAME_FIELD = (By.ID, "add-participant-last-name")
    ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD = (By.ID,"add-participant-rootuser-mail-id")
    ORGANIZATION_CONTACT_NUMBER = (By.ID, "add-participant-phone-number")
    SELECT_COSTEWARD_DROP_DOWN = (By.ID,"select_costeward")
    SELECT_COSTEWARD = (By.ID,"select-costeward-7")
    CANCEL_BUTTON = (By.ID,"add-participant-cancel-button")
    SUBMIT_BUTTON = (By.ID, "add-participant-submit-button")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASEURL)
        sleep(2)

    """This is to get the Homepage title"""

    def get_Home_page_title(self, title):
        return self.get_title(title)

    """ These are the page actions for the Login_page"""

    def do_login(self, username, OTP):
        # signout_button = self.driver.find_element(By.ID,"navbar-signout")
        # print(signout_button)
        # if signout_button == "Signout":
        #
        #     self.do_click(self.SIGNOUT_BUTTON)
        # # else:
        self.do_click(self.LOGIN_AS_ADMIN_BUTTON)
        self.do_sendkeys(self.USERNAME_FIELD, username)
        self.do_click(self.SEND_OTP_BUTTON)
        self.do_sendkeys(self.ENTER_OTP, OTP)
        self.do_click(self.VERIFY_OTP_BUTTON)
        # return Homepage(self.driver)
