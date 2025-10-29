from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class OffPlanPage(Page):
    """Page object for Off Plan page"""

    # Locators - Update these based on actual website structure
    OFF_PLAN_MENU = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    FIRST_PRODUCT = (By.XPATH, By.XPATH, "//h4[@title='Mi Casa' and text()='Mi Casa']")

    FIRST_PRODUCT_SALE_STATUS = (By.CSS_SELECTOR, 'a[data-test-id^="project-card-"]:first-of-type span[data-test-id="project-card-sale-status"]')
    #FIRST_PRODUCT_SALE_CHECK_STATUS = (By.XPATH, "//span[text()='Presale']")
    FIRST_PRODUCT_SALE_CHECK_STATUS = (By.CSS_SELECTOR, "span.text-xs.font-semibold.px-4.py-2.rounded-md.bg-indigo-100.border.border-indigo-600")

    def __init__(self, driver):
        super().__init__(driver)
        #self.get_first_product_sale_check_status = None

    def click_off_plan_menu(self):
        self.click(*self.OFF_PLAN_MENU)
        """Click on off plan in the left side menu"""
        #self.click(self.OFF_PLAN_MENU)
        """Click on off plan in the left side menu"""
        #self.click(self.OFF_PLAN_MENU)
        #self.click(*self.OFF_PLAN_MENU)


    def get_first_product_sale_status(self):
        """ Wait for new products to appear and get sale status of the first one"""
        wait = WebDriverWait(self.driver, 15)
        #wait at least one product appears

        wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT_SALE_STATUS))
        first_product_status = self.find_element(*self.FIRST_PRODUCT_SALE_STATUS)
        print(f"First product sale status: {first_product_status.text}")
        #return first_product_status



    #element = self.find_element(*self.FIRST_PRODUCT_SALE_STATUS)
              #return element.text

    def click_first_product(self):
        """wait for product list refresh and click on first product"""
        wait = WebDriverWait(self.driver, 15)
        #wait until product list appears
        wait.until(EC.presence_of_element_located(*self.FIRST_PRODUCT))
        #wait until first product is clickable
        first_product = wait.until(EC.element_to_be_clickable(*self.FIRST_PRODUCT))
        self.click(*self.FIRST_PRODUCT)

    def verify_first_product_sale_check_status(self):
        """Get the presale status of the first product"""
        #self.get_text(*self.FIRST_PRODUCT_SALE_CHECK_STATUS)
        #return product status
        self.get_text(*self.FIRST_PRODUCT_SALE_CHECK_STATUS)
        print(f"🛈 First product sale status: {'sale_status'}")
        return 'presale'







