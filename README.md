# widgets-exp
The following actions were taken to improve the system:
- Adjusted time-based alerts and generated alerts from 2020-08-26 to the latest available date in the database. This period was chosen due to the presence of critical alerts such as 1050, 6030, 6040, 7020, and 7030.
- Deactivated the detection of alert 7020 and recorded all alerts (1050, 7020, 7030, 6040, and 6030) in the database between 08-03-2023 and 17-04-2023.
- Requested AL to run KMSPRO to display the alerts in KMSWEB Test and verified some alerts in KMSWEB, which appeared to be functioning correctly. The FPI teams will review these alerts.
- +AL: After improving the CDK code calculation functions, AL decided to rewrite CDK PARAMS as a function to determine the parameters of CDK for the project. This function was implemented, and the necessary changes were made to make the code for KPIs and alert calculations more generic and explicit. These changes need to be integrated into dev_alerts to improve the CDK calculations alerts.
- Decided with AL to create KPIs for CDK based on batch like pkg_nb, track_number, batch_start_date. Started to prepare the code for those KPIs.
- Made minor changes requested by AL, cleaned up the code, and pushed the changes. AL merged all the code into develop, so the develop branch needs to be merged into the dev_cdk branch.
