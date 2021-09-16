from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

driver = webdriver.Chrome()
driver.get("http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber")


# a path to the site..
website = "http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber"

# a path to subpage personalsida
staffPage = "http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/personalsida"

# resolution for screenshots
# d = desktop
# m = mobile
screenResolution = [[1920, 1080, "d"], [2560, 1440, "d"], [1080, 1920, "m"], [360, 640, "m"]]

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
    checkForText("ÖPPETTIDER")
    checkForText("HITTA OSS")
    checkForText("KONTAKTUPPGIFTER")
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

#staff page pictures
def staffPagePictures():
    driver.find_element_by_id("staff")#staff member 1
    driver.find_element_by_id("staff")#staff member 2
    driver.find_element_by_id("staff")#staff member 3
    print("Staff page images test Completed")
#OpeningHoursLive
def openingHourslive():

    dates = [
        ["new Date('13 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #monday before just opening
        ["new Date('13 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #monday before soon opening
        ["new Date('13 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #monday after opening
        ["new Date('13 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #monday before closing
        ["new Date('13 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #monday after closing

        ["new Date('14 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #tuesday before just opening
        ["new Date('14 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #tuesday before soon opening
        ["new Date('14 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #tuesday after opening
        ["new Date('14 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #tuesday before closing
        ["new Date('14 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #tuesday after closing

        ["new Date('15 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #wednesday before just opening
        ["new Date('15 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #wednesday before soon opening
        ["new Date('15 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #wednesday after opening
        ["new Date('15 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #wednesday before closing
        ["new Date('15 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #wednesday after closing

        ["new Date('16 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #thursday before just opening
        ["new Date('16 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #thursday before soon opening
        ["new Date('16 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #thursday after opening
        ["new Date('16 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #thursday before closing
        ["new Date('16 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #thursday after closing

        ["new Date('17 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #friday before just opening
        ["new Date('17 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #friday before soon opening
        ["new Date('17 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #friday after opening
        ["new Date('17 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #friday before closing
        ["new Date('17 Sep 2021 18:05:00 GMT+2')", "Öppnar imorgon kl 12"], #friday after closing

        ["new Date('18 Sep 2021 11:25:00 GMT+2')", "Öppnar idag kl 12"], #saturday before just opening
        ["new Date('18 Sep 2021 11:55:00 GMT+2')", "Öppnar snart"], #saturday before soon opening
        ["new Date('18 Sep 2021 12:05:00 GMT+2')", "Öppet just nu"], #saturday after opening
        ["new Date('18 Sep 2021 14:05:00 GMT+2')", "Stänger snart"], #saturday before closing
        ["new Date('18 Sep 2021 15:05:00 GMT+2')", "Öppnar på måndag kl 10"], #saturday after closing
        
        ["new Date('19 Sep 2021 9:25:00 GMT+2')", "Öppnar imorgon kl 10"], #sunday before just opening
        ["new Date('19 Sep 2021 9:55:00 GMT+2')", "Öppnar imorgon kl 10"], #sunday before soon opening
        ["new Date('19 Sep 2021 10:05:00 GMT+2')", "Öppnar imorgon kl 10"], #sunday after opening
        ["new Date('19 Sep 2021 15:05:00 GMT+2')", "Öppnar imorgon kl 10"], #sunday before closing
        ["new Date('19 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #sunday after closing

        ["new Date('13 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # monday midnight
        ["new Date('14 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # tuesday midnight
        ["new Date('15 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # wednesday midnight
        ["new Date('16 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # thursday midnight
        ["new Date('17 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # friday midnight
        ["new Date('18 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 12"], # saturday midnight
        ["new Date('19 Sep 2021 00:00:00 GMT+2')", "Öppnar imorgon kl 10"] # sunday midnight

    ]
    for i in dates:
        codeToExecute = "liveOpeningHours("+ i[0] +")"
        print(i)
        driver.execute_script(codeToExecute)
        checkForText(i[1])
    print("liveOpeningHours Test Completed")

#Screenshots
def screenShots(resolutions):

    now = datetime.now()
    for res in resolutions:

        # adds a time stamp for the screenshots
        dt_string = now.strftime(" , %d-%m-%Y , %Hh %Mm %Ss")

        # checks if the resolution is for mobile or desktop
        if(res[2] == "d"):
            # sets the resolution for the desktop emulation
            emulation = {
                "deviceMetrics": { "width": res[0], "height": res[1], "pixelRatio": 1.0 }
            }
        elif(res[2] == "m"):
            # sets the resolution for the mobile emulation
            emulation = {
                "deviceMetrics": { "width": res[0], "height": res[1], "pixelRatio": 1.0 },
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
            }
        else:
            print(res + "invalid device type")

        chrome_options = Options()
        
        # runs the emulation for different resolutions
        chrome_options.add_experimental_option("mobileEmulation", emulation)


        driver = webdriver.Chrome( options = chrome_options)


        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + ".jpg")
        
        driver.get(staffPage)

        time.sleep(3) 

        driver.save_screenshot( "Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " staffpage" + ".jpg")

        driver.close()



        
    print("Screenshots completed")

#----RUN TESTS
# runs all tests for the website
# runs driver separately from the screenshot function
driver.get(website)
# sleeps for 3 seconds to make sure site is fully loaded!
time.sleep(3)


testTitleName("Florist Celeber")
checkForOpeningHours()
checkForAddress()
checkForContact()
headerInfo()
footerInfo()
checkForWelcomeMessage()
openingHourslive()

driver.get(staffPage)
time.sleep(3) 

testTitleName("Florist Celeber")
headerInfo()
footerInfo()

staffPageInfo()
staffPagePictures()
checkForStaffIntroduction()
driver.close()
screenShots(screenResolution)
print("ALL TESTS PASSED!")