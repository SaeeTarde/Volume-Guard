from pycaw.pycaw import AudioUtilities


def get_active_output_device_name():
    device = AudioUtilities.GetSpeakers()
    return device.FriendlyName.lower()


def headphones_connected():
    name = get_active_output_device_name()

    keywords = [
        "headphone",
        "headset",
        "earphone",
        "bluetooth",
        "buds"
    ]

    for word in keywords:
        if word in name:
            return True

    return False
