let Angle_Boussole = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showNumber(input.compassHeading())
})
input.onGesture(Gesture.Shake, function () {
    input.calibrateCompass()
})
basic.forever(function () {
    Angle_Boussole = input.compassHeading()
    if (Angle_Boussole == 0) {
        basic.showLeds(`
            # . . # .
            # # . # .
            # . # # .
            # . . # .
            # . . # .
            `)
    } else if (Angle_Boussole == 270) {
        basic.showLeds(`
            # # # . .
            # . . . .
            # # . . .
            # . . . .
            # # # . .
            `)
    } else if (Angle_Boussole == 90) {
        basic.showLeds(`
            # # # # .
            # . . # .
            # . . # .
            # . . # .
            # # # # .
            `)
    } else if (Angle_Boussole == 180) {
        basic.showLeds(`
            # # # . .
            # . . . .
            . # . . .
            . . # . .
            # # # . .
            `)
    } else {
        basic.showIcon(IconNames.No)
    }
})
