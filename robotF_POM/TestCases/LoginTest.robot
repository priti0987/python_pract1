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