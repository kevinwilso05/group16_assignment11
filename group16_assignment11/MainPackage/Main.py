'''
Name: Kevin Wilson, Brett Perez
email: perezbd@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations: 
https://edan.si.edu/openaccess/apidocs/#api-_
Anything else that's relevant:
'''
# API Link: view-source:https://api.si.edu/openaccess/api/v1.0/search?api_key=egqk7unCsFkJqCiurbvF1x4gNZZyjKJwCIBVt5qw&q=history

import json
import requests

response = requests.get('https://api.si.edu/openaccess/api/v1.0/search?api_key=egqk7unCsFkJqCiurbvF1x4gNZZyjKJwCIBVt5qw&q=history')
json_string = response.content
    
parsed_json = json.loads(json_string)

print(parsed_json)