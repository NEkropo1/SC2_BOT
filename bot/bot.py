from loguru import logger

from sc2.bot_ai import BotAI
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer


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


class NekroMakroBot(BotAI):
    async def on_start(self):
        """
        ВЫЗЫВАЕТСЯ ПЕРЕД НАЧАЛОМ ИГРЫ
        :return:
        """
        logger.info("The game has started")

    def __init__(self):
        self.unit_command_uses_self_do = True

    async def on_step(self, iteration: int):
        """
        ВЫЗЫВАЕТСЯ КАЖДЫЙ КАДР
        :param iteration:
        :return:
        """
        if iteration == 0:

            for nexus in self.townhalls.ready:
                nexus.train(UnitTypeId.PROBE)
                self.do(nexus(AbilityId.EFFECT_CHRONOBOOST, nexus))

            workers = list()
            minerals = list()
            for worker in self.workers:
                workers.append(worker)
                if len(workers) == 2:
                    for counted_worker in workers:
                        for mineral in self.mineral_field.sorted_by_distance_to(worker):
                            if mineral not in minerals:
                                minerals.append(mineral)
                                counted_worker.gather(mineral)
                                break
                            else:
                                continue

    async def chronoboost(self):
        for nexus in self.townhalls.ready:
            if nexus.energy >= 50:
                await self.do(nexus(AbilityId.EFFECT_CHRONOBOOST, nexus))
