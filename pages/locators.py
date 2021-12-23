from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONF_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESS_ADD_TO_BASKET_MESSAGE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    ORDER_NAME_ON_PAGE = (
        By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    ORDER_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ORDER_PRICE_ON_PAGE = (
        By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    ORDER_PRICE_IN_BASKET = (
        By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (
        By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
