from project.bakery import Bakery

bakery = Bakery("pederastbakery")
bakery.add_food("Bread", "hleb", 2)
bakery.add_food("Bread", "pakhleb", 3)
bakery.add_food("Cake", "hipstercake", 4)
bakery.add_drink("Water", "otchuchura", 1, "cheshmiana")
bakery.add_drink("Tea", "nadedotichaia", 2, "nestea")
bakery.add_table("InsideTable", 3,  10)
bakery.add_table("OutsideTable", 3,  50)
bakery.reserve_table(50)