Angle_Boussole = 0

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_number(input.compass_heading())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    input.calibrate_compass()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global Angle_Boussole
    Angle_Boussole = input.compass_heading()
    if Angle_Boussole == 0:
        basic.show_leds("""
            # . . # .
                        # # . # .
                        # . # # .
                        # . . # .
                        # . . # .
        """)
    elif Angle_Boussole == 270:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        # # . . .
                        # . . . .
                        # # # . .
        """)
    elif Angle_Boussole == 90:
        basic.show_leds("""
            # # # # .
                        # . . # .
                        # . . # .
                        # . . # .
                        # # # # .
        """)
    elif Angle_Boussole == 180:
        basic.show_leds("""
            # # # . .
                        # . . . .
                        . # . . .
                        . . # . .
                        # # # . .
        """)
    else:
        basic.show_leds("""
            # . . # .
                        . # # . .
                        . # # . .
                        . # # . .
                        # . . # .
        """)
basic.forever(on_forever)
