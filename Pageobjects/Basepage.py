from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

"""This is parent class of the pages (Login page)"""

"""It contains all the generic methods and Utilities for all the pages"""


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        # print("element in click fun", by_locator, element)
        element.click()

    def do_click_Delete_Button(self):
        wait = WebDriverWait(self.driver, 10)  # Wait for a maximum of 10 seconds
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']")))
        element.click()
        # self.driver.find_element(By.XPATH, "//button[text()='Delete']").click()

    def do_click_ADD_DATAPOINT_ATTRIBUTE_NAME_FIELD(self):
        wait = WebDriverWait(self.driver, 10)  # Wait for a maximum of 10 seconds
        element = wait.until(EC.presence_of_all_elements_located((By.ID, "datapoint-attribute-input-box-id")))
        print("element", element)
        element[0].click()
    def do_click_LOAD_MORE(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[5]/div/button").click()

    # def do_hover_to_element(self):
    #     element = self.driver.find_element(By.CSS_SELECTOR,"button#New-load-more-button")
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).perform()
    #     # Scroll the element into view if it's not visible after hover
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     element.click()

    # def do_hover_to_element(self, SELECT_ALL_COLUMNS_CHECKBOX_1):
    #     actions = ActionChains(self.driver)
    # WebDriverWait(self.driver, 20).until(actions.move_to_element(SELECT_ALL_COLUMNS_CHECKBOX_1)).perform().click()

    def do_click_constanly_updating_checkbox(self):
        self.driver.find_element(By.ID, "check-box-undefined").click()

    def do_click_costeward_checkbox(self):
        self.driver.find_element(By.ID, "add-participant-make-costeward").click()

    def do_click_apply_button(self):
        self.driver.find_element(By.ID, "generate_button").click()

    def do_clickable_Checkbox_Connectors_2(self):
        self.driver.find_element(By.ID, "select-all-1-columns").click()

    def do_clickable_mask(self):
        self.driver.find_element(By.ID, "check-box-1").click()

    def do_clickable_CATEGORY(self):
        self.driver.find_element(By.ID, "check-box-0").click()

    def do_clickable_REGISTER_USER(self):
        self.driver.find_element(By.ID, "usege-policy-register-user-dataset-checkbox").click()

    def do_clickable_MYSQL_COLUMN_CHECKBOX(self):
        self.driver.find_element(By.ID, "MySQL-uploaded-data-checkbox-id-0").click()
        self.driver.find_element(By.ID, "MySQL-uploaded-data-checkbox-id-1").click()
        self.driver.find_element(By.ID, "MySQL-uploaded-data-checkbox-id-2").click()
        self.driver.find_element(By.ID, "MySQL-uploaded-data-checkbox-id-3").click()
        self.driver.find_element(By.ID, "MySQL-uploaded-data-checkbox-id-4").click()

    def do_clickable_POSTGRES_COLUMN_CHECKBOX(self):
        self.driver.find_element(By.ID, "Postgres-uploaded-data-checkbox-id-0").click()
        self.driver.find_element(By.ID, "Postgres-uploaded-data-checkbox-id-1").click()
        self.driver.find_element(By.ID, "Postgres-uploaded-data-checkbox-id-2").click()
        self.driver.find_element(By.ID, "Postgres-uploaded-data-checkbox-id-3").click()
        self.driver.find_element(By.ID, "Postgres-uploaded-data-checkbox-id-4").click()

    def do_clickable_Checkbox_Connectors(self):
        self.driver.find_element(By.ID, "select-all-0-columns").click()

    def do_click_DATABASE_NAME_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-db-name-id").click()

    def do_sendkeys_DATABASE_NAME_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-db-name-id").send_keys("suitecrm")

    def do_click_USER_NAME_MYSQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-user-name-id").click()

    def do_sendkeys_USER_NAME_MYSQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-user-name-id").send_keys("readonly")

    def do_click_PASSWORD_MYSQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-password-id").click()

    def do_sendkeys_PASSWORD_MYSQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-password-id").send_keys("KLxnnme.C_2GR#G")

    def do_click_DATABASE_HOST_URL_MySQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-database-host-url-id").click()

    def do_sendkeys_DATABASE_HOST_URL_MySQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-database-host-url-id").send_keys(
            "copiamexiconoetlparadigitalgreen.cskysn2rpea7.us-east-2.rds.amazonaws.com")

    def do_sendkeys_MYSQL_PORT_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-port-id").send_keys("3306")

    def do_click_MYSQL_PORT_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-port-id").click()

    def do_click_MYSQL_CONNECT_BUTTON(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-connect-btn").click()

    def do_click_SELECT_TABLE_MYSQL_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-select-id").click()

    def do_click_SELECT_TABLE_MYSQL(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-select-id-7").click()

    def do_click_FILE_NAME_MYSQL_IMPORT_DATA_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-filename-id").click()

    def do_sendkeys_FILE_NAME_MYSQL_IMPORT_DATA_FIELD(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-filename-id").send_keys("FILE_NAME_SQL")

    def do_click_IMPORT_BUTTON_MYSQL(self):
        self.driver.find_element(By.ID, "MySQL-upload-dataset-import-btn").click()

    def do_click_DATABASE_NAME_FIELD_Postgres(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-db-name-id").click()

    def do_sendkeys_DATABASE_NAME_FIELD_Postgres(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-db-name-id").send_keys("postgres")

    def do_click_USER_NAME_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-user-name-id").click()

    def do_sendkeys_USER_NAME_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-user-name-id").send_keys("root")

    def do_click_PASSWORD_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-password-id").click()

    def do_sendkeys_PASSWORD_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-password-id").send_keys("xKG1A4bQ2XX3@e!8d")

    def do_click_DATABASE_HOST_URL_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-database-host-url-id").click()

    def do_sendkeys_DATABASE_HOST_URL_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-database-host-url-id").send_keys(
            "52.64.104.116")

    def do_click_POSTGRES_PORT_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-port-id").click()

    def do_sendkeys_POSTGRES_PORT_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-port-id").send_keys("5542")

    def do_click_POSTGRES_CONNECT_BUTTON(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-connect-btn").click()

    def do_click_SELECT_TABLE_POSTGRES_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-select-id").click()

    def do_click_SELECT_TABLE_POSTGRES(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-select-id-1").click()

    def do_click_FILE_NAME_POSTGRES_IMPORT_DATA_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-filename-id").click()

    def do_sendkeys_FILE_NAME_POSTGRES_IMPORT_DATA_FIELD(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-filename-id").send_keys("FILE_NAME_POSTGRES")

    def do_click_IMPORT_BUTTON_POSTGRES(self):
        self.driver.find_element(By.ID, "Postgres-upload-dataset-import-btn").click()

    def do_select_all(self, by_locator):
        Text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Text.send_keys(Keys.COMMAND, "a")

    def do_clear(self, by_locator):
        Text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Text.send_keys(Keys.BACK_SPACE)

    def do_enter(self, by_locator):
        Text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        Text.send_keys(Keys.ENTER)

    def do_scroll_down(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.PAGE_DOWN)

    def do_scroll_up(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.PAGE_UP)

    def do_sendkeys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_sendkeys_1(self):
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/PXD Feed (1).xlsx")

    def do_sendkeys_edit_dataset(self):
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/LDI_31.xls")

    def do_sendkeys_ORG_LOGO(self):
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/DigitalGreen_logo.png")

    def do_sendkeys_POLICIES(self):
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
            "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/Warranties.pdf")

    def do_click_checkbox_filter_Subcategories(self):
        self.driver.find_element(By.ID, "check-box-1").click()

    def do_sendkeys_UPDATE_POLICIES(self):
        self.driver.find_element(By.ID, "file-upload-drag-and-drop-0-file-update").send_keys(
            "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/Warranties.pdf")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_AUTH_TOKEN(self):
        AUTH_TOKEN = self.driver.execute_script("return window.localStorage.getItem('JWTToken')")
        return AUTH_TOKEN
