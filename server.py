from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/my-webhook', methods=['POST'])
def webhook():
    data = request.get_json()  
    print(f"Received data: {data}")  
    return jsonify({'status': 'success', 'message': 'Webhook received!'})

if __name__ == '__main__':
    app.run(port=9000, debug=True)  