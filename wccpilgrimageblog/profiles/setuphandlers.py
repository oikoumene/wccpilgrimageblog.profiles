from collective.grok import gs
from wccpilgrimageblog.profiles import MessageFactory as _

@gs.importstep(
    name=u'wccpilgrimageblog.profiles', 
    title=_('wccpilgrimageblog.profiles import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wccpilgrimageblog.profiles.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
