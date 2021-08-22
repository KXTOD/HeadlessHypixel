import os
from dotenv import load_dotenv

# Getting creds
load_dotenv("crd.env")
USR = os.getenv('USR')
PSS = os.getenv('PSS')

print(USR, PSS)