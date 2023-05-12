# widgets-exp
- Rectified the configuration errors related to the new Key Performance Indicators (KPIs), including code writing and thorough testing.

- Conducted an investigation into the root causes of errors pertaining to bundle end date entries, identifying two primary reasons. Efforts were made to address these issues, while AL (presumably a colleague) recommended enhancing the end date determination process by avoiding extrapolation.

- Modified the function responsible for retrieving CDK batches from the database, incorporating start date and end date data.

- Tested the alterations during bank testing by recalculating the end date for certain bundles. Upon executing the corrected code, the revised end dates were successfully incorporated. Validation with AL is pending.
