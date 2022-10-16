from loguru import logger
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2 import position
from sc2.base_bot import BaseBot
from sc2.wrappers import *
from sc2.managers import Manager, BaseManager, ExpansionManager
from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.ids.unit_typeid import UnitTypeId
from sc2.main import run_game
from sc2.player import Bot, Computer
from examples.terran.onebase_battlecruiser import BCRushBot
import random
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class NekroMakroBot(BaseBot):
    def __init__(self):
        #self.unit_command_uses_self_do = True
        self.raw_affects_selection = True
        self.pylon_counter = 0
        self.managers = [BaseManager() for _ in range(10)]


    async def on_start(self):
        """
        ВЫЗЫВАЕТСЯ ПЕРЕД НАЧАЛОМ ИГРЫ
        :return:
        """
        logger.info("The game has started")


    async def on_step(self, iteration: int):
        """
        ВЫЗЫВАЕТСЯ КАЖДЫЙ КАДР
        :param iteration:
        :return:
        """
        Manager.update_instances()
        await self.distribute_workers()
        await self.build_workers()
        await self.build_supply()
        await self.build_gas()
        await self.expand()
        print(len(self.workers))

        #if iteration == 0:
            # this is for reminding how self.do works
            # for worker in self.workers:
            #  self.do(worker(AbilityId.ATTACK, self.enemy_start_locations[0]))
            # first

    async def build_workers(self):
        for nexus in self.townhalls.ready:
            if nexus.energy >= 50 and not nexus.is_idle:
                nexus(AbilityId.EFFECT_CHRONOBOOSTENERGYCOST, nexus)
            if nexus.is_idle and self.can_afford(UnitTypeId.PROBE) \
                    and (self.supply_workers <= nexus.ideal_harvesters*len(self.townhalls) + 8) \
                    and self.can_feed(UnitTypeId.PROBE) \
                    and self.supply_workers < 66:
                nexus.train(UnitTypeId.PROBE)

    async def build_supply(self):
        ccs = self.townhalls(UnitTypeId.NEXUS).ready
        if ccs.exists:
            cc = ccs.first
            if self.supply_left < 3 and not self.already_pending(UnitTypeId.PYLON) and self.pylon_counter < 2:
                if self.can_afford(UnitTypeId.SUPPLYDEPOT):
                    await self.build(UnitTypeId.PYLON, near=cc.position.towards(self.game_info.map_center, 5))
                    self.pylon_counter += 1

            elif self.pylon_counter >= 2 < 20:
                if self.can_afford(UnitTypeId.PYLON):
                    nexus = self.townhalls.random
                    print(nexus.position[0] + nexus.position[1])
                    # key = abs([point2] - nexus.position)
                    pos = self.start_location.towards(self.game_info.map_center, random.randrange(8, 15))
                    if self.can_place(UnitTypeId.PYLON, [pos, pos]):
                        self.workers.random.build(UnitTypeId.PYLON, position=pos)
                        self.pylon_counter += 1

    async def build_gas(self):
        for nexus in self.townhalls.ready:
            vgs = self.vespene_geyser.closer_than(15, nexus)
            for vg in vgs:
                if not self.can_afford(UnitTypeId.ASSIMILATOR):
                    break
                worker = self.select_build_worker(vg.position, force=True)
                if worker is None:
                    break
                if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
                    worker.build(UnitTypeId.ASSIMILATOR, vg)
                    worker.stop(queue=True)

    async def expand(self):
        if self.townhalls(UnitTypeId.NEXUS).amount < 3 and self.can_afford(UnitTypeId.NEXUS):
            await self.expand_now()


def main():
    run_game(
        maps.get("2000AtmospheresAIE_NO_AI"),
        [Bot(Race.Protoss, NekroMakroBot()), (Race.Terran, BCRushBot())],
        realtime=False,
    )


if __name__ == "__main__":
    main()
