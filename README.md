# widgets-exp

- Addressed two minor bugs in the digital graph as pointed out by AD. Instead of using "children" as a property for Dcc.Store, we switched to using "data" property. Additionally, there was an issue with tooltip position when hovering over the digital signals graph with a scroll bar. AD suggested applying the same approach used in the KPI graph. We adjusted the callback in the KPI graph to align with the digital graph. We thoroughly tested the changes and pushed the updated code.

- Continued reviewing the issues in batches. While plotting signals by package number and by batch-bundle, we observed that the package number 6149-2 appeared only twice in the data of package number 213, indicating abnormal data. This confirms that the anomalies in the raw data caused errors in defining the package number for the batch-bundle.

- After consulting with AL, we made the decision to calculate the package number at the start of each batch and then use the KPI package number to retrieve signals for the batch-bundle in the kmsweb CDK. This approach eliminates the need for a separate calculation function.

- Implemented additional security measures in the package number definition for the batch-bundle to ensure accurate determination by the function.

- Introduced comprehensive tests for CDK events. Ran all the tests and ensured that they passed successfully, validating the code changes.

- Conducted code cleanup in both the development CDK and Kmsweb CDK, enhancing readability and pushing the refined code.

- Initiated the process of retrieving data from a text file for the Canfor project. The script successfully reads the file, extracts start and end dates, and writes the target Mc and final Mc. Thorough testing was performed to verify the accuracy of the data extraction and processing.
