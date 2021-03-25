import os
import pandas as pd
from Lesson05.AlgParams.Enums import AlgParamOperationType, SensorType, PipeMaterialType


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

    def _handle_override(self, params, key):
        if key in self.alg_params_data:
            params_override = self.alg_params_data[key]
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


class AlgParams(AlgParamBase):
    def __init__(self):
        super().__init__()
        self.alg_params = None

    def read_alg_params(self, project_id=-1):
        if self.alg_params_raw is None:
            self._read_alg_params_from_file_pandas('AlgParams.csv')
        self.alg_params = self._make_simple()
        if project_id != -1:
            key = project_id
            self._handle_override(self.alg_params, key)
        return self.alg_params

    def _read_alg_params_from_file_pandas(self, file_name):
        super()._read_alg_params_from_file_pandas(file_name)
        self.alg_params_raw, self.alg_params_data = {}, {}
        for row in self.alg_params_rows:
            project_id = row['project_id']
            param_name = row['param_name']
            key = project_id
            self.alg_params_raw[(project_id, param_name)] = row
            if key not in self.alg_params_data:
                self.alg_params_data[key] = {}
            self.alg_params_data[key][param_name] = row


class AlgParamsMaterial(AlgParamBase):
    def __init__(self):
        super().__init__()
        self.alg_params = None

    def read_alg_params(self,
                        couple_calc_type: SensorType = SensorType.Any,
                        material_id: PipeMaterialType= PipeMaterialType.Any,
                        project_id: int=-1):
        if self.alg_params_raw is None:
            self._read_alg_params_from_file_pandas('AlgParamsMaterials.csv')
        self.alg_params = self._make_simple()
        if couple_calc_type.value != -1:
            self._handle_override(self.alg_params,
                                  key=(couple_calc_type.value, -1, -1))
        if material_id.value != -1:
            self._handle_override(self.alg_params,
                                  key=(-1, material_id.value, -1))
        if couple_calc_type.value != -1 and material_id.value != -1:
            self._handle_override(
                self.alg_params,
                key=(couple_calc_type.value, material_id.value, -1))
        if project_id != -1:
            self._handle_override(self.alg_params, key=(-1, -1, project_id))
            self._handle_override(
                self.alg_params,
                key=(couple_calc_type.value, material_id.value, project_id))
        return self.alg_params

    def _read_alg_params_from_file_pandas(self, csv_file_name):
        super()._read_alg_params_from_file_pandas(csv_file_name)
        self.alg_params_raw, self.alg_params_data = {}, {}
        for row in self.alg_params_rows:
            couple_calc_type = row['couple_calc_type']
            material_id = row['material_id']
            project_id = row['project_id']
            param_name = row['param_name']
            key = (couple_calc_type, material_id, project_id)
            self.alg_params_raw[
                (couple_calc_type, material_id, project_id, param_name)
            ] = row
            if key not in self.alg_params_data:
                self.alg_params_data[key] = {}
            self.alg_params_data[key][param_name] = row


if __name__ == '__main__':
    worker1 = AlgParams()
    alg_params = worker1.read_alg_params(project_id=305)
    worker1._print_alg_params('AlgParams', alg_params)

    worker2 = AlgParamsMaterial()
    alg_params = worker2.read_alg_params(
        couple_calc_type=SensorType.Hydrophone,
        material_id=PipeMaterialType.DuctileIron, project_id=305)
    worker2._print_alg_params('AlgParamsMaterial', alg_params)
