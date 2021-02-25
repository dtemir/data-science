# Nobel Prize Laureates Data Visualization

* In the [**Scraping Nobel Prize Winners Jupyter Notebook**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/Scraping%20Nobel%20Prize%20Winners.ipynb), 
  we use the BeautifulSoup4 library to scrape Wikipedia's [List of Nobel Laureates](https://en.wikipedia.org/wiki/List_of_Nobel_laureates).
  <details>
  
    * We use **BeautifulSoup's** lxml parser to select the table with the xpath of <code>table.sortable.wikitable</code>.
    * We then iterate over the columns and rows of the table to fetch information like name, year, category, and link in a list.
    * We also try to scrape nationalities of each laureate by making a request to each of their personal pages and
    sending a request to fetch it from the xpath of <code>table.infobox tr</code>.
    * See the notebook for more, [**NBViewer**](https://nbviewer.jupyter.org/github/dtemir/data-science/blob/main/data-visualization-oreilly/Scraping%20Nobel%20Prize%20Winners.ipynb). 
  </details>

* In the [**nobel_winners**](https://github.com/dtemir/data-science/tree/main/data-visualization-oreilly/nobel_winners) directory, 
  we use Scrapy to build spiders that crawl Wikipedia's [List of Nobel laureates by country](https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country)
  for data.
  
  <details>

    * We use **Scrapy** and xpath to scrape data from the pages.
    * The first spider is [**nwinners_list_spider**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/nobel_winners/nobel_winners/spiders/nwinners_list_spider.py), 
      for scraping a list of Nobel Laureates into a *json* file, [**nobel_winners.json**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/nobel_winners/nobel_winners/nobel_winners.json).
      * The spider scrapes information like name, year, category, country, year of birth, year of death.
    * The second spider is [**nwinners_minibio**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/nobel_winners/nobel_winners/spiders/nwinners_minibio.py), 
      for scraping each Laureate individual bio from their wikipage into a *json* file, [**minibios.json**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/nobel_winners/nobel_winners/minibios.json).
      * The spider scrapes information like the first paragraph of their bio, image urls, and link to their webpage. 
        (check [**pipelines.py**](https://github.com/dtemir/data-science/blob/main/data-visualization-oreilly/nobel_winners/nobel_winners/pipelines.py) for how it saves the images)
  </details>
 