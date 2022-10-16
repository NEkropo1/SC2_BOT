from loguru import logger
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from sc2.wrappers import *
from sc2.base_bot import *


class Manager:
    _instances = set()

    def __new__(cls):
        obj = super().__new__(cls)
        cls._instances.add(obj)
        return obj

    @classmethod
    def update_instances(cls):
        for instance in cls._instances:
            instance.update()


class BaseManager(Manager):
    def __init__(self):
        self.minerals_list = list()
        self.workers = list()
        self.unit_command_uses_self_do = True

    def update(self):
        print("i'm updating", self)
        for worker in self.workers:
            print(f'{worker.position}')


class ExpansionManager(Manager):
    def __int__(self):
        self.nexus = None
        self.pylons = list()
        self.gas_stations = list()
        #if not Expansion.has_base and self.can_afford(UnitTypeId.NEXUS):
        #    break
        pass



