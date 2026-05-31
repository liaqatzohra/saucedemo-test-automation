import pytest
import allure  # allure library for beautiful reports
from pages.login_page import LoginPage
from test_data.login_data import VALID_USER, VALID_PASS, INVALID_LOGIN_DATA


# @allure.feature = groups all tests in this class under "Login" in the report
# Think of it like a folder name in the report
@allure.feature("Login")
class TestLogin:

    # ==========================================
    # HELPER
    # ==========================================

    def login_first(self, driver):
        login = LoginPage(driver)
        login.login(VALID_USER, VALID_PASS)

    # ==========================================
    # POSITIVE TESTS
    # ==========================================

    # @allure.story = sub folder inside feature
    # Login → Valid Login (like folder → subfolder)
    @allure.story("Valid Login")

    # @allure.severity = how important is this test?
    # CRITICAL = if this breaks, major feature is broken
    # Other options: BLOCKER, NORMAL, MINOR, TRIVIAL
    @allure.severity(allure.severity_level.CRITICAL)

    def test_valid_login(self, driver):

        # allure.step = shows each action as a step in the report
        # Report will show: "Step 1 - Open login page"
        with allure.step("Open login page"):
            # Arrange - create login page object
            login = LoginPage(driver)

        # Report will show: "Step 2 - Login with valid credentials"
        with allure.step("Login with valid credentials"):
            # Act - perform login
            login.login(VALID_USER, VALID_PASS)

        # Report will show: "Step 3 - Verify redirected to products page"
        with allure.step("Verify redirected to products page"):
            # Assert - check login was successful
            assert login.is_login_successful(), \
                f"Login failed! Current URL: {driver.current_url}"

    # ==========================================
    # NEGATIVE TESTS
    # ==========================================

    @allure.story("Invalid Login")

    # NORMAL = regular importance, not critical but still important
    @allure.severity(allure.severity_level.NORMAL)

    # parametrize runs this test multiple times with different data
    # each tuple from INVALID_LOGIN_DATA becomes one test run
    @pytest.mark.parametrize("username, password, expected_error",
                             INVALID_LOGIN_DATA)

    def test_invalid_login(self, driver, username, password, expected_error):

        with allure.step("Open login page"):
            # Arrange
            login = LoginPage(driver)

        # f-string shows actual values in report
        # e.g. "Login with username='wrong_user' password='secret_sauce'"
        with allure.step(f"Login with username='{username}' password='{password}'"):
            # Act
            login.login(username, password)

        with allure.step(f"Verify error message contains '{expected_error}'"):
            # Assert - read error and check it contains expected text
            error = login.get_error_message()
            assert expected_error in error, \
                f"Expected '{expected_error}' but got '{error}'"