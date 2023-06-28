# widgets-exp

- +AL: Investigated the slow performance of the KMSWEB CDK side in signal display. Added a decorator to profile the function using the CProfile library, allowing for a comprehensive analysis of execution time and function calls. Discovered that the `read` method of `_ssl._SSLSockt` is consuming a significant amount of time and making numerous calls.
- Shared the analysis results with AL and decided to optimize data transfer by reducing the number of requests made to the database. Began investigating methods to decrease the number of calls and overall execution time of the function.
- +AL: Discussed the next task, which involves adding a digital signals graph for project K-22-01. Provided an explanation of the objective and the specific signals that need to be displayed.
- AL requested to disable the Filter interface by default and requested translation of the words related to the filter interface into French. Made the necessary changes and pushed the code.
- +AL: Conducted a quick review of the compute start batch based on CDK KPIs. Made the requested minor changes.
