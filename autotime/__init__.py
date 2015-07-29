from __future__ import print_function

import time

from IPython.core.magics.execution import _format_time as format_delta


class LineWatcher(object):

    """Class that implements a basic timer.

    Notes
    -----
    * Register the `start` and `stop` methods with the IPython events API.
    """

    def __init__(self):
        self.start_time = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        stop_time = time.time()

        if self.start_time:
            diff = stop_time - self.start_time
            assert diff >= 0
            print('time: {}'.format(format_delta(diff)))


timer = LineWatcher()


def load_ipython_extension(ip):
    ip.events.register('pre_run_cell', timer.start)
    ip.events.register('post_run_cell', timer.stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', timer.start)
    ip.events.unregister('post_run_cell', timer.stop)


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
