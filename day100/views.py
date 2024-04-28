from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Curriculum, DayLog
from .serializers import CurriculumSerializer, DayLogSerializer


# Create your views here.
@csrf_exempt
def create_user(request):
    data = JSONParser().parse(request)
    username = data['username']
    email = data['email']
    password = data['password']

    User.objects.create_user(username, email, password)
    return HttpResponse(status=201)

@csrf_exempt
def log_user_in(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']
    
    session_data = request.session
    session_data['username'] = username
    print(session_data['username'])

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'username': username})
        # Send a success message

    else:
        print('user not authenticated')
        return HttpResponse(status=500)
        # Return an 'invalid login' error message


@csrf_exempt
# @login_required
def get_all_curriculums(request):
    """
    List all curriculums, or create a new curriculum.
    """
    print('getting curriculums')
    if request.method == 'GET':
        curriculums = Curriculum.objects.all()
        serializer = CurriculumSerializer(curriculums, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CurriculumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
# @login_required
def get_recent_curriculums(request):
    return 'get_recent_curriculums'
    

@csrf_exempt
# @login_required
def get_one_curriculum(request, curriculum_id):
    """
    Retreive, update or delete a curriculum.
    """
    try:
        curriculum = Curriculum.objects.get(pk=curriculum_id)
    except Curriculum.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CurriculumSerializer(curriculum)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = CurriculumSerializer(curriculum, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        curriculum.delete()
        return HttpResponse(status=204)


@csrf_exempt
# @login_required
def get_all_daylogs(request, curriculum_id):

    if request.method == 'GET':
        daylogs = DayLog.objects.filter(curriculum=curriculum_id)
        serializer = DayLogSerializer(daylogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DayLogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
# @login_required
def get_recent_daylogs(request, curriculum_id):

    if request.method == 'GET':
        daylogs = DayLog.objects.filter(curriculum=curriculum_id).order_by('-id')[:3]
        serializer = DayLogSerializer(daylogs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    return 'get_recent_daylogs'


@csrf_exempt
# @login_required
def get_one_daylog(request, curriculum_id, daylog_id):
    """
    Retreive, update or delete a daylog.
    """
    try:
        daylog = DayLog.objects.get(curriculum=curriculum_id, pk=daylog_id)
    except DayLog.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = DayLogSerializer(daylog)
        return JsonResponse(serializer.data)
    
    return 'get_one_daylog'