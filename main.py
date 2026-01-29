import time
from volume_utils import get_system_volume, set_system_volume
from device_utils import headphones_connected
from cute_notifier import show_cute_warning

THRESHOLD_VOLUME = 20   # warn if above this
SAFE_VOLUME = 10        # reduce volume to this
CHECK_INTERVAL = 0.2      # seconds

alerted = False

print("🎧 Volume Guard is running...")

while True:
    if headphones_connected():
        current_volume = get_system_volume()

        if current_volume > THRESHOLD_VOLUME and not alerted:
            show_cute_warning(current_volume, SAFE_VOLUME)
            set_system_volume(SAFE_VOLUME)
            alerted = True

        elif current_volume <= THRESHOLD_VOLUME:
            alerted = False
    else:
        alerted = False

    time.sleep(CHECK_INTERVAL)
