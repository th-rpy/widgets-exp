
- Canfor Project: Developed a function to write tag data frames into the database and thoroughly tested it. The function performed successfully by effectively adding Mc values to the database.
- Restructured the read data functions by converting all the functions into a Python class. This modification enhanced code readability and robustness.
- Enhanced the file data result by incorporating a kiln number. Extracted the kiln number from the text file using the "Sch Number" label.
- Began adjusting the tests after implementing the aforementioned changes and introduced a new test as well.
- Incorporated a tag config file (Python file) to centralize all the necessary configurations required to run the code. This file now includes the path to the data folder, a list of equipment, signal names (both digital and analog), and tag configurations for analog signals (Mc signals).
- Modified the code to utilize this tag config file instead of passing the configurations as arguments. This approach enhances modularity and simplifies the code structure.
