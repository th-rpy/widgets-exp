# .

- 

+AL: A solution was found to update the dates for bundles in kmslive 1. The end and start dates were manually changed to random dates within the original range. This allowed for the subsequent update with the correct dates. After running the code to re-extract and update the dates, the changes were successfully applied to kmslive1. The next step is to update the dates on the production side.

Following the correction of the dates, the calculation for the average push rate KPI was re-run, resulting in the removal of negative values.

An investigation was conducted to identify the cause of consistently lower fill rate values in the daily KPIs over the past few days. It was discovered that the volume, length, and package number KPIs had issues. After fixing the problems and re-running the code, the values were corrected and the updated code was pushed.

+AL: The list of invalid effecto IDs has been shared for the necessary fixes. The removal values for water have now been corrected.

Furthermore, a script was completed to import all black box events and the importation process was improved. As a result, all black box events are now successfully stored in the database
