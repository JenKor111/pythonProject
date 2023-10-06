import time

from selene import browser
from selenium.webdriver.common.alert import Alert

from sue_testing.model1 import suemade

def test_sue():
    suemade.open()
    suemade.maximize_window()
    time.sleep(2)
    suemade.account()
    time.sleep(2)
    suemade.authorization()
    time.sleep(2)
    suemade.catalog()
    suemade.inset()
    suemade.product()
    suemade.characteristics()
    time.sleep(3)
    suemade.buy()
    time.sleep(3)
    suemade.check()
    suemade.delete_product()
    time.sleep(2)
    suemade.main_page()
    time.sleep(2)
    suemade.search_product('Гель для вмивання Prebiotic')
    time.sleep(2)
    suemade.check1()
    suemade.contacts()
    time.sleep(2)
    suemade.profile1()
    time.sleep(3)
    suemade.profile2()
    time.sleep(2)
    suemade.exit()
    time.sleep(2)
    suemade.reentry()
    time.sleep(2)
    suemade.incorrect_password()
    time.sleep(2)
    suemade.correct_password()
    time.sleep(2)
    suemade.youtube()
    time.sleep(5)







