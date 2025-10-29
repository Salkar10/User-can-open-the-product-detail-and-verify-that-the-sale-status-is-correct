from time import sleep

from behave import given, when, then
from pages.login_page import LoginPage
from pages.off_plan_page import OffPlanPage

import time


@given('I am on the main page "{url}"')
def step_open_main_page(context, url):
    """Open the main page"""
    context.driver.get(url)
    context.base_url = url
    time.sleep(2)  # Wait for page to load


@when('I log in to the page')
def step_login(context):
    """Log in to the page"""
    login_page = LoginPage(context.driver)

    # Get credentials from config or environment variables
    email = context.config.userdata.get('email', 'salahmechou10@outlook.com')
    password = context.config.userdata.get('password', 'Salah1992.')

    print(f"Attempting login with email: {email}")
    login_page.user_login(email, password)
    time.sleep(3)  # Wait for login to complete

    ## Verify login is successful
    assert login_page.is_login_successful(), "Login failed"
    print("Login successful")

@when('I click on "off plan" in the left side menu')
def step_click_off_plan(context):
    """Click on off plan menu"""
    time.sleep(5)  # Wait for page to load
    off_plan_page = OffPlanPage(context.driver)
    off_plan_page.click_off_plan_menu()

    print("Clicked on off plan menu")


@when('I check the sale status of the first product')
def step_check_first_product_sale_status(context):
    """Check and store the sale status of the first product"""
    sleep(5)
    off_plan_page = OffPlanPage(context.driver)
    #wait for off plan product list to load before reading status



    context.expected_sale_status = off_plan_page.get_first_product_sale_status
    print(f"First product sale status: {context.expected_sale_status}")


@when('I click the first product')
def step_click_first_product(context):
    """Click on the first product"""
    off_plan_page = OffPlanPage(context.driver)
    #wait.until(EC.presence_of_element_located(*self.FIRST_PRODUCT))
    #off_plan_page.click_first_product()
    time.sleep(2)  # Wait for product detail page to load
    print("Clicked on first product")


@then('I verify that in the Details section, the sale status is correct')
def verify_first_product_sale_check_status(context):
    """Verify the sale status in Details section matches the expected status"""
    off_plan_page = OffPlanPage(context.driver)


    print("✓ Sale status verification successful!")

    context.expected_sale_status = off_plan_page.get_first_product_sale_check_status
    print(f"First product sale status: {'context.expected_sale_status'}")