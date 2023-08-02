from Pageobjects.Basepage import Basepage
from selenium.webdriver.common.by import By
from Configurations.config import Testdata


class Participant_page(Basepage):
    PARTICIPANTS_BUTTON = (By.ID, "navbar-participants")
    PARTICIPANT_BUTTON = (By.ID, "Participant1")
    PARTICIPANT_LOAD_MORE = (By.CSS_SELECTOR,"button[data-testid=load-more-button-test-button]")
    PARTICIPANT_CARD_BUTTON = (By.ID, "Participants-card-")
    ORGANIZATION_NAME_FIELD = (By.ID, "organisation-name-id")
    ORGANIZATION_EMAIL_ID_FIELD = (By.ID, "add-participant-mail-id")
    ORGANIZATION_WEBSITE_LINK = (By.ID, "add-participant-website-link")
    ORGANIZATION_ADDRESS = (By.ID, "add-participant-organisation-address")
    COUNTRY_DROP_DOWN = (By.ID, "country-in-add-participants")
    SELECT_COUNTRY = (By.ID, "country-[object Object]103")
    PINCODE_FIELD = (By.ID, "add-participant-pin-code")
    FIRST_NAME_FIELD = (By.ID, "add-participant-first-name")
    LAST_NAME_FIELD = (By.ID, "add-participant-last-name")
    ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD = (By.ID, "add-participant-rootuser-mail-id")
    ORGANIZATION_CONTACT_NUMBER = (By.ID, "add-participant-phone-number")
    SUBMIT_BUTTON = (By.ID, "add-participant-submit-button")
    CO_STEWARD_CHECKBOX = (By.ID, "add-participant-make-costeward")
    SIGN_OUT_BUTTON = (By.ID, "navbar-signout")
    COSTEWARD_TAB = (By.ID, "Co-Steward0")
    COSTEWARD_LIST_VIEW_BUTTON = (By.ID,"Co-stewardlist-view-title")
    PARTICIPATE_LIST_VIEW_BUTTON = (By.ID,"Participantslist-view")
    COSTEWARD_LOAD_MORE_BUTTON = (By.ID,"Co-steward-load-more-button")
    NEW_PARTICIPANT_REQUEST = (By.ID, "New Participant Requests2")
    NEW_PARTICIPANT_REQUEST_LIST_VIEW_BUTTON = (By.ID,"Newlist-view")
    PARTICIPANT_REQUEST = (By.ID, "Newgrid-card-id0")
    LOAD_MORE_BUTTON = (By.ID, "New-load-more-button")
    # LOAD_MORE_BUTTON = (By.XPATH, "//button[@id='New-load-more-button']")
    APPROVE_BUTTON = (By.ID, "details-page-approve-button")
    REJECT_BUTTON = (By.ID,"details-page-reject-button")
    BACK_BUTTON = (By.ID,"details-page-back-button")
    INVITE_PARTICIPANT_BUTTON= (By.ID,"add-participant-submit-button")
    INVITE_PARTICIPANT_EMAIL_FIELD = (By.ID,"invite-participants-emails-textfield")
    ADD_INVITE_NOTE = (By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/div[2]/div/div/div")
    INVITE_SUBMIT_BUTTON = (By.ID,"details-page-load-more-dataset-button")
    INVITE_CANCEL_BUTTON = (By.ID,"")
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASEURL)

    """ These are the page actions for the Add_participant_page"""

    def adding_participant(self):
        self.do_click(self.PARTICIPANTS_BUTTON)
        self.do_click(self.PARTICIPANT_BUTTON)
        self.do_click(self.PARTICIPANT_CARD_BUTTON)
        self.do_click(self.ORGANIZATION_NAME_FIELD)
        self.do_sendkeys(self.ORGANIZATION_NAME_FIELD, Testdata.ORGANIZATION_NAME)
        self.do_click(self.ORGANIZATION_EMAIL_ID_FIELD)
        self.do_sendkeys(self.ORGANIZATION_EMAIL_ID_FIELD, Testdata.ORGANIZATION_EMAIL_ID)
        self.do_click(self.ORGANIZATION_WEBSITE_LINK)
        self.do_sendkeys(self.ORGANIZATION_WEBSITE_LINK, Testdata.ORGANIZATION_WEBSITE_LINK)
        self.do_click(self.ORGANIZATION_ADDRESS)
        self.do_sendkeys(self.ORGANIZATION_ADDRESS, Testdata.ORGANIZATION_ADDRESS)
        self.do_click(self.SELECT_COUNTRY)
        self.do_sendkeys(self.PINCODE_FIELD, Testdata.PINCODE)
        self.do_click(self.FIRST_NAME_FIELD)
        self.do_sendkeys(self.FIRST_NAME_FIELD, Testdata.FIRST_NAME)
        self.do_click(self.LAST_NAME_FIELD)
        self.do_sendkeys(self.LAST_NAME_FIELD, Testdata.LAST_NAME)
        self.do_click(self.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD)
        self.do_sendkeys(self.ORGANIZATION_ROOT_USER_EMAIL_ID_FIELD, Testdata.ORGANIZATION_ROOT_USER_EMAIL_ID)
        self.do_click(self.ORGANIZATION_CONTACT_NUMBER)
        self.do_sendkeys(self.ORGANIZATION_CONTACT_NUMBER,Testdata.CONTACT_NUMBER)
        self.do_click(self.CO_STEWARD_CHECKBOX)
        self.do_click(self.SUBMIT_BUTTON)
        self.do_click(self.COSTEWARD_TAB)

