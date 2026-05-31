import pytest
from pages.login_page import LoginPage
from test_data.login_data import VALID_USER, VALID_PASS, INVALID_LOGIN_DATA


class TestLogin:

    # ==========================================
    # POSITIVE TESTS
    # ==========================================

    def test_valid_login(self, driver):
        # Arrange
        login = LoginPage(driver)

        # Act
        login.login(VALID_USER, VALID_PASS)

        # Assert
        assert login.is_login_successful(), \
            f"Login failed! Current URL: {driver.current_url}"

    # ==========================================
    # NEGATIVE TESTS
    # ==========================================

    @pytest.mark.parametrize("username, password, expected_error",
                             INVALID_LOGIN_DATA)
    def test_invalid_login(self, driver, username, password, expected_error):
        # Arrange
        login = LoginPage(driver)

        # Act
        login.login(username, password)

        # Assert
        error = login.get_error_message()
        assert expected_error in error, \
            f"Expected '{expected_error}' but got '{error}'"