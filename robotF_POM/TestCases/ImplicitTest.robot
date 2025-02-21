*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
RegTest
    open browser    https://demowebshop.tricentis.com/register      chrome
    maximize browser window
    set selenium implicit wait      3 seconds
    select radio button     Gender      F
    input text      name:FirstName1      testname
    input text      name:LastName       testlastname
    sleep       3