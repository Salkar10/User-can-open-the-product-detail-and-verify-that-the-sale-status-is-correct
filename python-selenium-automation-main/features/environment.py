from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#def browser_init(context):
    #"""
    #:param context: Behave context
    #"""
    #from selenium.webdriver.chrome.options import Options

    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')

    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service, options=options)

    #context.driver.implicitly_wait(15)

def browser_init(context):
    """
    ##:param context: Behave context
    #"""
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

#def browser_init(context):
    #"""
    #:param context: Behave context
    #"""
    #from selenium.webdriver.firefox.service import Service as FirefoxService
    #from webdriver_manager.firefox import GeckoDriverManager

    #driver_path = GeckoDriverManager().install()
    #service = FirefoxService(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    #context.driver.maximize_window()
    #context.driver.implicitly_wait(4)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
