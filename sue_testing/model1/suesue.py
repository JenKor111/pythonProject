from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')

class SUE:

    def __init__(self):
        self.my_URL = 'https://suemade.com/'

    # Go to the website
    def open(self):
        browser.open('https://suemade.com/')
        return self

    def maximize_window(self):
        browser.driver.maximize_window()
        return self

    def account(self):
        browser.element('.but_nav.but_profile').click()
        return self

    #Authorization
    def authorization(self):
        browser.element('[name="login"]').type('evgeniyaakornienko@gmail.com').press_enter()
        browser.element('[name="pass"]').type('12345q').press_enter()
        browser.element('.log-column-left .but').click()
        return self

    #Go to the Catalog tab
    def catalog(self):
        browser.element('#dd_info > div > div.nav > ul > li:nth-child(1)').click()
        return self

    #Go to the face cosmetics tab
    def inset(self):
        browser.element('[name="for-face"]').click()
        return self

    #Product selection Micellar water with filters
    def product(self):
        browser.element('#uid_item_71420 > a > h3').click()
        browser.element('#uid_product > div > div.base > div:nth-child(6) > span.counter > span > i:nth-child(3)').click()
        browser.element('#uid_product > div > div.base > div:nth-child(6) > span.price_multi > span:nth-child(2)').click()
        return self

    #look at the feedback and look at the method of use and like the product
    def characteristics(self):
        browser.element('[href="#prod_comment"]').click()
        browser.element('[href="#prod_recept_block"]').click()
        browser.element('a.but_fav').click()
        return self

    #Buy goods
    def buy(self):
        browser.element('a.avail_1').click()
        return self

    #Check the availability of goods in the cart
    def check(self):
        search_results_text = browser.all('[href="cart/"]')
        assert len(search_results_text) > 0, 'No found'
        return self

    #Go to the main page and click on the search button and enter the product and add it to the cart +
    def search_product(self, suemade: str):
        browser.element('body > div.nav_bar > div > a.logo').click()
        browser.element('body > div.nav_bar > div > a.but_nav.but_search').click()
        browser.element('[name="query"]').type(suemade).press_enter()
        browser.element('#uid_item_72052 > a > span.block > span.add_to_cart.avail_3').click()
        search_results_text = browser.all('#uid_item_72052 > a > h3')
        assert len(search_results_text) > 0, 'No found'
        return self

    #Check the availability of goods in the cart
    def check1(self):
        search_results_text = browser.all('[href="cart/"]')
        assert len(search_results_text) > 0, 'No found'
        browser.element('[href="cart/"]').click()
        return self

    #Go to the contacts tab
    def contacts(self):
        browser.element('#dd_info > div > div.nav > ul > li:nth-child(2) > a').click()
        browser.element('[name="contact/"]').click()
        return self

    #Go to the profile and edit the data
    def profile1(self):
        browser.element('[href="profile/"]').click()
        browser.element('#uid_profile_data > div > a').click()
        browser.element('#block_delivery_city > span > a').click()
        return self

    def profile2(self):
        browser.element('[name="locality"]').type('Кременчук').press_enter()
        browser.element('#uid_popup_profile_edit > form > a').double_click()
        return self

    #Exit
    def exit(self):
        browser.element('body > div.main > div > div.profile > a').click()
        return self

    #Re-authorization (negative test)
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

    #Feedback
    def response(self):
        browser.element('[href="reviews/"]').click()
        browser.element('#prod_comment > a:nth-child(1)').click()
        browser.element('[name="author"]').type('111').press_enter()
        browser.element('[name="email"]').type('evgen').press_enter()
        browser.element('[name="text"]').type('Гарний сайт').press_enter()
        browser.element('[title="Рекомендую"]').click()
        return self

    def response1(self):
        browser.element('.edit .but').click()
        browser.element('.popup-close').click()
        return self

    #Еransition from the site to the YouTube page
    def youtube(self):
        browser.element('[href="https://www.youtube.com/channel/UCukwNr6G-K1pmBbcbSKgarg?view_as=subscriber"]').click()
        return self





