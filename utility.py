import csv


class Utility:
    @staticmethod
    def validate_string(string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("Argument must be a string.")

        return string.replace("'", "''")

    @staticmethod
    def build_data_csv(file_path: str, column: int, class_name: type) -> list:
        data = set()
        data_as_class = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                validated_string = Utility.validate_string(row[column])

                if not validated_string in data:
                    data_as_class.append(class_name(validated_string))
                    data.add(validated_string)

        return data_as_class