import sys

class CustomException(Exception):

    def __init__(
        self,
        error_message,
        error_detail: sys
    ):
        self.error_message = (
            self.get_error_message(
                error_message,
                error_detail
            )
        )

        super().__init__(
            self.error_message
        )

    @staticmethod
    def get_error_message(
        error_message,
        error_detail
    ):

        _, _, exc_tb = error_detail.exc_info()

        return (
            f"Error: {error_message} "
            f"Line Number: {exc_tb.tb_lineno}"
        )
    