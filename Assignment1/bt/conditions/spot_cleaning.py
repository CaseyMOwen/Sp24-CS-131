#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.0 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import SPOT_CLEANING


class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "Spot Cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking Spot Cleaning")
        if blackboard.get_in_environment(SPOT_CLEANING, False):
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
