from flask import Flask, request
from count import count
import json

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route('/upload/<arg1>',methods=['GET'])
def upload(arg1):
        print(arg1)
        with open("report.txt","a") as fo:
                fo.write(arg1)

        return app.send_static_file("dataSave.html")

@app.route('/uploadSysInfo/<arg1>',methods=['GET'])
def uploadSysInfo(arg1):
        print(arg1)
        with open("app/sysInfo.js","w") as fo:
                fo.write(arg1)

        return app.send_static_file("dataSave.html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

        usage = {}
        with open('report.txt','r') as f:
                text = f.read()
                
                specialKeyFound = False
                tempSpecialKey = ''
                for i in range (0,len(text)):
                        # print(text[i])

                        if text[i] == '[':
                                specialKeyFound = True
                                tempSpecialKey = text[i]
                        elif specialKeyFound:
                                if text[i] == ']':
                                        tempSpecialKey = tempSpecialKey + ']'
                                        count(tempSpecialKey,usage)
                                        specialKeyFound = False
                                        tempSpecialKey = ''
                                else:
                                        tempSpecialKey = tempSpecialKey + text[i]
                        else:
                                count(text[i],usage)
                print(usage)

        # Generando el reporte en JSON para visualizarlo en la página.
        with open('app/db.js','w') as f:
                
                cadena = json.dumps(usage)
                f.write("var db = " + cadena)
        
        return app.send_static_file(path)


if __name__ == '__main__':
        app.run(debug=True)