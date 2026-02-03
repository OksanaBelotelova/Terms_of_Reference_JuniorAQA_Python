from selenium.webdriver.common.by import By
from pages.main_page import MainPage
import allure

class LoginPage(MainPage):

    USERNAME_FIELD = [By.ID, "user-name"]
    PASSWORD_FIELD = [By.ID, "password"]
    LOGIN_BUTTON = [By.ID, "login-button"]
    ERROR_MESSAGE = [By.XPATH, './/h3[@data-test="error"]']
    CLOSE_ICON =  [By.XPATH, './/input[contains(@class,"input_error ")]/following-sibling::*']
    CLOSE_BUTTON = [By.CLASS_NAME, "error-button"]
    
    
    def __init__(self, driver):
        super().__init__(driver)  
   

    @allure.step('Введи имя пользователя')
    def input_username(self, username):
        self.find_element(self.USERNAME_FIELD).send_keys(username)

    @allure.step('Введи пароль')
    def input_password(self, password):
        self.find_element(self.PASSWORD_FIELD).send_keys(password)

    @allure.step('Кликни на кнопку "Login"')
    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    @allure.step('Подожди пока загрузится страница')
    def wait_until_page_loaded(self):
        self.wait_until_visible(self.INVENTORY_IMAGE)

    @allure.step('Проверь что поле "username" подсвечено красным')
    def get_username_field_border(self):
        return self.find_element(self.USERNAME_FIELD).value_of_css_property('border-bottom-color')
    
    @allure.step('Проверь что поле "password" подсвечено красным')
    def get_password_field_border(self):
        return self.find_element(self.PASSWORD_FIELD).value_of_css_property('border-bottom-color')
   
    @allure.step('Проверь сообщение об ошибке')
    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    
    @allure.step('Проверь close-icon у каждого поля')
    def get_close_icon(self):
        return self.find_element(self.CLOSE_ICON)
    
    @allure.step('Проверь close button у сообщения об ошибке')
    def get_close_button(self):
        return self.find_element(self.CLOSE_BUTTON)