from collections import namedtuple

Parts = namedtuple("Parts", "id_num desc cost amount")
auto_parts = Parts(id_num = '1234', desc = 'ford_engine', cost = 1200.00, amount = 10)
print(auto_parts.id_num)
print(auto_parts.desc)
print()
print()

parts_container = {'id_num':'1234', 'desc':'Ford Engine', 'cost':1200.00,'amount': 50.0}
parts_named_tuple = namedtuple("Parts", parts_container.keys())(**parts_container)
print(parts_named_tuple)
id_num, desc, cost, amount = parts_named_tuple
print(parts_named_tuple.id_num)
print(parts_named_tuple.desc)
print(id_num)
print(desc)
print()
print()
