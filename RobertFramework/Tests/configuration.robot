*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Test Setup      open the browser with phptravels url
Test Teardown   Close Browser Session
Resource        resource.robot
# Selenium
*** Variables ***
${Error_Message_Login}      //div[@class='message']
${Homepage_element_visible}     //*[@class='main-menu-content']/nav/ul/li/a

*** Test Cases ***
Validate UnSuccesful login
    fill the login form     ${User_name}     ${Invalid_Password}
    wait until element is located in the page       ${Error_Message_Login}
    verify error message is displaying

Validate tab details in home page
    fill the login form     ${User_name}     ${Valid_Password}
    wait until element is located in the page       ${Homepage_element_visible}


*** Keywords ***
fill the login form
    [arguments]     ${Username}     ${Password}
    Input text      xpath://input[@placeholder='Email']     ${Username}
    input password  xpath://input[@placeholder='Password']  ${Password}
    click button    xpath://*[@type='submit']

wait until element is located in the page
    [arguments]     ${element}
    Wait Until Element Is Visible  ${Error_Message_Login}

verify error message is displaying
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings  ${result}    Wrong credentials. try again!
