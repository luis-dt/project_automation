import sys
import os
from github import Github
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github('github token').get_user()
    user.create_repo(folderName)
    logger.info("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
