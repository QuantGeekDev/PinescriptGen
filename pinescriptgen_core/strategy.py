import logging

logger = logging.getLogger(__name__)


class Strategy:
    def __init__(self):
        self.long_conditions = []
        self.short_conditions = []
        self.take_profit = {}
        self.stop_loss = {}
        self.operation_management = {}

    def add_long_condition(self, condition):
        try:
            logger.info("Adding long condition to Strategy.")
            self.long_conditions.append(condition)
            logger.info("Long condition added to Strategy successfully.")
        except Exception as e:
            logger.error(f"Error adding long condition to Strategy: {e}")
            raise e

    def add_short_condition(self, condition):
        self.short_conditions.append(condition)

    def set_take_profit(self, tp_data):
        self.take_profit = tp_data

    def set_stop_loss(self, sl_data):
        self.stop_loss = sl_data

    def set_operation_management(self, op_mgmt_data):
        self.operation_management = op_mgmt_data
