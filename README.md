# pyreiseamt
The German Foreign Office publishes travel information for nearly all countries in the world. This includes information on security and medical matters. Information is up-to-date and allows to asses whether a certain country is safe to visit or not.

pyreiseamt is designed to crawl the information on https://www.auswaertiges-amt.de/de/ReiseUndSicherheit/reise-und-sicherheitshinweise and present the data in structured JSON format. Also, pyreiseamt can deliver sentiment analysis for every country and every category. This allows you to mine the available data more efficently.

### Installation
You can install pyreiseamt via pip.

```bash
pip install pyreiseamt
```

After installation has finished, you have the choice to use pyreiseamt as a CLI tool or input its scraper into one of your scripts.

### Usage

pyreiseamt offers a unified point of entry for two basic tasks: *list* available countries and *extract* information on one or more countries.

#### List Available Countries
If you want to get a list of available country names (or want to make sure that you use the correct one), you can use the *list* command. There are no additonal arguments needed for that:

```bash
pyreiseamt list
```

After fetching the newest data from the Foreign Office's website, you will get a list of all available countries printed to your screen. There are four countries for every row and the single countries are seperated by ' | '.


#### Extract Information
Assume that you want to crawl information on all available countries. You can use the *extract* with the *-o* (output path) argument. *-o* should point to a json file where the results will be written to. Note that your output file should always end with '.json'

```bash
pyreiseamt extract -o ~/all_countries.json
```

If you want to limit the crawl job to certain countries, you can use the *-c* argument. A single string should list all countries you want to extract, seperated by a semicolon.

```bash
pyreiseamt extract -o ~/select_countries.json -c "Frankreich;Georgien;Griechenland"
```

This will limit the extraction to France, Georgia, and Greece.

There are two remaining options to the extract command. The presence of *-s* will calculate the sentiment for every top category for every country. Also, *-n* will make sure that the top category names are all consistent for every country. The last option is necessary due to the fact that a category might have a different name in one country than in the other (despite the same content). If you want to extract information on all countries but also include sentiment and consistent category names, you could use pyreiseamt like so:

```bash
pyreiseamt extract -o ~/all_countries.json -s -n
```

#### Use the Scraper in your own scripts
If you prefer to use the built-in crawler in your scripts, you can do so by importing the scraper from the package (assuming that you've installed the package).

```python
from pyreiseamt.scraper import extract_country

url = "https://www.auswaertiges-amt.de/de/ReiseUndSicherheit/australiensicherheit/213920"

australia = extract_country(url)
```

australia will be a dictionary holding the relevant texts for every top and sub category.

### Links
pyreiseamt is a crawler with a CLI to https://www.auswaertiges-amt.de/de/ReiseUndSicherheit/reise-und-sicherheitshinweise. However, right now there is only information on country specific security issues, general travel guidances, and medical conditions. You can use the website to extract more information if needed.
