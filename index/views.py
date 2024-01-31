from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def index_view(request):
    context = {}

    user = request.user
    context["session_id"] = request.session['session_id']

    return render(request, 'index/chatbot.html', context)