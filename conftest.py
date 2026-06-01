import pytest
from selenium import webdriver

# Chrome needs its own Service class
from selenium.webdriver.chrome.service import Service as ChromeService

# Safari needs its own Service class
# We rename both to avoid naming conflict
from selenium.webdriver.safari.service import Service as SafariService

# Automatically downloads correct chromedriver for your Chrome version
from webdriver_manager.chrome import ChromeDriverManager

# Our custom screenshot utility
from utilities.screenshot import take_screenshot


# ============================================================
# pytest_addoption = adds custom command line options to pytest
# This function is special — pytest calls it automatically
# It lets us type things like: pytest --browser=safari
# ============================================================
def pytest_addoption(parser):

    # --keep-open option
    # action="store_true" means: if flag present → True, if not → False
    # default=False means: by default browser closes immediately
    parser.addoption(
        "--keep-open",
        action="store_true",
        default=False,
        help="Keep browser open after each test"
    )

    # --headless option
    # When passed: pytest --headless → runs Chrome invisibly
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser invisibly in background"
    )

    # --browser option
    # action="store" means: store whatever value user types
    # default="chrome" means: if not specified, use Chrome
    # Usage: pytest --browser=safari OR pytest --browser=chrome
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or safari"
    )


# ============================================================
# driver fixture = sets up and tears down browser for every test
# @pytest.fixture = tells pytest this is a setup helper
# request = special pytest object that reads command line options
# ============================================================
@pytest.fixture
def driver(request):

    # --- SETUP ---

    # Read which browser user wants from command line
    # e.g. pytest --browser=safari → browser = "safari"
    # e.g. pytest → browser = "chrome" (default)
    browser = request.config.getoption("--browser")

    # ============================================================
    # SAFARI BROWSER SETUP
    # ============================================================
    if browser == "safari":
        # Safari uses Apple's built in SafariDriver
        # No options needed — Apple handles everything
        # Must run: sudo safaridriver --enable (done once)
        driver = webdriver.Safari()
        print("🌐 Running on Safari")

    # ============================================================
    # CHROME BROWSER SETUP (default)
    # ============================================================
    else:
        # Create empty Chrome settings object
        options = webdriver.ChromeOptions()

        # Hide the flag that tells websites "I am a robot"
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Remove "Chrome is being controlled by automated software" banner
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Disable Chrome's built in automation extension websites can detect
        options.add_experimental_option("useAutomationExtension", False)

        # Disable "Save password?" popup after login
        options.add_argument("--disable-save-password-bubble")

        # Disable all browser notifications
        options.add_argument("--disable-notifications")

        # Use incognito mode = fresh browser every time
        # No saved passwords, no history, no popups!
        # This fixed our "Change your password" popup problem
        options.add_argument("--incognito")

        # Disable password manager and notifications via Chrome preferences
        options.add_experimental_option("prefs", {
            # Don't offer to save passwords
            "credentials_enable_service": False,
            # Disable password manager completely
            "profile.password_manager_enabled": False,
            # Block all notifications (2 = block)
            "profile.default_content_setting_values.notifications": 2
        })

        # Read --headless flag from command line
        headless = request.config.getoption("--headless")

        if headless:
            # Run Chrome without opening a visible window
            options.add_argument("--headless")
            # Set window size even in headless mode
            # Without this some elements might not be visible
            options.add_argument("--window-size=1920,1080")

        # Open Chrome with all our settings applied
        # ChromeDriverManager().install() = auto downloads correct chromedriver
        # Service() = manages starting and stopping chromedriver process
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        print("🌐 Running on Chrome")

    # ============================================================
    # COMMON SETUP FOR ALL BROWSERS
    # ============================================================

    # Implicit wait = wait up to 10 seconds for any element before failing
    # Set once here → applies to every element search in every test
    driver.implicitly_wait(10)

    # Set browser window to full HD size
    # Important! Small window = some elements hidden = tests fail
    driver.set_window_size(1920, 1080)

    # Maximize window to fill screen
    driver.maximize_window()

    # Open SauceDemo website
    # Every test starts here automatically
    driver.get("https://www.saucedemo.com")

    # yield = pause here and give driver to the test
    # Test runs here
    # After test finishes, code below yield runs automatically
    yield driver

    # ============================================================
    # TEARDOWN - runs after every test automatically
    # ============================================================

    # Check if --keep-open flag was passed
    keep_open = request.config.getoption("--keep-open")

    if keep_open:
        import time
        # Keep browser open for 10 seconds so you can see what happened
        time.sleep(10)

    # Close browser completely and end chromedriver process
    # Always runs whether test passed or failed
    driver.quit()


# ============================================================
# pytest_runtest_makereport = special pytest hook
# Runs automatically after every test
# We use it to take screenshots when tests fail
# ============================================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # outcome = yield lets us wrap around the test execution
    # Test runs at this yield point
    outcome = yield

    # Get the test result object
    # Contains: did it pass/fail? what was the error?
    report = outcome.get_result()

    # report.when == "call" = this is the actual test execution phase
    # pytest has 3 phases: setup → call → teardown
    # We only want screenshots during the actual test (call phase)

    # report.failed = did this test fail?
    if report.when == "call" and report.failed:

        # Get the driver fixture from the test
        # item.funcargs = all fixtures the test is using
        driver = item.funcargs.get("driver")

        if driver:
            # Take screenshot and save to screenshots folder
            # item.name = name of the failed test
            screenshot_path = take_screenshot(driver, item.name)

            # Attach screenshot to HTML report
            # hasattr checks if report has extra section
            if hasattr(report, "extra"):
                from pytest_html import extras
                # extras.image() = attach image to HTML report
                report.extra = [extras.image(screenshot_path)]