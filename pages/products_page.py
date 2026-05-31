from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    # --- Locators ---
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test*='add-to-cart']")
    REMOVE_BUTTON      = (By.CSS_SELECTOR, "[data-test*='remove']")
    CART_BADGE         = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_ICON          = (By.ID, "shopping_cart_container")
    CART_OPEN          =(By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON    = (By.ID, "checkout")
    ADD_TO_CART_BACKPACK = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")
    ADD_TO_CART_BIKE_LIGHT = (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.ADD_TO_CART_BUTTON)
        )
        # Scroll button into view first
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", button
        )
        # Then click
        self.driver.execute_script(
            "arguments[0].click();", button
        )
        print("✅ Clicked add to cart!")

    def remove_from_cart(self):
        button = self.wait.until(
            EC.presence_of_element_located(self.REMOVE_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", button
        )
        self.driver.execute_script(
            "arguments[0].click();", button
        )
        print("✅ Clicked remove!")

    def get_cart_count(self):
        try:
            badge = self.wait.until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            count = int(badge.text)
            print(f"✅ Cart count: {count}")
            return count
        except Exception as e:
            print(f"❌ Badge not found: {e}")
            return 0

    def open_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CART_OPEN)
        )
        button.click()

    def click_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        button.click()

    def is_on_products_page(self):
        return "inventory" in self.driver.current_url

    def add_to_cart_first_product(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK)
        )
        button.click()

    def add_to_cart_second_product(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BIKE_LIGHT)
        )
        button.click()