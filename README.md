# widgets-exp



- +AL reviewed the local code of the database and found errors when testing it. We need to add the creation of the schema database. The build db code is not functioning correctly and there are additional errors that need to be fixed.

- The errors were fixed by enhancing the security in the create db code. Now, if one or more tables or datatypes fail to be created successfully, we won't proceed with functions creation.

- Another error was discovered and resolved. The main issue was that certain tables depended on others, so we needed to create the tables in the correct order. A function was added to obtain references for tables and ensure they are created in the proper sequence.

- AL tested the code and pushed it for further testing.

- The configuration of CDK KPIs was continued, and some issues were fixed. Additionally, certain KPIs that need to be removed were disabled. The code for RTD probes was completed by renaming all signal names.

- Following a meeting with the FPI teams, it was determined that we need to add the "work_fan_time_pct" KPI per zone. The configuration is finished, and the code is ready for testing.

- +AL reviewed the KPI values in the Kmsweb test bench and identified some KPIs based on the set point temperature that need to be changed to "nan." The code was updated accordingly.

- For the push rate, certain values need to be verified.
