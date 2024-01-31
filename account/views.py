import uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . forms import LoginForm

# Create your views here.


def login_view(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            context['form'] = form
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Generate a new session ID (using UUID for uniqueness)
                new_session_id = str(uuid.uuid4())

                # Set the new session ID
                request.session['session_id'] = new_session_id

                return redirect('chatbot')
            else:
                messages.error(request, 'Email or Password Incorrect.')

    else:
        context['form'] = LoginForm()

    return render(request, 'account/login.html', context)




    