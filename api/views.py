from django.contrib.auth import logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
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
        data = request.POST.dict()
        session_id = data.get('session_id')
        user_input = data.get('user_input').lower()

        # Get or create user session
        user, created = UserSession.objects.get_or_create(session_id=session_id)

        # Retrieve current state and response
        current_state = user.current_state
        current_step = Step.objects.get(name=current_state)
        next_step = Step.objects.get(name=current_state.next_state)

        response_message = next_step.response_message

        # Handle state transitions and responses
        if current_state == 'greeting':
            if user_input in ['hi', 'hello', 'hola', 'hey']:
                user.current_state = next_step.name
                user.save()
        elif current_state == 'question':
            if user_input == 'yes':
                user.current_state = next_step.name
                user.save()
        elif current_state == 'answer':
            user.current_state = next_step.name
            user.save()
        elif user_input in ['bye', 'exit', 'goodbye']:
            user.current_state = 'end'
            user.save()

            logout(request)        
        else:
            response_message = "I'm sorry, I didn't understand that."

        # Log user response
        Log.objects.create(user=user, message=user_input)
    
    else:
        current_step = Step.objects.get(name='greeting')
        response_message = current_step.response_message
    
    return JsonResponse({'response': response_message}, status=status.HTTP_200_OK)