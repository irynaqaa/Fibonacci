*** Keywords ***
Create Product Payload
    [Documentation]    Create a valid product payload.
    ${payload}=    Create Dictionary    name=Test Product    price=19.99    description=This is a test product.
    RETURN    ${payload}

Create Product
    [Arguments]    ${payload}
    Create Session    product_api    ${BASE_URL}
    ${response}=    POST On Session    product_api    /    json=${payload}
    Should Be Equal As Strings    ${response.status_code}    201    'Expected status code 201'

Validate Product Creation
    [Arguments]    ${payload}
    ${response}=    GET On Session    product_api    /${payload['name']}
    Should Be Equal As Strings    ${response.status_code}    200    'Expected status code 200'
    Should Be Equal As Strings    ${response.json()['name']}    ${payload['name']}    'Product name should match'

Delete Created Product
    [Documentation]    Clean up by deleting the created product.
    ${response}=    GET On Session    product_api    /${payload['name']}
    ${product_id}=    ${response.json()['id']}
    DELETE On Session    product_api    /${product_id}