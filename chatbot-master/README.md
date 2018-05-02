
### Requirements
    Python >= 2.7
    Flask >= 0.10

## Installation steps (assuming python 2.xx version is installed.Currently using pyhton 2.7. AIML does not work properly in python 3.xx as of now)

1. Clone and navigate to chatbot directory.

2. Install python 2.7 and the required packages.
    ```bash
    for windows type the following command in cmd:
    python -m pip install --upgrade pip setuptools wheel
    
    pip install -r requirements.txt 
    
    pip install PyAIML
    ```
3.Run database.sql in mysql client to import the database web_customer_service.

4. Run the python server.
    ```bash
    python main.py
    ```
5. Open **http://127.0.0.1:8080** in your browser.

6. You're done and let's chat with your Robot via browser.


