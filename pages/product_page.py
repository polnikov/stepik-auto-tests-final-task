import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "Login link is not presented"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_good_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE),\
            "You did not add order to basket"

    def check_order_name_in_basket(self):
        assert self.text_from_element(*ProductPageLocators.ORDER_NAME_ON_PAGE) == self.text_from_element(*ProductPageLocators.ORDER_NAME_IN_MESSAGE),\
            "Order in basket not correct"

    def check_order_price_in_basket(self):
        assert self.text_from_element(*ProductPageLocators.ORDER_PRICE_ON_PAGE) == self.text_from_element(*ProductPageLocators.ORDER_PRICE_IN_BASKET),\
            "Order price in basket not correct"

    def should_not_be_good_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_good_message_all_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MESSAGE), \
            "Success message did not dissapear"
