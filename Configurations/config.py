import random
import string


class Testdata:
    CHROME_EXECUTABLE_PATH = "/Users/shaikmohamedimran/Desktop/D/Web drivers/chromedriver.exe"

    BASEURL = "https://datahubethstage.farmstack.co/"
    USER_NAME = "imran+1@digitalgreen.org"
    OTP = "123456"
    HOMEPAGE_TITLE = "DataHub"
    N = 10
    ORGANIZATION_NAME = ''.join(random.choices(string.ascii_letters, k=N))

    # ORGANIZATION_EMAIL_ID:
    # generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    # generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # create the email address
    ORGANIZATION_EMAIL_ID = f"{username}@{domain}.com"

    # INVITE PARTICIPANT_EMAIL_ID:
    # generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(9))

    # generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(8))

    # create the email address
    INVITE_PARTICIPANT_EMAIL_ID = f"{username}@{domain}.com"
    ADD_INVITE_NOTE_TEXT = "I have gone through your website, I am interest to join in your organization"
    # ORGANIZATION_EMAIL_ID_2:
    # generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

    # create the email address
    ORGANIZATION_EMAIL_ID_2 = f"{username}@{domain}.com"

    # generate a random domain name
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # create the website link
    ORGANIZATION_WEBSITE_LINK = f"https://www.{domain}.com"

    ORGANIZATION_ADDRESS = "Bangalore"

    # generate a random 6-digit pin code
    PINCODE = random.randint(100000, 999999)

    N = 10
    FIRST_NAME = ''.join(random.choices(string.ascii_letters, k=N))
    N = 10
    LAST_NAME = ''.join(random.choices(string.ascii_letters, k=N))

    CONTACT_NUMBER = "9876545678"

    # generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(5))

    # create the email address
    ORGANIZATION_ROOT_USER_EMAIL_ID = f"{username}@{domain}.com"

    # generate a random username
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    # generate a random domain
    domain = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

    # create the email address
    ORGANIZATION_ROOT_USER_EMAIL_ID_2 = f"{username}@{domain}.com"

    ACCOUNT_FIRST_NAME = "Imran"
    ACCOUNT_LAST_NAME = "Shaik"
    ACCOUNT_CONTACT_NUMBER = "9876543876"

    # Update the Organization settings:

    UPDATE_ORGANIZATION_NAME = "Imran Agri Solutions"
    UPDATE_ORGANIZATION_MAIL_ID = "imranagrisolutions@gmail.com"
    UPDATE_ORGANIZATION_WEBSITE_LINK = "https://www.ImranAgriSolutions@gmail.co"
    UPDATE_ORGANIZATION_CONTACT_NUMBER = "7013733824"
    UPDATE_ORGANIZATION_ADDRESS = "Bangalore"
    UPDATE_ORGANIZATION_PINCODE = "567876"
    UPDATE_ORGANIZATION_DESCRIPTION = "Data and information can be exchanged trustworthily without the need to monetise or pay for insights."

    # Update the Policy Settings:
    N = 10
    POLICY_NAME = ''.join(random.choices(string.ascii_letters, k=N))
    POLICY_DESCRIPTION = "Warranties"

    N = 10
    UPDATE_POLICY_NAME = ''.join(random.choices(string.ascii_letters, k=N))
    UPDATE_POLICY_DESCRIPTION = "Terms and Conditions"

    # Update the Policy Settings:
    N = 12
    CATEGORY_NAME = ''.join(random.choices(string.ascii_letters, k=N))
    CATEGORY_DESCRIPTION = "SERICULTURE"

    N = 8
    ADD_SUB_CATEGORY_NAME = ''.join(random.choices(string.ascii_letters, k=N))

    N = 10
    DATAPOINT_CATEGORY_NAME = ''.join(random.choices(string.ascii_letters, k=N))

    DATAPOINT_CATEGORY_DESCRIPTION = "Testing"

    N = 9
    ADD_DATAPOINT_ATTRIBUTES = ''.join(random.choices(string.ascii_letters, k=N))


    UPDATED_DATAPOINT_CATEGORY_NAME = "DIGITALGREEN"

    N = 15
    characters = string.ascii_letters + string.digits
    CONNECTOR_NAME = ''.join(random.choices(characters, k=N))

    # N = 16
    # CONNECTOR_NAME_MySQL = ''.join(random.choices(string.ascii_letters, k=N))
    #
    # N = 13
    # CONNECTOR_NAME_Postgres = ''.join(random.choices(string.ascii_letters, k=N))

    N = 10
    characters = string.ascii_letters + string.digits
    CONNECTOR_DESCRIPTION = ''.join(random.choices(characters, k=N))

    N = 15
    characters = string.ascii_letters + string.digits
    DATASET_NAME = ''.join(random.choices(characters, k=N))

    N = 10
    characters = string.ascii_letters + string.digits
    DATASET_DESCRIPTION = ''.join(random.choices(characters, k=N))

    N = 16
    characters = string.ascii_letters + string.digits
    DATASET_NAME_MYSQL = ''.join(random.choices(characters, k=N))

    N = 10
    characters = string.ascii_letters + string.digits
    DATASET_DESCRIPTION_MYSQL = ''.join(random.choices(characters, k=N))

    N = 14
    characters = string.ascii_letters + string.digits
    DATASET_NAME_POSTGRES = ''.join(random.choices(characters, k=N))

    N = 10
    characters = string.ascii_letters + string.digits
    DATASET_DESCRIPTION_POSTGRES = ''.join(random.choices(characters, k=N))

    N = 18
    characters = string.ascii_letters + string.digits
    DATASET_NAME_REST_API = ''.join(random.choices(characters, k=N))

    N = 10
    characters = string.ascii_letters + string.digits
    DATASET_DESCRIPTION_REST_API = ''.join(random.choices(characters, k=N))
    # Upload file from Local:
    UPLOAD_FILE = "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/PXD Feed (1).xlsx"

    DATABASE_NAME_MYSQL = "suitecrm"
    USER_NAME_MYSQL = "readonly"
    PASSWORD_MYSQL = "KLxnnme.C_2GR#G"
    DATABASE_HOST_URL_MYSQL = "copiamexiconoetlparadigitalgreen.cskysn2rpea7.us-east-2.rds.amazonaws.com"
    PORT_MYSQL = "3306"

    DATABASE_NAME_POSTGRES = "postgres"
    USER_NAME_POSTGRES = "root"
    PASSWORD_POSTGRES = "xKG1A4bQ2XX3@e!8d"
    DATABASE_HOST_URL_POSTGRES = "52.64.104.116"
    PORT_POSTGRES = "5542"

    N = 12
    FILE_NAME_SQL = ''.join(random.choices(string.ascii_letters, k=N))

    N = 12
    FILE_NAME_POSTGRES = ''.join(random.choices(string.ascii_letters, k=N))

    GET_API_URL_NOAUTH = "https://datahubethstage.farmstack.co/be/microsite/admin_organization/"
    GET_API_URL_API_KEY = "https://chilly.qualix.ai/portal/scan/scan-history?from_date=15-02-2023&to_date=17-02-2023"
    GET_API_URL_BEARER = "https://datahubethstage.farmstack.co/be/datahub/dataset/v2/category/"

    API_KEY_NAME = "API-KEY"
    API_KEY_VALUE = "9zvtydnon1a6jr3ltzex"
    N = 12
    FILE_NAME_NOAUTH = ''.join(random.choices(string.ascii_letters, k=N))

    N = 12
    FILE_NAME_API_KEY = ''.join(random.choices(string.ascii_letters, k=N))

    N = 12
    FILE_NAME_BEARER = ''.join(random.choices(string.ascii_letters, k=N))

    SEARCH_INPUT_TEXT = "Dataset"

    FILTER_START_DATE = "01/01/2023"

    FILTER_END_DATE = "30/07/2023"

    UPLOAD_POLICY_FILE = "/Users/shaikmohamedimran/Desktop/CIMMYT_Data/Warranties.pdf"

    UPDATE_CATGEORY_NAME_FIELD = "Agricultural crops"
