# python-Flask-demo-usage-Project-

Question1 : Write API: 
Using Python Flask or ExpressJS, Write a REST API that reads the body and  returns JSON.
 
API Method POST
 URL : /find_symbols_in_names
 
# Input JSON Body of the API:
{
    "chemicals": ['Amazon', 'Microsoft', 'Google'],
    "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
}
 
# Output: display the chemical names with their symbol surrounded by square brackets:
{
    "result": "[Am]azon, Mi[cro]soft, Goog[le]"
}
