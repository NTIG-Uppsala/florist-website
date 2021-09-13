# florist-website


## Definition of Done

### General
- Website published to the web
- All files listed in README.md
- Try not to commit files with known errors, the day before deadline

### Code
- Code refactored
- Comments describing functions in JavaScript files
- Other comments if needed
- Reviewed by teammate
- Committed to GitHub

### Tests
- Tests made
- Tests passed

#### Resolution Tests
- Test with 5 different resolutions
- Use Toggle Device Toolbar (Ctrl + Shift + M)
- Screenshots are not needed just have to be looked at

##### Different test modes
- Nexus 5X (412x732)
- Galaxy S5 (360x640)
- iPhone 5/SE (320x568)
- iPhone X (375x812)
- iPad (768x1024)

## Development Environment

### IDE
- Visual Studio Code v1.59.1

### Extensions
- HTML CSS Support v1.10.2
- HTML Snippets v1.10.2
- JavaScript (ES6) code snippets v1.8.0
- ESLint v2.1.23

### Git
- GitHub
- Git-bash
- NTIG-Uppsala Organization
- Explanatory commit message

### Other
- Google Chrome v92.0.4515.195
- [Selenium IDE](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd) chrome extension v3.17.0
- [The Nu HTML Checker](https://validator.github.io/validator/) v20.6.30

## Programming Language
- English function names and variable names
- English comments
- Comments before function
- If comment mid function wright it 4 spaces after semicolon
- camelCasing on functions, variable names, id and more
- File name camelCasing

### HTML
#### Standard
- index.html
- Use ""
- External CSS
- External JavaScript
- Defer in script tag
- Language tag "sv"
- HTML Charset UTF-8
```
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="ENTER PATH" defer></script>
    <link rel="stylesheet" href="ENTER PATH">
    <link rel="icon" type="image/png" href="ENTER PATH">
    <title>ENTER TITLE</title>
</head>
<body>

</body>
</html>
```

### CSS
#### Standard
- Use all browser's animation standards
- padding: 0px; on body tag
- margin: 0px; on body tag
- No position: absolute;

### JavaScript
#### Standard
- Use ' '
- Let/Const for variables
- Opening curly bracket end of first line
- Use one space before the opening bracket
- Place the curly closing bracket on a new line
- Arrays, every item new line
- Space around operands and after commas
- Always use 4 spaces for indentation of code blocks
- Avoid long lines
- Avoid global variables

## Other Specifications

- [Tabler Icons](https://tablericons.com/) MIT License
- [Bootstrap](https://github.com/startbootstrap/startbootstrap-agency) MIT License

# Documentation

## florist-celeber

#### index.html
- Main file that structures the website.

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
- Our own css code.

### JavaScript
#### script.js
- Menu becomes readable on smaller resolutions by making it a drop-down menu.
- The header becomes smaller when scrolling downwards and it stays on top.

### Tests
- infoButtonTest.side
- websiteInfoTextTest.side
- socialMediaLinksTest.side
- copyrightTextTest.side
- dropdownMenuMobileTest.side
- clickonLinksTest.side
- clickonMenuLinksTest.side
- clickonMobilMenuLinksTest.side

### Pre-commit Tests for devpage
#### In .git/hooks/pre-commit
```
#!/bin/bash



PATH TO BROWSER "https://validator.nu/?doc=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev" #HTML
PATH TO BROWSER "http://jigsaw.w3.org/css-validator/validatoruri=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en" #CSS
PATH TO BROWSER "https://validator.w3.org/checklink?uri=http%3A%2F%2Fwww.itgwebb.se%2Fklass%2Fwebb2%2Fchristoffer%2Fdev&hide_type=all&depth=&check=Check" #Links on webpage
PATH TO BROWSER "https://codebeautify.org/jsvalidate?url=http://www.itgwebb.se/klass/webb2/christoffer/dev/js/scripts.js" #JS
```
