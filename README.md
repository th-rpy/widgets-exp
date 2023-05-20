# widgets-exp
Here are the improved versions of the sentences:

- After configuring the KPIs, KPIs with the "show enabled" parameter set to False still appear in Kmsweb. Upon examining the Kmsweb code, I discovered that all KPIs in the enabled group (where "show enabled" is true) are being displayed. As a solution, I added a condition in the "get KPIs" function to only return KPIs with the "show enabled" parameter set to true. I pushed the updated code to the Kmsweb CDK and now I'm waiting for the AD (Application Developer) to fix this issue in the test bench.

- I attempted to disable a group from Kmsweb using the kmsui console, but it didn't work. I have contacted the RG (Responsible Group) to verify this issue.

- The KPIs in the test bench are now available for verification by Samuel and the FPI teams. However, I'm still waiting for the AD to merge the code into the Kmsweb branch.

- I have finished applying the CDK alerts in the test bench.

- I have started writing code for alerts related to the thermometer wet: 1030, 1040, and 1050 for all TPGs (Thermometer Pressure Groups). I am currently testing them and fixing any errors in the alert signals calculations.

- When importing the data logger file, I discovered that there are files with invalid content. The values for the signals do not correspond to the total number of signals. To address this, I have added a function to verify the validity of the file.

- I have completed the script to import all files (DL and HF). Now all the files are stored in the database.
