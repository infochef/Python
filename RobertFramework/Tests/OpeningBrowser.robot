*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Test Teardown   Close Browser
# Resources
# Selenium
*** Variables ***
${Error_Message_Login}      //div[@class='message']

*** Test Cases ***
Validate UnSuccesful login
    open the browser with phptravels url
    fill the login form
    wait until it checks and display the error message
    verify error message is displaying

*** Keywords ***
open the browser with phptravels url
    Create Webdriver    Chrome
    maximize browser window
    Go To   https://www.phptravels.net/login

fill the login form
    Input text      xpath://input[@placeholder='Email']     abd@gmail.com
    input password  xpath://input[@placeholder='Password']  12345678
    click button    xpath://*[@type='submit']

wait until it checks and display the error message
    Wait Until Element Is Visible  ${Error_Message_Login}

verify error message is displaying
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings  ${result}    Wrong credentials. try again!
