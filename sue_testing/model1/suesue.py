from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')

class SUE:

    def __init__(self):
        self.my_URL = 'https://suemade.com/'

    def open(self):
        browser.open('https://suemade.com/')
        return self

    def maximize_window(self):
        browser.driver.maximize_window()
        return self

    def account(self):
        browser.element('.but_nav.but_profile').click()
        return self

    def authorization(self):
        browser.element('[name="login"]').type('evgeniyaakornienko@gmail.com').press_enter()
        browser.element('[name="pass"]').type('12345q').press_enter()
        browser.element('.log-column-left .but').click()
        return self

    def catalog(self):
        browser.element('#dd_info > div > div.nav > ul > li:nth-child(1)').click()
        return self

    def inset(self):
        browser.element('[name="for-face"]').click()
        return self

    def product(self):
        browser.element('#uid_item_71420 > a > h3').click()
        browser.element('#uid_product > div > div.base > div:nth-child(6) > span.counter > span > i:nth-child(3)').click()
        browser.element('#uid_product > div > div.base > div:nth-child(6) > span.price_multi > span:nth-child(2)').click()
        return self

    def characteristics(self):
        browser.element('[href="#prod_comment"]').click()
        browser.element('[href="#prod_recept_block"]').click()
        browser.element('a.but_fav').click()
        return self

    def buy(self):
        browser.element('a.avail_1').click()
        return self

    def check(self):
        search_results_text = browser.all('[href="cart/"]')
        assert len(search_results_text) > 0, 'No found'
        browser.element('[href="cart/"]').click()
        return self

    def delete_product(self):
        browser.element('.but_delete').click()
        return self

    def main_page(self):
        browser.element('#page_cart > div.empty > a').click()
        browser.element('body > div.nav_bar > div > a.but_nav.but_search').click()
        return self

    def search_product(self, suemade: str):
        browser.element('[name="query"]').type(suemade).press_enter()
        browser.element('#uid_item_72052 > a > span.block > span.add_to_cart.avail_3').click()
        return self

    def check1(self):
        search_results_text = browser.all('[href="cart/"]')
        assert len(search_results_text) > 0, 'No found'
        browser.element('[href="cart/"]').click()
        return self

    def contacts(self):
        browser.element('#dd_info > div > div.nav > ul > li:nth-child(2) > a').click()
        browser.element('[name="contact/"]').click()
        return self

    def profile1(self):
        browser.element('[href="profile/"]').click()
        browser.element('#uid_profile_data > div > a').click()
        browser.element('#block_delivery_city > span > a').click()
        return self

    def profile2(self):
        browser.element('[name="locality"]').type('Кременчук').press_enter()
        browser.element('#uid_popup_profile_edit > form > a').double_click()
        return self

    def exit(self):
        browser.element('body > div.main > div > div.profile > a').click()
        return self

    def reentry(self):
        browser.element('.but_nav.but_profile').click()
        return self

    def incorrect_password(self):
        browser.element('[name="pass"]').type('12345').press_enter()
        browser.element('.log-column-left .but').click()
        return self

    def correct_password(self):
        browser.element('[name="pass"]').type('q').press_enter()
        browser.element('.log-column-left .but').click()
        return self

    def youtube(self):
        browser.element('[href="https://www.youtube.com/channel/UCukwNr6G-K1pmBbcbSKgarg?view_as=subscriber"]').click()
        return self



