def setupVarious(context):
    if context.readDataFile('wcc.policy.marker.txt') is None:
        # Not your add-on
        return
