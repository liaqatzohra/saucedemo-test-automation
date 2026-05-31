from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # --- Locators ---
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME      = (By.ID, "first-name")
    LAST_NAME       = (By.ID, "last-name")
    ZIP_CODE        = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON   = (By.ID, "finish")
    CANCEL_BUTTON   = (By.ID, "cancel")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, ".error-message-container")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()

    def enter_firstname(self, firstname):
        field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        field.clear()
        field.send_keys(firstname)

    def enter_lastname(self, lastname):
        field = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        field.clear()
        field.send_keys(lastname)

    def enter_zipcode(self, zipcode):
        field = self.wait.until(
            EC.visibility_of_element_located(self.ZIP_CODE)
        )
        field.clear()
        field.send_keys(zipcode)

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        button.click()

    def click_finish(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )
        button.click()

    def click_cancel(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        )
        button.click()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text

    def get_success_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return message.text

    def is_order_complete(self):
        return "checkout-complete" in self.driver.current_url

    def fill_checkout_form(self, firstname, lastname, zipcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.click_continue()