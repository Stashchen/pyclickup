import os, sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, 'src')
sys.path.append(SOURCE_PATH)

os.environ["CLICKUP_AUTH_TOKEN"] = "some token"
