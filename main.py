from eos_app_package.validate import save_array_to_file
import argparse

if __name__ == '__main__':
    """
    Parses CLI command and receives file_name and array as strings. 
    Calls a method to validate inputs, process array and save into 
    file provided by file_name argument.
    
    Usage:
    main.py [-h] <filename> <array>
    
    main.py [-h] "data/arrays/array.csv" "[[1,2],[3,4]]"
    main.py [-h] "array.json" "[[0,0],[421,13245],[12456,65463]]"
    
    """
    parser = argparse.ArgumentParser(description="Receives file name, array.")
    parser.add_argument('file_name', type=str, help='FIle name')

    parser.add_argument('array', type=str, help='Array')
    args = parser.parse_args()

    save_array_to_file(args.file_name, args.array)
