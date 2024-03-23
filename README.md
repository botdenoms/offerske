# OffersKE

A sales, offers, flash sales scrapping project. for Kenyan based e-commerce sites
the products scrapped can be exported in native scrapy output type, i.e json, csv, e.t.c
plus custom mongodb database export capabilities.

### Supported Sites
- jumia

### Under Development Sites
1. Kilimall
2. Carrierfour
3. Jiji

## Getting Started
> ### Virtual environment set up
Recommend use of a virtual environment, not mandatory. use the command below in your desired location in your system

if not using virtual environment skip to getting repo or  installation of modules
```
python -m venv env-name
# or
virtualenv env-name
```
if using a virtual environment remember to activate it.
use the command in the terminal on the same location 
```
source env-name/bin/activate 
```

> ### Getting repo
From the githbub [repository](https://github.com/botdenoms/offerske),  clone or download the zip and extract to your desired location( if using virtual environment, where the environment was created ).

> ### Install modules
Run pip install to install the need modules.
```
pip install -r requirement.txt
# or
pip3 install -r requirement.txt
```

> ### running spider
#### jumia
To run the Jumia spider from their [flash sales offers](https://www.jumia.co.ke/flash-sales/) use the command below
```
scrapy crawl jumia  
```
Export options available
```
scrapy crawl jumia -o filename.json | filename.csv | filename.jsonl | filename.pickle
```
#### custom mongo export
## settings.py file
1. Add your working **MONGO_URI** () string
2. Enable the pipeline by uncommenting the line if commented
3. run the crawl without export options
```
scrapy crawl jumia  
```
### extras
if familiar with scrapy twist the settings file to adjust the scrapper to your liking, add more pipelines if need be.

