#!/bin/env python

import clientlib
from clientlib import info


def classifier(task):
    deploy_control = control()
    if task == "deploy":
        ans = deploy_control.deploy(task)
    elif task == "delete":
        ans = deploy_control.delete(task)
    elif task == "reconfig":
        ans = deploy_control.reconfig(task)
    return ans


class control(object):

    def deploy(self, task):
        print("Deploy {0}".format(task))
        self._preaction(task)
        return ("Deploying")
        
    def _preaction(self, task):
        print("action 1")
        clientlib.info.getinfo()

    def delete(self, task):
        print("Deleting")
        clientlib.info.destroy()
        return ("Deleting")

    def reconfig(self, task):
        print("reconfiguriing")
        info()
        return ("reconfigure")