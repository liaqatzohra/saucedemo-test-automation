import os
from datetime import datetime


def take_screenshot(driver, test_name):
    # Create screenshots folder if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Create unique filename with test name and exact time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"

    # Take the screenshot and save it
    driver.save_screenshot(filename)

    print(f"Screenshot saved: {filename}")

    return filename