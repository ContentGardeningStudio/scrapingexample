# scrapingexample
Example scraping code using BeautifulSoup and requests

1st you have to import the libraries with import
if you don't have the libraries you have to use pip install

Then you have to send a request get to the url you want to extract informations

If the status code is 200 (it means that the url is ok), you can create an object soup with BeautifulSoup like :
soup =  BeautifulSoup(res.text, 'html-parser')
You are free to use the parser you want

After, you must initialize a variable that will store the result of your scraping
In our case, we will store the main title of the website

In the end, we can display the title with a print