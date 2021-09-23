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
website = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber"

# a path to subpage Kiruna
kirunaPage = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/kiruna"

# a path to subpage Luleå
luleaPage = "https://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/lulea"


# resolution for screenshots
# d = desktop
# m = mobile
screenResolution = [[1920, 1080, "d"], [2560, 1440, "d"], [2500, 5000, "d"], [1080, 1920, "m"], [360, 640, "m"], [812, 375 ,"m"]]

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
        driver.get(kirunaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Chrome " + "kiruna" + ".png")

        driver.get(luleaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Chrome " + "lulea" + ".png")

        driver.close()

        #FIREFOX

        driver = webdriver.Firefox(executable_path="C:/webdrivers/geckodriver.exe")
        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Firefox " + ".png")
        
        # Loads staff Page 
        driver.get(kirunaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Firefox " + " kiruna" + ".png")


        driver.get(luleaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Firefox " + "lulea" + ".png")

        driver.close()

        #Microsoft Edge

        driver = webdriver.Edge(executable_path='C:/webdrivers/msedgedriver.exe')

        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Edge " + ".png")
        
        # Loads staff Page 
        driver.get(kirunaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Edge " + " kiruna" + ".png")

        driver.get(luleaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Edge " + "lulea" + ".png")

        driver.close()

         #Opera

        driver = webdriver.Opera(executable_path="C:/webdrivers/operadriver.exe")

        driver.get(website) 

        # sleeps for 3 seconds to make sure site is fully loaded!
        time.sleep(3) 

        driver.save_screenshot( "../../Screenshots/Image (" + dt_string  + str(res[0]) + " x " + str(res[1]) + ")" + " Opera " + ".png")
        
        # Loads staff Page 
        driver.get(kirunaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" + " Opera " + " kiruna" + ".png")

        driver.get(luleaPage)

        time.sleep(3) 

        # Saves images in map 2 steps back. format(time, resolution 1 x resolution 2)(.jpg can be changed to other image types)
        driver.save_screenshot( "../../Screenshots/Image (" + dt_string + str(res[0]) + " x " + str(res[1]) + ")" +  " Opera " + "lulea" + ".png")

        driver.close()
        
    print("Screenshots completed")