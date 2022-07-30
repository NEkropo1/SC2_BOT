from loguru import logger
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from .base_bot import BaseBot
from .wrappers import *
from .managers import Manager, BaseManager


class NekroMakroBot(BaseBot):
    def __init__(self):
        self.unit_command_uses_self_do = True
        self.raw_affects_selection = True

    async def on_start(self):
        """
        ВЫЗЫВАЕТСЯ ПЕРЕД НАЧАЛОМ ИГРЫ
        :return:
        """
        logger.info("The game has started")
        self.managers = [BaseManager() for _ in range(10)]

    async def on_step(self, iteration: int):
        """
        ВЫЗЫВАЕТСЯ КАЖДЫЙ КАДР
        :param iteration:
        :return:
        """
        Manager.update_instances()

        if iteration == 0:

            for nexus in self.townhalls.ready:
                self.do(nexus(AbilityId.NEXUSTRAIN_PROBE))
                self.do(nexus(AbilityId.EFFECT_CHRONOBOOST))

        if iteration > 0:

            for nexus in self.townhalls.ready:
                if nexus.energy >= 50 and not nexus.is_idle:
                    self.do(nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus))
                if nexus.is_idle and self.can_afford(UnitTypeId.PROBE) and self.supply_workers < nexus.ideal_harvesters and self.can_feed(UnitTypeId.PROBE):
                    self.do(nexus(AbilityId.NEXUSTRAIN_PROBE))


