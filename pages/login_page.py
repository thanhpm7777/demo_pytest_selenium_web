# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://localhost:4443/c/main"
    USERNAME = (By.ID, "ext-gen1180")
    PASSWORD = (By.ID, "ext-gen1185")
    SIGN_IN = (By.ID, "augmentedButton-1047")
    FORGOT = (By.LINK_TEXT, "Forgot the password?")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='ext-gen1174']")
    LOGOUT_BUTTON=(By.ID, "ext-gen1952")

    # ----- ACTIONS -----
    def open_page(self):
        self.open(self.URL)

    def username_field(self):
        return self.wait.until(EC.presence_of_element_located(self.USERNAME))

    def pass_field(self):
        return self.wait.until(EC.presence_of_element_located(self.PASSWORD))

    def button_sign_in(self):
        return self.wait.until(EC.presence_of_element_located(self.SIGN_IN))


    def enter_username(self, email):
        self.type_text(self.USERNAME, email)

    def enter_password(self, password):
        self.type_text(self.PASSWORD, password)

    def click_sign_in(self):
        self.click(self.SIGN_IN)

    def login_page(self, username, password):
        self.open_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_sign_in()

    def is_logout_displayed(self):
        try:
            return self.is_displayed(self.LOGOUT_BUTTON)
        except Exception:
            return False

    def is_sign_in_disabled(self):
        btn = self.button_sign_in()
        disabled = btn.get_attribute("disabled")
        aria_disabled = btn.get_attribute("aria-disabled")
        return (disabled is not None and disabled.lower() in ("true", "disabled")) or (aria_disabled == "true")

    def get_error_message(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return element.text
        except:
            return ""

    def forgot_visible(self):
        return self.is_displayed(self.FORGOT)


    def is_password_masked(self):
        t = self.get_attribute(self.PASSWORD, "type")
        return t == "password"