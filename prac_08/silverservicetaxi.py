from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.00):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${}/km plus flagfall of ${}".format(self.name, self.fuel,
                                        self.odometer, self.current_fare_distance, self.price_per_km, self.flagfall)

