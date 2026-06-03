"""
Clock
"""
import asyncio
from pyplanet.utils.background import run_detached

from pyplanet.apps.config import AppConfig
from pyplanet.apps.core.maniaplanet import callbacks as mp_signals
from pyplanet.contrib.setting import Setting
from .views import ClockWidget
from pyplanet.core.signals import pyplanet_start_after


class Clock(AppConfig):
    game_dependencies = ['trackmania', 'trackmania_next', 'shootmania']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = ClockWidget(self)

        self.setting_enabled = Setting(
            'clock_enabled', 'Show clock widget', Setting.CAT_DESIGN, type=bool,
            description='Show the real-time clock widget in the bottom-right of the screen.',
            default=False, change_target=self.reload_clock
        )

    async def on_start(self):
        await self.context.setting.register(self.setting_enabled)
        self.context.signals.listen(mp_signals.player.player_connect, self.player_connect)
        self.context.signals.listen(mp_signals.map.map_begin, self.map_start)
        self.context.signals.listen(pyplanet_start_after, self.on_after_start)

    async def player_connect(self, player, **kwargs):
        if await self.setting_enabled.get_value():
            await self.widget.display(player)

    async def map_start(self, *args, **kwargs):
        if await self.setting_enabled.get_value():
            await self.widget.display()

    async def on_after_start(self, *args, **kwargs):
        await asyncio.sleep(1)
        run_detached(asyncio.gather(*[
            self.player_connect(p) for p in self.instance.player_manager.online
        ]))

    async def reload_clock(self, *args, **kwargs):
        # Show or hide the widget immediately when the setting is toggled.
        if await self.setting_enabled.get_value():
            await self.widget.display()
        else:
            await self.widget.hide()
