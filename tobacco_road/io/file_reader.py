import os
import os.path


class FileReader:
    """
    """

    def __init__(self, f_path: str = None):
        pass

    @classmethod
    def read(f_path):
        with open(f_path, "r") as f_in:
            header = f.readline().strip().split(",")
            lines = f.readlines()

        data = []
        for line in lines:
            line_dict = {
                header[idx].lower(): int(row) for idx, row in zip(header, line.strip().split(","))
            }
            data.append(line_dict)

        return data


# __END__
