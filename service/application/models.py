from typing import List


class Position:
    """
    Posição com as coordenadas a serem percorridas ao logo das rotas
    """
    lat: float
    long: float

    def __init__(self, lat:float, long:float) -> None:
        self.lat = lat
        self.long = long


class Route:
    """
    Classe que define a rota com a posição inicial e a posição final
    """
    ID: str
    CLIENTID: str
    POSITIONS : List[Position]

    def __init__(self, id:str, client_id:str, positions:List[Position] = []) -> None:
        self.ID = id
        self.CLIENTID = client_id
        self.POSITIONS = positions


class PartialRoutePosition:
    """
    Estrutura criada para envio
    """
    ID: str
    client_id: str
    position = List[Position]
    fineshed: bool

    def __init__(self, id:str, client_id: str, position:list= [], fineshed:bool = False) -> None:
        self.ID = id
        self.client_id = client_id
        self.position = position
        self.fineshed = fineshed

    
