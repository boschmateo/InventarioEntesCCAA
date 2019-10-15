

class EntityScraper:
    
    def __init__(self, driver, link_ref):
        self.driver = driver
        link_ref.click()
        input("fsd")
        self.driver.execute_script("window.history.go(-1)")
        input("sdfdf")