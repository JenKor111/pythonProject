import time

from selene import Browser, by
from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.conditions import have

def test_sue():
    #Go to the website
    browser.open('https://suemade.com/')
    browser.driver.maximize_window()
    browser.element('.but_nav.but_profile').click()
    time.sleep(2)
    #Authorization
    browser.element('[name="login"]').type('evgeniyaakornienko@gmail.com').press_enter()
    browser.element('[name="pass"]').type('12345q').press_enter()
    browser.element('.log-column-left .but').click()
    time.sleep(2)
    #Go to the Catalog tab
    browser.element('#dd_info > div > div.nav > ul > li:nth-child(1)').click()
    time.sleep(2)
    #Go to the face cosmetics tab
    browser.element('[name="for-face"]').click()
    time.sleep(2)
    #Product selection Micellar water with filters
    browser.element('#uid_item_71420 > a > h3').click()
    time.sleep(2)
    browser.element('#uid_product > div > div.base > div:nth-child(6) > span.counter > span > i:nth-child(3)').click()
    time.sleep(2)
    browser.element('#uid_product > div > div.base > div:nth-child(6) > span.price_multi > span:nth-child(2)').click()
    time.sleep(2)
    #look at the feedback
    browser.element('[href="#prod_comment"]').click()
    time.sleep(2)
    #Look at the method of use
    browser.element('[href="#prod_recept_block"]').click()
    time.sleep(2)
    #Like the product
    browser.element('a.but_fav').click()
    time.sleep(2)
    #Buy goods
    browser.element('a.avail_1').click()
    time.sleep(2)
    #Check the availability of goods in the cart
    search_results_text = browser.all('[href="cart/"]')
    assert len(search_results_text) > 0, 'No found'
    time.sleep(2)
    #Go to the main page
    browser.element('body > div.nav_bar > div > a.logo').click()
    time.sleep(2)
    #Click on the search button and enter the product and add it to the cart
    browser.element('body > div.nav_bar > div > a.but_nav.but_search').click()
    time.sleep(2)
    browser.element('[name="query"]').type('Гель для вмивання Prebiotic').press_enter()
    time.sleep(2)
    browser.element('#uid_item_72052 > a > span.block > span.add_to_cart.avail_3').click()
    search_results_text = browser.all('#uid_item_72052 > a > h3')
    assert len(search_results_text) > 0, 'No found'
    time.sleep(2)
    #Check the availability of goods in the cart
    search_results_text = browser.all('[href="cart/"]')
    assert len(search_results_text) > 0, 'No found'
    time.sleep(2)
    #Go to the contacts tab
    browser.element('#dd_info > div > div.nav > ul > li:nth-child(2) > a').click()
    time.sleep(2)
    browser.element('[name="contact/"]').click()
    time.sleep(2)
    #Go to the profile and edit the data
    browser.element('[href="profile/"]').click()
    time.sleep(3)
    browser.element('#uid_profile_data > div > a').click()
    time.sleep(2)
    browser.element('#block_delivery_city > span > a').click()
    time.sleep(2)
    browser.element('[name="locality"]').type('Кременчук').press_enter()
    time.sleep(3)
    browser.element('#uid_popup_profile_edit > form > a').double_click()
    time.sleep(5)
    #Exit
    browser.element('body > div.main > div > div.profile > a').click()
    time.sleep(5)
    #Re-authorization (negative test)
    browser.element('.but_nav.but_profile').click()
    browser.element('[name="pass"]').type('12345').press_enter()
    browser.element('.log-column-left .but').click()
    browser.element('[name="pass"]').type('q').press_enter()
    browser.element('.log-column-left .but').click()
    time.sleep(5)
    #Feedback
    browser.element('[href="reviews/"]').click()
    browser.element('#prod_comment > a:nth-child(1)').click()
    browser.element('[name="author"]').type('111').press_enter()
    browser.element('[name="email"]').type('evgen').press_enter()
    browser.element('[name="text"]').type('Гарний сайт').press_enter()
    time.sleep(2)
    browser.element('[title="Рекомендую"]').click()
    time.sleep(2)
    browser.element('.edit .but').click()
    browser.element('.popup-close').click()
    time.sleep(3)
    #Еransition from the site to the YouTube page
    browser.element('[href="https://www.youtube.com/channel/UCukwNr6G-K1pmBbcbSKgarg?view_as=subscriber"]').click()













