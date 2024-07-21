from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver setup
driver = webdriver.Chrome()
driver.get("https://useinsider.com/")

# Click on Company -> Careers
company_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Company")))
company_menu.click()

careers_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Careers")))
careers_link.click()

# Check for Careers page elements
assert "Careers" in driver.title
assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='locations']")))
assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='teams']")))
assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='life-at-insider']")))

# Close the browser session
driver.quit()
