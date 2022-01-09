*** Settings ***
Documentation   A resource file with reusable keywords and variables
...
...             The system specific keywords created here from our own
...             domain specific language. They utilize keywords provided
...             by the imported SeleniumLibrary.
Library         SeleniumLibrary

*** Variables ***
${User_name}     user@phptravels.com
${Invalid_Password}        user
${Valid_Password}        demouser
${Site_Url}     https://www.phptravels.net/login

*** Keywords ***
open the browser with phptravels url
    Create Webdriver    Chrome
    maximize browser window
    Go To   ${Site_Url}

Close Browser Session
    Close Browser
