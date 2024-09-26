"""
Restaurant : Base class
This has different sections of restaurant
"""
from abc import ABC, abstractmethod


class Restaurant(ABC):
    def __init__(self, owner):
        self.owner = owner
        print("Welcome to FineDine Restaurant!, Currently only Billing Service is active")

    def kitchen_service(self):
        return self.owner

    @abstractmethod
    def billing_service(self):
        pass

    def cleaning_service(self):
        return self.owner

    def delivery_service(self):
        return self.owner
