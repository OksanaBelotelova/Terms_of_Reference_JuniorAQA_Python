from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class MainPage:
    
    LOGO = [By.CLASS_NAME, "app_logo"]
    MENU_BUTTON = [By.CLASS_NAME, "bm-icon"]
    SHOPPING_CART = [By.CLASS_NAME, "shopping_cart_link"]
    INVENTORY_LIST = [By.XPATH,'.//div[@class= "inventory_item"]']
    PRODUCTS_TITLE = [By.CLASS_NAME, "title"]
    SORT_MENU = [By.CLASS_NAME, "product_sort_container"]
    ADD_TO_CART_BUTTON = [By.XPATH, './/button[text()="Add to cart"]']
    PRICE = [By.CLASS_NAME, "inventory_item_price"]
    INVENTORY_NAME = [By.CLASS_NAME, "inventory_item_name"]
    INVENTORY_IMAGE = [By.XPATH, './/img[@class = "inventory_item_img"]']
    INVENTORY_DESCRIPTION = [By.CLASS_NAME, "inventory_item_desc"]
    ELEMENTS_LIST = [LOGO, MENU_BUTTON,SHOPPING_CART, PRODUCTS_TITLE, SORT_MENU,INVENTORY_LIST, ADD_TO_CART_BUTTON, PRICE, INVENTORY_NAME, INVENTORY_IMAGE, INVENTORY_DESCRIPTION]
    
    
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, element):
        return self.driver.find_element(*element)

    def wait_until_visible(self, element, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located((element)))
        
    @allure.step('Проверь URL')
    def get_current_page(self):
        return self.driver.current_url
    
    @allure.step('Проверь отображение элементов на странице')
    def check_elements(self, element):
        return self.find_element(element)
    
 