# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver, 15)
# -----------------------------------TASK1------------------------------------
# driver.get('https://www.facebook.com/')
# wait_obj=WebDriverWait(driver, 20)
# driver.find_element('xpath','//input[@name="email"]').send_keys('##username')
# driver.find_element('xpath','//input[@name="pass"]').send_keys('##passeord')
# driver.find_element('xpath','//span[text()="Log in"]').click()
# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//span[@id="_R_6lal8pl5bb6ismj5ilipam_"]')))
#     print("Verification Successful")
# except:
#     print("Verification Failed")

# -----------------------------------TASK2------------------------------------

#
# import time
# from selenium import webdriver
#
# driver = webdriver.ChromeOptions()
# driver.add_experimental_option("detach", True)
#
# c_driver = webdriver.Chrome(driver)
# c_driver.get("https://www.myntra.com/")
#
# time.sleep(3)
#
# # search puma
# c_driver.find_element('class name', 'desktop-searchBar').send_keys("puma")
# time.sleep(3)
#
# # click first suggestion
# c_driver.find_element('xpath', '//li[text()="Puma Shoes"]').click()
# time.sleep(4)
#
# # click first product
# c_driver.find_element('xpath', '(//div[@class="product-productMetaInfo"])[1]').click()
# time.sleep(3)
#
# # handle new tab
# tabs = c_driver.window_handles
# c_driver.switch_to.window(tabs[1])
# time.sleep(3)
#
# # select size (if needed)
# try:
#     c_driver.find_element('xpath', '(//div[contains(@class,"size-buttons-size-buttons")]//button)[1]').click()
#     time.sleep(2)
# except:
#     print("Size not required")
#
# # add to cart
# c_driver.find_element('xpath', '(//P[@class="size-buttons-unified-size"])[4]').click()
# c_driver.find_element('xpath', '//div[contains(@class,"pdp-add-to-bag")]').click()
#
#
#
# print("Product added to cart")
# -----------------------------------TASK3------------------------------------

# driver.get('https://www.icici.bank.in/')
# wait_obj = WebDriverWait(driver, 20)

# wait_obj.until(EC.element_to_be_clickable(('xpath','//a[contains(text(),"Accounts")]'))).click()
# wait_obj.until(EC.element_to_be_clickable(('xpath','//a[contains(text(),"Apply")]'))).click()

# driver.switch_to.window(driver.window_handles[1])

# driver.find_element('xpath','//input[@name="fullName"]').send_keys('Test User')
# driver.find_element('xpath','//input[@name="mobileNumber"]').send_keys('9999999999')

# driver.find_element('xpath','//button[contains(text(),"Apply Now")]').click()

# try:
#     wait_obj.until(EC.visibility_of_element_located(('xpath','//*[contains(text(),"error")]')))
#     print("Validation Successful")
# except:
#     print("Validation Failed")

# -----------------------------------TASK4------------------------------------

# driver.get('https://www.netmeds.com/')
# wait_obj = WebDriverWait(driver, 20)

# actions = ActionChains(driver)

# med = wait_obj.until(EC.visibility_of_element_located(('xpath','//a[contains(text(),"Medicines")]')))
# actions.move_to_element(med).perform()

# wait_obj.until(EC.element_to_be_clickable(('xpath','//a[contains(text(),"Order Online")]'))).click()

# driver.find_element('xpath','//input[@type="file"]').send_keys('C:\\Users\\KIIT\\Desktop\\test.txt')

# print("File Uploaded")     

# -----------------------------------TASK5------------------------------------

# driver.get('https://www.netmeds.com/')
# wait_obj = WebDriverWait(driver, 20)

# wait_obj.until(EC.element_to_be_clickable(('xpath','//span[contains(text(),"Sign in")]'))).click()

# driver.find_element('xpath','//input[@id="phoneNo"]').send_keys('your_number')

# driver.find_element('xpath','//button[contains(text(),"Get OTP")]').click()

# otp = input("Enter OTP: ")
# driver.find_element('xpath','//input[@id="otp"]').send_keys(otp)

# print("OTP Entered")

# -----------------------------------TASK6------------------------------------

# driver.get('https://www.irctc.co.in/nget/train-search')
# wait_obj = WebDriverWait(driver, 20)

# wait_obj.until(EC.element_to_be_clickable(('xpath','//button[contains(text(),"OK")]'))).click()

# driver.find_element('xpath','//input[@placeholder="From*"]').send_keys('Delhi')
# time.sleep(2)
# driver.find_element('xpath','//li').click()

# driver.find_element('xpath','//input[@placeholder="To*"]').send_keys('Kolkata')
# time.sleep(2)
# driver.find_element('xpath','//li').click()

# driver.find_element('xpath','//button[contains(text(),"Search")]').click()

# print("Search Done")

# -----------------------------------TASK7------------------------------------

# driver.get('https://www.purplle.com/')
# wait_obj = WebDriverWait(driver, 20)

# actions = ActionChains(driver)

# brand = wait_obj.until(EC.visibility_of_element_located(('xpath','//a[contains(text(),"Brands")]')))
# actions.move_to_element(brand).perform()

# driver.find_element('xpath','//input[@placeholder="Search brand"]').send_keys('lakme')

# time.sleep(2)
# driver.find_element('xpath','//li').click()

# wait_obj.until(EC.element_to_be_clickable(('xpath','//div[contains(@class,"product")]'))).click()

# driver.find_element('xpath','//input[@placeholder="Enter Pincode"]').send_keys('700001')
# driver.find_element('xpath','//button').click()

# print("Pincode Checked")

# -----------------------------------TASK8------------------------------------

# driver.get('https://lifeinsurance.adityabirlacapital.com/')
# wait_obj = WebDriverWait(driver, 20)

# data = [('Test1','25'),('Test2','30')]

# for name, age in data:
#     driver.find_element('xpath','//input[@name="name"]').send_keys(name)
#     driver.find_element('xpath','//input[@name="age"]').send_keys(age)
#     print("Data Entered")

# ------------------------------------TASK9------------------------------------

# driver.get('https://www.apollopharmacy.in/')
# wait_obj = WebDriverWait(driver, 20)

# wait_obj.until(EC.element_to_be_clickable(('xpath','//a[contains(text(),"Find Doctors")]'))).click()

# wait_obj.until(EC.element_to_be_clickable(('xpath','//p[contains(text(),"General Physician")]'))).click()

# wait_obj.until(EC.element_to_be_clickable(('xpath','//div[contains(@class,"doctor")]'))).click()

# driver.find_element('xpath','//button[contains(text(),"Continue")]').click()

# print("Doctor Selected")

# ------------------------------------TASK10------------------------------------

# driver.get('https://porter.in/')
# wait_obj = WebDriverWait(driver, 20)

# time.sleep(8)  # IMPORTANT (full load hone do)

# # Step 1: Click Packers & Movers
# try:
#     driver.find_element('xpath','//*[contains(text(),"Packers")]').click()
#     time.sleep(3)
# except:
#     print("Packers click issue")

# # Step 2: Inject City using JS
# try:
#     driver.execute_script("""
#         let inputs = document.querySelectorAll('input');
#         if(inputs.length > 0){
#             inputs[0].value = 'Kolkata';
#             inputs[0].dispatchEvent(new Event('input'));
#         }
#     """)
#     print("City Entered")
# except:
#     print("City failed")

# time.sleep(2)

# # Step 3: Pickup
# try:
#     driver.execute_script("""
#         let inputs = document.querySelectorAll('input');
#         if(inputs.length > 1){
#             inputs[1].value = 'Salt Lake';
#             inputs[1].dispatchEvent(new Event('input'));
#         }
#     """)
#     print("Pickup Entered")
# except:
#     print("Pickup failed")

# time.sleep(2)

# # Step 4: Drop
# try:
#     driver.execute_script("""
#         let inputs = document.querySelectorAll('input');
#         if(inputs.length > 2){
#             inputs[2].value = 'Howrah';
#             inputs[2].dispatchEvent(new Event('input'));
#         }
#     """)
#     print("Drop Entered")
# except:
#     print("Drop failed")

# # Step 5: Phone
# try:
#     driver.execute_script("""
#         let inputs = document.querySelectorAll('input');
#         if(inputs.length > 3){
#             inputs[3].value = '9999999999';
#             inputs[3].dispatchEvent(new Event('input'));
#         }
#     """)
#     print("Phone Entered")
# except:
#     print("Phone failed")

# print("Flow Completed ✅")