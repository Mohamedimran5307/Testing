from selenium.webdriver.common.by import By

from Configurations.config import Testdata
from Pageobjects.Basepage import Basepage

"""By locators"""

class Connectorspage(Basepage):
    CONNECTOR_BUTTON = (By.ID, "navbar-connectors")
    ADD_CONNECTOR_BUTTON = (By.ID, "add-connector")
    CONNECTOR_NAME_FIELD = (By.ID, "connector-name")
    CONNECTOR_DESCRIPTION_FIELD = (By.ID, "connector-description")
    SELECT_ORGANIZATION_DROPDOWN = (By.ID, "connectors-select-orgnisation-id")
    SELECT_ORGANIZATION_1 = (By.XPATH ,"//li[text()='Imran Agri Solutions']")
    SELECT_ORGANIZATION_2 = (By.XPATH ,"//li[text()='Imran growers']")
    SELECT_DATASET_DROPDOWN = (By.ID, "connectors-select-dataset-id")
    SELECT_DATASET_1 = (By.XPATH, "//li[text()='PXD 1']")
    SELECT_DATASET_2 = (By.XPATH, "//li[text()='LDI 1']")
    SELECT_FILE_DROPDOWN = (By.ID, "connectors-select-file-id")
    SELECT_DATASET_FILE = (By.ID, "connectors-select-file-id-option0")
    ADD_BUTTON = (By.ID, "add-connector-button")
    DELETE_DATASET_FILE = (By.ID, "delete-integration-card0")  # indexing needed
    SELECT_ALL_COLUMNS_CHECKBOX_1 = (By.ID, "select-all-0-columns")
    # SELECT_ALL_COLUMNS_CHECKBOX_1 = (By.XPATH, "//input[@id='select-all-columns']")
    SELECT_ALL_COLUMNS_CHECKBOX_2 = (By.ID, "select-all-1-columns")
    JOIN_BY_ICON = (By.ID, "link-icon")
    LEFT_JOIN_FIELD = (By.ID, "primary_col_0_select_for_join")
    SELECT_ANY_COLUMN_LEFT = (By.ID, "file-9-columns-left")  # LACTATION_STAGE
    RIGHT_JOIN_FIELD = (By.ID, "secondary_col_select_for_join")
    SELECT_ANY_COLUMN_RIGHT = (By.ID, "file-9-columns-right")  # LACTATION_STAGE
    JOIN_TYPE_ICON = (By.ID, "innerjoin")
    APPLY_BUTTON = (By.ID, "generate_button_apply")
    CANCEL_BUTTON = (By.ID, "generate_button_apply")
    DOWNLOAD_BUTTON = (By.ID, "download_button")
    INTEGRAGTE_MORE_DATASETS_BUTTON = (By.ID, "integrate-more-datasets-button")
    SAVE_CONNECTOR_BUTTON = (By.ID, "save-connector-button")
    DELETE_CONNECTOR_BUTTON = (By.ID, "delete-connector-button")
    CANCEL_CONNECTOR_BUTTON = (By.ID, "cancel-button")

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASEURL)

    def add_connector(self):
        self.do_click(self.CONNECTOR_BUTTON)
        self.do_click(self.ADD_CONNECTOR_BUTTON)
        self.do_click(self.CONNECTOR_NAME_FIELD)
        self.do_sendkeys(self.CONNECTOR_NAME_FIELD, Testdata.CONNECTOR_NAME)
        self.do_click(self.CONNECTOR_DESCRIPTION_FIELD)
        self.do_sendkeys(self.CONNECTOR_DESCRIPTION_FIELD, Testdata.CONNECTOR_DESCRIPTION)
        self.do_click(self.SELECT_ORGANIZATION_DROPDOWN)
        self.do_click(self.SELECT_ORGANIZATION)
        self.do_click(self.SELECT_DATASET_DROPDOWN)
        self.do_click(self.SELECT_DATASET)
        self.do_click(self.SELECT_FILE_DROPDOWN)
        self.do_click(self.SELECT_DATASET_FILE)
        self.do_click(self.ADD_BUTTON)
        # self.do_clickable_2()
        self.do_scroll_up(self.CONNECTOR_NAME_FIELD)
        self.do_click(self.SELECT_ORGANIZATION_DROPDOWN)
        self.do_click(self.SELECT_ORGANIZATION)
        self.do_click(self.SELECT_DATASET_DROPDOWN)
        self.do_click(self.SELECT_DATASET)
        self.do_click(self.SELECT_FILE_DROPDOWN)
        self.do_click(self.SELECT_DATASET_FILE)
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.SELECT_ALL_COLUMNS_CHECKBOX_2)
        self.do_click(self.JOIN_BY_ICON)
        self.do_click(self.LEFT_JOIN_FIELD)
        self.do_click(self.SELECT_ANY_COLUMN_LEFT)
        self.do_click(self.RIGHT_JOIN_FIELD)
        self.do_click(self.SELECT_ANY_COLUMN_RIGHT)
