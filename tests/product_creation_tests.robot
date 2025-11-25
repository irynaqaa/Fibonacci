*** Settings ***
Library           RequestsLibrary
Resource          application/tests/common_resources.robot
Suite Teardown    Delete Product After Tests    ${product_id}

*** Variables ***
${BASE_URL}      http://localhost:8000
${PRODUCT_ENDPOINT}    ${BASE_URL}/products

*** Test Cases ***
Create Product With Valid Data
    [Documentation]    Verify that a product can be created with valid data.
    [Tags]    TC_PRODUCTS_001    High    Functional
    ${data}=    Create Product Data    Test Product    10.99
    ${response}=    POST On Session    ${PRODUCT_ENDPOINT}    json=${data}
    Should Be Equal As Strings    ${response.status_code}    201    'Expected status code 201'
    ${response_body}=    GET On Session    ${PRODUCT_ENDPOINT}/${data['id']}
    Should Contain    ${response_body}    ${data['name']}
    Should Contain    ${response_body}    ${data['price']}

Create Product With Invalid Data
    [Documentation]    Ensure that creating a product with invalid data fails.
    [Tags]    TC_PRODUCTS_002    High    Negative
    ${invalid_data}=    Create Invalid Product Data
    ${response}=    POST On Session    ${PRODUCT_ENDPOINT}    json=${invalid_data}
    Should Be Equal As Strings    ${response.status_code}    400    'Expected status code 400'

*** Keywords ***
Delete Product After Tests
    [Documentation]    Clean up by deleting the product created during tests.
    [Arguments]    ${product_id}
    ${response}=    DELETE On Session    ${PRODUCT_ENDPOINT}/${product_id}
    Should Be Equal As Strings    ${response.status_code}    204    'Expected status code 204'
    Log    Product with ID ${product_id} deleted successfully.
