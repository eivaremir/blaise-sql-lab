import sys
import os
import json
import sqlite3
from flask import Flask, render_template, jsonify, request

if getattr('sys','frozen',False):
    template_folder = os.path.join(sys._MEIPASS,'templates')
    static_folder = os.path.join(sys._MEIPASS,'static')
    print(template_folder)
    #app = Flask(__name__,template_folder=template_folder,static_folder=static_folder)
else:
    
    app = Flask(__name__)


# -------------------- VIEWS----------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello",methods=['POST','GET'])
def hello():
    return jsonify({"about": "hello"})


@app.route("/query2")
def js():
    return jsonify({'Key':123})


@app.route("/test",methods=['POST','GET'])
def test():
    print(request.content_type)
    print(request.get_json())
    print(request.get_data())
    return "<h1>hola</h1>"

@app.route("/query",methods=['POST'])
def query():
    """
    json must be dict with the following keys:
        db: text (sqlite db path location)
        query: text (query content to be sent to sqlite)
    """
    

    content = request.get_json() # returns dict
    if not content:
        content = json.loads(request.get_data())
    
    if not 'db' in content:
        return jsonify({"Error":"db path not specified"}), 400
    if not 'query' in content:    
        return jsonify({"Error":"query not specified"}) , 400 

    conn = sqlite3.connect(content['db'],check_same_thread = False)
    cursor = conn.cursor()

    try:
        for query in content['query'].split(";")[:-1]:
            print("Executing...",query)
            cursor.execute(query)
        
        rows = cursor.fetchall()
        #count = cursor.rowcount
        #print(cursor.description)
        columns = []
        for description in cursor.description:
            columns.append(description[0])
        
        cursor.close()
        conn.close()
    except Exception as ex:
        print("Exception:",ex)
        cursor.close()
        conn.close()
    ##print(rows)
    
    
    
    return jsonify({
        "columns":columns,
        "content":rows,
        
    })
    


    


# ------------------- INIT SERVER -----------------------
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)


