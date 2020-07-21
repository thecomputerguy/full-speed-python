from collections import ChainMap
car_parts = {"hood": 500, "engine": 5000, "front_door": 750}
car_options = {}
car_accessories = {}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing["hood"])
