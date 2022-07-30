from loguru import logger
import sc2
from sc2.bot_ai import BotAI
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from bot import *
from .wrappers import *


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

    def update(self):
        print("i'm updating", self)

    #async def on_step(self, iteration: int):
    #    for worker in NekroMakroBot.workers:
    #        self.workers.append(worker)
    #        if len(workers) == 2:
    #            for mineral in self.mineral_field.sorted_by_distance_to(worker)[:7]:
    #                for counted_worker in workers:
    #                    if mineral not in minerals:
    #                        self.do(counted_worker(AbilityId.HARVEST_GATHER_PROBE, mineral))
    #                        self.draw_sphere(counted_worker.position)

    #                if mineral not in minerals:
    #                    minerals.append(mineral)
    #                # if mineral not in BaseWrapper.MINERAL_LIST:
    #            workers.clear()
