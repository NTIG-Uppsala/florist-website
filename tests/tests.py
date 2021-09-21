from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

from selenium.webdriver.opera.webdriver import OperaDriver



# a path to the site..
website = "http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber"

# a path to subpage personalsida
staffPage = "http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/personalsida"

# resolution for screenshots
# d = desktop
# m = mobile
screenResolution = [[1920, 1080, "d"], [2560, 1440, "d"], [1080, 1920, "m"], [360, 640, "m"], [640, 360, "m"], [812, 375 ,"m"]]

#----TESTS----

#looks for text
def checkForText(text):
    assert text in driver.find_element_by_xpath("/html/body").text

#Website Title
def testTitleName(titlename):
    assert titlename in driver.title

#Opening Hours Info
def checkForOpeningHours():
    checkForText("Måndag - Fredag")
    checkForText("Lördag")
    checkForText("10-16")
    checkForText("12-15")
    print("checkForOpeningHours test completed")

#Welcome message 
def checkForWelcomeMessage():
    checkForText("Välkommen till")
    checkForText("FLORIST CELEBER")
    print("checkForWelcomeMessage test completed")

#Staff Introduction
def checkForStaffIntroduction():
    checkForText("Detta är")
    checkForText("VÅR UNDERBARA PERSONAL")
    print("checkForStaffIntroduction test completed")

#Find us Info
def checkForAddress():
    checkForText("Fjällgatan 32H")
    checkForText("981 39")
    checkForText("Kiruna")
    print("checkForAdress test completed")

#Contact us Info
def checkForContact():
    checkForText("0630-555-555")
    checkForText("info@itgwebb.se")
    print("checkForContact test completed")

#Header Info
def headerInfo():
    checkForText("INFO")
    checkForText("HEM")
    checkForText("PERSONAL")
    print("headerInfo test completed")

#footer Info
def footerInfo():
    checkForText("Copyright © Florist Celeber 2021")
    print("footerInfo test completed")

#staff page info
def staffPageInfo():
    checkForText("Fredrik Örtqvist")
    checkForText("Ägare")
    checkForText("Örjan Johansson")
    checkForText("Florist")
    checkForText("Anna Pettersson")
    checkForText("Hortonom")
    print("Staff Page Info Test Completed")

#producs test
def productsInfo():
    checkForText("Sommarbukett")
    checkForText("Från")
    checkForText("200 kr")
    checkForText("Bröllopsbruketter")
    checkForText("1200 kr")
    checkForText("Begravningskrans")
    checkForText("800 kr")
    checkForText("Höstbukett")
    checkForText("400 kr")
    checkForText("Rosor 10-pack")
    checkForText("150 kr")
    checkForText("Tulpaner 10-pack")
    checkForText("100 kr")
    checkForText("Konsultation 30 min")
    checkForText("250 kr")
    print("productsInfo test completed")

def productsImages():
    driver.find_element_by_xpath("//img[@alt='Sommarbukett']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
    driver.find_element_by_xpath("//img[@alt='Bröllopsbruketter']")
    driver.find_element_by_xpath("//img[@alt='Begravningskrans']")
    driver.find_element_by_xpath("//img[@alt='Höstbukett']")
    driver.find_element_by_xpath("//img[@alt='Rosor 10-pack']")
    driver.find_element_by_xpath("//img[@alt='Tulpaner 10-pack']")
    driver.find_element_by_xpath("//img[@alt='Konsultation 30 min']") 
    print("ProductsImages test completed")

#staff page pictures
def staffPagePictures():
    driver.find_element_by_xpath("//img[@alt='Fredrik Örtqvist']") #Locates The Alt @ in all Image @ If the alt Is correct the image shall be there. Proof can be seen In screenshot
    driver.find_element_by_xpath("//img[@alt='Anna Pettersson']")
    driver.find_element_by_xpath("//img[@alt='Örjan Johansson']")
    print("Staff page images test Completed")

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

#OpeningHoursLive
def openingHourslive():

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

#Screenshots
def screenShots(resolutions):

    now = datetime.now()
    for res in resolutions:

        # adds a time stamp for the screenshots
        dt_string = now.strftime(" , %d-%m-%Y , %Hh %Mm %Ss")

        # checks if the resolution is for mobile or desktop.
        if(res[2] == "d"):
            # sets the resolution for the desktop emulation
            emulation = {
                "deviceMetrics": { "width": res[0], "height": res[1], "pixelRatio": 1.0 }
            }
        elif(res[2] == "m"):
            # sets the resolution for the mobile emulation
            emulation = {
                "deviceMetrics": { "width": res[0], "height": res[1], "pixelRatio": 1.0 },
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        else:
            print(res + "invalid device type")




        #CHROME

        chrome_options = Options()
        # runs the emulation for different resolutions
        chrome_options.add_experimental_option("mobileEmulation", emulation)

        driver = webdriver.Chrome( options = chrome_options)

        

        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Chrome " +".png")
        
        # Loads staff Page 
        driver.get(staffPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Chrome " + "staffpage" + ".png")

        driver.close()

        #FIREFOX

        driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")
        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Firefox " + ".png")
        
        # Loads staff Page 
        driver.get(staffPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Firefox " + " staffpage" + ".png")

        driver.close()

        #Microsoft Edge

        driver = webdriver.Edge(executable_path='C:/webdrivers/msedgedriver.exe')

        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Edge " + ".png")
        
        # Loads staff Page 
        driver.get(staffPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Edge " + " staffpage" + ".png")

        driver.close()

         #Opera

        driver = webdriver.Opera(executable_path="C:/webdrivers/operadriver.exe")

        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Opera " + ".png")
        
        # Loads staff Page 
        driver.get(staffPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Opera " + " staffpage" + ".png")

        driver.close()
        
    print("Screenshots completed")

#----RUN TESTS
#CHROME
driver = webdriver.Chrome(executable_path="C:/webdrivers/chromedriver.exe")
driver.maximize_window()

# runs all tests for the website
driver.get(website)
time.sleep(3)

# Runs tests
testTitleName("Florist Celeber")
checkForOpeningHours()
checkForAddress()
checkForContact()
headerInfo()
footerInfo()
checkForWelcomeMessage()

openingHourslive()

productsInfo()
productsImages()



socialMediaLinks()



# switch Page to staff page
driver.get(staffPage)
time.sleep(3) 

# Runs Tests for staff page
testTitleName("Florist Celeber")
headerInfo()
footerInfo()

staffPageInfo()
staffPagePictures()
checkForStaffIntroduction()

socialMediaLinks()
driver.close()



#FIREFOX

driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")
driver.maximize_window()

driver.get(website)
time.sleep(3)

# Runs tests
testTitleName("Florist Celeber")
checkForOpeningHours()
checkForAddress()
checkForContact()
headerInfo()
footerInfo()
checkForWelcomeMessage()

productsInfo()
productsImages()

socialMediaLinks()

openingHourslive()

# switch Page to staff page
driver.get(staffPage)
time.sleep(3) 

# Runs Tests for staff page
testTitleName("Florist Celeber")
headerInfo()
footerInfo()

staffPageInfo()
staffPagePictures()
checkForStaffIntroduction()

socialMediaLinks()
driver.close()


#Microsoft Edge 

driver = Edge(executable_path='C:/webdrivers/msedgedriver.exe')
driver.maximize_window()

driver.get(website)
time.sleep(3)

# Runs tests
testTitleName("Florist Celeber")
checkForOpeningHours()
checkForAddress()
checkForContact()
headerInfo()
footerInfo()
checkForWelcomeMessage()

productsInfo()
productsImages()

socialMediaLinks()

openingHourslive()

# switch Page to staff page
driver.get(staffPage)
time.sleep(3) 

# Runs Tests for staff page
testTitleName("Florist Celeber")
headerInfo()
footerInfo()

staffPageInfo()
staffPagePictures()
checkForStaffIntroduction()

socialMediaLinks()
driver.close()

#Opera

driver = OperaDriver(executable_path='C:/webdrivers/operadriver.exe')
driver.maximize_window()

driver.get(website)
time.sleep(3)

# Runs tests
testTitleName("Florist Celeber")
checkForOpeningHours()
checkForAddress()
checkForContact()
headerInfo()
footerInfo()
checkForWelcomeMessage()

productsInfo()
productsImages()

socialMediaLinks()

openingHourslive()

# switch Page to staff page
driver.get(staffPage)
time.sleep(3) 

# Runs Tests for staff page
testTitleName("Florist Celeber")
headerInfo()
footerInfo()

staffPageInfo()
staffPagePictures()
checkForStaffIntroduction()

socialMediaLinks()
driver.close()

screenShots(screenResolution)
print("ALL TESTS PASSED!")