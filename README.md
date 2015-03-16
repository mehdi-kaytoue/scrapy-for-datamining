# scrapy-for-datamining
Examples of Python Scrapy to get data from the Web for Data mining

# The Miller Center dataset: speeches of the USA presidents
You have access to several speeches: http://millercenter.org/president/. The goal is to list all of them and extract the relevant information (title, date, president, text of the speech).
    This is where Scrapy enters into action.

## Get the data:
>scrapy crawl millercenter -o data.json

 Data are store in 'data.json'
 You can now test several NLP and
 supervised classification techniques

### To test CSS selectors for the data items
> scrapy shell http://millercenter.org/president/obama/speeches/speech-4427

-###################-
-## Happy mining! ##-
-## Share results!##-
-## @MehdiKaytoue ##-
-###################-
