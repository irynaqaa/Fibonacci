*** Settings ***
Library           RequestsLibrary

*** Keywords ***
Create Product Data
    [Documentation]    Create a dictionary with valid product data.
    ${data}=    Create Dictionary    name=Test Product    price=19.99    description=This is a test product.
    RETURN    ${data}

Create Invalid Product Data
    [Documentation]    Create a dictionary with invalid product data.
    ${invalid_data}=    Create Dictionary    name=    price=not_a_number
    RETURN    ${invalid_data}

Generate Fibonacci Numbers
    [Arguments]    ${n}
    [Documentation]    Generate Fibonacci numbers up to the nth number.
    ${response}=    GET On Session    ${FIBONACCI_ENDPOINT}    params={"n": ${n}}
    Should Be Equal As Strings    ${response.status_code}    200    'Expected status code 200'
    RETURN    ${response.json()}

Delete Product After Tests
    [Documentation]    Clean up by deleting the product created during tests.
    [Arguments]    ${product_id}
    ${response}=    DELETE On Session    ${PRODUCT_ENDPOINT}/${product_id}
    Should Be Equal As Strings    ${response.status_code}    204    'Expected status code 204'
    Log    Product with ID ${product_id} deleted successfully.