*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${Browser}      Chrome
${SiteUrl}      https://www.saucedemo.com/

*** Test Cases ***
LoginTestNopcommerce
    open browser     ${SiteUrl}      ${Browser}
    Wait Until Element Is Visible       //input[@id='login-button']
    maximize browser window
    Input text        //input[@id='user-name']       standard_user
    Input text        //input[@id='password']       secret_sauce
    click button      //input[@id='login-button']
    Wait Until Page Contains        Products

