import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

website="http://champaca.in/"
password ="password"
email="your email id"
country="India"
fname="Firstname"
lname="Lastname"
address1="HKBK College of Engineering Opposite Manyata Tech Park Road Vyalikaval HBCS Layout Nagavara"
address2="No.22/1"
city="Banglore"
State="Karnataka"
pincode="560045"
phone="7895462186"

# Initialize the webdriver
driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()
driver.delete_all_cookies()

# Wait for the website to load
time.sleep(3)

# Click on the login link
try:
    driver.find_element(By.XPATH,"//ul[@class='header-bar__module header-bar__module--list']//a[@id='customer_login_link']").click()
    print("Login page opened successfully.")
except Exception as e:
    print(f"Failed to open login page: {e}")

time.sleep(2)

# Enter email address
try:
    email_id = driver.find_element(By.XPATH,"//input[@id='CustomerEmail']")
    email_id.send_keys(email)
    print("Email entered successfully.")
except Exception as e:
    print(f"Failed to enter email: {e}")
time.sleep(1)

# Enter password
try:
    password_input = driver.find_element(By.XPATH, "//input[@id='CustomerPassword']")
    password_input.send_keys(password)
    print("Password entered successfully.")
except Exception as e:
    print(f"Failed to enter password: {e}")
time.sleep(1)

# Click on Sign In
try:
    driver.find_element(By.XPATH,"//input[@value='Sign In']").click()
    print("Sign in successful.")
except Exception as e:
    print(f"Failed to sign in: {e}")

time.sleep(5)

# Search for a product
try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("A Day of Fallen Night")
    search_box.submit()
    print("Product search successful.")
except Exception as e:
    print(f"Failed to search for product: {e}")

# Click on the product image
try:
    driver.find_element(By.XPATH, "//img[@id='SearchImage-6817878736931']").click()
    print("Product page opened successfully.")
except Exception as e:
    print(f"Failed to open product page: {e}")

time.sleep(2)

# Add product to cart
try:
    driver.find_element(By.XPATH,"//button[@id='AddToCart']").click()
    print("Product added to cart successfully.")
except Exception as e:
    print(f"Failed to add product to cart: {e}")

time.sleep(2)

# Continue shopping
try:
    driver.find_element(By.XPATH,"//a[normalize-space()='Continue shopping']").click()
    print("Continue shopping successful.")
except Exception as e:
    print(f"Failed to continue shopping: {e}")

time.sleep(2)

# Click on another product
try:
    driver.find_element(By.XPATH, "//img[@id='ProductImage-29023682002979']").click()
    print("Second product page opened successfully.")
except Exception as e:
    print(f"Failed to open second product page: {e}")

time.sleep(2)

# Add second product to cart
try:
    driver.find_element(By.XPATH,"//button[@id='AddToCart']").click()
    print("Second product added to cart successfully.")
except Exception as e:
    print(f"Failed to add second product to cart: {e}")

time.sleep(2)

# Adjust quantity
try:
    quantity = driver.find_element(By.ID,"updates_39504135913507:c12ecc992422e09ef64f941b0b7818d5")
    quantity.click()
    quantity.clear()
    quantity.send_keys('2')
    print("Quantity updated successfully.")
except Exception as e:
    print(f"Failed to update quantity: {e}")

time.sleep(2)

# Update cart
try:
    driver.find_element(By.XPATH,"//button[normalize-space()='Update Cart']").click()
    print("Cart updated successfully.")
except Exception as e:
    print(f"Failed to update cart: {e}")

time.sleep(2)

# Proceed to checkout
try:
    driver.find_element(By.XPATH,"//button[normalize-space()='Check Out']").click()
    print("Proceeded to checkout successfully.")
except Exception as e:
    print(f"Failed to proceed to checkout: {e}")

time.sleep(2)

# Marketing opt-in
try:
    driver.find_element(By.XPATH,"//input[@id='marketing_opt_in']").click()
    print("Marketing opt-in successful.")
except Exception as e:
    print(f"Failed to opt-in to marketing: {e}")

time.sleep(2)

# Enter email in checkout
try:
    email_id1 = driver.find_element(By.XPATH,"//input[@id='email']")
    email_id1.clear()
    email_id1.send_keys(email)
    print("Email entered in checkout successfully.")
except Exception as e:
    print(f"Failed to enter email in checkout: {e}")

time.sleep(2)

# Select country
try:
    Country1 = driver.find_element(By.XPATH,"//select[@id='Select0']")
    Country1.send_keys(country)
    print("Country selected successfully.")
except Exception as e:
    print(f"Failed to select country: {e}")

time.sleep(2)

# Enter first name
try:
    F_Name = driver.find_element(By.XPATH,"//input[@id='TextField0']")
    F_Name.clear()
    F_Name.send_keys(fname)
    print("First name entered successfully.")
except Exception as e:
    print(f"Failed to enter first name: {e}")

time.sleep(2)

# Enter last name
try:
    L_Name = driver.find_element(By.XPATH,"//input[@id='TextField1']")
    L_Name.clear()
    L_Name.send_keys(lname)
    print("Last name entered successfully.")
except Exception as e:
    print(f"Failed to enter last name: {e}")

time.sleep(2)

# Enter address 1
try:
    Address_1 = driver.find_element(By.XPATH,"//input[@id='shipping-address1']")
    Address_1.clear()
    Address_1.send_keys(address1)
    print("Address 1 entered successfully.")
except Exception as e:
    print(f"Failed to enter address 1: {e}")

time.sleep(2)

# Enter address 2
try:
    Address_2 = driver.find_element(By.XPATH,"//input[@id='TextField2']")
    Address_2.clear()
    Address_2.send_keys(address2)
    print("Address 2 entered successfully.")
except Exception as e:
    print(f"Failed to enter address 2: {e}")

time.sleep(3)

# Enter town/city
try:
    Town = driver.find_element(By.XPATH,"//input[@id='TextField3']")
    Town.clear()
    Town.send_keys(city)
    print("City entered successfully.")
except Exception as e:
    print(f"Failed to enter city: {e}")

time.sleep(2)

# Select state/region
try:
    region = driver.find_element(By.XPATH,"//select[@id='Select1']")
    region.send_keys(State)
    print("State selected successfully.")
except Exception as e:
    print(f"Failed to select state: {e}")

time.sleep(2)

# Enter postal code
try:
    Pin_code1 = driver.find_element(By.XPATH,"//input[@id='TextField4']")
    Pin_code1.clear()
    Pin_code1.send_keys(pincode)
    print("Pincode entered successfully.")
except Exception as e:
    print(f"Failed to enter pincode: {e}")

time.sleep(2)

# Enter phone number
try:
    phone_number = driver.find_element(By.XPATH,"//input[@id='TextField5']")
    phone_number.clear()
    phone_number.send_keys(phone)
    print("Phone number entered successfully.")
except Exception as e:
    print(f"Failed to enter phone number: {e}")

time.sleep(2)

# Complete checkout process
try:
    driver.find_element(By.XPATH,"//button[@id='checkout-pay-button']").click()
    print("Checkout completed successfully.")
except Exception as e:
    print(f"Failed to complete checkout: {e}")

time.sleep(12)

# Quit the driver
driver.quit()
print("Test script executed and browser closed.")
