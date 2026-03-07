# Write a script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Books
# Add first book to cart
# Click Shopping Cart
# Verify the product is present in the cart.

from selenium import webdriver
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element('xpath', '(//a[contains(text(),"Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="button"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Shopping cart"]').click()
# time.sleep(2)

# Write a Selenium script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element('xpath', '(//a[contains(text(),"Electronics")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="Show products in category Cell phones"]').click()

# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.

# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(2)
# driver.find_element("xpath", "//button[text()='Start']").click()
# time.sleep(5)
# text = driver.find_element("xpath", "//h4").text
# print("Text displayed:", text)




# Write a script to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(2)
#
# driver.find_element("xpath", "//button[text()='Remove']").click()
# time.sleep(5)
#
# driver.find_element("xpath", "//button[text()='Add']").click()




# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# driver.find_element("xpath", "//div[@id='withOptGroup']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//div[text()='Group 2, option 1']").click()
# time.sleep(2)
#
# value = driver.find_element("xpath", "//div[contains(@class,'singleValue')]").text
#
# print("Selected value:", value)

# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.

# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
#
# driver.execute_script("window.scrollBy(0,600)")
# time.sleep(2)
#
# multi = select(driver.find_element("xpath", "//select[@id='cars']"))
#
# multi.select_by_visible_text("Volvo")
# multi.select_by_visible_text("Saab")
# multi.select_by_visible_text("Opel")
#
# for option in multi.all_selected_options:
#     print(option.text)


#task7
# Write a Selenium script to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1


# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://demoqa.com/menu/")
# time.sleep(2)
#
# action = ActionChains(driver)
#
# main = driver.find_element("xpath", "//a[text()='Main Item 2']")
# action.move_to_element(main).perform()
# time.sleep(2)
#
# sub = driver.find_element("xpath", "//a[text()='SUB SUB LIST »']")
# action.move_to_element(sub).perform()
# time.sleep(2)
#
# item = driver.find_element("xpath", "//a[text()='Sub Sub Item 1']")
# item.click()


#task8
# Write a Selenium script to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!

# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://demoqa.com/droppable")
# time.sleep(2)
#
# drag = driver.find_element("xpath", "//div[@id='draggable']")
# drop = driver.find_element("xpath", "//div[@id='droppable']")
#
# action = ActionChains(driver)
# action.drag_and_drop(drag, drop).perform()
#
# print(driver.find_element("xpath", "//div[@id='droppable']").text)


#task9
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
#
# driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
#
# alert = driver.switch_to.alert
# alert.accept()
#
# result = driver.find_element("xpath", "//p[@id='result']").text
# print(result)


#task10
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@id='file-upload']").send_keys("C:\\Users\\KIIT\\Desktop\\capg_assessment.txt")
#
# driver.find_element("xpath", "//input[@id='file-submit']").click()
#
# print(driver.find_element("xpath", "//h3").text)


#question, Write the steps to read the data from excel
# Write the syntax for the xpath to locate the elements using
# 	*	attributes --//tagname[@attribute='value']
# 	*	text--//tagname[text()='value']
# 	*	group indexing--(xpath_expression)[index]
# 	*	contains--//tagname[contains(@attribute,'value')]








