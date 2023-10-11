import flask as Flask

#initializing application
app=Flask(__name__)

@app.route('/') # '/' denotes root 
def hello_world():
    return("Hello world!")
if __name__ ="__main__":  #Main driver function
   
