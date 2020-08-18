from selenium.webdriver.common.by import By


class BasePage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    LINK_TO_MENU_1 = (By.CSS_SELECTOR, '#menu href')
    LINK_TO_MAC = (By.CSS_SELECTOR, 'li href')

