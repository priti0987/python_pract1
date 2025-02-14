*** Settings ***
Library     SeleniumLibrary
Variables   ..//PageObjects//Locators.py

*** Keywords ***
Open my browser
    [Arguments]     ${SiteUrl}      ${Browser}
    open browser    ${SiteUrl}      ${Browser}
    Maximize Browser Window

Click on Regration Link
    click link      ${link_reg}

Enter FirstName
    [Arguments]     ${FirstName}
    Input Text      ${txt_firstName}     ${FirstName}

Enter lastName
    [Arguments]	    ${lastName}
    Input Text      ${txt_lastName}     ${lastName}

Enter phone
    [Arguments]	    ${phone}
    Input Text      ${txt_phone}    ${phone}

Enter email
    [Arguments]	    ${email}
    Input Text      ${txt_email}    ${email}

Enter add1
    [Arguments]	    ${add1}
    Input Text      ${txt_add1}     ${add1}

Enter city
    [Arguments]	    ${city}
    Input Text      ${txt_city}     ${city}

Enter state
    [Arguments]	    ${state}
    Input Text      ${txt_state}    ${state}

Enter postCode
    [Arguments]	    ${postCode}
    Input Text      ${txt_postCode}     ${postCode}

Select country
    [Arguments]	    ${country}
    select from list by label     ${drp_country}      ${country}

Enter userName
    [Arguments]	    ${userName}
    Input Text      ${txt_userName}     ${userName}

Enter Password
    [Arguments]	    ${Password}
    Input Text      ${txt_Password}     ${Password}

Enter confirmedPassword
    [Arguments]	    ${confirmedPassword}
    Input Text      ${txt_confirmedPassword}    ${confirmedPassword}

Click submit
        click button    ${btn_submit}





Verify Successfull Login
    page should contain    Thank you for registering

Close my browser
    close all browsers