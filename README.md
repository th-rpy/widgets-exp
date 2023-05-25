# widgets-exp
- +AL: Reviewed the Key Performance Indicators (KPIs) for water removal. Discovered that certain bundles contain an unusually high amount of water. Verified the calculations and identified that the issue originates from the packtallys data.

- Upon examining the effecto data for the invalid bundles, found instances of duplicate packtallys data for a single bundle. Decided to compile a list of effecto IDs corresponding to the invalid packs.

- Developed code to list out the effecto IDs of the invalid bundles and stored them in an Excel file.

- Reviewed the average push rate KPI values and removed a filter from the push rate calculation. After eliminating the filter, encountered negative values. Upon analyzing the code, determined that these issues were related to the calculation of start dates and end dates.

- Commenced improving the start and end date calculation by incorporating a function to determine the end date for bundles with invalid position data.

- Tested the improvement by generating a CSV file. +AL validated the results, confirming their accuracy.

- Executed the code in a test bench to update the dates. Although the dates were correct, they were not updated in kmslive 1!

- Implemented code for daily KPIs temperature grouping.

- Developed code for alerts, specifically for codes 4011, 4021, and 4031.

- Modified certain parameters in alert 3111 and made changes to the code of other alerts.

- Generated a CSV file containing alerts and obtained numerous entries. To ensure accuracy, verification with +AL was necessary.

- Resolved a bug in the SQL function importation for black box events.

- Initiated the process of writing code to import all black box files.

- Added the signal red ID to the sign name for displaying the complete signal name during data viewing. Pushed the code.
