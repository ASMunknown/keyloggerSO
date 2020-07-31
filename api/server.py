from flask import Flask, jsonify, request

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route('/upload/<arg1>',methods=['GET'])
def upload(arg1):
        print(arg1)
        with open("db.json","a") as fo:
                fo.write(arg1)

        return app.send_static_file("dataSave.html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

if __name__ == '__main__':
        app.run(debug=True)