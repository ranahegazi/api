from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SingUpSerializer , UserSerializer , MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import refreshstore

# from .models import user

# Create your views here.
@api_view(['POST'])
def register(request):
    data = request.data
    user = SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            user =User.objects.create(

                first_name = data['first_name'],
                last_name = data['last_name'],
                # name = data['name'],
                email = data['email'],
                username = data['email'],
                password = make_password(data['password']),
            )
            return Response(
                {'details':'your account registered'},
                status = status.HTTP_201_CREATED
            )
        else:
             return Response(
                {'details':'your account is already exist'},
                status = status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user)
    return Response(user.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    user.first_name = data["first_name"]
    user.last_name = data["last_name"]
    user.username = data["email"]
    user.email = data["email"]


    if data["password"] != "":
         user.password = make_password(data["password"]),



    user.save()
    serializer = UserSerializer(user , many=False)
    return Response(serializer.data)





class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# def storerefresh(TokenObtainPairView):
#     data = TokenObtainPairView.data
#     serializer = refreshSerializer(data = data)
#     if serializer.is_valid():
#         refreshtoken = refreshstore.objects.create(**data,user=TokenObtainPairView.user)
#         res = refreshSerializer(refreshtoken,many=False)
#         return Response({"refreshstore":res.data})
    


# def TokenObtainPairView(TokenObtainPairView):
#     data = TokenObtainPairView.data
#     serializer = refreshSerializer(data = data)
#     if serializer.is_valid():
#         refreshtoken = refreshstore.objects.store(**data,user=TokenObtainPairView.user)
#         res = refreshSerializer(refreshtoken,many=False)
#         return Response({"refreshstore":res.data})


