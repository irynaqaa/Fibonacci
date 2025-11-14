*** Settings ***
Library           RequestsLibrary
Resource          common_resources.robot
Suite Teardown    Delete Created Product

*** Variables ***
${BASE_URL}       http://localhost:5000/api/products  # Replace with the actual API endpoint

*** Test Cases ***
Create Product With Valid Payload
    [Documentation]    Verify that a product can be created with a valid payload.
    [Tags]    TC_PRODUCTS_005    High    Functional
    ${payload}=    Create Product Payload
    Create Product    ${payload}
    Validate Product Creation    ${payload}

*** Keywords ***
Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}