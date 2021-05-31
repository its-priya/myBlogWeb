
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong!'
        try:
            data = request.data
            if not data.get('username'):
                response['message'] = 'Username cannot be empty!'
                raise Exception('Username is empty')

            if not data.get('password'):
                response['message'] = 'Password cannot be empty!'
                raise Exception('Password is empty')

            check_user = User.objects.filter(username = data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid Username!'
                raise Exception('Username not found')

            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'Welcome!' 
        
            else:
                response['message'] = 'Username or Password is wrong!'
                raise Exception('Username or Password is wrong')

        except Exception as e:
            print(e)

        return Response(response)

LoginView = LoginView.as_view()
