# Pub reaper: *tools for gathering scientific publication information*

Many scientific journal publishers, such as the American Chemical Society (ACS), do not provide an API which enables the public to access large-scale trends in scientific publications over time. Other services like Google Scholar enable the public to search thorough multiple publication databases, but only provide 10 search results at a time, and do not allow export of the search results into a useful format for further analysis.


This repository contains tools for aggregating online scientific publication data in order to develop models for how publication trends and topics evolve over time.

### Description of files
* **scholar_scraper.ipynb**: Jupyter notebook which scrapes publication data from Google Scholar and eports it to file
* **scholar_scraper_methods**: Python functions used in *scholar_scraper.ipynb* notebook
* **.txt files**: examples of exported publication data which has been aggregated online and exported to file
