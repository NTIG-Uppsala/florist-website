import time
from screenshotTests import screenShots, screenResolution
import opera
import edge
import chrome
import firefox

# Runs tests

chrome.chromeTests()

firefox.firefoxTests()

edge.edgeTests()

opera.operaTests()

screenShots(screenResolution)