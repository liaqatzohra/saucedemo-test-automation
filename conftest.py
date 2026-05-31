import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.screenshot import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--keep-open",
        action="store_true",
        default=False,
        help="Keep browser open after each test"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser invisibly"
    )


@pytest.fixture
def driver(request):
    # --- SETUP ---
    options = webdriver.ChromeOptions()

    # Hide robot flags
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # ✅ Fresh profile - no saved passwords, no popups!
    options.add_argument("--incognito")

    # ✅ Disable ALL Chrome popups
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    })

    # Headless mode if flag passed
    headless = request.config.getoption("--headless")
    if headless:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    yield driver

    # --- TEARDOWN ---
    keep_open = request.config.getoption("--keep-open")
    if keep_open:
        import time
        time.sleep(10)

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra = [extras.image(screenshot_path)]