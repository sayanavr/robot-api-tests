*** Settings ***
Library    RequestsLibrary
Library    Process

*** Variables ***
${API_URL}  https://jsonplaceholder.typicode.com

*** Test Cases ***
Get All Users And Send Email
    [Documentation]    This test case makes an API call and then sends an email via SNS using a Python script.
    
    # Make a GET request to the API
    ${response}=  GET  ${API_URL}/users
    
    # Check if the response status is 200
    Status Should Be  200  ${response}
    
    # Verify that a user is found in the response text
    Should Contain  ${response.text}  "Leanne Graham"
    
    # After successful API request, send the email via SNS
    Run Process    python    emailReport.py

