from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver setup
driver = webdriver.Chrome()
driver.get("https://useinsider.com/careers/quality-assurance/")

# Click "View Role" button
view_role_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View Role']")))
view_role_button.click()

# Check if redirected to Lever Application form page
assert "lever.co" in driver.current_url

# Close the browser session
driver.quit()
