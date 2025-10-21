from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class OffPlanPage(Page):
    """Page object for Off Plan page"""

    # Locators - Update these based on actual website structure
    OFF_PLAN_MENU = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    FIRST_PRODUCT = (By.CSS_SELECTOR, "div.project-card:first-child h4")
    FIRST_PRODUCT_SALE_STATUS = (By.CSS_SELECTOR, 'a[data-test-id^="project-card-"]:first-of-type span[data-test-id="project-card-sale-status"]')


    def click_off_plan_menu(self):
        self.click(*self.OFF_PLAN_MENU)
        """Click on off plan in the left side menu"""
        #self.click(self.OFF_PLAN_MENU)
        """Click on off plan in the left side menu"""
        #self.click(self.OFF_PLAN_MENU)
        #self.click(*self.OFF_PLAN_MENU)

    def get_first_product_sale_status(self):
        """ Wait for new products to appear and get sale status of the first one"""
        wait = WebDriverWait(self.driver, 10)
        #wait at least one product appears

        #wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT_SALE_STATUS))
        return self.get_text(*self.FIRST_PRODUCT_SALE_STATUS)

    def click_first_product(self):
        """wait for product list refresh and click on first product"""
        wait = WebDriverWait(self.driver, 10)
        #wait until product list appears
        wait.until(EC.presence_of_element_located(*self.FIRST_PRODUCT))
        #wait until first product is clickable
        first_product = wait.until(EC.element_to_be_clickable(*self.FIRST_PRODUCT))
        self.click(*self.FIRST_PRODUCT)

    def get_products_sale_status(self):
        """Get the count of products displayed"""
        products = self.find_elements(*self.PRODUCT_STATUS)
        #return len(products)
        return self.get_text(*self.PRODUCT_STATUS)

