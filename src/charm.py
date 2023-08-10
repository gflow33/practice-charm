#!/usr/bin/env python3
# Copyright 2023 Kaioh
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following tutorial that will help you
develop a new k8s charm using the Operator Framework:

https://juju.is/docs/sdk/create-a-minimal-kubernetes-charm
"""

import logging
import os
import shutil
import subprocess

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus, MaintenanceStatus

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)



class PracticeCharmCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.start, self._on_start)
        self.framework.observe(self.on.stop, self._on_stop)
        #self._stored.set_default(message=self.config["message"])

    def _on_install(self, event):
        logger.info(f"Installing cmatrix")
        os.system('apt install -y cmatrix')

    # def _on_config_changed(self, event):
    #     """ 
    #     Update the message configuration and set the unit status
    #     """

    #     self.unit.status = ActiveStatus(f"")

    def _on_start(self, event):
        logger.info(f"Starting cmatrix")
        subprocess.Popen(['cmatrix'])
        # os.system('cmatrix')
        if not os.system('apt list | grep cmatrix') == 0:
            logger.info("cmatrix is not installed")
            self.unit.status = MaintenanceStatus("Not installed.")
        else:
            logger.info(f"cmatrix is running")
            self.unit.status = ActiveStatus("Running")

    def _on_stop(self, event):
        logger.info(f"Stopping cmatrix")
    #     source_path = 'bash/cmatrix.sh'
    #     destination_path = os.path.expanduser('~/cmatrix.sh')

    # try:
    #     shutil.copyfile(source_path, destination_path)
    #     os.system('bash ~/cmatrix.sh')
    # except FileNotFoundError:
    #     logger.error(f"Source file '{source_path}' not found.")
    # except Exception as e:
        # logger.error(f"An error occurred: {e}")
        # 
        shutil.copy('script/cmatrix.sh', os.path.expanduser('~/cmatrix.sh'))
        os.system('bash ~/cmatrix.sh')
            

if __name__ == "__main__": 
    main(PracticeCharmCharm)
