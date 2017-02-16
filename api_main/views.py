from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .serializers import magic_box_all_serializer
from rest_framework import permissions
import urllib.request
from bs4 import BeautifulSoup
import re

items = []
class magic_box_product(object):
	def __init__(self, product_name, product_cost, product_url):
		self.product_name = product_name
		self.product_cost = product_cost
		self.product_url = product_url

class magic_box_all(APIView):
	def get(self, request):
		url = 'https://www.infibeam.com/deal-of-the-day/'
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		f = urllib.request.urlopen(req)
		soup = BeautifulSoup(f, 'html.parser')
		#get all items' price
		all_item_price = soup.findAll("div", { "class" : "final-price" })
		all_item_prices = [x.find('span', {"class" : "price"}).text for x in all_item_price]
		#get all items' name and link
		mb_items_all = soup.findAll("h1", {'class':re.compile('^product-title-')})
		if (len(mb_items_all) != 56):
			return Response("Internal Error")
		print(len(mb_items_all))
		item_names = [x.find('a').text for x in mb_items_all]
		all_item_names = item_names[::2]
		item_links = [x.find('a')['href'] for x in mb_items_all]
		all_item_links = item_links[::2]
		for item in range(0, len(all_item_names)):
			single_item = magic_box_product(all_item_names[item], all_item_prices[item], all_item_links[item])
			items.append(single_item)
		serialized_items = magic_box_all_serializer(items, many=True)
		return Response(serialized_items.data)