import os
from Lesson05.AlgParams.AlgParamsBase import AlgParamBase
from Lesson05.AlgParams.Enums import SensorType, PipeMaterialType


class AlgParamsMaterial(AlgParamBase):
    def __init__(self):
        super().__init__()
        self.alg_params_data = None
        self.alg_params = None

    def read_alg_params(self, couple_calc_type: SensorType = SensorType.Any,
                        material_id: PipeMaterialType= PipeMaterialType.Any, project_id: int=-1):
        if self.alg_params_raw is None:
            self._read_alg_params_from_file('AlgParamsMaterials.csv')
        self.alg_params = self._make_simple()
        if couple_calc_type.value != -1:
            params_override = self.alg_params_data[(couple_calc_type, -1, -1)]
            self._handle_override(self.alg_params, params_override)
        if material_id.value != -1:
            params_override = self.alg_params_data[(-1, material_id, -1)]
            self._handle_override(self.alg_params, params_override)
        if couple_calc_type.value != -1 and material_id.value != -1:
            params_override = self.alg_params_data[(couple_calc_type, material_id, -1)]
            self._handle_override(self.alg_params, params_override)
        if project_id != -1:
            params_override = self.alg_params_data[(-1, -1, project_id)]
            self._handle_override(self.alg_params, params_override)
            params_override = self.alg_params_data[(couple_calc_type.value, material_id.value, project_id)]
            self._handle_override(self.alg_params, params_override)
        return self.alg_params

    def _read_alg_params_from_file(self, csv_file_name):
        super()._read_alg_params_from_file(csv_file_name)
        file_name = os.path.join('Data', csv_file_name)
        self.alg_params_raw, self.alg_params_data = {}, {}
        for row in self.alg_params_rows:
            couple_calc_type = row['couple_calc_type']
            material_id = row['material_id']
            project_id = row['project_id']
            param_name = row['param_name']
            key = (couple_calc_type, material_id, project_id)
            self.alg_params_raw[(couple_calc_type, material_id, project_id, param_name)] = row
            if key not in self.alg_params_data:
                self.alg_params_data[key] = {}
            self.alg_params_data[key][param_name] = row


if __name__ == '__main__':
    worker = AlgParamsMaterial()
    alg_params = worker.read_alg_params(project_id=305)
    worker._print_alg_params('AlgParamsMaterial', alg_params)

