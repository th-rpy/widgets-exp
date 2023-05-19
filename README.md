# widgets-exp


- +RG addressed some errors and issues in the SQL function after applying the new changes.

- Modified the Python code for data import: considered all changes in data logger import and HF data files. To expedite the code, utilized pandas functions to extract data values for signals, resulting in a faster execution. Saved 3 seconds per HF file import. Tested the updated code, and it worked successfully.

- Created a Python script to retrieve all files from the drive and import them. Currently testing the code. If it functions correctly, we will remove all imports in the database and re-import all the files.

- Completed writing all KPIs per batch and per day in the "kmslive 1" database. Some KPIs that I disabled from the KPIs configuration using the "kmsui" console are still accessible in "Kmsweb." This needs to be verified with +RG.

- Cleaned up the code and pushed it. It should be reviewed by AL before sharing the results with Samuel and Marc for deployment in production.
- 


