*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
RegTest
    open browser    https://demowebshop.tricentis.com/register      chrome
    maximize browser window
    ${timeout}=     get selenium timeout

    set selenium timeout    2 seconds
    wait until page contains       Register
    select radio button     Gender      F
    input text      name:FirstName      testname
    input text      name:LastName       testlastname

    sleep       3