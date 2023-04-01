import unittest
from eos_app_package.validate import validate_path, validate_process_array, save_array_to_file
from pathlib import Path
import numpy as np


class TestFilename(unittest.TestCase):
    """
    A unit test class for validating file paths and extensions.

    Tests the behaviour of the 'validate_path' function for the correct and incorrect extensions, existing a file.

    :param self.files : list of instances type of pathlib.Path. One for csv and one for json file.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """Declares files list and creates a directory for test files."""
        cls.files = [Path('test', 'test_file.csv'),
                     Path('test', 'test_file.json')]
        cls.files[0].parent.mkdir()

    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes test directory at the end of testing this class."""
        cls.files[0].parent.rmdir()

    def test_extension(self) -> None:
        """Testing validate_path function by sending invalid extensions for filename"""
        wrong_ext = ['.jsn', '.', '45']
        for ext in wrong_ext:
            with self.assertRaises(ValueError):
                validate_path(str(self.files[0].with_suffix(ext)))

    def test_file_not_exists(self) -> None:
        """Testing validate_path function by sending valid filename """
        for file in self.files:
            self.assertEqual(validate_path(str(file)), None)

    def test_file_exists(self) -> None:
        """Testing case when filename is valid but file already exists"""
        for file in self.files:
            with self.assertRaises(FileExistsError):
                with open(file, 'w'):
                    pass
                validate_path(file)
            if file.is_file():
                file.unlink()


class TestArray(unittest.TestCase):
    """
    A unit test class for validating and process array.

    Tests the behaviour of the 'validate_process_array' function for the valid input and input with wrong dimensionality.
    """

    def test_dimensions(self) -> None:
        """Testing arrays with inappropriate dimensionality."""
        test_array = ['[[1], [4], [8]]',
                      '[[1, 3, 5], [4, 7, 0], [8, 12, 54]]',
                      '[[1], [4, 2], [8, 4, 6]]']
        for array in test_array:
            with self.assertRaises(ValueError):
                validate_process_array(array)

    def test_valid_input(self) -> None:
        """Testing with valid input."""
        test_array = np.array([[1., 2], [4, 5], [7, 8]], dtype=np.int32)
        np.testing.assert_array_equal(test_array, validate_process_array('[[1,2],[4,5], [7,8]]'))


class TestSave(unittest.TestCase):
    """
    A unit test class for saving json and csv files.

    Tests the behaviour of the 'save_array_to_file' function for creating a file.

    :param self.files : list of instances type of pathlib.Path. One for csv and one for json file.
    :param self.array : array covered by string.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Declares files list, array and creates a directory for test files."""
        cls.files = [Path('test', 'test_file.csv'),
                     Path('test', 'test_file.json')]
        cls.files[0].parent.mkdir()
        cls.array = '[[1, 2], [4, 5], [7, 8]]'

    @classmethod
    def tearDownClass(cls) -> None:
        """Deletes test directory and files in it at the end of testing this class."""
        for file in cls.files:
            if file.is_file():
                file.unlink()
        cls.files[0].parent.rmdir()

    def test_save(self) -> None:
        """Testing saving file to a directory"""
        for file in self.files:
            save_array_to_file(str(file), self.array)
            if not file.resolve().is_file():
                raise AssertionError("The file was not created")


if __name__ == "__main__":
    unittest.main()
