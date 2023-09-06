from pinescriptgen_core.strategy import Strategy
from pinescriptgen_core.conditions import Condition
from pinescriptgen_core.indicators import IndicatorFactory, Indicator

import logging


logger = logging.getLogger(__name__)


class FormHandler:
    def __init__(self, request_form):
        self.request_form = request_form
        self.strategy = Strategy()

    def handle_form_input(self):
        for i in range(4):
            # Comprueba si hay valores en longEmaSma y los procesa
            if f'longEmaSma_{i}_indicatorA' in self.request_form:
                self._process_longEmaSma(i)
        # Comprueba si hay valores en longPrice y los procesa
        if "longPrice" in self.request_form:
            self._process_longPrice()

        # Comprueba si hay valores en longAdxCci y los procesa
        for i in range(2):  # Since you have 2 sets of conditions for longAdxCci
            if f'longAdxCci_{i}_indicator' in self.request_form:
                self._process_longAdxCci(i)
        if 'longDmi_indicatorA' in self.request_form:
            self._process_longDmi()

        for i in range(2):
            if f'longRsiMacd_{i}_indicatorA' in self.request_form:
                self._process_longRsiMacd(i)

    def _process_longEmaSma(self, index):
        indicatorA_value = self.request_form[f'longEmaSma_{index}_indicatorA']
        valueA = self.request_form[f'longEmaSma_{index}_valueA']
        condition_value = self.request_form[f'longEmaSma_{index}_condition']
        indicatorB_value = self.request_form[f'longEmaSma_{index}_indicatorB']
        valueB = self.request_form[f'longEmaSma_{index}_valueB']

        # Check if any of the values are empty; if they are, skip this condition
        if not (indicatorA_value and valueA and condition_value and indicatorB_value and valueB):
            return

        # Use the factory to create the indicators
        indicator1 = IndicatorFactory.create_indicator(indicatorA_value, valueA)
        indicator2 = IndicatorFactory.create_indicator(indicatorB_value, valueB)

        # Create the Condition object
        condition = Condition(condition_value, indicator1, indicator2)
        self.strategy.add_long_condition(condition)

    def _process_longPrice(self):
        price = self.request_form.get('longPrice', '')
        condition = self.request_form.get('longPrice_condition', '')
        indicator_value = self.request_form.get('longPrice_indicator', '')
        indicator_value_num = self.request_form.get('longPrice_indicatorValue', '')

        # Check if any of the values are empty; if they are, skip this condition
        if not (price and condition and indicator_value and indicator_value_num):
            return

        # If all values are non-empty, proceed with creating the Condition object
        if price == 'price':
            price = 'close'
        price_indicator = Indicator(price)
        other_indicator = Indicator(indicator_value, indicator_value_num)
        price_condition = Condition(price_indicator, condition, other_indicator)
        print(price_condition)
        self.strategy.add_long_condition(price_condition)

    def _process_longAdxCci(self, index):
        indicator_value = self.request_form.get(f'longAdxCci_{index}_indicator', '')
        condition = self.request_form.get(f'longAdxCci_{index}_condition', '')
        value = self.request_form.get(f'longAdxCci_{index}_value', '')

        # Check if any of the values are empty; if they are, skip this condition
        if not (indicator_value and condition and value):
            return

        # If all values are non-empty, proceed with creating the Condition object
        if indicator_value == 'adx':
            condition_indicator = Indicator(indicator_value, value)
            adx_cci_condition = Condition(condition_indicator, condition)
        else:
            condition_indicator = Indicator(indicator_value, value)
            adx_cci_condition = Condition(condition_indicator, condition)
        self.strategy.add_long_condition(adx_cci_condition)

    def _process_longDmi(self):
        indicatorA_value = self.request_form.get('longDmi_indicatorA', '')
        condition_value = self.request_form.get('longDmi_condition', '')
        indicatorB_value = self.request_form.get('longDmi_indicatorB', '')

        # Check if any of the values are empty; if they are, skip this condition
        if not (indicatorA_value and condition_value and indicatorB_value):
            return

        # If all values are non-empty, proceed with creating the Condition object
        indicatorA = Indicator(indicatorA_value)
        indicatorB = Indicator(indicatorB_value)
        dmi_condition = Condition(indicatorA, condition_value, indicatorB)
        print(dmi_condition)
        self.strategy.add_long_condition(dmi_condition)

    def _process_longRsiMacd(self, index):
        indicatorA_value = self.request_form[f'longRsiMacd_{index}_indicatorA']
        condition_value = self.request_form[f'longRsiMacd_{index}_condition']
        indicatorB_value = self.request_form[f'longRsiMacd_{index}_indicatorB']
        indicatorB_value_num = self.request_form[f'longRsiMacd_{index}_indicatorBValue']

        # Check if any of the values are empty; if they are, skip this condition
        if not (indicatorA_value and condition_value and indicatorB_value and indicatorB_value_num):
            return

        # If all values are non-empty, proceed with creating the Condition object
        indicatorA = Indicator(indicatorA_value)
        indicatorB = Indicator(indicatorB_value, indicatorB_value_num)
        rsi_macd_condition = Condition(indicatorA, condition_value, indicatorB)
        print(rsi_macd_condition)
        self.strategy.add_long_condition(rsi_macd_condition)
