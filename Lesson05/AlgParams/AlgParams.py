import os
from Lesson05.AlgParams.AlgParamsBase import AlgParamBase
# from Lesson05.AlgParams.Enums import SensorType, PipeMaterialType, AlgParamOperationType


class AlgParams(AlgParamBase):
    def __init__(self):
        super().__init__()
        self.alg_params_raw = None
        self.alg_params_data = None
        self.alg_params = None
        self.param_names = None

    def read_alg_params(self, project_id=-1):
        if self.alg_params_raw is None:
            self._read_alg_params_from_file()
        self.alg_params = self._make_simple()
        if project_id != -1:
            params_override = self.alg_params_data[project_id]
            self._handle_override(self.alg_params, params_override)
        return self.alg_params

    def _read_alg_params_from_file(self):
        file_name = os.path.join('Data', 'AlgParams.csv')
        self.alg_params_raw, self.alg_params_data = {}, {}
        with open(file_name, 'rt') as fdes:
            lines = fdes.readlines()
            header_line = lines[0]
            self.param_names = header_line[:-1].split(sep=',')
            for line in lines[1:]:
                row_values = line[:-1].split(sep=',')
                row = {param_name: row_values[i] for i, param_name in enumerate(self.param_names)}
                int_fields = ['project_id', 'operation']
                float_fields = ['value']
                for field_name in int_fields:
                    row[field_name] = int(row[field_name])
                for field_name in float_fields:
                    row[field_name] = float(row[field_name])
                project_id_tmp = row['project_id']
                param_name = row['param_name']
                self.alg_params_raw[(project_id_tmp, param_name)] = row
                if project_id_tmp not in self.alg_params_data:
                    self.alg_params_data[project_id_tmp] = {}
                self.alg_params_data[project_id_tmp][param_name] = row

    def _make_simple(self):
        alg_params = {}
        for key, row in self.alg_params_raw.items():
            project_id, param_name = key
            if project_id == -1:
                alg_params[param_name] = row['value']
        return alg_params


if __name__ == '__main__':
    worker = AlgParams()
    alg_params = worker.read_alg_params(project_id=305)
    worker._print_alg_params('AlgParams', alg_params)

