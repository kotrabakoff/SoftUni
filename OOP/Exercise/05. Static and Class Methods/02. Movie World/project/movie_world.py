from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) == MovieWorld.CUSTOMER_CAPACITY:
            return
        self.customers.append(customer)


    def add_dvd(self, dvd: DVD):
        if len(self.dvds) == MovieWorld.DVD_CAPACITY:
            return
        self.dvds.append(dvd)

    def __find_by_id(self, entities, entity):
        for i in entities:
            if i.id == entity:
                return i


    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        if dvd.is_rented:
            return "DVD is already rented"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

        # for customer in self.customers:
        #     if customer.id == customer_id:
        #         for dvd in self.dvds:
        #             if dvd.id == dvd_id:
        #                 if dvd_id in customer.rented_dvds:
        #                     return f"{customer.name} has already rented {dvd.name}"
        #                 if customer.age < dvd.age_restriction:
        #                     return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        #                 if dvd.is_rented:
        #                     return "DVD is already rented"
        #                 dvd.is_rented = True
        #                 customer.rented_dvds.append(dvd)
        #                 return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"


    def __repr__(self):
        return "\n".join([repr(x) for x in self.customers]) + "\n" + "\n".join([repr(x) for x in self.dvds])







