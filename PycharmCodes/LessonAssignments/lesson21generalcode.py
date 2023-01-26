import json

import requests

# def bored_api_random():
#     bored_url = "https://www.boredapi.com/api/activity"
#     response = requests.get(bored_url)
#     if response.status_code == 200:
#         print(f"type of response {type(response)}")
#         response_as_dict = json.loads(response.text)
#         print(f"type of response_as_dict {type(response_as_dict)}")
#         print(response_as_dict['activity'])
#     else:
#         # raise exception
#         # raise error
#         # whatever
# bored_api_random()

###query parameters
# genderize_url = "https://api.genderize.io"
# # query_parameter_url = "https://www.api.genderize.io/?name=omer"  #name=omer$city=telaviv
# genderize_url = "https://api.genderize.io/"
# response = requests.get(genderize_url, params={'name': 'omer'})
# if response.status_code == 200:
#     print(response.json()['gender'])

###path parameters
# countries_url = 'https://restcountries.com/v3.1/{name}'

if __name__ == '__main__':
    countries_url = 'https://restcountries.com/v3.1/'
