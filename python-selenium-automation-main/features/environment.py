#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from app.application import Application


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#def browser_init(context):
#def browser_init(context, scenario_name):




#def after_scenario(context, scenario):
   # context.driver.quit()





#BROWSERSTACK_USERNAME  = "hamzamechou_Wh3pcM"
#BROWSERSTACK_ACCESS_KEY  = "JmHL7q59zCXfpGqTJmky"
#url = f'http://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY }@hub-cloud.browserstack.com/wd/hub'

#options = Options()
#bstack_options = {

          #"os" : "Windows",
          #"osVersion" : "10",
          #"browserName": "Chrome",
          #"browserVersion" : "latest",
           #"buildName": "bstack-Internship",
            #"projectName": "BrowserStack product sale status"
#}
#options.set_capability("bstack:options", bstack_options)
#context.driver = webdriver.Remote(command_executor=url, options=options)






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

def browser_init(context, scenario_name):
    """
    ##:param context: Behave context
    """
    ### CHROME CONFIGURATION ###
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### BROWSERSTACK CONFIGURATION ###
    # BROWSERSTACK_USERNAME = "hamzamechou_Wh3pcM"
    # BROWSERSTACK_ACCESS_KEY = "JmHL7q59zCXfpGqTJmky"
    #
    # url = f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "10",
    #     "browserName": "Chrome",
    #     "browserVersion": "latest",
    #     "buildName": "bstack-Internship",
    #     "projectName": "BrowserStack product sale status",
    #     "sessionName": scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ### HEADLESS CONFIGURATION ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

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
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
