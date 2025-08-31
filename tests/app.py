from typing import TypedDict, Dict
import json


class Customer(TypedDict):
    name: str
    email: str
    age: int
    loyalty_points: int
    address: str


class App:
    def __init__(self, database: str):
        # Minimal App stub for tests; replace with real import if available
        with open(database, "r") as data:
            self.customers: Dict[str, Customer] = json.load(data).get("customers", {})

    def get_customer(self, id: str):
        return self.customers.get(id)


# Run this command to test security flaws in app 
# bandit -r {module}

# Add this setup.cfg to configure bandit
# [bandit]
# exclude: /test
# tests: B101,B102,B301