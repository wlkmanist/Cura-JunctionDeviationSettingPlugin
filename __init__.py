# Copyright (c) 2024 wlkmanist
# The JunctionDeviationSettingPlugin is released under the terms of the AGPLv3 or higher.

from . import JunctionDeviationSettingPlugin


def getMetaData():
    return {}

def register(app):
    return {"extension": JunctionDeviationSettingPlugin.JunctionDeviationSettingPlugin()}
