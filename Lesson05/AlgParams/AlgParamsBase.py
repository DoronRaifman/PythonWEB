
from Lesson05.AlgParams.Enums import AlgParamOperationType


class AlgParamBase:
    def __init__(self):
        pass

    @staticmethod
    def _handle_override(params, params_override):
        for param_name, param_data in params_override.items():
            operation = param_data['operation']
            if operation == AlgParamOperationType.Replace.value:
                params[param_name] = param_data['value']
            elif operation == AlgParamOperationType.Multiply.value:
                params[param_name] *= param_data['value']
            else:
                print(f"Override without operation for param {param_name}")

    @staticmethod
    def _print_alg_params(title, alg_params):
        print(title)
        sorted_names = sorted(alg_params.keys())
        for param_name in sorted_names:
            value = alg_params[param_name]
            print(f'\t{param_name}: {value}')

