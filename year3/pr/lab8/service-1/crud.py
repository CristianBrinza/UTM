import requests
from models.electro_scooter import ElectroScooter
from models.database import db

class CRUDElectroScooter:
    def __init__(self, leader : bool, followers : dict = None):
        self.leader = leader
        if self.leader:
            self.followers = followers
            print("Followers: ", self.followers)

    def create(self, scooter_dict : dict):
        try:
            electro_scooter = ElectroScooter(
                name=scooter_dict['name'], 
                battery_level=scooter_dict['battery_level']
            )
            
            db.session.add(electro_scooter)
            db.session.commit()

            if self.leader:
                for follower in self.followers:
                    requests.post(f"http://{follower['host']}:{follower['port']}/api/electro-scooters",
                                    json = scooter_dict,
                                    headers = {"Token" : "Leader"})

            return electro_scooter.as_dict(), 201
        
        except KeyError:
            return {"error": "Invalid request data"}, 400
    
    def get_by_id(self, scooter_id : str):
        scooter = ElectroScooter.query.get(scooter_id)
        
        if scooter is not None:
            return scooter.as_dict(), 200 
        else:
            return {"error": "Electro Scooter not found"}, 404

    def get_all(self):
        all_scooters = ElectroScooter.query.all()
        return [scooter.as_dict() for scooter in all_scooters], 200
        
    def update(self, scooter_id : str, scooter_dict : dict):
        try:
            scooter = ElectroScooter.query.get(scooter_id)
            
            if scooter is not None:                
                scooter.name = scooter_dict.get('name', scooter.name)
                scooter.battery_level = scooter_dict.get('battery_level', scooter.battery_level)
                
                db.session.commit()
                
                if self.leader:
                    for follower in self.followers:
                        requests.put(f"http://{follower['host']}:{follower['port']}/api/electro-scooters/{scooter_id}",
                                    json = scooter_dict,
                                    headers = {"Token" : "Leader"})
                
                return scooter.as_dict(), 200
            
            else:
                return {"error": "Electro Scooter not found"}, 404
        
        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, scooter_id : str):
        try:
            scooter = ElectroScooter.query.get(scooter_id)
            
            if scooter is not None:                
                db.session.delete(scooter)
                db.session.commit()
                
                if self.leader:
                    for follower in self.followers:
                        requests.delete(f"http://{follower['host']}:{follower['port']}/api/electro-scooters/{scooter_id}",
                                        headers = {"Token" : "Leader"})
                
                return scooter.as_dict(), 200
            
            else:
                return {"error": "Electro Scooter not found"}, 404
        
        except Exception as e:
            return {"error": str(e)}, 500
    

