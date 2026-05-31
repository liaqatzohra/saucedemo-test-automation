import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from test_data.checkout_data import (VALID_FIRSTNAME, VALID_LASTNAME,
                                     VALID_ZIPCODE, INVALID_CHECKOUT_DATA)
from test_data.login_data import VALID_USER, VALID_PASS
import time


class TestCheckout:

    # ==========================================
    # HELPERS
    # ==========================================

    def login_first(self, driver):
        # Step 1 - Login
        login = LoginPage(driver)
        login.login(VALID_USER, VALID_PASS)

    def go_to_checkout(self, driver):
        # Step 2 - Add product and go to checkout
        products = ProductsPage(driver)
        products.add_to_cart_first_product()
        products.open_cart()
        products.click_checkout()

    # ==========================================
    # POSITIVE TESTS
    # ==========================================

    def test_full_checkout(self, driver):
        # Arrange
        self.login_first(driver)
        self.go_to_checkout(driver)
        checkout = CheckoutPage(driver)

        # Act
        checkout.fill_checkout_form(VALID_FIRSTNAME, VALID_LASTNAME, VALID_ZIPCODE)
        checkout.click_finish()

        # Assert
        assert checkout.is_order_complete(), \
            f"Order not complete! URL: {driver.current_url}"

    def test_success_message(self, driver):
        # Arrange
        self.login_first(driver)
        self.go_to_checkout(driver)
        checkout = CheckoutPage(driver)

        # Act
        checkout.fill_checkout_form(VALID_FIRSTNAME, VALID_LASTNAME, VALID_ZIPCODE)
        checkout.click_finish()

        # Assert
        message = checkout.get_success_message()
        assert "Thank you" in message, \
            f"Expected thank you message but got: {message}"

    # ==========================================
    # NEGATIVE TESTS
    # ==========================================

    @pytest.mark.parametrize("firstname, lastname, zipcode, expected_error",
                             INVALID_CHECKOUT_DATA)
    def test_invalid_checkout_info(self, driver, firstname, lastname,
                                   zipcode, expected_error):
        # Arrange
        self.login_first(driver)
        self.go_to_checkout(driver)
        checkout = CheckoutPage(driver)

        # Act
        checkout.fill_checkout_form(firstname, lastname, zipcode)

        # Assert
        error = checkout.get_error_message()
        assert expected_error in error, \
            f"Expected '{expected_error}' but got '{error}'"