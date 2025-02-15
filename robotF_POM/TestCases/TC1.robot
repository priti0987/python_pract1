*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${Browser}      Chrome
${SiteUrl}      https://www.saucedemo.com/

*** Test Cases ***
LoginTestSauceDemoApp
    openMyApplication
    ValidateLoginPage
    EnterCredentials
    ValidateAfterLoginPage
    Add1stProductToCart
    sleep       3
*** Keywords ***
openMyApplication
    open browser                        ${SiteUrl}      ${Browser}
    Wait Until Element Is Visible       //input[@id='login-button']
    maximize browser window

ValidateLoginPage
    Page Should Contain Element     //input[@id='login-button']

EnterCredentials
    Input text        //input[@id='user-name']       standard_user
    Input text        //input[@id='password']        secret_sauce
    click button      //input[@id='login-button']
    Wait Until Page Contains        Products

ValidateAfterLoginPage
    Page Should Contain Element     //button[@id='react-burger-menu-btn']

Add1stProductToCart
    Click element      //img[@alt='Sauce Labs Backpack']
    Wait Until Page Contains Element        //button[@id='back-to-products']
    ${price}=       Get Text        //div[@class='inventory_details_price']
    log     ${price}