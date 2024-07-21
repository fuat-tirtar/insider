from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver setup
driver = webdriver.Chrome()
driver.get("https://useinsider.com/careers/quality-assurance/")

# Click "See all QA jobs" button
see_all_jobs_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='See all QA jobs']")))
see_all_jobs_button.click()

# Apply filters: Location - Istanbul, Turkey and Department - Quality Assurance
location_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='location']/option[text()='Istanbul, Turkey']")))
location_filter.click()

department_filter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='department']/option[text()='Quality Assurance']")))
department_filter.click()

# Check presence of job listings
job_listings = driver.find_elements(By.XPATH, "//div[@class='job']")

assert len(job_listings) > 0

# Check job details (Position, Department, Location)
for job in job_listings:
    assert "Quality Assurance" in job.find_element(By.CLASS_NAME, "job-position").text
    assert "Quality Assurance" in job.find_element(By.CLASS_NAME, "job-department").text
    assert "Istanbul, Turkey" in job.find_element(By.CLASS_NAME, "job-location").text

# Close the browser session
driver.quit()
