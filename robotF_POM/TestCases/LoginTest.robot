*** Settings ***
Library        SeleniumLibrary
Resource        ../Resources/LoginKeywords.robot

*** Variables ***
${Browser}      Chrome
${SiteUrl}      https://demo.guru99.com/test/newtours/
${username}     tutorial
${password}     tutorial


*** Test Cases ***
LoginTest
    Open my browser     ${SiteUrl}      ${Browser}
    sleep       5
    Enter UserName      ${username}
    Enter Password      ${password}
    Click SignIn
    sleep       10
    Verify Successfull Login