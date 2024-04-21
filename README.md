# Project Name: Information Retrieval System

## Overview

This project comprises three main components:
- A Scrapy-based Crawler for downloading web documents in HTML format.
- A Scikit-Learn-based Indexer for constructing an inverted index in pickle format.
- A Flask-based Processor for handling free text queries in JSON format.

## Table of Contents
1. [Abstract](#abstract)
2. [Overview](#overview)
3. [Design](#design)
4. [Architecture](#architecture)
5. [Operation](#operation)
6. [Conclusion](#conclusion)
7. [Data Sources](#data-sources)
8. [Test Cases](#test-cases)
9. [Source Code](#source-code)
10. [Bibliography](#bibliography)

## Abstract

This project aims to develop a web document crawler and query processor system using Scrapy, Scikit-Learn, and Flask. The objectives include efficient web document retrieval, indexing using TF-IDF and cosine similarity, and providing accurate and fast text query processing. Next steps involve optimizing the system for scalability and incorporating advanced search techniques.

## Overview

The solution consists of a Scrapy-based crawler that retrieves web documents, a Scikit-Learn-based indexer that constructs an inverted index, and a Flask-based processor for handling free text queries. Relevant literature includes web scraping techniques, information retrieval methods, and natural language processing for query handling.

## Design

The system's design encompasses the capabilities of each component: content crawling, search indexing, and query processing. Interactions between the crawler, indexer, and processor are coordinated for seamless operation.

## Architecture

Software components include the Scrapy crawler, Scikit-Learn indexer, and Flask processor. Interfaces are defined for data input/output and system integration. Implementation details cover the use of libraries for web scraping, text analysis, and web service development.

## Operation

### SCRAPER: 
Navigate to the Crawler directory and from there, into the Spiders Directory. There you will find the "crawlingspider.py" file. This is the main spider that was used to crawl the internet. In order to use it locate the start_urls variable, there you can swap it out for whatever website you would like. 

```start_urls = ['https://en.wikipedia.org/wiki/League_of_Legends']```
```# this is already preloaded with the starting wikipedia article```

You will also need to update the link extractor in order to allow you to navigate to different links, locate the ```__init__``` function and from there, it will be the first variable initialized

```self.link_extractor = LinkExtractor(allow='https://en.wikipedia.org/wiki/League_of_Legends', unique=True)```

The allow= parameter will be updated to the link of your choice. make sure that it is still within the single quote. From there you are done with updating the link and can simply run the program directly as I have added the function calls 
```process.crawl(MyCrawler)```

```process.start()```
in order to allow you to skip having to use the terminal to navigate to the directory and run the spider from there. 

### INDEXER:
There is not much to test in the indexer, if you would like to see the contents of the pickle file you can use the pickler.py file. simply edit this to the file that you would like to access 

```with open('similarity_matrix.pkl', 'rb') as f:```

```similarity_matrix = pickle.load(f)```

in this case you would change the similarity_matrix.pkl file. you can also update the number of rows. Due to the size of the files you can only see up to a certain amount at a time. the files themselves are well commented in order for easy reading and understanding. 

### FLASK:
The final section in operating the file would be Flask. Simply run the file and you will be given a link to your local machine on port 5000. A short guide on how to use it in tandum with Postman. 

- Create a new request on Postman
- Post the link of the Request to the link provided by the flask file, ENSURE YOU ADD "/query" AT THE END OF YOUR LINK OR IT WILL NOT WORK!
- Navigate to the headers tab after you connect, add a new value-key pair. under keys add "Content-Type" and under value add "application/json"
- Change GET to POST in the search bar, and naviate to the body tab
- select raw, and then you can add your query in the form of a json. for test cases, please see the test cases section of the Readme file. 

## Conclusion

The project successfully implements a web document crawler and query processor. Results demonstrate efficient content retrieval, accurate indexing, and fast query responses. Limitations include scalability challenges with large datasets and potential improvements in search accuracy.

## Data Sources

HTML files are located in the TestDocuments directory of the repository. The contents of which can be swapped using the steps in the operation section of this readme and the scraper provided. For sake of testing, the TestDocuments folder already comes loaded with Files for testing purposes

## Test Cases

Test queries:

```{"query": "League of legends"}```

```{"query": "League"}```

```{"query": "Noah"}```

```{"query": "Shulk"}```

```{"query": "video game"}```

these two should not return anything as they have nothing to do with videogames

```{"query": "Ice cream"}``` 

```{"query": "Chocolate"}```


## Bibliography

- AI Softwares 
- Library documentations