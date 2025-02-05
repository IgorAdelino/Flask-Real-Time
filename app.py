from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
  return jsonify({'message': "The payment has been created"})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
  return jsonify({'message': "The payment has been confirmed"})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def get_payment_pix(payment_id):
  return jsonify({'message': "Payment ID: " + str(payment_id)})

if app == '__main__':
  app.run(debug=True)