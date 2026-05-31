from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavbarPage:
    # --- Locators ---
    MENU_BUTTON  = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK  = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        button.click()

    def click_logout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        button.click()

    def is_logged_out(self):
        return self.driver.current_url == "https://www.saucedemo.com/"

    def logout(self):
        self.open_menu()
        self.click_logout()