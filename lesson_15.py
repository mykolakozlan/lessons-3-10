#поліморфізм
#re

#requests (urllib.parse, urlparse)
#security (dotenv, load_dotenv)
import json
import re
import requests
from requests_oauthlib import OAuth1

# # class BBox:
# #     def __init__(self, x0, y0, x1, y1):
# #         self._x0 = x0
# #         self._y0 = y0
# #         self._x1 = x1
# #         self._y1 = y1
# #
# #     def __repr__(self):
# #         return f"({self._x0};{self._y0})-({self._x1};{self._y1})"
# #
# #     def __add__(self, other):
# #         new_x0 = min(self._x0, other._x0)
# #         new_y0 = min(self._y0, other._y0)
# #         new_x1 = max(self._x1, other._x1)
# #         new_y1 = max(self._y1, other._y1)
# #         return BBox(new_x0, new_y0, new_x1,new_y1)
# #
# #     def __gt__(self, other):
# #         area_1 = self.get_area()
# #         area_2 = other.get_area()
# #         return area_1 > area_2
# #
# #     def get_area(self):
# #         return (self._x1 - self._x0) * (self._y1 - self._y0)
# #
# #
# # bb_box_1 = BBox(7, 3, 5,2)
# # # print(bb_box_1.get_area())
# # bb_box_2 = BBox(4, 1, 2,3)
# # # bb_box_3 = bb_box_1.__add__(bb_box_2)
# # # bb_box_3 = bb_box_1 + bb_box_2
# # # result = bb_box_1 > bb_box_2
# #
# # # print(result)
# #
# # box_list = [bb_box_1, bb_box_2]
# # print(sorted(box_list, reverse=True))
#
# ########### re #########
#
#
# def read_json(filename):
#     with open(filename, 'r') as f:
#         data = json.load(f)
#     return data
#
#
# def sort_by_name(some_dict):
#     return some_dict["name"].split()[-1]
#
#
# def sort_by_bday(some_dict):
#     yaers = some_dict["years"]
#     # patern = r'\d+'    # [0-9] = \d - only digits \w - word only letters, [a-z] - всі маленькі літери латиницею [A-Za-z] - вся латиниця [А-Я] - всі великі кирилиці(рос) [А-ЯІЇГ] - українська
#     # years = re.findall(r'\d+', yaers)
#     years = re.findall(r'[0-9]+', yaers)
#     bday = int(years[0]) if "BC" not in some_dict["years"] else - int(years[0])
#     # print(years)
#     return bday
#
#
# def sort_by_text_len(some_dict):
#     return len(some_dict["text"].split())
#
#
# def custom_sorter(some_dict):
#     return sort_by_bday(some_dict), some_dict["name"].split()[-1], some_dict["name"].split()[0], sort_by_text_len(some_dict)
#
#
# data = read_json('math.json')
# sorted_data = sorted(data, key=sort_by_text_len, reverse=True)
# print(sorted_data)
























# response = requests.get('https://forismatic.com/en/#50716b4968/')
# print(response.status_code, response.content)


# url = "http://api.forismatic.com/api/1.0/"
#
# params = {"method": "getQuote",
#           "format": "json",
#           "key": 1,
#           "lang": "en"}
#
# response = requests.get(url, params=params)
# # print(response.status_code, response.json())
#
# data = response.json()
# print(data['quoteText'])







import os
from dotenv import load_dotenv

load_dotenv()                                   # виклик ключів через .env файл
SECRET_API_KEY = os.getenv("SECRET_API_KEY")
print(SECRET_API_KEY)




# api = os.getenv('API_TEST')      # викликає змінні віртуального середовища
#
# print(api)






# auth = OAuth1(api_key, secret_api_key)
# endpoint = "https://api.thenounproject.com/v2/icon/1"
#
# response = requests.get(endpoint, auth=auth)
# print(response.content)














