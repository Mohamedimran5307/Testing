from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage

"""By locators"""


class Homepage(Basepage):
    SETTINGS_BUTTON = (By.ID, "navbar-settings")
    PARTICIPANT_TAB = (By.ID,"navbar-participants")
    DATASETS_TAB = (By.ID,"navbar-dataset")
    CONNECTORS_TAB = (By.ID,"navbar-connectors")
    DASHBOARD_TAB = (By.ID,"navbar-new_dashboard")
    SIGN_OUT_BUTTON = (By.ID, "navbar-signout")
    HOME_BUTTON = (By.ID,"navbar-home")
    GET_STARTED_BUTTON_1 = (By.ID,"home-get-started-btn")
    GET_STARTED_BUTTON_2 = (By.ID,"home-get-started-btn2-id")
    VIEW_ALL_DATASETS_BUTTON = (By.ID,"details-page-load-more-dataset-button")
    VIEW_ALL_CO_STEWARDS_BUTTON = (By.ID,"home-view-all-costeward-btn-id")
    VIEW_ALL_PARTICIPANTS_BUTTON = (By.ID,"home-view-all-participants-btn-id")

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
        # self.driver.get(Testdata.BASEURL)

        """This is to get the Homepage title"""

    def get_Home_page_title(self, title):
        return self.get_title(title)

    """ These are the page actions for the Home_page"""

    def is_settings_button_exists(self):
        return self.is_visible(self.SETTINGS_BUTTON)

    def is_signout_button_exists(self):
        return self.is_enabled(self.SIGN_OUT_BUTTON)

    def test_get_started(self):
        self.do_click(self.HOME_BUTTON)
        self.do_click(self.GET_STARTED_BUTTON_1)

    def test_View_all_datasets(self):
        self.do_click(self.HOME_BUTTON)
        self.do_scroll_down(self.VIEW_ALL_DATASETS_BUTTON)
        self.do_click(self.VIEW_ALL_DATASETS_BUTTON)

    def test_view_all_Costeward(self):
        self.do_click(self.HOME_BUTTON)
        self.do_scroll_down(self.VIEW_ALL_CO_STEWARDS_BUTTON)
        self.do_click(self.VIEW_ALL_CO_STEWARDS_BUTTON)

    def test_view_all_Participants(self):
        self.do_click(self.HOME_BUTTON)
        # self.do_scroll_down(self.VIEW_ALL_PARTICIPANTS_BUTTON)
        self.do_scroll_down(self.GET_STARTED_BUTTON_2)
        self.do_click(self.VIEW_ALL_PARTICIPANTS_BUTTON)
        self.do_scroll_up(self.GET_STARTED_BUTTON_2)

    def test_get_started_2(self):
        self.do_click(self.HOME_BUTTON)
        self.do_click(self.GET_STARTED_BUTTON_2)
