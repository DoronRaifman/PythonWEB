import os
from Lesson05.AlgParams.AlgParamsBase import AlgParamBase


class AlgParams(AlgParamBase):
    def __init__(self):
        super().__init__()
        self.alg_params = None

    def read_alg_params(self, project_id=-1):
        if self.alg_params_raw is None:
            self._read_alg_params_from_file_pandas('AlgParams.csv')
        self.alg_params = self._make_simple()
        if project_id != -1:
            params_override = self.alg_params_data[project_id]
            self._handle_override(self.alg_params, params_override)
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


if __name__ == '__main__':
    worker = AlgParams()
    alg_params = worker.read_alg_params(project_id=305)
    worker._print_alg_params('AlgParams', alg_params)

