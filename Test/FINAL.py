import time

from selene import Browser, by
from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.conditions import have

def test_sue():
    browser.open('https://suemade.com/')
    browser.element('.but_nav.but_profile').click()
    time.sleep(2)
    #Авторизація
    browser.element('[name="login"]').type('evgeniyaakornienko@gmail.com').press_enter()
    browser.element('[name="pass"]').type('12345q').press_enter()
    browser.element('.log-column-left .but').click()
    time.sleep(2)
    #Перехід на вкладку Каталог
    browser.element('#dd_info > div > div.nav > ul > li:nth-child(1)').click()
    time.sleep(2)
    #Перехід на вкладку косметика для обличчя
    browser.element('[name="for-face"]').click()
    time.sleep(2)
    #Вибір товару Міцелярна вода з фільтрами
    browser.element('#uid_item_71420 > a > h3').click()
    time.sleep(2)
    browser.element('#uid_product > div > div.base > div:nth-child(6) > span.counter > span > i:nth-child(3)').click()
    time.sleep(2)
    browser.element('#uid_product > div > div.base > div:nth-child(6) > span.price_multi > span:nth-child(2)').click()
    time.sleep(2)
    #Дивимось відгуки
    browser.element('[href="#prod_comment"]').click()
    time.sleep(2)
    #Дивимось на спосіб використання
    browser.element('[href="#prod_recept_block"]').click()
    time.sleep(2)
    #Натиснути вподойбайку на товар
    browser.element('a.but_fav').click()
    time.sleep(2)
    #Покупаємо товар
    browser.element('a.avail_1').click()
    time.sleep(2)
    #Перевірка наявності товару в кошику + натискаємо на кошик
    search_results_text = browser.all('[href="cart/"]')
    assert len(search_results_text) > 0, 'No found'
    time.sleep(2)
    browser.element('[href="cart/"]').click()
    time.sleep(2)
    #Видалити товар з кошику
    browser.element('.but_delete').click()
    time.sleep(2)
    #Перейти на головну сторінку
    browser.element('#page_cart > div.empty > a').click()
    time.sleep(2)
    #Натискаємо на кнопку пошук та вводимо товар та додаємо у кошик
    browser.element('body > div.nav_bar > div > a.but_nav.but_search').click()
    time.sleep(2)
    browser.element('[name="query"]').type('Гель для вмивання Prebiotic').press_enter()
    time.sleep(2)
    browser.element('#uid_item_72052 > a > span.block > span.add_to_cart.avail_3').click()
    time.sleep(2)
    # Перевірка наявності товару в кошику
    search_results_text = browser.all('[href="cart/"]')
    assert len(search_results_text) > 0, 'No found'
    time.sleep(2)
    #перейти на вкладку контакти, продивитись
    browser.element('#dd_info > div > div.nav > ul > li:nth-child(2) > a').click()
    time.sleep(2)
    browser.element('[name="contact/"]').click()
    time.sleep(2)
    #Переходимо в профіль та редагуємо дані
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
    #Вихід
    browser.element('body > div.main > div > div.profile > a').click()
    time.sleep(5)
    #Негативний тест
def test_negsue():
    browser.open('https://suemade.com/')
    browser.element('.but_nav.but_profile').click()
    time.sleep(2)
    # Авторизація
    browser.element('[name="login"]').type('evgeniyakornienk@gmail.com').press_enter()
    browser.element('[name="pass"]').type('12345').press_enter()
    browser.element('.log-column-left .but').click()
    time.sleep(5)













