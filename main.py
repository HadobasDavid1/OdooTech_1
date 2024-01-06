import os
import json

class Auto:
    def __init__(self, id, type, ajtok, marka):
        self.id = id
        self.type = type
        self.ajtok = ajtok
        self.marka = marka

    def __str__(self):
        return f"ID: {self.id}, {self.type}, ajtók száma: {self.ajtok}, márka: {self.marka}"

class Bicikli:
    def __init__(self, id, type, terhelhetoseg, marka):
        self.id = id
        self.type = type
        self.terhelhetoseg = terhelhetoseg
        self.marka = marka

    def __str__(self):
        return f"ID: {self.id}, {self.type}, terhelhetőség: {self.terhelhetoseg}, márka: {self.marka}"

def read_data(directory):
    vehicles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".dat"):
                file_path = os.path.join(root, file)
                print(f"Feldolgozás alatt: {file_path}")
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if data['type'] == 'auto':
                        vehicle = Auto(file.rstrip('.dat'),data['type'], data['ajtok_szama'], data['marka'])
                    elif data['type'] == 'bicikli':
                        vehicle = Bicikli(file.rstrip('.dat'),data['type'], data['terhelhetoseg'], data['marka'])
                    vehicles.append(vehicle)
                    print(f"Hozzáadva: {vehicle}")
    return vehicles

def print_data(vehicle_list):
    for vehicle in vehicle_list:
        print(vehicle)

dir = "data"
jarmu_list = read_data(dir)
print("\nJárművek listája:")
print_data(jarmu_list)