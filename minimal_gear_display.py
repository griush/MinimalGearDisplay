"""
    Minimal Gear Display 1.2
    
    minimal_gear_display.py made by griush (Github profile: https://github.com/griush/)
    made for Assetto Corsa app Minimal Gear Display (Github repo: https://github.com/griush/MinimalGearDisplay)
                                                    (Race Department: https://www.racedepartment.com/downloads/minimal-gear-display.47703/)

    Licensed under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

    Thanks to Rombik for "SimInfo" class.

"""

import os
import sys
import traceback

import ac
import acsys

try:

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dll'))
    from third_party.sim_info import info

except Exception:
        ac.console("MGD : import Error: %s" % traceback.format_exc())
        ac.log("MGD : import Error: %s" % traceback.format_exc())

""" Settings """
limitRPMPerCent = 0.04
limitRPM = 0
optimalRPM = 1300 # Not used

""" Objects """
l_gear = 0
l_shadow = 0

gear = 0
gear_text = "N"

rpms = 0

app_window = 0

def acMain(ac_version):

    global limitRPMPerCent, limitRPM
    
    app_name = "Minimal Gear Display"
    
    limitRPM = info.static.maxRpm * limitRPMPerCent

    # Window creation
    global app_window
    app_window = ac.newApp(app_name)
    ac.setSize(app_window, 100, 140)
    ac.setTitle(app_window, "")
    ac.drawBorder(app_window, 0)
    ac.setIconPosition(app_window, 0, -9001)
    ac.setBackgroundOpacity(app_window, 0)
    ac.addRenderCallback(app_window, acUpdate)
    
    # Shadow label creation
    global l_shadow
    l_shadow = ac.addLabel(app_window, gear_text)
    ac.setPosition(l_shadow, 28, 3)
    ac.setFontAlignment(l_shadow, "center")
    ac.setFontSize(l_shadow, 85)
    ac.setFontColor(l_shadow, 0.1, 0.1, 0.1, 0.7)
    
    # Label creation
    global l_gear
    l_gear = ac.addLabel(app_window, gear_text)
    ac.setPosition(l_gear, 25, 0)
    ac.setFontAlignment(l_gear, "center")
    ac.setFontSize(l_gear, 85)
    ac.addRenderCallback(l_gear, acUpdate)
    
    return app_name

def acUpdate(deltaT):
    global l_gear, gear, rpms, limitRPM

    gear_c = ac.getCarState(0, acsys.CS.Gear)

    """ Window update """
    ac.setBackgroundOpacity(app_window, 0)

    """ Label color update """
    maxRPM = info.static.maxRpm
    rpms = ac.getCarState(0, acsys.CS.RPM)
    
    if gear_c > 1:
        if maxRPM - rpms < limitRPM:
            ac.setFontColor(l_gear, 1, 0, 0, 1)
        # elif maxRPM - rpms < optimalRPM:
        #     ac.setFontColor(l_gear, 0, 1, 0, 1)
        else:
            ac.setFontColor(l_gear, 1, 1, 1, 1)
    else:
        if maxRPM - rpms < limitRPM:
            ac.setFontColor(l_gear, 1, 0, 0, 1)
        else:
            ac.setFontColor(l_gear, 1, 1, 1, 1)
    
    """ Gear text update """

    if gear_c != gear:
        gear = gear_c

        if gear == 0:
            gear_text = "R"
        elif gear == 1:
            gear_text = "N"
        else:
            gear_text = str(gear - 1)

        ac.setText(l_shadow, "{}".format(gear_text))
        ac.setText(l_gear, "{}".format(gear_text))
