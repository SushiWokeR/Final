from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_in_url(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "login is not presented in current URL"

    def should_be_login_form(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email field in login is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Password field in login is not presented"

    def should_be_register_form(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Email field in reg form is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Password in reg form field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_CONFIRMPASS), "Email field in reg form in reg form is " \
                                                                            "not presented "
