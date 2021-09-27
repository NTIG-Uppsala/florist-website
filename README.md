# florist-website
## [Website](http://www.itgwebb.se/klass/webb2/christoffer/florist-celeber/)

# Documentation

## florist-celeber

#### index.html
- Main file that structures the website.

### kiruna
#### index.html
- Main file for subpage

### lulea
#### index.html
- Main file for subpage

### Favicon
- favicon.ico
- android-chrome-192x192.png
- android-chrome-512x512.png
- apple-touch-icon.png
- browserconfig.xml
- favicon-16x16.png
- favicon-32x32.png
- mstile-150x150.png
- safari-pinned-tab.svg
- site.webmanifest

### Assets
#### img
- Contains images for the website.

### CSS
#### styles.css
- All styles for the elements (Bootstrap).
#### style.css
- Our own CSS code.

### JavaScript
#### script.js
- Menu becomes readable on smaller resolutions by making it a drop-down menu.
- The header becomes smaller when scrolling downwards and it stays on top.
- Live opening hours feature

### Tests
#### main.py
- Runs all the tests

#### chrome.py
-creates tests for Chrome webdriver

#### firefox.py
-creates tests for Firefox webdriver

#### edge.py
-creates tests for Edge webdriver

#### opera.py
-creates test for Opera webdriver

#### screenshotTests.py
-takes screenshots in different resolutions on all web browsers

### Webdrivers
- chromedriver.exe
- geckodriver.exe
- operadriver.exe
- msedgedriver.exe 
- msedgedriver requieres the following addon
- py -m pip install msedge-selenium-tools selenium==3.141

### Pre-commit Tests for devpage
#### In .git/hooks/pre-commit
```
#!/bin/bash

start chrome "https://validator.nu/?doc=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fflorist-celeber" #HTML
start chrome "https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fflorist-celeber%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en" #CSS
start chrome "https://validator.w3.org/checklink?uri=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fflorist-celeber&hide_type=all&depth=&check=Check" #Links on the webpages
start chrome "https://codebeautify.org/jsvalidate?url=http://www.itgwebb.se/klass/webb2/christoffer/dev/florist-celeber/js/scripts.js" #JS
start chrome "https://validator.nu/?doc=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fflorist-celeber%2Fkiruna%2F" #HTML for kiruna-page
start chrome "https://validator.nu/?doc=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fflorist-celeber%2Flulea%2F" #HTML for lulea-page

```
