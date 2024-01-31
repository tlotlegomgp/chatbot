from django.contrib.auth import logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import redirect
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import UserSession, Step, Log

# Create your views here.

@api_view(["POST", "GET"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def chat_view(request):

    if request.method == 'POST':

        session_id = request.data.get('session_id')
        user_input = request.data.get('user_input').lower()

        # Get or create user session
        user = request.user
        user_session, created = UserSession.objects.get_or_create(session_id=session_id)

        # Retrieve current state and response
        current_state = user_session.current_state
        current_step = Step.objects.get(name=current_state)

        if current_step.next_state:
            next_step = Step.objects.get(name=current_step.next_state)
            response_message = next_step.response_message
        else:
            response_message = "Chat session closed."
            logout(request)
            return JsonResponse({'message': response_message}, status=status.HTTP_200_OK)

        # Handle state transitions and responses
        if user_input in ['bye', 'exit', 'goodbye']:
            user_session.current_state = 'end'
            user_session.save()
            logout(request)
        elif current_state == 'greeting':
            if user_input in ['hi', 'hello', 'hola', 'hey']:
                user_session.current_state = next_step.name
                user_session.save()
        elif current_state == 'question':
            if user_input == 'yes':
                user_session.current_state = next_step.name
                user_session.save()
            else:
                response_message = "I promise it will be funny."
        elif current_state == 'answer':
            user_session.current_state = next_step.name
            user_session.save()
        elif current_state == 'end':
            response_message = current_step.response_message
        else:
            response_message = "I'm sorry, I didn't understand that."

        # Log user response
        Log.objects.create(user=user, message=user_input)
    
    else:
        current_step = Step.objects.get(name='greeting')
        response_message = current_step.response_message
    
    return JsonResponse({'message': response_message}, status=status.HTTP_200_OK)