import os
import pandas as pd
from Lesson05.AlgParams.Enums import AlgParamOperationType


class AlgParamBase:
    def __init__(self):
        self.alg_params_rows = None
        self.param_names = None
        self.alg_params_raw = None
        self.alg_params_data = None

    def _read_alg_params_from_file_pandas(self, file_name):
        file_name = os.path.join('Data', file_name)
        data = pd.read_csv(file_name)
        self.alg_params_rows = data.to_dict(orient='records')
        self.param_names = self.alg_params_rows[0].keys()

    # demonstrate how much more complicated without pandas
    def _read_alg_params_from_file(self, file_name):
        file_name = os.path.join('Data', file_name)
        self.alg_params_rows = []
        with open(file_name, 'rt') as fdes:
            lines = fdes.readlines()
            header_line = lines[0]
            self.param_names = header_line[:-1].split(sep=',')
            for line in lines[1:]:
                row_values = line[:-1].split(sep=',')
                row = {param_name: row_values[i] for i, param_name in enumerate(self.param_names)}
                int_fields = ['project_id', 'operation', 'couple_calc_type', 'material_id']
                float_fields = ['value']
                for field_name in int_fields:
                    if field_name in row:
                        row[field_name] = int(row[field_name])
                for field_name in float_fields:
                    if field_name in row:
                        row[field_name] = float(row[field_name])
                self.alg_params_rows.append(row)

    def _make_simple(self):
        alg_params = {}
        for key, row in self.alg_params_raw.items():
            is_default = True
            for val in key[:-1]:
                if val != -1:
                    is_default = False
                    break
            if is_default:
                alg_params[key[-1]] = row['value']
        return alg_params

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
