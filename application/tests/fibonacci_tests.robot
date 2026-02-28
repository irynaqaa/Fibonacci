*** Settings ***
Library           Collections
Library           RequestsLibrary
Resource          ../tests/resources/common_resources.robot

*** Variables ***
${FIBONACCI_URL}    http://localhost:5000/fibonacci  # Replace with the actual endpoint
# Valid input number for Fibonacci sequence generation: 5

*** Test Cases ***
Valid Fibonacci Sequence Generation
    [Documentation]    Verify that the Fibonacci sequence is generated correctly for a given number.
    [Tags]    TC_FIBO_001    High    Functional
    Send Fibonacci Request    5
    ${body}=    Get Response    ${response}
    Should Be Equal As Strings    ${body['sequence']}    [0, 1, 1, 2, 3]    'Expected Fibonacci sequence for 5'
    [Teardown]    Log    Completed Valid Fibonacci Sequence Generation Test

Invalid Fibonacci Sequence Generation Request
    [Documentation]    Ensure that an error is returned for invalid input.
    [Tags]    TC_FIBO_002    High    Negative
    ${response}=    Post Request    ${FIBONACCI_URL}    json=${{"number": -1}}
    Should Be Equal As Strings    ${response.status_code}    400    'Expected status code 400 for invalid input'
    [Teardown]    Log    Completed Invalid Fibonacci Sequence Generation Test

Invalid Fibonacci Sequence Generation Non-Integer
    [Documentation]    Ensure that an error is returned for non-integer input.
    [Tags]    TC_FIBO_003    High    Negative
    ${response}=    Post Request    ${FIBONACCI_URL}    json=${{"number": "string"}}
    Should Be Equal As Strings    ${response.status_code}    400    'Expected status code 400 for non-integer input'
    [Teardown]    Log    Completed Invalid Fibonacci Sequence Generation Non-Integer Test

Generate Fibonacci for valid input
    [Documentation]    Sends a POST request to generate Fibonacci sequence for a valid number.
    [Tags]    TC_FIBO_004    High    Functional
    Send Fibonacci Request    5
    ${body}=    Get Response    ${response}
    Should Be Equal As Strings    ${body['sequence']}    [0, 1, 1, 2, 3]    'Expected Fibonacci sequence for 5'
    [Teardown]    Log    Completed Generate Fibonacci for Valid Input Test

*** Keywords ***
Send Fibonacci Request
    [Documentation]    Sends a POST request to the Fibonacci endpoint with a valid number and checks the response status.
    [Arguments]    ${number}
    ${response}=    Post Request    ${FIBONACCI_URL}    json=${{"number": ${number}}}
    Should Be Equal As Strings    ${response.status_code}    200    'Expected status code 200'

Stub Keyword
    [Arguments]    ${keyword_name}    @{args}
    Log    Stub: Called ${keyword_name} with arguments ${args}
    RETURN    ${EMPTY}