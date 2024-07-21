import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://useinsider.com/")
    yield driver
    driver.quit()

def test_home_page_is_opened(setup):
    assert "Insider" in setup.title

def test_careers_page(setup):
    driver = setup
    company_menu = driver.find_element(By.XPATH, "//a[text()='Company']")
    company_menu.click()
    careers_link = driver.find_element(By.XPATH, "//a[text()='Careers']")
    careers_link.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='locations']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='teams']")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='life']")))

    assert "Locations" in driver.page_source
    assert "Teams" in driver.page_source
    assert "Life at Insider" in driver.page_source
