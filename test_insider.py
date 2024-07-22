import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InsiderWebsiteTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://useinsider.com/")
        
    def tearDown(self):
        self.driver.quit()
        
    def test_homepage_loaded(self):
        self.assertIn("Insider", self.driver.title)
        
    def test_careers_page_navigation(self):
        # Navigate to Careers page
        company_menu = self.driver.find_element_by_link_text("Company")
        company_menu.click()
        
        careers_link = self.driver.find_element_by_link_text("Careers")
        careers_link.click()
        
        # Check if key blocks are present
        self.assertTrue(self.driver.find_element_by_id("career"))
        self.assertTrue(self.driver.find_element_by_id("locations"))
        self.assertTrue(self.driver.find_element_by_id("teams"))
        self.assertTrue(self.driver.find_element_by_id("life"))
        
if __name__ == "__main__":
    unittest.main()
