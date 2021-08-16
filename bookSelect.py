from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://amazon.com")
driver.find_element_by_id("twotabsearchtextbox").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("Books")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("The Green Mile")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_tag_name("img[alt='The Green Mile']").click()
driver.find_element_by_id("productTitle")


driver.close()

