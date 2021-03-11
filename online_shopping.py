from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time
import os


def webpage1():
    driver.get(# Website 1 to start checking if item in stock)


def webpage2():
    driver.get(# Website 2 for checking multiple items)


# loops through string to enter into element
def word_entry(element, word):
    for i in word:
        element.send_keys(i)


# checks if survey pops up
def survey():
    print("Checking Survey")
    checking_survey = True
    while checking_survey:
        try:
            driver.find_element_by_xpath("//*[@id='survey_invite_no']").click()
            checking_survey = False
            print("    Survey Declined")
            time.sleep(1)
        except Exception:
            print("    No Survey")
            checking_survey = False


# checks if spinner is invisible to continue to check out
def spinner_check():
    try:
        WebDriverWait(driver, 5).until(ec.invisibility_of_element_located((By.CLASS_NAME, "page-spinner")))
        print("Spinner Gone")
    except Exception:
        print("Spinner Not There")
        pass


# checks if file that holds names, card info, etc..
def filethere(file):
    if os.path.exists(file):
        filename = open(file, "r").read()
    else:
        filename = open(file, "w")
    return filename


files = ["name.txt","lastname.txt","city.txt","email.txt","pass.txt","card.txt","expire.txt"]
for i in files:
    print(filethere(i))


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path="C:\Windows\geckodriver.exe")
driver.set_window_size(900, 1000)
webpage1()
print("***Loading Website Waiting 5 seconds***")
time.sleep(5)

survey()

checkingaccount = True
while checkingaccount:
    try:
        driver.find_element_by_xpath("//*[@class='leading-icon']").click()
        print("Style 1")
        checkingaccount = False
    except NameError:
        driver.find_element_by_xpath("//*[@class='btn-unstyled']").click()
        print("Style 2")
        checkingaccount = False
    except:
        driver.find_element_by_xpath("//*[@class='BtnTxt']").click()
        print("Style 3")
        checkingaccount = False

print("***Found Account Button***")

driver.find_element_by_class_name("lam-signIn__button").click()
print("***Found Sign-In Button***")

# Enter Email
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "fld-e")))
emailAddressElement = driver.find_element_by_id("fld-e")
word_entry(emailAddressElement, filethere("email.txt"))
print("***Entered Email***")

# Enter Password
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "fld-p1")))
emailPasswordElement = driver.find_element_by_id("fld-p1")
word_entry(emailPasswordElement, filethere("pass.txt"))
print("***Entered Password***")
survey()

WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "btn-secondary")))
driver.find_element_by_class_name("btn-secondary").click()
print("***Logged In***")
survey()

buyButton = True
while buyButton:
    try:
        webpage1()
        driver.find_element_by_class_name("btn-disabled")
        time.sleep(4)
        webpage2()
        time.sleep(4)
        driver.find_element_by_class_name("btn-disabled")
    except Exception:
        add_button = driver.find_element_by_class_name("btn-primary")
        time.sleep(3)
        add_button.click()
        buyButton = False

spinner_check()
print("***Found add to cart***")

driver.get("https://www.bestbuy.com/cart")
print("***Loading Cart***")

WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div/main/div/div[2]/div[1]/div/div[1]"
                                                                     "/div[1]/section[1]/div[4]/ul/li/section/div[2]"
                                                                     "/div[2]/form/div[2]/fieldset/div[2]/div[1]/div"
                                                                     "/div/div/input")))
driver.find_element_by_xpath("/html/body/div/main/div/div[2]/div[1]/div/div[1]"
                             "/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]"
                             "/form/div[2]/fieldset/div[2]/div[1]/div/div/div/input").click()

print("***Changed to Shipping***")

spinner_check()
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
driver.find_element_by_xpath("/html/body").click()
ship = driver.find_element_by_class_name("btn-primary")
driver.execute_script("arguments[0].scrollIntoView(true);", ship)
spinner_check()
ship.click()
print("***Checkout Button Hit***")


# INFORMATION FOR SHOPPING CART
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@id='consolidatedAddresses.ui_address_2.street']")))
address = driver.find_element_by_xpath("//input[@id='consolidatedAddresses.ui_address_2.street']")
word_entry(address, "10115 S. Peoria ST")
print("**Added Street Address**")
# FIRST NAME
firstName = driver.find_element_by_xpath("//input[@id='consolidatedAddresses.ui_address_2.firstName']")
word_entry(firstName, filethere('name.txt'))
print("**Added First Name**")

# LAST NAME
lastName = driver.find_element_by_xpath("//input[@id='consolidatedAddresses.ui_address_2.lastName']")
word_entry(lastName, filethere('lastname.txt'))
print("**Added Last Name**")

# CITY
city = driver.find_element_by_xpath("//*[@id='consolidatedAddresses.ui_address_2.city']")
word_entry(city, filethere('city.txt'))
print("**Added City**")

# ZIP CODE
cityZipCode = driver.find_element_by_xpath("//input[@id='consolidatedAddresses.ui_address_2.zipcode']")
word_entry(cityZipCode, "80134")
print("**Added ZipCode**")

# SELECT STATE
driver.find_element_by_xpath("//*[@id='consolidatedAddresses.ui_address_2.state']").send_keys("CO")
print("**Selected State**")

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]"
                             "/div[2]/form/section/div/div[2]/div/div/button").click()
print("***Loading Payment***")

# CARD INFO
time.sleep(5)
cardNumber = driver.find_element_by_xpath("//*[@id='optimized-cc-card-number']")
word_entry(cardNumber, filethere("card.txt"))

month = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]"
                                            "/main/div[2]/div[3]/div/section/div[1]/div/section"
                                            "/div[2]/div[1]/div/div[1]/label/div/div/select"))
month.select_by_value("10")

year = Select(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]"
                                           "/main/div[2]/div[3]/div/section/div[1]/div/section"
                                           "/div[2]/div[1]/div/div[2]/label/div/div/select"))
year.select_by_value("2028")
