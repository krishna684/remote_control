bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
    cuteBot.stopcar()
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    receivedString = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    // --- CUTEBOT MOTOR CONTROL ---
    // --- SERVO CONTROL (P2) ---
    // Only listening for 'x' now.
    // Fixes "half slide" by mapping 0-100 input to 0-180 degrees.
    if (receivedString == "up") {
        cuteBot.motors(50, 50)
    }
    if (receivedString == "down") {
        cuteBot.motors(-50, -50)
    }
    if (receivedString == "right") {
        cuteBot.motors(40, -40)
    }
    if (receivedString == "left") {
        cuteBot.motors(-40, 40)
    }
    if (receivedString == "stop") {
        cuteBot.stopcar()
    }
    if (receivedString.charAt(0) == "x") {
        rawValue = parseFloat(receivedString.substr(1, 3))
        // Map slider value (0 to 100) to Servo Angle (0 to 180)
        angle = pins.map(
        rawValue,
        0,
        100,
        90,
        0
        )
        pins.servoWritePin(AnalogPin.P2, angle)
    }
})
let angle = 0
let rawValue = 0
let receivedString = ""
bluetooth.startUartService()
basic.showIcon(IconNames.Square)
