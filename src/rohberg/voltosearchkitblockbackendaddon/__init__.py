"""Init and utils."""
import logging
from zope.i18nmessageid import MessageFactory


PACKAGE_NAME = "rohberg.voltosearchkitblockbackendaddon"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
