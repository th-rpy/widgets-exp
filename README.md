# widgets-exp

- Collaborated with AL to implement the CDK KPIs in the production environment. Resolved warnings in the daily KPI calculations and fixed minor bugs. Pushed the updated code. It is necessary to optimize the execution time of the daily KPI calculations, as the code may run slowly without the nb KPI package. To prevent calculation errors, a function was implemented that uses raw signals to determine the package number when the nb KPI package is unavailable. Additionally, we need to enhance the calculation speed by leveraging matrix operations, as we did in the fill rate calculation, to optimize the code further.

- Initiated adjustments to the code for time-based alert calculations. Identified the list of alerts that require modification and shared them with AL. Confirmed that these alerts are the correct ones to be updated.

- Began updating and adjusting the alert signal calculations to accommodate time-based factors.

- Verified the accuracy of some adjusted alert calculations by testing them using a CSV file. The calculations appeared to be correct. Additionally, tested the updated alerts by writing them into the database and displaying them in the kmsweb test bench.

- Continued modifying the alert signal calculations and further adjusted the code for alert calculations. It is crucial to clarify the start date and end date calculations for alerts that utilize KPIs.

- Collaborated with AL to fix issues encountered while merging branches into the develop branch. Addressed the bugs and pushed the updated code.
