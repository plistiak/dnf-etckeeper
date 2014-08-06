# etckeeper.py, support etckeeper for dnf
#
# Copyright (C) 2014 Peter Listiak
#

from dnfpluginscore import logger

import os
import dnf


class Etckeeper(dnf.Plugin):

    name = 'etckeeper'

    def _out(self, msg):
        logger.debug('Etckeeper plugin: %s', msg)

    def resolved(self):
        self._out('pre transaction commit')
        servicecmd = '/usr/bin/etckeeper'
        command = '%s %s' % (servicecmd, " pre-install")
        ret = os.system(command)
        if ret != 0:
            raise dnf.exceptions.Error('etckeeper returned %d' % (ret >> 8))

    def transaction(self):
        self._out('post transaction commit')
        servicecmd = '/usr/bin/etckeeper'
        command = '%s %s > /dev/null' % (servicecmd, "post-install")
        os.system(command)

