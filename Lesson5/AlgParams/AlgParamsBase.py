
from Lesson5.AlgParams.Enums import AlgParamOperationType


class AlgParamBase:
    def __init__(self):
        pass

    @staticmethod
    def _handle_override(params, params_override):
        for param_name, param_data in params_override.items():
            operation = param_data['operation']
            if operation == AlgParamOperationType.Replace.value:
                params[param_name]['value'] = param_data['value']
            elif operation == AlgParamOperationType.Multiply.value:
                params[param_name]['value'] *= param_data['value']
            else:
                print(f"Override without operation for param {param_name}")

