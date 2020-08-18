from Pages.BasePage import BasePage

def test_logo(get_driver):
    driver, url = get_driver
    driver.get(url)
    driver.find_element(*BasePage.LOGO)

def test_go_to_mac(get_driver):
    driver, url = get_driver
    driver.get(url)
    l1 = driver.find_element(*BasePage.LINK_TO_MENU_1)
    l2 = l1.find_element(*BasePage.LINK_TO_MAC).click()
    driver.find_element_by_id('sddd')
