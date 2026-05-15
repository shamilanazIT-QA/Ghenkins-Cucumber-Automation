from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@when('I enter "{username}" into the username field')
def step_impl(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)

@when('I enter "{password}" into the password field')
def step_impl(context, password):
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I should be on the "{expected_page}" page')
def step_impl(context, expected_page):
    try:
        # Wait up to 10 seconds for the URL to change
        WebDriverWait(context.driver, 10).until(
            EC.url_contains(expected_page)
        )
        print(f"Success! Reached the {expected_page} page.")
    except:
        actual_url = context.driver.current_url
        assert expected_page in actual_url, f"Failed! Expected {expected_page} but was at {actual_url}"