# 🌐🤖 Webhook Hello World App

## 📚 About the Project
This project showcases a basic Webhook server built with Flask and Python. 🚀
It listens for incoming HTTP POST requests on the /my-webhook endpoint and processes the data seamlessly.

## 🚀 Getting Started

**🛠️ What You’ll Need**

✔️ Ensure you have Python installed on your machine.
🔎 To check the version, run this command:
```bash
python --version
 ```
⚡ You’ll need Python 3.8.3 or later to proceed.


## 📥 Installation
**1️⃣: Clone the Repository**
Run the following command to clone the project:
```sh
   git clone https://github.com/Karina1014/Webhook_Python_Hello_world.git
```
**2️⃣: Set Up a Virtual Environment**
Prepare your development environment by creating and activating a virtual environment:
   ```sh
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
  ```
**3️⃣: Install Dependencies**
Install the necessary packages using pip:
   ```sh
pip install flask
  ```

## ⚙️ Running the Server
**1️⃣: Launch the Flask Application**
Start the server by running:
```sh
python server.py
```
**2️⃣: Test Your Webhook**
You can test the webhook endpoint using tools like Postman or cURL.

Using Postman:
1. Create a new POST request and set the URL to:
```sh
http://127.0.0.1:5000/my-webhook
```
2. Add the following header:
- Key: Content-Type
- Value: application/json

3. In the body section, choose raw and set the format to JSON, then include this:
```sh
{
  "message": "Hello world!"
}

```

# Result:
![image](https://github.com/user-attachments/assets/f3c78aff-dfdb-4964-82c7-7932dc944bdd)
