import logging


logger = logging.getLogger(__name__)


class PineScriptGenerator:
    @staticmethod
    def generate(strategy):
        try:
            logger.info("Generating PineScript for the given strategy.")
            script_lines = ["@version=5", "strategy(\"PinescriptGen Strategy\", overlay=true)"]

            long_conditions = []
            for condition in strategy.long_conditions:
                long_conditions.append(PineScriptGenerator.generate_condition(condition))
            script_lines.append(f"longCondition = {' and '.join(long_conditions)}")

            short_conditions = []
            for condition in strategy.short_conditions:
                short_conditions.append(PineScriptGenerator.generate_condition(condition))
            script_lines.append(f"shortCondition = {' and '.join(short_conditions)}")

            for tp_key, tp_val in strategy.take_profit.items():
                script_lines.append(f"{tp_key} = close * (1 + {tp_val['percent']}/100)")
            percent_val = strategy.stop_loss.get('percent', 0)  # Default to 0 if 'percent' isn't present
            script_lines.append(f"stopLoss = close * (1 - {percent_val}/100)")

            script_lines.append(
                "strategy.entry(\"Long\", strategy.long, when=longCondition, stop=stopLoss, takeprofit={tp1, tp2, tp3})")
            script_lines.append(
                "strategy.entry(\"Short\", strategy.short, when=shortCondition, stop=stopLoss, takeprofit={tp1, tp2, tp3})")

            if 'trailing' in strategy.operation_management:
                script_lines.append(
                    f"strategy.exit(\"Exit Long\", from_entry=\"Long\", trail_offset={strategy.operation_management['trailing']})")
                script_lines.append(
                    f"strategy.exit(\"Exit Short\", from_entry=\"Short\", trail_offset={strategy.operation_management['trailing']})")
            if 'breakEven' in strategy.operation_management:
                script_lines.append(
                    f"if (strategy.position_size > 0 and close > strategy.position_avg_price + {strategy.operation_management['breakEven']['pips']})")
                script_lines.append(
                    "    strategy.exit(\"Break Even Long\", from_entry=\"Long\", limit=strategy.position_avg_price)")
                script_lines.append(
                    f"if (strategy.position_size < 0 and close < strategy.position_avg_price - {strategy.operation_management['breakEven']['pips']})")
                script_lines.append(
                    "    strategy.exit(\"Break Even Short\", from_entry=\"Short\", limit=strategy.position_avg_price)")
            logger.info("PineScript generated successfully.")
            return "\n".join(script_lines)
        except Exception as e:
            logger.error(f"Error generating PineScript: {e}")
            raise e

    @staticmethod
    def generate_condition(condition):
        if condition.condition == "crossUp":
            return f"crossover({condition.indicatorA.formatted()}, {condition.indicatorB.formatted()})"
        elif condition.condition == "crossDown":
            return f"crossunder({condition.indicatorA.formatted()}, {condition.indicatorB.formatted()})"

        if condition.indicatorB is None:
            # Only use indicatorA and condition
            return f"{condition.indicatorA.formatted()} {condition.condition}"
        else:
            # Use both indicators
            return f"{condition.indicatorA.formatted()} {condition.condition} {condition.indicatorB.formatted()}"
