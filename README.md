# Chatbot State Machine - README

This repository contains a state machine chatbot built with Django. The chatbot interacts with users through a single API endpoint, guiding them through a predefined conversation flow.

![](/chatbot.png)

### Tech Stack:
* Python 3.10.5
* Django 5.0.1
* Bootstrap 5

### How to run locally:

1. Set up virtual environment:
```bash
    mkdir chatbot
    cd chatbot
    pip install virtualenv
    python -m venv virtual
    source virtual/Scripts/activate
```


2. Clone project and install requirements:
```bash
    git clone 'repo_address'
    cd chatbot
    pip install -r requirements.txt
```

3. Migrate and run project:
```bash
    python manage.py migrate
    python manage.py createsuperuser  # follow prompts to create a super user
    python manage.py populate_chat_states
    python manage.py runserver
```

### API Explanation

The chatbot communicates with users through a single API endpoint.

#### Endpoint:
* /chat/

#### Methods:
* POST: To interact with the chatbot
* GET: To initiate a chat session

#### Authentication:
* Basic Authentication is required
* Permission: Users must be authenticated

#### Request Payload (POST):
* session_id: Unique identifier for the user session
* user_input: User's input in lowercase

#### Response:
* JSON response containing the chatbot's message

#### State Transitions:
* Greeting -> Question -> Answer -> End

#### Logic:
The API follows a state machine approach with four defined steps:

Greeting: Welcomes the user and prompts for a response.
Asks a question and expects a yes/no answer.
Answer: Provides a response based on the user's answer.
End: Terminates the chat session.
The API processes user input based on the current state:

POST request:
Gets the user's session ID and input message.
Retrieves the current state for the user session.
Processes the input based on the current state:
Handles transitions to next state based on pre-defined rules and user input.
Generates appropriate response messages.
Logs user input for analysis.
If no valid transition found, provides a generic "not understood" message.
If state reaches "end", closes the session and logs out the user.
GET request (initial greeting):
Sets the initial state to "greeting" and provides the welcome message.

#### Examples:

* Start a chat session:
```bash
    curl -X GET http://localhost:8000/chat/
```

* Provide user input:
```bash
    curl -X POST http://localhost:8000/chat/ -d 'session_id=unique_id&user_input=hello'
```

* Get greeting message:
```bash
    curl http://localhost:8000/chat/
```
#### Notes:

* Internet connection is required for rendering static content.
* The chatbot handles various user inputs and transitions through states accordingly.
* Session management is based on unique session identifiers.

