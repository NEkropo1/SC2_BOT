from sc2 import maps
from sc2.player import Bot, Computer
from sc2.main import run_game
from sc2.data import Race, Difficulty

from bot import NekroBot

run_game(maps.get("2000AtmospheresAIE_NO_AI"), [
    Bot(Race.Terran, NekroBot()),
    Computer(Race.Terran, Difficulty.Medium)
], realtime=False, save_replay_as="replays/replay.SC2Replay"
)
