from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


def _get_volume_interface():
    device = AudioUtilities.GetSpeakers()
    interface = device._dev.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))


def get_system_volume():
    volume = _get_volume_interface()
    return int(volume.GetMasterVolumeLevelScalar() * 100)


def set_system_volume(percent):
    volume = _get_volume_interface()
    volume.SetMasterVolumeLevelScalar(percent / 100, None)
