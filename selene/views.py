from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import create
import time

# Create your views here.
@api_view(['GET'])
def walk(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(10)
    time.sleep(1)
    r.stop()
    response = JsonResponse({'response': 200})
  return response
@api_view(['GET'])
def turn(request):
  pass
@api_view(['GET'])
def u_turn(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, 180)
    time.sleep(1)
    r.stop()
    response = JsonResponse({'response': 200})
  return response
@api_view(['GET'])
def turn_left(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, 90)
    time.sleep(1)
    r.stop()
    response = JsonResponse({'response': 200})
  return response
@api_view(['GET'])
def turn_right(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, -90)
    time.sleep(1)
    r.stop()
    response = JsonResponse({'response': 200})
  return response
def walk_back():
  u_turn()
@api_view(['GET'])
def wwalk(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.sense()
    thistime = time.time()
    while (r.bump_left or r.bump_right) and ttime:
      
      r.sense()
