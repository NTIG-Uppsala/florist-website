from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

driver = webdriver.Chrome()
driver.get("http://www.itgwebb.se/klass/webb2/christoffer/dev/")

# a path to the site
website = "http://www.itgwebb.se/klass/webb2/christoffer/dev/"
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

#Find us Info
def checkForAddress():
    checkForText("Fjällgatan 32H")
    checkForText("981 39")
    checkForText("Kiruna")

#Contact us Info
def checkForContact():
    checkForText("0630-555-555")
    checkForText("info@itgwebb.se")

#Header Info
def headerInfo():
    checkForText("INFO")
    checkForText("ÖPPETTIDER")
    checkForText("HITTA OSS")
    checkForText("KONTAKTUPPGIFTER")

#footer Info
def footerInfo():
    checkForText("Copyright © Florist Celeber 2021")


#OpeningHoursLive
def openingHourslive():

    dates = [
        ["new Date('13 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #måndag innan strax öppning
        ["new Date('13 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #måndag innan snart öppning
        ["new Date('13 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #måndag efter öppning
        ["new Date('13 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #måndag innan stängning
        ["new Date('13 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #måndag efter stängning

        ["new Date('14 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #tisdag innan strax öppning
        ["new Date('14 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #tisdag innan snart öppning
        ["new Date('14 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #tisdag efter öppning
        ["new Date('14 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #tisdag innan stängning
        ["new Date('14 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #tisdag efter stängning

        ["new Date('15 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #onsdag innan strax öppning
        ["new Date('15 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #onsdag innan snart öppning
        ["new Date('15 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #onsdag efter öppning
        ["new Date('15 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #onsdag innan stängning
        ["new Date('15 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #onsdag efter stängning

        ["new Date('16 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #torsdag innan strax öppning
        ["new Date('16 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #torsdag innan snart öppning
        ["new Date('16 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #torsdag efter öppning
        ["new Date('16 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #torsdag innan stängning
        ["new Date('16 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #torsdag efter stängning

        ["new Date('17 Sep 2021 9:25:00 GMT+2')", "Öppnar idag kl 10"], #fredag innan strax öppning
        ["new Date('17 Sep 2021 9:55:00 GMT+2')", "Öppnar snart"], #fredag innan snart öppning
        ["new Date('17 Sep 2021 10:05:00 GMT+2')", "Öppet just nu"], #fredag efter öppning
        ["new Date('17 Sep 2021 15:05:00 GMT+2')", "Stänger snart"], #fredag innan stängning
        ["new Date('17 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 12"], #fredag efter stängning

        ["new Date('18 Sep 2021 11:25:00 GMT+2')", "Öppnar idag kl 12"], #lördag innan strax öppning
        ["new Date('18 Sep 2021 11:55:00 GMT+2')", "Öppnar snart"], #lördag innan snart öppning
        ["new Date('18 Sep 2021 12:05:00 GMT+2')", "Öppet just nu"], #lördag efter öppning
        ["new Date('18 Sep 2021 14:05:00 GMT+2')", "Stänger snart"], #lördag innan stängning
        ["new Date('18 Sep 2021 15:05:00 GMT+2')", "Öppnar på måndag kl 10"], #lördag efter stängning
        
        ["new Date('19 Sep 2021 9:25:00 GMT+2')", "Öppnar imorgon kl 10"], #söndag innan strax öppning
        ["new Date('19 Sep 2021 9:55:00 GMT+2')", "Öppnar imorgon kl 10"], #söndag innan snart öppning
        ["new Date('19 Sep 2021 10:05:00 GMT+2')", "Öppnar imorgon kl 10"], #söndag efter öppning
        ["new Date('19 Sep 2021 15:05:00 GMT+2')", "Öppnar imorgon kl 10"], #söndag innan stängning
        ["new Date('19 Sep 2021 16:05:00 GMT+2')", "Öppnar imorgon kl 10"], #söndag efter stängning

        ["new Date('13 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # måndag midnatt
        ["new Date('14 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # tisdag midnatt
        ["new Date('15 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # onsdag midnatt
        ["new Date('16 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # torsdag midnatt
        ["new Date('17 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 10"], # fredag midnatt
        ["new Date('18 Sep 2021 00:00:00 GMT+2')", "Öppnar idag kl 12"], # lördag midnatt
        ["new Date('19 Sep 2021 00:00:00 GMT+2')", "Öppnar imorgon kl 10"] # söndag midnatt
    ]
    for i in dates:
        codeToExecute = "liveOpeningHours("+ i[0] +")"
        print(codeToExecute)
        driver.execute_script(codeToExecute)
        checkForText(i[1])

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

        driver.save_screenshot( "Screenshots/Image (" + str(res[0]) + " x " + str(res[1]) + ")" + dt_string + ".png")
        
        driver.close()


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

openingHourslive()

driver.close()

screenShots(screenResolution)