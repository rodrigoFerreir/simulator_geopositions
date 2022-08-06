from typing import List
from .models import PartialRoutePosition, Position, Route


def load_positions(route: Route):
    if route.ID == "":
        raise Exception("route id not declaretion")
    try:
        with open(f'./service/destinations/{route.ID}.txt') as file:
            for val in file.readlines():
                lat = val.split(',')[0]
                long = val.split(',')[1]
                route.POSITIONS.append(Position(lat, long))
    
    except Exception as err:
        print(f"Erro ao carregar posições {err}")
        raise Exception(f"Ocorreu um erro ao carregar posições")



def export_json_positions(r: Route) -> List[PartialRoutePosition]:
   
    result = []
    total = len(r.POSITIONS)

    for v in r.POSITIONS:
        i = r.POSITIONS.index(v)
        route = PartialRoutePosition(
            id=r.ID, 
            client_id=r.CLIENTID, 
            position=[float(v.lat), float(v.long)],
            fineshed=False
        )
        if total - 1 == i:
            route.fineshed = True
        
        result.append(route)

    return result