from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
colony = AntColony(None, hive, ant_types(), layout, dimensions)
thrower = ThrowerAnt()
near_bee = Bee(2) # A Bee with 2 armor
far_bee = Bee(3)  # A Bee with 3 armor
ant_place = colony.places['tunnel_0_0']
near_place = colony.places['tunnel_0_3']
far_place = colony.places['tunnel_0_6']
ant_place.add_insect(thrower)
near_place.add_insect(near_bee)
far_place.add_insect(far_bee)
nearest_bee = thrower.nearest_bee(colony.hive)
print(nearest_bee.armor)