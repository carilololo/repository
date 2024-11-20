from flask import Flask
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('tabla-juangomez')

@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {
    **data
  }

  table.put_item(Item=item)
  
  return 'Se guardo exitosamente'



if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
