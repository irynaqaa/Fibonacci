*** Settings ***
Library           RequestsLibrary
Resource          common_resources.robot

*** Variables ***
${BASE_URL}       http://localhost:5000

*** Test Cases ***
Create Product With Valid Payload
    [Documentation]    Create a new product with valid payload
    [Tags]    TC_PRODUCT_CREATION_001    High    Functional
    ${payload}    Create Dictionary    name=Test Product    price=10.99    description=This is a test product
    ${response}    Post Request    ${BASE_URL}/products    data=${payload}    headers=${VALID_HEADERS}
    Should Be Equal As Strings    ${response.status_code}    201
    ${product_id}    Get Json Value    ${response.content}    $.id
    Should Not Be Empty    ${product_id}
    [Teardown]    Delete Product    ${product_id}

Query Product Existence
    [Documentation]    Verify product existence in the database
    [Tags]    TC_PRODUCT_EXISTENCE_001    High    Functional
    ${response}    Get Request    ${BASE_URL}/products/1
    Should Be Equal As Strings    ${response.status_code}    200
    ${product_name}    Get Json Value    ${response.content}    $.name
    Should Be Equal As Strings    ${product_name}    Test Product

Create Product With Missing Fields
    [Documentation]    Create a new product with missing fields
    [Tags]    TC_PRODUCT_CREATION_002    Medium    Negative
    ${payload}    Create Dictionary    price=10.99    description=This is a test product
    ${response}    Post Request    ${BASE_URL}/products    data=${payload}    headers=${VALID_HEADERS}
    Should Be Equal As Strings    ${response.status_code}    400

Create Product With Invalid Data Types
    [Documentation]    Create a new product with invalid data types
    [Tags]    TC_PRODUCT_CREATION_003    Medium    Negative
    ${payload}    Create Dictionary    name=Test Product    price=invalid    description=This is a test product
    ${response}    Post Request    ${BASE_URL}/products    data=${payload}    headers=${VALID_HEADERS}
    Should Be Equal As Strings    ${response.status_code}    400

*** Keywords ***
Delete Product
    [Arguments]    ${product_id}
    ${response}    Delete Request    ${BASE_URL}/products/${product_id}
    Should Be Equal As Strings    ${response.status_code}    204