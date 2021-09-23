from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# a path to the site..
website = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber"

# a path to subpage Kiruna
kirunaPage = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/kiruna"

# a path to subpage Luleå
luleaPage = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/lulea"


#----TESTS----

#looks for text
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

#Website Title
def testTitleName(titlename):
    assert titlename in driver.title

#Welcome message 
def checkForWelcomeMessage():
    checkForText("Välkommen till")
    checkForText("FLORIST CELEBER")
    print("checkForWelcomeMessage test completed")

#Header Info
def headerInfo():
    checkForText("BUTIKER")
    checkForText("HEM")
    checkForText("PRODUKTER")
    checkForText("TJÄNSTER")
    print("headerInfo test completed")

#footer Info
def footerInfo():
    checkForText("Copyright © Florist Celeber 2021")
    print("footerInfo test completed")

#producs test
def productsInfo():
    checkForText("PRODUKTER")
    checkForText("Sommarbuketter")
    checkForText("Från")
    checkForText("200 kr")
    checkForText("Bröllopsbuketter")
    checkForText("1200 kr")
    checkForText("Begravningskrans")
    checkForText("800 kr")
    checkForText("Höstbuketter")
    checkForText("400 kr")
    checkForText("Rosor 10-pack")
    checkForText("150 kr")
    checkForText("Tulpaner 10-pack")
    checkForText("100 kr")
    print("productsInfo test completed")

#producs images
def productsImages():
    driver.find_element_by_xpath("//img[@alt='Sommarbuketter']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
    driver.find_element_by_xpath("//img[@alt='Bröllopsbuketter']")
    driver.find_element_by_xpath("//img[@alt='Begravningskrans']")
    driver.find_element_by_xpath("//img[@alt='Höstbuketter']")
    driver.find_element_by_xpath("//img[@alt='Rosor 10-pack']")
    driver.find_element_by_xpath("//img[@alt='Tulpaner 10-pack']")
    print("ProductsImages test completed")

#servives image and text
def services():
    checkForText("Services")
    checkForText("Konsultation 30 min")
    checkForText("250 kr")
    print("Services Test Completed")

#social media links 
def socialMediaLinks():
    facebookLink = driver.find_element_by_id("Facebook") #Locate id Facebook
    driver.execute_script("window.scrollTo(0, 100000)") #Scroll to bottom of page
    time.sleep(1)
    facebookLink.click()    #click link
    time.sleep(2)
    driver.back()    #go back to main site
    print("facebookLink Test Passed")

    time.sleep(1)
    twitterLink = driver.find_element_by_id("Twitter") ##SAME AS ABOVE
    driver.execute_script("window.scrollTo(0, 100000)")
    time.sleep(1)
    twitterLink.click()
    time.sleep(2)
    driver.back()
    print("twitterLink Test Passed")

    time.sleep(1)
    instagramLink = driver.find_element_by_id("Instagram")
    driver.execute_script("window.scrollTo(0, 100000)")
    time.sleep(1)
    instagramLink.click()
    time.sleep(2)
    driver.back()
    print("instagramLink Test Passed")

    print("Social media links test Completed")

#Store Buttons
def storeButtons():
    driver.find_element_by_xpath("//a[@href='kiruna/']")
    driver.find_element_by_xpath("//a[@href='lulea/']")
    print("storeButtons Test Completed")

#WelcomeToKiruna test
def welcomeKiruna():
    checkForText("KIRUNA")

#Opening Hours Info Kiruna
def checkForOpeningHoursKiruna():
    checkForText("Måndag - Fredag")
    checkForText("Lördag")
    checkForText("10-16")
    checkForText("12-15")
    print("checkForOpeningHours test completed")

#Find us Info Kiruna
def checkForAddressKiruna():
    checkForText("Fjällgatan 32H")
    checkForText("981 39")
    checkForText("Kiruna")
    print("checkForAdress test completed")

#Contact us Info Kiruna
def checkForContactKiruna():
    checkForText("0630-555-555")
    checkForText("info@itgwebb.se")
    print("checkForContact test completed")

#staff page info Kiruna
def staffInfoKiruna():
    checkForText("Fredrik Örtqvist")
    checkForText("Ägare")
    checkForText("Örjan Johansson")
    checkForText("Florist")
    checkForText("Anna Pettersson")
    checkForText("Hortonom")
    print("Staff Page Info Test Completed")

#staff page pictures Kiruna
def staffPicturesKiruna():
    driver.find_element_by_xpath("//img[@alt='Fredrik Örtqvist']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
    driver.find_element_by_xpath("//img[@alt='Anna Pettersson']")
    driver.find_element_by_xpath("//img[@alt='Örjan Johansson']")
    print("Staff page images test Completed")

#OpeningHoursLive Kiruna
def openingHoursliveKiruna():

    dates = [
        ["new Date('13 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #monday more than 30 minutes before opening
        ["new Date('13 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #monday less than 30 minutes before opening
        ["new Date('13 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #monday just after opening
        ["new Date('13 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #monday less than 1 hour before closing
        ["new Date('13 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #monday just after closing

        ["new Date('14 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #tuesday more than 30 minutes before opening
        ["new Date('14 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #tuesday less than 30 minutes before opening
        ["new Date('14 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #tuesday just after opening
        ["new Date('14 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #tuesday less than 1 hour before closing
        ["new Date('14 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #tuesday after closing

        ["new Date('15 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #wednesday more than 30 minutes before opening
        ["new Date('15 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #wednesday less than 30 minutes before opening
        ["new Date('15 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #wednesday just after opening
        ["new Date('15 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #wednesday less than 1 hour before closing
        ["new Date('15 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #wednesday after closing

        ["new Date('16 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #thursday more than 30 minutes before opening
        ["new Date('16 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #thursday less than 30 minutes before opening
        ["new Date('16 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #thursday just after opening
        ["new Date('16 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #thursday less than 1 hour before closing
        ["new Date('16 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #thursday after closing

        ["new Date('17 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #friday more than 30 minutes before opening
        ["new Date('17 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #friday less than 30 minutes before opening
        ["new Date('17 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #friday just after opening
        ["new Date('17 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #friday less than 1 hour before closing
        ["new Date('17 Sep 2021 18:05:00 GMT+2')", "Öppnar imorgon kl. 12"], #friday after closing

        ["new Date('18 Sep 2021 11:25:00 GMT+2')", "Öppnar idag kl. 12"], #saturday more than 30 minutes before opening
        ["new Date('18 Sep 2021 11:55:00 GMT+2')", "Öppnar snart"], #saturday less than 30 minutes before opening
        ["new Date('18 Sep 2021 12:05:00 GMT+2')", "Öppet just nu"], #saturday just after opening
        ["new Date('18 Sep 2021 14:05:00 GMT+2')", "Stänger snart"], #saturday less than 1 hour before closing
        ["new Date('18 Sep 2021 15:05:00 GMT+2')", "Öppnar på måndag kl. 10"], #saturday after closing
        #SUNDAY SHOULD BE CLOSED ALL DAY!!
        ["new Date('19 Sep 2021 9:25:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday more than 30 minutes before normal opening time
        ["new Date('19 Sep 2021 9:55:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday less than 30 minutes before normal opening time
        ["new Date('19 Sep 2021 10:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday just after normal opening time
        ["new Date('19 Sep 2021 15:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday less than 1 hour before normal closing time
        ["new Date('19 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday after normal closing time

        ["new Date('13 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # monday midnight
        ["new Date('14 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # tuesday midnight
        ["new Date('15 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # wednesday midnight
        ["new Date('16 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # thursday midnight
        ["new Date('17 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # friday midnight
        ["new Date('18 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 12"], # saturday midnight
        ["new Date('19 Sep 2021 00:00:00 GMT+2')", "Öppnar imorgon kl. 10"] # sunday midnight

    ]
    for i in dates:
        codeToExecute = "liveOpeningHours("+ i[0] +")"
        print(i)
        driver.execute_script(codeToExecute)
        checkForText(i[1])
    print("liveOpeningHours Test Completed  ")

#Welcome Luleå test
def welcomeLulea():
    checkForText("LULEÅ")

#Opening Hours Info Luleå
def checkForOpeningHoursLulea():
    checkForText("Måndagar")
    checkForText("Tisdagar")
    checkForText("Onsdagar")
    checkForText("Torsdagar")
    checkForText("Fredagar")
    checkForText("Lördag")
    checkForText("10-17")
    checkForText("10-16")
    checkForText("10-15")
    checkForText("12-15") 
    print("checkForOpeningHoursLulea test completed")

#Find us Info Luleå
def checkForAddressLulea():
    checkForText("Färjledsvägen 38")
    checkForText("961 93")
    checkForText("Luleå")
    checkForText("Södra Sunderbyn")
    print("checkForAdressLulea test completed")

#Contact us Info Luleå
def checkForContactLulea():
    checkForText("0640-555-333")
    checkForText("lulea@itgwebb.se")
    print("checkForContactLulea test completed")

#staff page info Luleå
def staffInfoLulea():
    checkForText("Anna Andersson")
    checkForText("Florist")
    checkForText("Johan Olsson")
    checkForText("Florist")
    checkForText("Elin Nygård")
    checkForText("Hortonom")
    print("Staff Page Info Lulea Test Completed")

#staff page pictures Luleå
def staffPicturesLulea():
    driver.find_element_by_xpath("//img[@alt='Anna Andersson']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
    driver.find_element_by_xpath("//img[@alt='Johan Olsson']")
    driver.find_element_by_xpath("//img[@alt='Elin Nygård']")
    print("Staff page images Lulea test Completed")

#OpeningHoursLive Luleå
def openingHoursliveLulea():

    dates = [
        ["new Date('13 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #monday more than 30 minutes before opening
        ["new Date('13 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #monday less than 30 minutes before opening
        ["new Date('13 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #monday just after opening
        ["new Date('13 Sep 2021 16:05:00 GMT+2')", "Stänger snart"], #monday less than 1 hour before closing
        ["new Date('13 Sep 2021 17:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #monday just after closing

        ["new Date('14 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #tuesday more than 30 minutes before opening
        ["new Date('14 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #tuesday less than 30 minutes before opening
        ["new Date('14 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #tuesday just after opening
        ["new Date('14 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #tuesday less than 1 hour before closing
        ["new Date('14 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #tuesday after closing

        ["new Date('15 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #wednesday more than 30 minutes before opening
        ["new Date('15 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #wednesday less than 30 minutes before opening
        ["new Date('15 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #wednesday just after opening
        ["new Date('15 Sep 2021 14:05:00 GMT+2')", "Stänger snart"], #wednesday less than 1 hour before closing
        ["new Date('15 Sep 2021 15:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #wednesday after closing

        ["new Date('16 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #thursday more than 30 minutes before opening
        ["new Date('16 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #thursday less than 30 minutes before opening
        ["new Date('16 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #thursday just after opening
        ["new Date('16 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #thursday less than 1 hour before closing
        ["new Date('16 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #thursday after closing

        ["new Date('17 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl. 10"], #friday more than 30 minutes before opening
        ["new Date('17 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #friday less than 30 minutes before opening
        ["new Date('17 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #friday just after opening
        ["new Date('17 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #friday less than 1 hour before closing
        ["new Date('17 Sep 2021 18:05:00 GMT+2')", "Öppnar imorgon kl. 12"], #friday after closing

        ["new Date('18 Sep 2021 11:25:00 GMT+2')", "Öppnar idag kl. 12"], #saturday more than 30 minutes before opening
        ["new Date('18 Sep 2021 11:55:00 GMT+2')", "Öppnar snart"], #saturday less than 30 minutes before opening
        ["new Date('18 Sep 2021 12:05:00 GMT+2')", "Öppet just nu"], #saturday just after opening
        ["new Date('18 Sep 2021 14:05:00 GMT+2')", "Stänger snart"], #saturday less than 1 hour before closing
        ["new Date('18 Sep 2021 15:05:00 GMT+2')", "Öppnar på måndag kl. 10"], #saturday after closing
        #SUNDAY SHOULD BE CLOSED ALL DAY!!
        ["new Date('19 Sep 2021 9:25:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday more than 30 minutes before normal opening time
        ["new Date('19 Sep 2021 9:55:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday less than 30 minutes before normal opening time
        ["new Date('19 Sep 2021 10:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday just after normal opening time
        ["new Date('19 Sep 2021 15:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday less than 1 hour before normal closing time
        ["new Date('19 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl. 10"], #sunday after normal closing time

        ["new Date('13 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # monday midnight
        ["new Date('14 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # tuesday midnight
        ["new Date('15 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # wednesday midnight
        ["new Date('16 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # thursday midnight
        ["new Date('17 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 10"], # friday midnight
        ["new Date('18 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl. 12"], # saturday midnight
        ["new Date('19 Sep 2021 00:00:00 GMT+2')", "Öppnar imorgon kl. 10"] # sunday midnight

    ]
    for i in dates:
        codeToExecute2 = "liveOpeningHours("+ i[0] +")"
        print(i)
        driver.execute_script(codeToExecute2)
        checkForText(i[1])
    print("liveOpeningHoursLulea Test Completed  ")


#Firefox

driver = webdriver.Firefox(executable_path='C:/webdrivers/geckodriver.exe')
driver.maximize_window()
def firefoxTests():
# runs all tests for the website
    driver.get(website)
    time.sleep(3)

    # Runs tests
    testTitleName("Florist Celeber")
    headerInfo()
    footerInfo()
    checkForWelcomeMessage()

    storeButtons()

    productsInfo()
    productsImages()

    #services()

    socialMediaLinks()


    # switch Page to kiruna page
    driver.get(kirunaPage)
    time.sleep(3) 

    # Runs Tests for staff page
    testTitleName("Florist Celeber")
    headerInfo()
    footerInfo()

    welcomeKiruna()
    checkForOpeningHoursKiruna()
    checkForAddressKiruna()
    checkForContactKiruna()

    staffInfoKiruna()
    staffPicturesKiruna()

    openingHoursliveKiruna()


    socialMediaLinks()

    # switch Page to luleå page
    driver.get(luleaPage)
    time.sleep(3) 

    # Runs Tests for staff page
    testTitleName("Florist Celeber")
    headerInfo()
    footerInfo()

    welcomeLulea()
    checkForOpeningHoursLulea()
    checkForAddressLulea()
    checkForContactLulea()

    staffInfoLulea()
    staffPicturesLulea()

    openingHoursliveLulea()


    socialMediaLinks()

    driver.close()