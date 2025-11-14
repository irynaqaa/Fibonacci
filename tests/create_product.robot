*** Settings ***
Library           RequestsLibrary
Library           BuiltIn
Resource          common_resources.robot

*** Variables ***
${BASE_URL}      http://localhost:8000

*** Test Cases ***
Create A New Product With Valid Payload
    [Documentation]    Verify that a new product can be created with valid payload.
    [Tags]    TC_PRODUCTS_001    High    Functional
    ${payload}=    Create Product Payload
    Create Session    my_api_session    ${BASE_URL}
    ${response}=    Post Request    my_api_session    /products    json=${payload}
    Should Be Equal As Numbers    ${response.status_code}    201    'Expected status code 201'
    Should Contain    ${response.json()}    Sample Product    'Expected product name in response'
    Should Contain    ${response.json()}    This is a sample product description.    'Expected product description in response'
    Should Contain    ${response.json()}    19.99    'Expected product price in response'
    Should Contain    ${response.json()}    100    'Expected product stock in response'

*** Keywords ***
Create Product Payload
    [Documentation]    Create a valid payload for product creation.
    [Arguments]    
    ${payload}=    Create Dictionary    name=Sample Product    description=This is a sample product description.    price=19.99    in_stock=100
    RETURN    ${payload}

Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}