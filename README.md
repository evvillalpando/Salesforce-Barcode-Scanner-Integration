# Salesforce barcode scanner integration
 Integration of wireless barcode scanners with Salesforce queries, using tracking numbers as keys.
 This was developed as a solution to tracking the movement of PC repairs for the company I currently work for–Skytech Gaming. This is still a work in progress and the goal is to make it entirely object-oriented (it is partially object-oriented at the moment).
 
 ## How it works
 With a wireless barcode scanner, it takes in tracking numbers and/or warehouse location barcodes as input. Once it receives empty input, it ceases taking input and outputs a dataframe with the following fields:
 - **Case Number**: Used as the key for RMA cases.
 - **URL for the tracking number**: Automatically determines if it's a UPS or FedEx tracking number. Goal: ~~add a webscraping method for pulling the date of arrival from the URL~~-- DONE! Date received is important for determining the queue for repairs.
 - **Model**: the SKU of the PC being tracked. This makes it easier for repair techs to know what they're looking for.
 - **RMA Status**: A factor with several levels, including Case in Progress, RMA Shipped, and RMA Resolved (among others). This is an important attribute because it's not uncommon for RMAs such as Refunds or Replacements to be resolved before the PC arrives.
 - **Customer Email Address**: This is primarily used to determine if the case belongs to a Rent-A-Center, as we often don't prioritize these cases.
 - **Location**: Location of the PC. This is determined using string-to-barcode labels attached to different locations in the warehouse. Examples include: R1T (Rack 1, Top), R2B (Rack 2, Bot), or P1 (pallet 1).

## Features in development
1. Proper documentation within the script
2. Shipping label consistency check: scan both the incoming label and the newly created outgoing label to ensure there is no label mixups with the PCs. This will help minimize human error in shipping. Scanning of outgoing label will also update Salesforce with the outgoing tracking number and set proper parameters in the case document to trigger a separate email script to send the tracking to the customer.
3. Make it *completely* consistent with object-oriented paradigms. As of now, it is not entirely object-oriented.
4. Create a UI for better accessibility.
