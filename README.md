# eos-app
Test task for Junior Data Engineer position.

Task: Create a package that allows saving a two-dimensional integer list to a JSON or CSV file. Also, create a module that provides a CLI interface for the user to input the file path and the list. Depending on the file extension, the package should determine which method (CSV or JSON) to use to save the list. The input data should be validated and errors should be reported in case of an existing file, unknown file extension, or a non-two-dimensional array. The package should also be covered with unit tests.

What was done:
1) Created project eos-app
2) Created package eos-app-package with init file and validate.py
3) Created main.py
4) Created test_module.py


**_eos-app-package.validate_** contains of 3 functions: </br>
  &nbsp;&nbsp;**validate_path for validating** conditions fo existing file and unknown file extension; </br>
  &nbsp;&nbsp;**validate_process_array** for converting string object to an array with checking it`s dimesionality;</br>
  &nbsp;&nbsp;**save_array_to_file** for calling 2 previous functions to validate and process recieved arguments and for saving result to a suitable file.
 
**_main_** function parses arguments given from CLI interface from the user and calls save_array_to_file.

**_test_module_** created to test package`s functions. It consist of 3 classes, each for separate function from package. Tests build to cover base instructions and to check functions by pushing valid arguments.

So, how does it work?

![image](https://user-images.githubusercontent.com/76254554/229301734-175588b9-2ee6-4d8e-b677-e20ddd05e344.png)

No output - great success!</br>
Now we are going to test our conditions.

![image](https://user-images.githubusercontent.com/76254554/229301810-9577498c-12c1-4053-a48a-1e04c50f3174.png)

FileExistsError. Just like we mentioned it to be!

![image](https://user-images.githubusercontent.com/76254554/229301844-327b4446-5ab3-497c-8ffa-fb6c742e1a60.png)

Unsupported extension! Yeah, we don`t know what ".cv" mean. CSV and JSON are my besties!

![image](https://user-images.githubusercontent.com/76254554/229301970-ef861c97-0f4a-421d-bcd6-36bbd94feb19.png)

What a disrepect! We don`t want to see ane non-two-dimensional arrays!

![image](https://user-images.githubusercontent.com/76254554/229302270-fbd6142d-6e1d-4ebe-8e21-a0ff1c0c9afc.png)

And finally our test results. Hope you liked it!
