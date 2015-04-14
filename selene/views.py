from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import create
import time
import random

# Create your views here.
@api_view(['GET'])
def walk(request):
   if request.method == 'GET':
      r = create.Create('/dev/tty.ElementSerial-ElementSe')
      done = r.walk()
      if not done:
         return JsonResponse({'response': 503})
      return JsonResponse({'response': 200})
   return JsonResponse({'response': 404})
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
    time_need = distance*10
    r.go(10)
    st = int(round(time.time()))
    print(st)
    ft = st + time_need
    bump=r.getSensor('BUMPS_AND_WHEEL_DROPS')
    rt = st
    print(bump, ft, rt)
    while ft > rt and ((bump[3] !=1 and bump[4]!=1)):
       bump=r.getSensor('BUMPS_AND_WHEEL_DROPS')
       rt = int(round(time.time()))
       print(bump,ft,rt)
    print("I am about to stop")
    r.stop()
    r.go(0,0)
    if bump[3]==1 or bump[4]==1:
       print(rt-st)
       r.go(0,45)
       time.sleep(4)
       r.stop()
       r.go(10)
       time.sleep(rt-st)
       r.stop()
       r.go(0,45)
       time.sleep(4)
       r.stop()
