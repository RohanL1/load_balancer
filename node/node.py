from flask import request, jsonify

class Node: 
    
    def __init__(self) -> None:
        pass

    
    def execute(self, req):
        json_data = req.get_json()
        
        out = { 
            "result" : json_data["num1"] + json_data["num2"]
        }
        print(out)
        return jsonify(out)