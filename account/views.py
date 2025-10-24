from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View




class SignUpView(CreateView):
    template_name = 'account/signup.html'
    def get(self, request):
        return render(request, 'account/signup.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, self.template_name, {'error': 'Username already exists!'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('task_list')


class LoginView(CreateView):
    template_name = 'account/login.html'
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')



