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

print("*********\n\nSmithsonian Institution Records Search\n\n*********\n")

# Search input to filter the request
search = input("Enter a search category here: ")

# Building url and submitting to server 
response = requests.get(f'https://api.si.edu/openaccess/api/v1.0/search?api_key=egqk7unCsFkJqCiurbvF1x4gNZZyjKJwCIBVt5qw&q={search}&rows=10')

# Storing response
json_string = response.content

# Parsing json 
parsed_json = json.loads(json_string)

# Grabbing the rows array from the request
response = parsed_json['response']['rows']

#print top 10 items from search 
try:
    print("\nTop 10 Results:\n")
    for item in response:
        print(f'Title: {item["title"]}\nUnitcode: {item["unitCode"]}\nID: {item["id"]}\nDatasource: {item["content"]["freetext"]["dataSource"][0]["content"]}\n')
except:
    pass 



