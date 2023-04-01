import numpy as np
from pathlib import Path
import json


def validate_path(file_path: str) -> None:
    """
    Validates provided path by this conditions:
    1) File by this path not exists;
    2) Provided extension is valid only if its CSV or JSON.

    Otherwise raises an Exception:
    FileExistsError - if file exists,
    ValueError - if unsupported extension was pushed

    :param file_path: str
           The path to validate
    :return: None.
    """
    file_path = Path(file_path)

    if file_path.exists():
        raise FileExistsError(f'File "{file_path}" already exists')

    if file_path.suffix not in ['.json', '.csv']:
        raise ValueError(f'Unsupported file extension "{file_path.suffix}"')

    # if path.is_dir():
    #     raise ValueError(f'"{path}" is a directory, not a file')

    # if not path.name.split('.')[0]:
    #     raise ValueError('Filename is empty')


def validate_process_array(string_array: str) -> np.ndarray:
    """
    Validates and process array from string to numpy array format.

    Raises an error if array is not 2-dimensional.

    :param string_array: str
           An array to validate and process.
    :return: arr: np.ndarray
           Resulting 2-dimensional array.
    """
    array = json.loads(string_array)
    if any(len(x) != 2 for x in array):
        raise ValueError('Array is not two-dimensional')

    arr = np.array(array, dtype=np.int32)
    return arr


def save_array_to_file(file_path: str, string_array: str) -> None:
    """
    Save a 2-dimensional numpy array as a CSV or JSON file.

    Raises an error if path exists, the file already exists or array is not 2-dimensional.

    :param file_path: The path of the output file.
    :param string_array: The input array.
    :return: None
    """
    validate_path(file_path)
    arr = validate_process_array(string_array)

    file_path = Path(file_path)

    if not file_path.parent.is_dir():
        file_path.parent.mkdir(parents=True)

    if file_path.suffix == '.json':
        arr_list = arr.tolist()
        with open(file_path, 'w') as f:
            json.dump(arr_list, f)
    else:
        np.savetxt(file_path, arr, delimiter=',')
