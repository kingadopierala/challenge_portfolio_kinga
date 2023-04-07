import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = '/Users/user/Desktop/challenge_portfolio_kinga/drivers/chromedriver'
service = Service(DRIVER_PATH)
IMPLICITLY_WAIT = 40
driver = webdriver.Chrome(service=service)


class Test(unittest.TestCase):


    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"