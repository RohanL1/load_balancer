import requests

class LoadBalancer:
    
    def __init__(self):
        self.node_count = 0
        self.node_details = []
        self.data = {}
        self.round_robin_idx = -1
        self.api_route = "/execute" 
        
    def distribute_task(self, req):
        return self.round_robin(req)

    def round_robin(self, req):
        def rotate_nodes():
            ln = len(self.node_details)
            self.round_robin_idx += 1
            if self.round_robin_idx  < 0 or self.round_robin_idx >= ln :
                self.round_robin_idx = 0
            return self.round_robin_idx 
            
            
        # Send a GET request
        idx = rotate_nodes()
        print(f"sending task to {idx} node")
        url = self.node_details[idx].node_address + self.api_route
        print(f"URL : {url}")
        print(req.get_json())
        return self.pass_request(url, req)
        
        
    def pass_request(self, url, req):
        response = requests.post(url, json=req.get_json())

        # Check if the request was successful
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            print(f"Error: {response.status_code}") 
    
    
    def set_node_deatils(self, addr_list,):
        for addr in addr_list:
            self.node_details.append(NodeDetails(addr))
            self.node_count += 1
            

class NodeDetails:
    id_count = 0
    def __init__(self, addr,) -> None:
        self.node_address = addr
        self.node_avg_task_time = -1
        self.node_id = (NodeDetails.id_count + 1)
        NodeDetails.id_count += 1
        
        
    

    
    
class Task:
    task_id = -1
    task_node_id = -1 
    task_data = -1
    