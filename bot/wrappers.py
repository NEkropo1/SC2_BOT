from loguru import logger
import sc2
from sc2.bot_ai import BotAI
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from .managers import *


class BaseWrapper:

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
