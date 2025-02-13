from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.contrib.auth import authenticate, login as auth_login




# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        # Add your post method implementation here
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        context = {
            'fieldValues': request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={
                    'uidb64': uidb64,
                    'token': token_generator.make_token(user)
                })
                
                activate_url = 'http://' + domain + link
                email_subject = 'Activate your account'
                email_body = 'Fala ' + user.username+ '! verifica tua conta nesse link, putão\n' + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@jgvalarc.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, 'User created successfully')  
                return render(request, 'authentication/register.html', context)
            
            return render(request, 'authentication/register.html')
        

@method_decorator(csrf_exempt, name='dispatch')
class EmailValidationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']

            if not validate_email(email):
                return JsonResponse({'email_error': 'Email not valid'}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({'email_error': 'Sorry, this email is already taken. Please try another email'}, status=409)

            return JsonResponse({'email_valid': True})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@method_decorator(csrf_exempt, name='dispatch')
class UsernameValidationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data['username']

            if not str(username).isalnum():
                return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({'username_error': 'Sorry, this username is already taken. Please try another username'}, status=409)

            return JsonResponse({'username_valid': True})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        
class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            
            if not token_generator.check_token(user, token):
                return redirect('login' + '?message=' + 'User already activated')
            
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            
            messages.success(request, 'Account activated successfully')
            return redirect('login')
            
        except Exception as ex:
            pass
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        
        username= request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    auth_login(request, user)
                    messages.success(request, 'Welcome, ' + user.username)
                    return redirect('expenses')
                
                messages.error(request, 'Account is not active, please check your email')
                return render(request, 'authentication/login.html')  
              
            messages.error(request, 'Invalid credentials, try again')    
            return render(request, 'authentication/login.html')
        
        messages.error(request, 'Please fill all fields')    
        return render(request, 'authentication/login.html')
    
from django.contrib.auth import logout as auth_logout

class LogoutView(View):
    def post(self, request):
        auth_logout(request)
        messages.success(request, 'Logout successful')
        return redirect('login')
