from flask import Flask, request
from node import Node
import sys

slave = Node()

# Initialize the Flask application
app = Flask(__name__)

@app.route('/execute', methods=['GET','POST'])
def execute():
    print("executing here")
    return slave.execute(request)
    
    

if __name__ == "__main__" :
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <port> !!")
        sys.exit(1)
    
    app.run(port=sys.argv[1], debug=True)
