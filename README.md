BLoto649
========
Beautiful Loto 6/49

BLoto649 parses the table from the Romanian lottery archives ( http://www.loto49.ro/arhiva-loto49.php ) and creates a dictionary with the number of occurrences for each of the 49 numbers serving the dictionary in a simple web page.

It uses BeautifulSoup for the HTML parsing and web.py to serve a simple page with the results (which uses Yahoo Pure for CSS styling but right now looks ugly as hell).

Future plans:

    - Use a task script which updates a Redis back-end every Sunday with the new results
    
    - Fetch the results from the memory database instead of parsing the archive for every request
    
    - Beautify
    
    - Use the numbers to generate some statistics-based draws.
