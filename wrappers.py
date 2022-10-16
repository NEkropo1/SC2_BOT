from loguru import logger
import sc2
from sc2.bot_ai import BotAI
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from sc2.managers import *


class BaseWrapper:

    MINERALS_LIST = list()

    def __init__(self, unit):
        self.unit = unit
        self.tag = unit.tag
        self.is_mineral_field = unit.is_mineral_field


    @classmethod
    def add_mineral(cls, unit):
        if unit.is_mineral_field:
            BaseWrapper.MINERALS_LIST.append(unit)

    @staticmethod
    def clear_minerals():
        BaseWrapper.MINERALS_LIST = list()


class Mineral(BaseWrapper):
    def __init__(self, unit, **kwargs):
        super().__init__(unit)
        self.workers = list()

    def add_worker(self, unit):
        self.workers.append(unit)


class Expansion(BaseWrapper):

    def __int__(self, unit, **kwargs):
        super().__init__(unit)
        self.workers = list()
        self.minerals = list()
        self.gas = list()
        self.base = 0
        self.MAX_WORKERS = len(self.minerals) * 2 + len(self.gas) * 3
        self.location = None

    def add_gas(self, unit):
        if len(self.gas) <= 2:
            self.gas.append(unit)

    def add_mineral(self, unit):
        if len(self.minerals) <= 14:
            self.workers.append(unit)

    def add_worker(self, unit):
        if len(self.workers) <= self.MAX_WORKERS:
            self.workers.append(unit)

    def has_base(self):
        return self.base


