# widgets-exp

- Verified why when we load for importation for equipment and sub section , we don't see any HF files : after looking into web server code and SQL function that get the list of importation, found that  this function don't take into account the last changes made by AP in HF file importation (link the HF imported  file to all sub equipment). 
- Changed the SQL function to take into account the new changes. 
Let the '-' and use past time
