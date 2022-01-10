*** Settings ***
Documentation   To validate the login form
Library     SeleniumLibrary
Library     Collections
Test Setup      open the browser with url
Test Teardown   Close Browser Session
Resource        resource.robot
# Selenium
*** Variables ***
${Error_Message_Login}      //div[@class='message']
${Homepage_element_visible}     //*[@class='main-menu-content']/nav/ul/li/a

*** Test Cases ***
#Validate UnSuccesful login
#    fill the login form     ${User_name}     ${Invalid_Password}
#    wait until element is located in the page       ${Error_Message_Login}
#    verify error message is displaying

#Validate tab details in home page
#    fill the login form     ${User_name}     ${Valid_Password}
#    wait until element is located in the page       ${Homepage_element_visible}
#    verify card titles in home page
#    select the card     Hotels

Validate login page and login form
    Fill the login details and login form   ${Username}     ${Password}

*** Keywords ***
fill the login form
    [arguments]     ${Username}     ${Password}
    Input text      xpath://input[@placeholder='Email']     ${Username}
    input password  xpath://input[@placeholder='Password']  ${Password}
    click button    xpath://*[@type='submit']

wait until element is located in the page
    [arguments]     ${element}
    Wait Until Element Is Visible  ${Homepage_element_visible}

verify error message is displaying
    ${result}=  Get Text    ${Error_Message_Login}
    Should Be Equal As Strings  ${result}    Wrong credentials. try again!

verify card titles in home page
    @{Expectedlist}=    Create List     Home    Hotels  Flights     Tours   Cars    Visa    Blog    Offers  Company
    ${elements}=    Get WebElements     xpath://*[@class='main-menu-content']/nav/ul/li/a
    @{actuallist}=  Create List

    FOR     ${element}  IN   @{elements}
        Log     ${element.text}
        Append To List  ${actuallist}   ${element.text}

    END
    Lists Should Be Equal   ${Expectedlist}     ${actuallist}

select the card
    [arguments]     ${cardname}
    @{elements}=    Get WebElements     xpath://*[@class='main-menu-content']/nav/ul/li/a
    ${index}=   Set Variable    1
    FOR     ${element}  IN   @{elements}
        Exit For loop if    "${cardname}" == "${element.text}"

        ${index} =     Evaluate     ${index} + 1
    END

    Click Link  link:${cardname}

Fill the login details and login form
    [arguments]     ${username}     ${password}
    Input text      id:username     ${Username}
    Input password  id:password     ${Password}
    Click Element   css:input[value='user']
    Wait Until Element Is Visible   css:.modal-body
    Click Element   id:okayBtn
    Wait Until Element Is Not Visible   css:.modal-body
    Select From List By Value   css:select.form-control     teach
    Select Checkbox     terms