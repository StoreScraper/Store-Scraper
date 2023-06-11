from Base import Retailer

class Amazon(Retailer):
    def __init__(self) -> None:
        self.name = "Amazon"
        self.url = "https://www.amazon.com.mx/s?k="
        
    def get_query():
        return []