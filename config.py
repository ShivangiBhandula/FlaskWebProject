import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'z5NFF_J5.09Q6d.-zd1Xrfm1TgFBEV-Cz5'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'shivangicms'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'a0pauZ7h3qIYam1vUOQwuglwVwrnpwmG6+qGQEm8lJ3KbyewlTpQf3+2Y8TIOdNr6FSKCT5IwKM4clVuL+Es9A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'shivangi-cms'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'shivangi-cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'shivangi-cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'rootadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'shivangi$123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "z5NFF_J5.09Q6d.-zd1Xrfm1TgFBEV-Cz5"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/ratandeepsharma19gmail.onmicrosoft.com"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "aee015ac-a7dd-4763-b258-e3c31a6583a9"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session