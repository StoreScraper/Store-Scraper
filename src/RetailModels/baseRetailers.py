from typing import Protocol

class Retailer(Protocol):
    name: str
    url: str
    current_query_items: list
    
    def get_query() -> list:
        ...
    
    def filter_current_query_by_price() -> None:
        ...

class Item():
    def __init__(self, name: str, price: float, image: str) -> None:
        self.name = name
        self.price = price
        self.image = image
        
    