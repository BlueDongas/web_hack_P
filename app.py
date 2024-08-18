from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/Reflected_result", methods=['GET'])
def Reflected_result():
    result = request.args.get("Script_Input")

    return render_template('Reflected_result.html',result=result)

@app.route("/Restored_result",methods=['POST'])
def Restored_result():

    result = request.form.get('Script_Input2')
    db = pymysql.connect(host='localhost', user='root',passwd='1234',db='webhack',charset='utf8')
    cur = db.cursor()
    write_sql = "INSERT INTO board (name, content) VALUES(%s,%s)"
    values = ("public",result)
    cur.execute(write_sql,values)
    db.commit()
    
    load_sql = "SELECT * from board"
    cur.execute(load_sql)

    data_list = cur.fetchall()
    
    return render_template('Restored_result.html',data_list=data_list)

#@app.route("/Delete",methods=['POST'])
#def Delete_file():
#    f=open('content.txt','w')
#    f.write("")
#    f.close()
#    return render_template("Delete.html")

if __name__ == "__main__":
    app.run('0.0.0.0',port=3000,debug=True)