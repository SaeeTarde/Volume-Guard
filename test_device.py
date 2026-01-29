from device_utils import headphones_connected, get_active_output_device_name

print("Active device:", get_active_output_device_name())

if headphones_connected():
    print("🎧 Headphones detected")
else:
    print("🔊 Speakers detected")
