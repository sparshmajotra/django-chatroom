# Django Chatroom

A real-time chatroom application built with Django that allows users to join chat rooms and communicate instantly. This project demonstrates the use of Django for backend development along with real-time messaging functionality.

## Features

* Real-time chat messaging
* Multiple users can join the same chat room
* Clean and simple UI
* Django-based backend architecture
* Session-based username handling
* Responsive frontend design
* Easy to extend and customize

## Tech Stack

* Python
* Django
* HTML5
* CSS3
* JavaScript
* Bootstrap / Tailwind CSS (if used)

## Project Structure

```bash
django-chatroom/
│
├── chat/               # Main chat application
├── templates/          # HTML templates
├── static/             # CSS, JS, Images
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sparshmajotra/django-chatroom.git
cd django-chatroom
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start development server

```bash
python manage.py runserver
```

Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

## How It Works

* Users enter a username before joining a room.
* Messages are sent instantly within the selected chat room.
* Django handles routing, templates, and backend logic.
* The project can be extended with WebSockets using Django Channels for advanced real-time functionality.

## Future Improvements

* User authentication system
* Private messaging
* Online/offline status
* Message persistence in database
* Emoji support
* Typing indicators
* File/image sharing
* WebSocket integration using Django Channels

## Learning Objectives

This project helped in understanding:

* Django project structure
* URL routing
* Template rendering
* Forms and user input handling
* Session management
* Real-time communication concepts
* Frontend and backend integration

## Screenshots

*Add screenshots of your application here.*

## Deployment

You can deploy this project using:

* Render
* Railway
* Heroku
* PythonAnywhere
* VPS hosting

## Author

Sparsh Majotra

GitHub: https://github.com/sparshmajotra

## License

This project is open-source and available under the MIT License.
