from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json
import timeit
# Create your views here.
@api_view(["POST"])
def fibonacci(num):
	la = 1
	la1 =1
	try:
		start_time = timeit.timeit()
		n = json.loads(num.body)

		for i in range(n):
			if i<1:
				c = la

			elif i == 1:
				c = la1

			else:
				c=la1+la
				la=la1
				la1=c
		end_time = timeit.timeit()
		total_time_taken = end_time - start_time
		return Response({'res':c,'time_taken':total_time_taken})

	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
