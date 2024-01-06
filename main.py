from flask import Flask, jsonify, request
app = Flask(__name__)
task = [
    {
        'id':1,
        'title':'buy groceries',
        'discription':'milk, cheese, fruits',
        'done':False

    },
    {
        'id':2,
        'title':'do homework',
        'discription':'maths, english, science',
        'done':False
    }
]
@app.route('/')
def pencil():
    return 'hello this is my first API'

@app.route('/getinfo')
def info():
    return jsonify({
        'data':task
    })
@app.route('/addtask',methods=['POST'])
def addtask():
    if not request.json :
        return jsonify({
            'status':'error',
            'message':'please provide the data'
            
        })


if __name__ =='__main__':
    app.run(debug = True)