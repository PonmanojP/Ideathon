# Canvas Editor with Voice Command

This is a web-based canvas editor built with Django, Fabric.js, and voice command integration using the Web Speech API. The application allows users to interact with the canvas using voice commands and supports copying, pasting, and dragging Fabric.js components between multiple canvases. Additionally, it offers a download functionality to save the canvas as a PNG.

## Features

- **Voice Command Integration**: Allows the user to input commands via voice using the Web Speech API.
- **Canvas Editor**: Built using Fabric.js, enabling interactive design elements.
- **Copy & Paste**: Supports `Ctrl+C` and `Ctrl+V` functionality to copy and paste Fabric.js objects between canvases.
- **Download Canvas**: Provides the ability to download the content of the dummy canvas as a PNG.

## Prerequisites

Before starting, make sure you have the following installed on your system:

- Python 3.x
- Django 4.x
- pip (Python package manager)
- Virtualenv (optional but recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PonmanojP/Ideathon.git

cd designer
```

### 2. Install Prerequisites

```bash
pip install django

pip install -q -U google-generativeai

```

### 3. API key setup
- In workspace/views.py on line 5, configure the API key with your API key.  It cannot be shared due to security concerns.
- Once the key is set run the following command.

```bash
python manage.py runserver
```

### Running the application
- You can go to http://127.0.0.1:8000 for the demo of the application.

### Sample Working : 
- Press ALT key and then you can start talking to the interface to get your items. (better use chrome for voice input)
- You can copy the rendered image in the left side by using ctrl+c and ctrl+v

![Screenshot 2024-09-08 142614](https://github.com/user-attachments/assets/14b8c4c0-9fcc-4fb4-ad11-dc49ee5c4e0e)

  
![Screenshot 2024-09-08 160332](https://github.com/user-attachments/assets/0a3a475c-f9a0-496c-8997-f68b85081a59)

# #LetTheAIcook🤖

