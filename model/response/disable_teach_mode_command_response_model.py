from model.response.response_model import ResponseModel


class DisableTeachModeCommandResponseModel(ResponseModel):
    def __init__(self):
        super().__init__()
        self._status = None
        self._message = None

    def get_disable_teach_mode_command_response_model(self, status):
        response_model = super().get(status=status)
        self._status = response_model.statuss
        return self

    def get_successfully_executed(self):
        self.get_disable_teach_mode_command_response_model(status=True)
        self._message = "disable teach mode command executed successfully"
        return self

    def get_exception(self, exception):
        self.get_disable_teach_mode_command_response_model(status=False)
        self._message = exception
        return self

