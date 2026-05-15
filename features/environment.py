from selenium import webdriver
import os


def before_all(context):
    options = webdriver.ChromeOptions()

    # If running on GitHub Actions, enforce headless mode
    if os.environ.get('CI') == 'true':
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()