*** Setting ***
Library     SeleniumLibrary

*** Variables ***
${Browser}      Chrome
${SiteUrl}      https://demo.nopcommerce.com/

*** Test Cases ***
LoginTestNopcommerce
    open browser     ${SiteUrl}      ${Browser}
    sleep       3

