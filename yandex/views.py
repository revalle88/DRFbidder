from django.shortcuts import render
from django.http import HttpResponse

#import json, urllib2, requests
import sys, datetime
import csv

#from yandex_direct import api
#from pprint import pprint

import requests, json
from requests.exceptions import ConnectionError
from time import sleep
from bidder.models import Campaign, Keyword

# Pythonic style

url4 = 'https://api.direct.yandex.ru/live/v4/json/'
url5 = 'https://api.direct.yandex.ru/json/v5/'
url4test = 'https://api-sandbox.direct.yandex.ru/live/v4/json/'
token = 'AQAAAAAfNADPAARs8_hXK0DksE3nlBtnQogvjKk'
login = 'test.gradient'
clientLogin = 'test.gradient'
CampaignsURL = 'https://api-sandbox.direct.yandex.com/json/v5/campaigns'
keywordsURL = 'https://api-sandbox.direct.yandex.com/json/v5/keywords'

clientLogin = 'test.gradient'
token = 'AQAAAAAfNADPAARs8_hXK0DksE3nlBtnQogvjKk'

def u(x):
	if type(x) == type(b''):
		return x.decode('utf8')
	else:
		return x



def index(request):
	# --- Подготовка, выполнение и обработка запроса ---
	#  Создание HTTP-заголовков запроса
	headers = {"Authorization": "Bearer " + token,  # OAuth-токен. Использование слова Bearer обязательно
	"Client-Login": 'test.gradient',  # Логин клиента рекламного агентства
	"Accept-Language": "ru",  # Язык ответных сообщений
	}

	# Создание тела запроса
	body = {"method": "get",  # Используемый метод.
	"params": {"SelectionCriteria": {},  # Критерий отбора кампаний. Для получения всех кампаний должен быть пустым
	"FieldNames": ["Id", "Name"]  # Имена параметров, которые требуется получить.
	}}

	# Кодирование тела запроса в JSON
	jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
	print(jsonBody)
# Выполнение запроса
	try:
		result = requests.post(CampaignsURL, jsonBody, headers=headers)
		print(result.status_code)
		if result.status_code != 200 or result.json().get("error", False):
			print("Произошла ошибка при обращении к серверу API Директа.")
			print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
			print("Описание ошибки: {}".format(u(result.json()["error"]["error_detail"])))
			print("RequestId: {}".format(result.headers.get("RequestId", False)))
		else:
			Campaign.objects.all().delete()
			print("RequestId: {}".format(result.headers.get("RequestId", False)))
			print("Информация о баллах: {}".format(result.headers.get("Units", False)))
			# Вывод списка кампаний
			for campaign in result.json()["result"]["Campaigns"]:
				print("Рекламная кампания: {} №{}".format(u(campaign['Name']), campaign['Id']))
				cmp = Campaign(directId=campaign['Id'], name=campaign['Name'])
				cmp.save()
			if result.json()['result'].get('LimitedBy', False):
			# Если ответ содержит параметр LimitedBy, значит,  были получены не все доступные объекты.
			# В этом случае следует выполнить дополнительные запросы для получения всех объектов.
			# Подробное описание постраничной выборки - https://tech.yandex.ru/direct/doc/dg/best-practice/get-docpage/#page
				print("Получены не все доступные объекты.")
# Обработка ошибки, если не удалось соединиться с сервером API Директа
	except ConnectionError:
	# В данном случае мы рекомендуем повторить запрос позднее
		print("Произошла ошибка соединения с сервером API.")

# Если возникла какая-либо другая ошибка
	except:
		print("Произошла непредвиденная ошибка.")

	campaign_list = Campaign.objects.all()
	print (campaign_list)
	return HttpResponse("Hello, world. You're at the polls index.")

	'''
	CampaignsListData={}
	#pprint(api.get_regions().get('data'))
	#return HttpResponse("Hello, world. You're at the polls index.")
	'''
def keywords(request, campaign_id):
	print("CAMPAIGN_ID")
	print(campaign_id)
	cmp = Campaign.objects.get(directId=campaign_id)
	# --- Подготовка, выполнение и обработка запроса ---
	#  Создание HTTP-заголовков запроса
	headers = {"Authorization": "Bearer " + token,  # OAuth-токен. Использование слова Bearer обязательно
	"Client-Login": 'test.gradient',  # Логин клиента рекламного агентства
	"Accept-Language": "ru",  # Язык ответных сообщений
	}

	# Создание тела запроса
	body = {"method": "get",  # Используемый метод.
	"params": {"SelectionCriteria": {
										"CampaignIds":[campaign_id],
									},  # Критерий отбора кампаний. Для получения всех кампаний должен быть пустым
	"FieldNames": ["Id", "Keyword", "Bid"]  # Имена параметров, которые требуется получить.
	}}

	# Кодирование тела запроса в JSON
	jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
	print(jsonBody)
# Выполнение запроса
	try:
		result = requests.post(keywordsURL, jsonBody, headers=headers)
		print(result.status_code)
		print(result)
		if result.status_code != 200 or result.json().get("error", False):
			print("Произошла ошибка при обращении к серверу API Директа.")
			print("Код ошибки: {}".format(result.json()["error"]["error_code"]))
			print("Описание ошибки: {}".format(u(result.json()["error"]["error_detail"])))
			print("RequestId: {}".format(result.headers.get("RequestId", False)))
		else:
			Keyword.objects.all().delete()
			print("RequestId: {}".format(result.headers.get("RequestId", False)))
			print("Информация о баллах: {}".format(result.headers.get("Units", False)))
			# Вывод списка кампаний
			print(result.json())
			for keyword in result.json()["result"]["Keywords"]:
				print("Step")
				print("Keyword: {} №{} Bid:{}".format(u(keyword['Keyword']), keyword['Id'], keyword['Bid']))
				kwd = Keyword(directId=keyword['Id'], keyword=keyword['Keyword'], bid = keyword['Bid'], campaign = cmp )
				kwd.save()
			if result.json()['result'].get('LimitedBy', False):
			# Если ответ содержит параметр LimitedBy, значит,  были получены не все доступные объекты.
			# В этом случае следует выполнить дополнительные запросы для получения всех объектов.
			# Подробное описание постраничной выборки - https://tech.yandex.ru/direct/doc/dg/best-practice/get-docpage/#page
				print("Получены не все доступные объекты.")
# Обработка ошибки, если не удалось соединиться с сервером API Директа
	except ConnectionError:
	# В данном случае мы рекомендуем повторить запрос позднее
		print("Произошла ошибка соединения с сервером API.")

# Если возникла какая-либо другая ошибка
	except:
		print("Произошла непредвиденная ошибка.")

	#keyword_list = Keyword.objects.all()
	#print (keyword_list)
	return HttpResponse("Hello, world. You're at the polls index.")
