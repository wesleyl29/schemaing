import csv


class Utility:
    @staticmethod
    def validate_string(string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("Argument must be a string.")

        return string.replace("'", "''")

    @staticmethod
    def build_data_csv_no_duplicates(file_path: str, column: int) -> list:
        data = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                validated_string = Utility.validate_string(row[column])

                if not validated_string in data:
                    data.append(validated_string)


        return list(dict.fromkeys(data)) # remove duplicates

    @staticmethod
    def build_data_csv(file_path: str, column: int) -> list:
        data = []

        with open(file_path, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                validated_string = Utility.validate_string(row[column])
                data.append(validated_string)

        return data