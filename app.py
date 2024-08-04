from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/Reflected_result", methods=['GET'])
def Reflected_result():
    result = request.args.get("Script_Input")

    return result #render_template('Reflected_result.html',result=result)

@app.route("/Restored_result",methods=['POST'])
def Restored_result():
    result = request.form.get('Script_Input2')
    f=open('content.txt','a')
    f.write(result)
    f.write("\n")
    f.close()
    content = open('./content.txt','r').read()
    
    return render_template('Restored_result.html',content=content)

@app.route("/Delete",methods=['POST'])
def Delete_file():
    f=open('content.txt','w')
    f.write("")
    f.close()
    return render_template("Restored_result.html")

if __name__ == "__main__":
    app.run('0.0.0.0',port=3000,debug=True)