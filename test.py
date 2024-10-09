import time
from ppadb.client import Client as AdbClient
from PIL import Image
import pytesseract

client = AdbClient(host="127.0.0.1", port=5037)

def connect_device():
    devices = client.devices()
    if not devices:
        print("No devices connected.")
        return None
    return devices[0] 

def take_screenshot(device):
    screenshot = device.screencap()
    with open("screenshot.png", "wb") as f:
        f.write(screenshot)

def find_text_position(image_path, text):
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    
    for i, word in enumerate(data['text']):
        if text.lower() in word.lower():
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            return (x + width // 2, y + height // 2)

    return None

def main():
    device = connect_device()
    if not device:
        return

    while True:
        take_screenshot(device)
        position = find_text_position("screenshot.png", "Brian")
        
        if position:
            x, y = position
            device.shell(f"input tap {x} {y}")
            print(f"Clicked at: ({x}, {y})")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
