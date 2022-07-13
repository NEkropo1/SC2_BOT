from loguru import logger

from sc2.bot_ai import BotAI
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId


class NekroMakroBot(BotAI):
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
        if iteration == 0:
            for worker in self.workers:
                worker.gather(self.mineral_field.closest_to(self.start_location))

            #for main_nexus in self.townhalls:
            #    main_nexus.train(UnitTypeId.PROBE)
