import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(capabilities={"marionette": False},
                           firefox_binary="/Applications/tools/tools_firefox/esr/FirefoxESR.app/Contents/MacOS/firefox-bin")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login_into_admin(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    sleep(1)   #  for Safari functionality
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
    index = len(driver.find_elements_by_id("app-"))  # main menu's rows
    for i in range(0, index):
        rows = driver.find_elements_by_id("app-")
        rows[i].find_element_by_tag_name("a").click()
