# widgets-exp
- Addressed the issues related to CDK KPI (productivity) calculations in AL. Enhanced the detection of end dates for batches and made necessary adjustments to the drying status. Thoroughly tested the implemented changes, and they successfully resolved the problems.

- Implemented the required modifications in dev_cdk and pushed the code to fix the KPI productivity calculations. AL: Integrated these changes into both the develop and master branches.

- Merged the develop branch into dev CDK to ensure that the code remains up to date.

- Introduced a script to adjust the information dates for older batches. Tested the script and confirmed that it performed as expected.

- Continued enhancing the digital figures by incorporating a scroll bar to the sign graph container.

- Initiated the implementation of AL's suggestions to make the figures more refined and elegant.

- Conducted an investigation on how to add a cursor to the figures.

- Implemented a hover template for the digital figure to improve the user experience.

- Replaced the API for obtaining raw signals with the db read function, "get raw data," to ensure that raw signals include digital signals. This change addressed significant issues and bugs that needed to be resolved.
