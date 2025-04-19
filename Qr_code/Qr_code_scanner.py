import cv2
from pyzbar.pyzbar import decode
import time
import webbrowser

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

webbrowser.register(
    'chrome',
    None,
    webbrowser.BackgroundBrowser(chrome_path)
)

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

scanned_data = set()

while True:
    success, frame = cam.read()
    if not success:
        break

    for barcode in decode(frame):
        data = barcode.data.decode('utf-8')
        if data not in scanned_data:
            scanned_data.add(data)
            print(f"Opening: {data}")
            webbrowser.get(using='chrome').open(data)
            time.sleep(6)

    cv2.imshow("My_QR_Code_Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()