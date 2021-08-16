from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://amazon.com")
driver.find_element_by_css_selector("input[type='text']").send_keys("Books")
driver.find_element_by_css_selector("input[id='nav-search-submit-button']").click()
driver.find_element_by_css_selector("input[type='text']").send_keys("the green mile")
driver.find_element_by_css_selector("input[id='nav-search-submit-button']").click()
driver.find_element_by_css_selector("img[alt='The Green Mile']").click()
d





