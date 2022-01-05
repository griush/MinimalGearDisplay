import sys
import ac
import acsys

l_gear = 0
gear = 0
gear_text = "N"

app_window = 0

def acMain(ac_version):
    global l_gear, app_window

    app_name = "Minimal Gear Display"

    # Window creation
    global app_window
    app_window = ac.newApp(app_name)
    ac.setSize(app_window, 100, 140)
    ac.setTitle(app_window, "")
    ac.drawBorder(app_window, 0)
    ac.setIconPosition(app_window, 0, -9001)
    ac.setBackgroundOpacity(app_window, 0)
    ac.addRenderCallback(app_window, acUpdate)

    # Label creation
    l_gear = ac.addLabel(app_window, gear_text)
    ac.setPosition(l_gear, 25, 0)
    ac.setFontAlignment(l_gear, "center")
    ac.setFontSize(l_gear, 85)

    return app_name

def acUpdate(deltaT):
    global l_gear, gear

    # Window update
    ac.setBackgroundOpacity(app_window, 0)

    # Gear update
    gear_c = ac.getCarState(0, acsys.CS.Gear)

    if gear_c != gear:
        gear = gear_c

        if gear == 0:
            gear_text = "R"
        elif gear == 1:
            gear_text = "N"
        else:
            gear_text = str(gear - 1)

        ac.setText(l_gear, "{}".format(gear_text))
