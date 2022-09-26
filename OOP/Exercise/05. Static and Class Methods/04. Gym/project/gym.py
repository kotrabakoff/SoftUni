from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        sub = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, sub.customer_id)
        trainer = self.__find_by_id(self.trainers, sub.trainer_id)
        plan = self.__find_by_id(self.plans, sub.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)
        return repr(sub) + "\n" + \
               repr(customer) + "\n" + \
               repr(trainer) + "\n" + \
               repr(equipment) + "\n" + \
               repr(plan)

    def __find_by_id(self, entities, entity_id):
        for ent in entities:
            if ent.id == entity_id:
                return ent

