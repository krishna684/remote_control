def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
    cuteBot.stopcar()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global receivedString, rawValue, angle
    receivedString = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    # --- CUTEBOT MOTOR CONTROL ---
    # --- SERVO CONTROL (P2) ---
    # Only listening for 'x' now.
    # Fixes "half slide" by mapping 0-100 input to 0-180 degrees.
    if receivedString == "up":
        cuteBot.motors(50, 50)
    elif receivedString == "down":
        cuteBot.motors(-50, -50)
    elif receivedString == "right":
        cuteBot.motors(40, -40)
    elif receivedString == "left":
        cuteBot.motors(-40, 40)
    elif receivedString == "stop":
        cuteBot.stopcar()
    elif receivedString.char_at(0) == "x":
        rawValue = parse_float(receivedString.substr(1, 3))
        # Map slider value (0 to 100) to Servo Angle (0 to 180)
        angle = pins.map(rawValue, 0, 100, 90, 0)
        pins.servo_write_pin(AnalogPin.P2, angle)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

angle = 0
rawValue = 0
receivedString = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)