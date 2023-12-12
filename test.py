
import time
from src.common.vkeys import press, key_down, key_up

# List of key mappings
class Key:
    # Movement
    JUMP = 'space'
    TELEPORT = 'ctrl'

    # Buffs
    MAGIC_GUARD = 'a'

    # Buffs Toggle

    # Skills
    MAGIC_CLAW = 'w'


def main():
    time.sleep(2)
    press(Key.JUMP, 3, down_time=0.1)
    press(Key.MAGIC_CLAW, 3, down_time=0.1)
    print("done")

main()