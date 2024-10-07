from flask import Flask, request, jsonify
from load_balancer import LoadBalancer

addr_list = ['http://127.0.0.1:8080', 'http://127.0.0.1:8081', 'http://127.0.0.1:8082', 'http://127.0.0.1:8083', ]

master = LoadBalancer()
master.set_node_deatils(addr_list)


# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root_msg():
    return "WRONG URL"
@app.route('/run', methods=['GET','POST'])
def run():
    return master.distribute_task(request)
    
    

if __name__ == "__main__" :
    app.run(debug=True)