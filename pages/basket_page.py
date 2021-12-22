from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY),\
            "Basket is not empty"

    def basket_is_not_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY),\
            "Basket is not empty"
