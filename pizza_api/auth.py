from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import viewsets

class AuthView(viewsets.ViewSet):
    def login(self, request):
        uname = request.data['username']
        upass = request.data['password']

        user = authenticate(username=uname, password=upass)

        if user is not None:
            request.session['name'] = uname
            request.session['pass'] = upass
            login(request, user)
            data = {
                'msg': 'logged in successfully'
            }
            return Response(data)
        else:
            return Response({'error':'check username/password'})    
    
    def loginview(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            data = {
                'success':request.user.username + ' is already logged in.'
            }
        else:
            data = {
                'message':'Please login.'
            }

        return Response(data)


    def logout(self, request):
	    logout(request)
	    return Response({'success':'loggedout'})

