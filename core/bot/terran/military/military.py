# coding=utf-8
from core.bot.generic.generic_bot_unit import GenericBotUnit
from sc2.ids.unit_typeid import UnitTypeId


class Military(GenericBotUnit):

    async def on_step(self, iteration):
        pass

    async def military_logic(self):
        num_units = len(self.units(UnitTypeId.MARINE))

        if num_units > self.number_marines:
            for marine in self.units(UnitTypeId.MARINE):
                # treinar um MARINE
                await self.do(marine.attack(self.enemy_start_locations[0]))
                self.number_marines += 5

    async def barracks_logic(self):
        marine_units = len(self.units(UnitTypeId.MARINE))
        barracks = self.units(UnitTypeId.BARRACKS).ready
        for barrack in barracks:
            if self.can_afford(UnitTypeId.BARRACKSTECHLAB) and barrack.noqueue:
                # await self.do(barrack.train(UnitTypeId.BARRACKSTECHLAB))
                pass
            elif self.can_afford(UnitTypeId.MARINE) and barrack.noqueue:
                if marine_units < 20:
                    # treinar um MARINE
                    await self.do(barrack.train(UnitTypeId.MARINE))
