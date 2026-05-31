import pytest
from pages.login_page import LoginPage
from pages.navbar_page import NavbarPage
from test_data.login_data import VALID_USER, VALID_PASS


class TestLogout:

    # ==========================================
    # HELPER
    # ==========================================

    def login_first(self, driver):
        login = LoginPage(driver)
        login.login(VALID_USER, VALID_PASS)

    # ==========================================
    # POSITIVE TESTS
    # ==========================================

    def test_logout(self, driver):
        # Arrange
        self.login_first(driver)
        navbar = NavbarPage(driver)

        # Act
        navbar.logout()

        # Assert
        assert navbar.is_logged_out(), \
            f"Logout failed! Current URL: {driver.current_url}"