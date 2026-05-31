import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from test_data.login_data import VALID_USER, VALID_PASS


class TestProducts:

    # ==========================================
    # HELPER - Login before testing products
    # ==========================================

    def login_first(self, driver):
        login = LoginPage(driver)
        login.login(VALID_USER, VALID_PASS)


    # ==========================================
    # POSITIVE TESTS
    # ==========================================

    def test_products_page_loads(self, driver):
        # Arrange
        self.login_first(driver)
        products = ProductsPage(driver)

        # Assert
        assert products.is_on_products_page(), \
            f"Not on products page! URL: {driver.current_url}"

    def test_add_to_cart(self, driver):
        # Arrange
        self.login_first(driver)
        products = ProductsPage(driver)

        # Act
        products.add_to_cart()

        # Assert
        assert products.get_cart_count() == 1, \
            f"Expected 1 but got {products.get_cart_count()}"

    def test_remove_from_cart(self, driver):
        # Arrange
        self.login_first(driver)
        products = ProductsPage(driver)

        # Act
        products.add_to_cart()
        products.remove_from_cart()

        # Assert
        assert products.get_cart_count() == 0, \
            f"Expected 0 but got {products.get_cart_count()}"

    def test_cart_count_increases(self, driver):
        # Arrange
        self.login_first(driver)
        products = ProductsPage(driver)

        # Act - add TWO DIFFERENT products
        products.add_to_cart_first_product()
        products.add_to_cart_second_product()

        # Assert
        assert products.get_cart_count() == 2, \
            f"Expected 2 but got {products.get_cart_count()}"