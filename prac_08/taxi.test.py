from prac_08.taxi import Taxi

prius1 = Taxi("Prius 1", 100)

prius1.drive(40)
print(prius1)
fare = prius1.get_fare()
print(fare)
prius1.add_fuel(100)
prius1.start_fare()
prius1.drive(100)
print(prius1)
fare = prius1.get_fare()
print(fare)

