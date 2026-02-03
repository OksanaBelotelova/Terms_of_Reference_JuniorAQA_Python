import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import URL, TestData, ErrorMessages, Styles

class TestLoginPage:

    @allure.title("Успешный логин")
    @allure.description("При вводе корректных данных юезер успешно логинится и попадает на главную страницу, все элементы главной страницы отображаются корректно")
    @pytest.mark.parametrize("element", MainPage.ELEMENTS_LIST)
    def test_successful_login(self, driver, element):
        login = LoginPage(driver)
        
        login.input_username(TestData.successful_username)
        login.input_password(TestData.password)
        login.click_login_button()
        login.wait_until_page_loaded()
     
        actual_url = login.get_current_page()
        expected_url = URL.main_url
        element = login.check_elements(element)
        
        assert actual_url == expected_url 
        assert element.is_displayed()


    @allure.title("Логин с неверным паролем")
    @allure.description("При вводе неверного пароля, появляется информационное сообщение, поля для ввода имени и пароля подсвечены красным")
    def test_login_with_wrong_password(self, driver):
        login = LoginPage(driver)
        
        login.input_username(TestData.successful_username)
        login.input_password(TestData.wrong_password)
        login.click_login_button()  

        username_is_highlighted  = login.get_username_field_border()
        password_is_highlighted = login.get_password_field_border()
        border_color = Styles.red_border_color
        close_icons_for_username_and_password_fields = login.get_close_icon()
        close_button = login.get_close_button()
        error_message = login.get_error_message()
        expected_error_message = ErrorMessages.wrong_data_msg
       
        assert username_is_highlighted == border_color
        assert password_is_highlighted == border_color
        assert close_icons_for_username_and_password_fields.is_displayed()
        assert error_message == expected_error_message
        assert close_button.is_displayed()


    @allure.title("Логин заблокированного пользователя")
    @allure.description("При логине заблокированного юзера, появляется информационное сообщение, поля для ввода имени и пароля подсвечены красным")
    def test_login_in_locked_out_user(self, driver):
        login = LoginPage(driver)
        
        login.input_username(TestData.locked_out_user)
        login.input_password(TestData.password)
        login.click_login_button()
       
        username_is_highlighted = login.get_username_field_border()
        password_is_highlighted = login.get_password_field_border()
        border_color = Styles.red_border_color
        close_icons_for_username_and_password_fields = login.get_close_icon()
        close_button = login.get_close_button()
        error_message = login.get_error_message()
        expected_error_message = ErrorMessages.locked_out_user_msg
       
        assert username_is_highlighted == border_color
        assert password_is_highlighted == border_color
        assert close_icons_for_username_and_password_fields.is_displayed()
        assert error_message == expected_error_message
        assert close_button.is_displayed()


    @allure.title("Логин с пустыми полями")
    @allure.description("При логине без ввода данных, появляется информационное сообщение, поля для ввода имени и пароля подсвечены красным")
    def test_login_with_empty_fields(self, driver):
        login = LoginPage(driver)

        login.click_login_button()

        username_is_highlighted = login.get_username_field_border()
        password_is_highlighted = login.get_password_field_border()
        border_color = Styles.red_border_color
        close_icons_for_username_and_password_fields = login.get_close_icon()
        close_button = login.get_close_button()
        error_message = login.get_error_message()
        expected_error_message = ErrorMessages.username_is_required_msg

        assert username_is_highlighted == border_color
        assert password_is_highlighted == border_color
        assert close_icons_for_username_and_password_fields.is_displayed()
        assert error_message == expected_error_message
        assert close_button.is_displayed()

    
    @allure.title("Логин при задержке соединения")
    @allure.description("При логине, происходит переход на главную траницу, которая открывается несмотря на возможные задержки")
    @pytest.mark.parametrize("element", MainPage.ELEMENTS_LIST)
    def test_login_with_performance_glitch_user(self, driver, element):
        login = LoginPage(driver)
        
        login.input_username(TestData.performance_glitch_user)
        login.input_password(TestData.password)
        login.click_login_button()
        login.wait_until_page_loaded()

        actual_url = login.get_current_page()
        expected_url = URL.main_url
        element = login.check_elements(element)
        
        assert actual_url == expected_url 
        assert element.is_displayed()