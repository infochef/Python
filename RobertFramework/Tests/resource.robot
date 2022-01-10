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
${Username}     rahulshettyacademy
${Password}     learning
${Site_Url}    https://rahulshettyacademy.com/loginpagePractise/     #https://www.phptravels.net/login

*** Keywords ***
open the browser with url
    Create Webdriver    Chrome
    maximize browser window
    Go To   ${Site_Url}

Close Browser Session
    Close Browser
