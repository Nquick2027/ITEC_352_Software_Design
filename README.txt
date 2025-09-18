Nathan Quick
02/24/2025
Created using ChatGPT

Product Viewer Program
=======================

Author: Nathan Quick  
Date: 02/24/2025  

Description:
------------
This program allows users to view details of various products, including their price, discount percentage, and final price after the discount. Users can also leave a rating and a review for each product.  

Files:
------
1. objects.py  
   - Contains class definitions for `Product`, `LineItem`, and `Quality`.  
   - `Product`: Represents a product with attributes like name, price, and discount percentage.  
   - `LineItem`: Represents a product with a quantity for total price calculation.  
   - `Quality`: Stores product rating, review, and total number of reviews.  

2. product_viewer.py  
   - Implements the main program logic.  
   - Displays a list of products and their details.  
   - Allows users to select a product and provide a review.  

How to Run:
-----------
1. Ensure Python is installed on your system.  
2. Place `objects.py` and `product_viewer.py` in the same directory.  
3. Open a terminal or command prompt.  
4. Run the program using:  
5. Follow on-screen prompts to view product details and submit reviews.  

Dependencies:
-------------
- No external dependencies; runs with standard Python libraries.  

Notes:
------
- Enter a product number to view its details.  
- Provide a rating (1-5) and a review when prompted.  
- Press 'y' to continue viewing products or 'n' to exit.  
