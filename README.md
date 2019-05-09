# Watch Dealer
### By: Eddy Nassif and Tom McKenzie

This project is designed to help watch buyers get a better deal on their used Rolex watch. By examining recent watch 
sales on Ebay, we help you determine if a current listing is a good or bad deal, and help you decipher where the market
is headed for a particular watch. To use this project, you need to understand its organization.

This project is designed so that each function is it's own Python Script. So the calculate_training_set script scrapes
Ebay and builds the dataset, the clean_ebay_data script cleans the dataset, join_data merges the current market prices
with our dataset, and so on. We hope the naming of the files makes their functions self explanatory. The different csv 
files hold our datsets across the different steps of the cleaning process. Since collecting the data using 
calculate_training_set takes a long time (about 15 minutes), we have kept our initial dirty csv file for you to look at
without having to run the code yourself. To explore specific classifiers, simply select and run the appropriate script.
The utils script has several helper functions used across other scripts. 


The 2 pdf files represent visualizations that were done to aid in the initial analysis of the data. 

The Jupyter Notebook within this project is a great place to get an overview of this projects capabilities and the 
results of different classifiers.