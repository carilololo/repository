from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('tabla-juangomez')

#Metodo para insertar un registro en la tabla
@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {
    **data
  }

  table.put_item(Item=item)
  
  return 'Se guardo exitosamente'

#Metodo para leer elementos de la tabla
@app.route('/get/<id>', methods=['GET'])
def get_item(id):
  try:
    response = table.get_item(Key={'id': id})

    if 'Item' in response:
      return jsonify(response['Item']), 200
    else:
      return jsonify({'message': 'No se encontro el registro'}), 404
  
  except Exception as e:
    return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
