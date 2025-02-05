*** Settings ***
Library     SeleniumLibrary
Variables   ../PageObjects/Locators.py

*** Keywords ***
Open my browser
    [Arguments]     ${SiteUrl}      ${Browser}
    open browser    ${SiteUrl}      ${Browser}
    Maximize Browser Window

Enter UserName
    [Arguments]     ${username}
    Input Text      txt_loginUserName     ${username}

Enter password
    [Arguments]     ${password}
    Input Text      txt_loginPassword     ${password}

Click SignIn
    click button    ${btn_signIn}

Verify Successfull Login
    title should be Find a Flight: Mercury Tours:

Close my browser
    close all browsers