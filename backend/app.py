import subprocess
import uuid
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from tempfile import TemporaryFile
import os

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


class Compiler(Resource):
    def post(self):
        data = request.get_json()
        try:
            code = data['code']
            rand = uuid.uuid4().hex
            file_name = 'code/' + rand + '.py'
            f = open(file_name, 'w+')
            f.write(code)
            f.close()
            command = 'python ' + file_name
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            os.remove(file_name)
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
        return {
                'message': 'success',
                'response': output.decode('utf-8')
                }

api.add_resource(Compiler, '/')

if __name__ == '__main__':
    app.run(debug=True)
