*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
When counter is set to ten the value becomes ten
    Go To  ${HOME_URL}
    Input Text  number  10
    Click Button  aseta
    Page Should Contain  nappia painettu 10 kertaa

When counter is set to zero the value becomes zero
    Go To  ${HOME_URL}
    Input Text  number  0
    Click Button  aseta
    Page Should Contain  nappia painettu 0 kertaa

When counter is set to negative ten the value becomes negative ten
    Go To  ${HOME_URL}
    Input Text  number  -10
    Click Button  aseta
    Page Should Contain  nappia painettu -10 kertaa