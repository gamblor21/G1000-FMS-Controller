import usb_hid
import time
import rotaryio
import digitalio
import board

time.sleep(10)
print("Starting")

in_rot = rotaryio.IncrementalEncoder(board.IO5, board.IO6)
in_rot.divisor = 2
out_rot = rotaryio.IncrementalEncoder(board.IO12, board.IO14)
out_rot.divisor = 2
button = digitalio.DigitalInOut(board.IO18)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

buttons = []
for pin in [board.IO33, board.IO38, board.IO1, board.IO3, board.IO7, board.IO10]:
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append(b)

device = usb_hid.devices[0]

report = bytearray(2)

last_in_position = 0
last_out_position = 0

while True:
    report[0] = 0
    report[1] = 0

    position = in_rot.position
    if position > last_in_position:
        report[0] |= 0x01
        last_in_position = position
    elif position < last_in_position:
        report[0] |= 0x02
        last_in_position = position

    position = out_rot.position
    if position > last_out_position:
        report[0] |= 0x04
        last_out_position = position
    elif position < last_out_position:
        report[0] |= 0x08
        last_out_position = position

    if button.value is False:
        report[0] |= 0x10

    for i in range(0,len(buttons)):
        if buttons[i].value is False:
            report[1] |= (1 << i)

    device.send_report(report)
    time.sleep(0.03)
