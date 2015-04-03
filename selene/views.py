from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
  return
@api_view(['GET'])
def turn(request):
  pass
@api_view(['GET'])
def u_turn(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, 45)
    time.sleep(4)
    r.stop()
  return
@api_view(['GET'])
def turn_left(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, 45)
    time.sleep(2)
    r.stop()
  return
@api_view(['GET'])
def turn_right(request):
  if request.method == 'GET':
    r = create.Create('/dev/tty.ElementSerial-ElementSe')
    r.go(0, -45)
    time.sleep(2)
    r.stop()
  return
@api_view(['GET'])
def turn(request):
  pass
