from selenium import webdriver

# WebDriver setup
driver = webdriver.Chrome()
driver.get("https://useinsider.com/")

# Assertion for homepage title or any other relevant element
assert "Insider" in driver.title

# Close the browser session
driver.quit()
