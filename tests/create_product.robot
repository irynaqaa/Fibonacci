*** Settings ***
Library           RequestsLibrary
Library           JSONLibrary

*** Variables ***
${BASE_URL}      http://localhost:8000  # Replace with the actual base URL of your FastAPI application

*** Test Cases ***
Create New Product
    [Documentation]    Test the creation of a new product with valid payload.
    [Tags]    TC_PRODUCT_001    High    Functional
    ${payload}=    Create Dictionary    name=Test Product    description=This is a test product    price=19.99    in_stock=100
    ${response}=    POST On Session    mysession    ${BASE_URL}/products    json=${payload}
    Should Be Equal As Strings    ${response.status_code}    201
    ${response_body}=    Get From Response    ${response}
    Should Contain    ${response_body}    Test Product
    Should Contain    ${response_body}    This is a test product
    Should Contain    ${response_body}    19.99
    Should Contain    ${response_body}    100
    # Verify product in database
    ${product_id}=    Get From Dictionary    ${response_body}    id
    ${get_response}=    GET On Session    mysession    ${BASE_URL}/products/${product_id}
    Should Be Equal As Strings    ${get_response.status_code}    200

Create Product With Invalid Payload
    [Documentation]    Test the creation of a product with an invalid payload.
    [Tags]    TC_PRODUCT_002    High    Negative
    ${invalid_payload}=    Create Dictionary    name=    # Missing required fields
    ${response}=    POST On Session    mysession    ${BASE_URL}/products    json=${invalid_payload}
    Should Be Equal As Strings    ${response.status_code}    400

*** Keywords ***
Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}