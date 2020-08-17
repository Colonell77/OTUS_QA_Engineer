

def test_(get_driver):
    driver = get_driver[0]
    url = get_driver[1]
    driver.get(url)
    assert driver.title == 'Интернет магазин Opencart "Русская сборка"'
