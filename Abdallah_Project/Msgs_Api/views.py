from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import * 
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from .serializer import *
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework import status, filters

from rest_framework.response import Response
from django.http import Http404
import base64
import sys
from rest_framework.decorators import api_view
 





# 6 Generics 
#6.1 get and post
class generics_list_msgstypes(generics.ListCreateAPIView):
    queryset = MsgsTypes.objects.all()
    serializer_class = MsgsTypesSerializer


   
   # authentication_classes = [TokenAuthentication]
    #authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class generics_pk_msgstypes(generics.RetrieveUpdateDestroyAPIView):
    queryset = MsgsTypes.objects.all()
    serializer_class = MsgsTypesSerializer
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

######################################
class generics_msgs(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessegasSerializer

#6.2 get put and delete 
class generics_pk_msgs(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessegasSerializer

###############################################



#2 model data default djanog without rest
def msgtypes_api(request):
    data = MeesageType.objects.all()
    response = {
        
        'MsgsTypesModel': list(data.values('id','MsgTypes','new_msg'))
        #'guests': dict(data.values('name','mobile'))
        
    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})
###############################

# https://medium.com/geekculture/building-django-api-views-without-django-rest-framework-4fa9883de0a8
# no rest framework api django
# 3306 port








def msgsapi (request,id):
    msgtype = MeesageType.objects.get(id=id)
    msg=Messages.objects.all().filter(ID_Type_id=msgtype.id)

    response = {
        'Msgs':list(msg.values('id','MessageName','new_msgs','ID_Type_id'))
        
    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})







def no_rest_msgs_all (request):
    data = Msgs.objects.all()
    response = {
        'data': list(data.values('msgs_types','msgs_name','new_msgs'))
    }

    return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})

# def no_rest_msgs (request,id):
#     msgtype = MsgsTypes.objects.get(id=id)
#     msg=Msgs.objects.all().filter(msgs_types_id=msgtype.id)

#     response = {
#         'Msgs':list(msg.values('msgs_name','new_msgs','msgs_types'))
#         # 'Msgs':list(msg.values('msgs_name','new_msgs','id_types'))
#         #                 'MsgsTypes': list(data.values('id','type_name','new_msg'))
        
#     }

#     return JsonResponse(response,safe=False,json_dumps_params={'ensure_ascii': False})
