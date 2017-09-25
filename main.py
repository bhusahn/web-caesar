from flask import Flask, request
from caesar import rotate_string

app=Flask(__name__)
app.config['DEBUG']= True

# a form for caeser encryption
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
    
      <form method="post">
        
        <label for="rot">
        Rotate by: 
            </label>
            <input type="text" id="rot" name="rot" value = "0"/>
           
            <textarea name= "text">{content}</textarea>
            <input type="submit" value="Submit Query" />
            
          </form>
        </body>
    </html>
"""
#create a route above the function definition to receive and handle the request form 



@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text'] 
    encrypted = rotate_string(text, rot)
    
    return form.format(content=encrypted)




@app.route("/")
def index():
    return form.format(content="")
    
app.run()