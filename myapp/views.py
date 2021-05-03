from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
import yaml
from datetime import datetime, timedelta
import jwt

# Helper Functions

def jwttoken(payload,JWT_SECRET = 'secret',JWT_ALGORITHM = 'HS256'):
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return jwt_token

def yamlfileopener(filename):
    filen = "myapp/{}.yaml".format(filename)
    with open(filen, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        #print(data)
        #print("Read successful")
        yamlfile.close()
    return data

def yamlfileloader(data,filename):
    filen = "myapp/{}.yaml".format(filename)
    with open(filen, 'w') as yfile:
        obj = yaml.dump(data, yfile)
        #print(data)
        #print("Write successful")
        yfile.close()

# Create your views here.

def index(request):
    return HttpResponse("Nurture Assignment - Vinayak Lal")

@csrf_exempt
def register(request):
    if request.method == 'GET':
        return HttpResponse("GET Request",status=200)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        for v in data.values():
            #print(v,list(data.values()))
            if len(v.strip()) > 0:
                flag = False
            else:
                flag = True
                break
        #print(flag)
        if flag:
            return HttpResponse("Bad Request",status=400)
        else:   
            users = yamlfileopener("users")
            name = data['name']
            email = data['email']
            password = data['password']
            userid = len(users) + 1
            details ={'userid':userid,'username':name,'email':email,'password':password}
            users.append(details)
            yamlfileloader(users,"users")
            jwt_token = jwttoken(details)
            json_object = json.dumps({"UserID":userid,"Token":jwt_token}, indent = 4)  
            #print(json_object) 
            return HttpResponse(json_object,status=200)
    else:
        return HttpResponse("Bad Request",status=400)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return HttpResponse("GET Request",status=200)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        users = users = yamlfileopener("users")
        for user in users:
            if user["username"] == data["username"] and user["password"] == data["password"]:
                flag = True
                user_details = user
                break
            else:
                flag = False
        #print(flag)
        if flag:
            jwt_token = jwttoken(user_details)
            json_object = json.dumps({"UserID":user_details['userid'],"Token":jwt_token}, indent = 4)
            #print(json_object)
            return HttpResponse(json_object,status=200)
        else:
            return HttpResponse("Bad Request",status=400)
    else:
        return HttpResponse("Bad Request",status=400)


@csrf_exempt
def get_advisor(request,user_id):
    print(user_id)
    if user_id>0 and request.method == 'GET':
        advisors = yamlfileopener("advisors")
        advisors_detail = {"data":advisors}
        json_object = json.dumps(advisors_detail, indent = 4)
        #print(json_object)
        return HttpResponse(json_object,status=200)
    else:
        return HttpResponse("Bad Request",status=400)

@csrf_exempt
def book_call(request,user_id,advisor_id):
    aflag,uflag=False,False
    if request.method == 'POST':
        advisors = yamlfileopener("advisors")
        users = yamlfileopener("users")
        bookings = yamlfileopener("bookings")
        for adv in advisors:
            if adv['advisorid'] == advisor_id:
                aflag = True
                advisor_details = adv
                break
        for user in users:
            if user['userid'] == user_id:
                uflag = True
                user_details = user
                break
        if uflag and aflag:
            data = json.loads(request.body.decode("utf-8"))
            booking_time = data['booking_time']
            booking_id = len(bookings)+1
            advisor_details['booking_time'] = booking_time
            advisor_details['booking_id'] = booking_id 
            print(advisor_details)
            booking = {
                booking_id: {
                    "User": user_details,
                    "Advisor": advisor_details
                }
            }
            bookings.append(booking)
            yamlfileloader(bookings,"bookings")
            #json_object = json.dumps(advisors_detail, indent = 4)
            #print(json_object)
            return HttpResponse(None,status=200)
        else:
            return HttpResponse("Bad Request",status=400)
    elif request.method == 'GET':
        return HttpResponse("GET Request",status=200)
    else:
        return HttpResponse("Bad Request",status=400)

@csrf_exempt
def get_bookings(request,user_id):
    if request.method == 'GET':
        bookings = yamlfileopener("bookings")
        booking_data = []
        booking_length = len(bookings)
        for length in range(0,booking_length):
            booking_data.append(bookings[length][length+1]["Advisor"])
        #print(booking_data)
        booking_details = {"data":booking_data}
        json_object = json.dumps(booking_details, indent = 4)
        #print(json_object)
        return HttpResponse(json_object,status=200)
    else:
        return HttpResponse("Bad Request",status=400)

@csrf_exempt
def add_advisor(request):
    if request.method == 'GET':
        return HttpResponse("GET Request",status=200)
    elif request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        for v in data.values():
            #print(v,list(data.values()))
            if len(v.strip()) > 0:
                flag = False
            else:
                flag = True
                break
        #print(flag)
        if flag:
            return HttpResponse("Bad Request",status=400)
        else:   
            advisors = yamlfileopener("advisors")
            advname = data['advisorname']
            advpic = data['advisorpic']
            advid = len(advisors) + 1
            details ={'advisorid':advid,'advisorname':advname,'advisorpic':advpic}
            advisors.append(details)
            yamlfileloader(advisors,"advisors")
            #print(json_object) 
            return HttpResponse(status=200)
    else:
        return HttpResponse("Bad Request",status=400)
