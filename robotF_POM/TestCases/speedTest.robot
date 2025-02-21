*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
RegTest
    ${selspeed}=    get selenium speed
    log        ${selspeed}
    open browser    https://demowebshop.tricentis.com/register      chrome
    maximize browser window
    set selenium speed      2 seconds
    select radio button     Gender      F
    input text      name:FirstName      testname
    input text      name:LastName       testlastname
    ${selspeed}=    get selenium speed
    log        ${selspeed}

    sleep       3