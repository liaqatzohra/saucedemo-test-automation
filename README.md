# SauceDemo Test Automation Framework

![Tests](https://github.com/liaqatzohra/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg)

An end-to-end test automation framework built with Selenium, Pytest and Python following the Page Object Model design pattern. Covers login, cart, checkout and logout flows with HTML reporting, Allure interactive reports, automatic screenshots on failure, GitHub Actions CI/CD pipeline and cross-browser support on Chrome and Safari.

---

## About

I am an Automation QA Engineer with experience in web, mobile, iOS and Android testing. I build and maintain test automation frameworks, write Selenium and Appium scripts in Python, perform API testing, and work within Agile/Scrum teams. This project demonstrates my automation skills and the professional standards I follow when structuring a test suite.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML reports with screenshots |
| Allure | Interactive visual test reports |
| webdriver-manager | Automatic driver management |
| GitHub Actions | CI/CD pipeline |
| Git | Version control |

---

## What It Tests

**Login Security** — 7 tests
- Valid credentials
- Wrong password error handling
- Empty field validation
- Locked out user scenario
- Multiple invalid scenarios via parametrize

**Product & Cart Functionality** — 4 tests
- Products page loads correctly after login
- Add to cart updates badge count
- Remove from cart resets count
- Multiple different items increase count correctly

**End to End Checkout Flow** — 6 tests
- Complete purchase journey from login to confirmation
- Form field validation (first name, last name, postal code)
- All fields empty validation
- Success message verification

**Logout & Navigation** — 1 test
- Logout via hamburger menu returns to login page

**Total: 18 automated test cases**

---

## Project Structure

```
saucedemo-test-automation/
│
├── .github/
│   └── workflows/
│       └── tests.yml        # GitHub Actions CI/CD pipeline
│
├── pages/
│   ├── login_page.py        # login page locators and actions
│   ├── products_page.py     # product and cart interactions
│   ├── checkout_page.py     # checkout form and confirmation
│   └── navbar_page.py       # navigation menu and logout
│
├── tests/
│   ├── test_login.py        # login test scenarios
│   ├── test_products.py     # cart functionality tests
│   ├── test_checkout.py     # end to end purchase tests
│   └── test_logout.py       # logout and navigation tests
│
├── test_data/
│   ├── login_data.py        # parametrized login scenarios
│   └── checkout_data.py     # parametrized form scenarios
│
├── utilities/
│   └── screenshot.py        # automatic failure screenshots
│
├── reports/
│   └── allure-results/      # Allure report data
├── screenshots/             # failure screenshots
├── conftest.py              # fixtures and browser configuration
├── pytest.ini               # pytest settings
└── requirements.txt         # dependencies
```

---

## Setup and Run

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run all tests on Chrome:**
```bash
pytest
```

**Run all tests on Safari:**
```bash
pytest --browser=safari
```

**Run silently in background:**
```bash
pytest --headless
```

**Run specific file:**
```bash
pytest tests/test_login.py -v
```

**Watch tests run in browser:**
```bash
pytest --keep-open
```

**View HTML report:**
```bash
open reports/report.html
```

**View Allure interactive report:**
```bash
allure serve reports/allure-results
```

---

## Key Features

**Page Object Model** — locators and actions are separated from test logic. If a locator changes it is updated in one place only.

**Parametrized Tests** — one test function covers multiple scenarios using `pytest.mark.parametrize` with external data files. One function handles 6+ scenarios cleanly.

**Smart Waits** — combines implicit and explicit waits to handle dynamic content without fixed sleep times.

**Auto Screenshots** — captures browser state automatically on every test failure and attaches to HTML report.

**Headless Execution** — supports background execution via `--headless` flag for CI/CD pipelines.

**JavaScript Clicks** — handles element interception and dynamic UI reliably using `execute_script`. Solved real browser popup interference issues during development.

**Allure Reports** — interactive reports with step by step breakdown, severity levels, feature grouping and visual timeline. Each test is decorated with `@allure.feature`, `@allure.story` and `@allure.severity`.

**GitHub Actions CI/CD** — tests run automatically on every push to main branch. HTML report and failure screenshots are uploaded as artifacts after every run.

**Cross Browser Testing** — supports Chrome and Safari via `--browser` flag. Chrome runs headless for CI/CD. Safari runs locally on Mac. Browser setup is fully centralized in conftest.py so adding a new browser requires changes in one place only.

**Incognito Mode** — each test runs in a fresh incognito Chrome session to prevent saved passwords and browser popups from interfering with test execution.

---

## CI/CD Pipeline

Every push to `main` branch automatically:
1. Sets up Python 3.11 on Ubuntu
2. Installs all dependencies from requirements.txt
3. Installs Chrome browser
4. Runs all 18 tests in headless mode
5. Uploads HTML report as downloadable artifact
6. Uploads failure screenshots if any test fails

---

## Skills Demonstrated

- Test automation framework design
- Page Object Model pattern
- Cross-platform testing (web, Android, iOS)
- Cross-browser testing (Chrome, Safari)
- Parametrized testing with external data files
- Implicit and explicit wait strategies
- Allure reporting with decorators
- CI/CD with GitHub Actions
- JavaScript execution via Selenium
- Bug tracking and reporting
- Agile and Scrum methodology
- Python scripting

---

## Contact

**Zohra Liaqat** — Automation QA Engineer
Based in Koblenz, Germany

[LinkedIn](https://www.linkedin.com/in/zohra-liaqat-b47986150/) | zohraliaqat786@gmail.com