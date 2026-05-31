# SauceDemo Test Automation Framework

An end-to-end test automation framework built with Selenium, Pytest and Python following the Page Object Model design pattern. 
Covers login, cart and checkout flows with HTML reporting and automatic screenshots on failure.

---

## About

I am an Automation QA Engineer with experience in web, mobile, iOS and Android testing. 
I build and maintain test automation frameworks, write Selenium and Appium scripts in Python, perform API testing, 
and work within Agile/Scrum teams. This project demonstrates my automation skills and the professional standards 
I follow when structuring a test suite.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML reports with screenshots |
| webdriver-manager | Automatic chromedriver management |
| Git | Version control |

---

## What It Tests

**Login Security**
- Valid credentials
- Wrong password error handling
- Empty field validation
- Locked out user scenario

**Product & Cart Functionality**
- Products page loads correctly
- Add to cart updates badge count
- Remove from cart resets count
- Multiple items increase count correctly

**End to End Checkout Flow**
- Complete purchase journey from login to confirmation
- Form field validation (first name, last name, postal code)
- Success message verification

**Total: 17 automated test cases**

---

## Project Structure

```
saucedemo-test-automation/
│
├── pages/
│   ├── login_page.py        # login page locators and actions
│   ├── products_page.py     # product and cart interactions
│   └── checkout_page.py     # checkout form and confirmation
│
├── tests/
│   ├── test_login.py        # login test scenarios
│   ├── test_products.py     # cart functionality tests
│   └── test_checkout.py     # end to end purchase tests
│
├── test_data/
│   ├── login_data.py        # parametrized login scenarios
│   └── checkout_data.py     # parametrized form scenarios
│
├── utilities/
│   └── screenshot.py        # automatic failure screenshots
│
├── reports/                 # generated HTML reports
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

**Run all tests:**
```bash
pytest
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

**View report:**

Open `reports/report.html` in any browser after running tests.

---

## Key Features

**Page Object Model** — locators and actions are separated from test logic. If a locator changes it is updated in one place only.

**Parametrized Tests** — one test function covers multiple scenarios using `pytest.mark.parametrize` with external data files.

**Smart Waits** — combines implicit and explicit waits to handle dynamic content without fixed sleep times.

**Auto Screenshots** — captures browser state automatically on every test failure and attaches to HTML report.

**Headless Execution** — supports background execution via `--headless` flag for CI/CD pipelines.

**JavaScript Clicks** — handles element interception and dynamic UI reliably using `execute_script`.

---

## Skills Demonstrated

- Test automation framework design
- Page Object Model pattern
- Cross-platform testing (web, Android, iOS)
- API testing and validation
- Agile and Scrum methodology
- Bug tracking and reporting
- CI/CD awareness (Jenkins, GitHub Actions)
- Python scripting

---

## Contact

**Zohra Liaqat** — Automation QA Engineer
[LinkedIn](https://www.linkedin.com/in/zohra-liaqat-b47986150/) | zohraliaqat786@gmail.com