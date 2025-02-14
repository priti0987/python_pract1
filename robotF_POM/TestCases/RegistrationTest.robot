*** Settings ***
Library        SeleniumLibrary
Resource        ../Resources/Registration.robot

*** Variables ***
${Browser}      Chrome
${SiteUrl}      https://demo.guru99.com/test/newtours/

*** Test Cases ***
RegistrationTest
    Open my browser     ${SiteUrl}      ${Browser}
    sleep       3
    Click on Regration Link
    Enter FirstName     Priti
    Enter lastName      Fuse
    Enter phone         8899779988
    Enter email         test@gmail.com
    Enter add1          Nerull
    Enter city          Mumbai
    Enter state         Maharastra
    Enter postCode      9988
    Select country      ALBANIA
    Enter userName      priti123
    Enter Password      indiA@1
    Enter confirmedPassword     indiA@1
    Click submit