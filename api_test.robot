*** Settings ***
Library  RequestsLibrary

*** Variables ***
${API_URL}  https://jsonplaceholder.typicode.com

*** Test Cases ***
Get All Users
    ${response}=  GET  ${API_URL}/users
    Status Should Be  200  ${response}
    Should Contain  ${response.text}  "Leanne Graham"

