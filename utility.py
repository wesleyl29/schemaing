class Utility:
    @staticmethod
    def validate_string(string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("Argument must be a string.")

        return string.replace("'", "''")