# Python Data Engineering & Data Science Study Notes 🐍📊

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Git](https://img.shields.io/badge/Git-2.40%2B-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/doc)
[![DataCamp](https://img.shields.io/badge/Courses-DataCamp-03EF62?style=for-the-badge&logo=datacamp&logoColor=05192D)](https://www.datacamp.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A curated collection of interactive **Jupyter Notebooks (`.ipynb`)** containing structured study notes, runnable code examples, and offline-ready mock datasets from ten **DataCamp** Python & Git courses.

Each notebook has been standardized for readability and enhanced with:
* **Key Takeaways** at the end of every chapter.
* **Actionable Step-by-Step Workflows** to apply the concepts in real-world projects.
* **Comprehensive Glossaries** detailing every package, command, function, method, and attribute covered—complete with accepted arguments and direct links to official documentation.
* **Self-Contained Mock Datasets & Sandboxed CLI Demos** (`./datasets/` & isolated temporary Git repos) so every code cell runs offline without broken file paths or external server dependencies.

---

## 📚 Course Notebooks Overview

| # | Notebook File | Course Title | Chapters & Core Topics Covered |
| :--- | :--- | :--- | :--- |
| **01** | [`Introduction_to_Python_for_Developers_revised.ipynb`](./Introduction_to_Python_for_Developers_revised.ipynb) | **Introduction to Python for Developers** | **Ch 1:** Syntax, variables, scalar types (`str`, `int`, `float`, `bool`), string methods<br>**Ch 2:** Lists, indexing/slicing, Dictionaries (`.keys()`, `.values()`, `.items()`), Sets, Tuples<br>**Ch 3:** Conditional statements (`if`/`elif`/`else`), `for` & `while` loops, safe dictionary workflows |
| **02** | [`Intermediate_Python_for_Developers_revised.ipynb`](./Intermediate_Python_for_Developers_revised.ipynb) | **Intermediate Python for Developers** | **Ch 1:** Built-in functions (`min`, `max`, `sum`, `len`, `round`, `sorted`), `os` & `string` modules, `pandas` basics<br>**Ch 2:** Custom functions (`def`), default/keyword arguments, docstrings (`__doc__`), `*args` & `**kwargs`<br>**Ch 3:** Anonymous `lambda` functions, `map()`, Tracebacks, Error Handling (`try`/`except`, `raise`) |
| **03** | [`Introduction_to_Importing_Data_in_Python_revised.ipynb`](./Introduction_to_Importing_Data_in_Python_revised.ipynb) | **Introduction to Importing Data in Python** | **Ch 1:** Plain text files (`with open()`), flat files with `NumPy` (`np.loadtxt`) and `pandas` (`pd.read_csv`)<br>**Ch 2:** Pickled files (`.pkl`), Excel (`pd.ExcelFile`), SAS (`.sas7bdat`), Stata (`.dta`), HDF5 (`h5py`), MATLAB (`scipy.io`)<br>**Ch 3:** Relational Databases (`SQLite`, `SQLAlchemy`), `SELECT`/`WHERE`/`INNER JOIN`, `pd.read_sql_query` |
| **04** | [`Intermediate_Importing_Data_in_Python_revised.ipynb`](./Intermediate_Importing_Data_in_Python_revised.ipynb) | **Intermediate Importing Data in Python** | **Ch 1:** Web file downloads (`urllib.request.urlretrieve`), HTTP GET requests (`urllib` vs `requests`), HTML scraping with `BeautifulSoup`<br>**Ch 2:** Web APIs, loading & traversing nested `JSON` payloads (`json.load`, `r.json()`)<br>**Ch 3:** Streaming APIs (`tweepy`), parsing JSON-lines (`tweets3.txt`), regex text analysis (`re.search`), `seaborn` plots |
| **05** | [`Introduction_to_APIs_in_Python_revised.ipynb`](./Introduction_to_APIs_in_Python_revised.ipynb) | **Introduction to APIs in Python** | **Ch 1:** SOAP vs REST vs GraphQL, URL anatomy, automatic query parameter encoding (`params=`)<br>**Ch 2:** HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`), HTTP status codes (`requests.codes`), Headers, Basic & Bearer Token Auth<br>**Ch 3:** JSON serialization (`dumps`/`loads`, `json=`), `ConnectionError` & `HTTPError` (`raise_for_status()`), rate-limit throttling (`time.sleep`) |
| **06** | [`Cleaning_Data_in_Python_revised.ipynb`](./Cleaning_Data_in_Python_revised.ipynb) | **Cleaning Data in Python** | **Ch 1:** Data type constraints (`.astype`), range capping (`.loc[]`), exact & partial deduplication (`.duplicated`, `.groupby().agg()`)<br>**Ch 2:** Membership constraints (`set.difference`, `.isin`), categorical binning (`pd.cut`, `pd.qcut`), text cleaning<br>**Ch 3:** Currency & date uniformity (`errors='coerce'`), cross-field validation, missingness (MCAR/MAR/MNAR, `dropna`, `fillna`)<br>**Ch 4:** Fuzzy string matching (`thefuzz` / Levenshtein distance) and Record Linkage (`recordlinkage` blocking, scoring, linking) |
| **07** | [`Writing_Efficient_Python_Code_revised.ipynb`](./Writing_Efficient_Python_Code_revised.ipynb) | **Writing Efficient Python Code** | **Ch 1:** Pythonic idioms (`import this`), built-ins (`range`, `enumerate`, `map`), `NumPy` array broadcasting & boolean indexing<br>**Ch 2:** Runtime benchmarking (`%timeit`, `%%timeit`), line-by-line profiling (`line_profiler` / `%lprun`), memory profiling (`sys.getsizeof`, `memory_profiler` / `%mprun`)<br>**Ch 3:** Combining & counting (`zip`, `collections.Counter`, `itertools.combinations`), Set theory ($O(1)$ membership, `intersection`, `difference`, `symmetric_difference`, `union`), eliminating & optimizing loops<br>**Ch 4:** `pandas` iteration hierarchy (`.iloc` vs `.iterrows()` vs `.itertuples()` vs `.apply()` vs `.values` NumPy vectorization) |
| **08** | [`Streamlined_Data_Ingestion_with_pandas.ipynb`](./Streamlined_Data_Ingestion_with_pandas.ipynb) | **Streamlined Data Ingestion with pandas** | **Ch 1:** Flat files with `pd.read_csv()` (`sep`, `usecols`, `nrows`, `skiprows`, `header=None`, `names`, `dtype`, `na_values`, `on_bad_lines`)<br>**Ch 2:** Excel workbooks with `pd.read_excel()` (letter ranges `W:AB, AR`, `sheet_name=None`, `true_values`/`false_values`, nullable booleans, `parse_dates` & `pd.to_datetime()`)<br>**Ch 3:** Relational databases with `sqlalchemy.create_engine()` & `pd.read_sql()` (`SELECT`, `WHERE`, `AND`/`OR`, `DISTINCT`, `GROUP BY`, `JOIN`)<br>**Ch 4:** JSON orientations (`pd.read_json(..., orient='split')`), REST APIs (`requests.get()`, `params`, `headers`), flattening nested JSON (`pd.json_normalize()`), `pd.concat()`, & `df.merge()` |
| **09** | [`Introduction_to_Git.ipynb`](./Introduction_to_Git.ipynb) | **Introduction to Git** | **Ch 1:** Version control fundamentals, shell navigation (`pwd`, `ls`, `cd`), initializing repos (`git init`), inspecting status (`git status`), staging & committing (`git add`, `git commit -m`)<br>**Ch 2:** Git architecture (`Commit`, `Tree`, `Blob`, SHA-1 hashes), history inspection (`git log`, `git show`), comparing versions (`git diff`, `HEAD`), undoing & unstaging (`git revert`, `git checkout`, `git restore --staged`) |
| **10** | [`Intermediate_Git.ipynb`](./Intermediate_Git.ipynb) | **Intermediate Git** | **Ch 1:** Branch workflows (`git branch`, `git switch -c`), comparing branches (`git diff`), renaming & deleting (`-m`, `-d`, `-D`), fast-forward merging (`git merge`)<br>**Ch 2:** Resolving merge conflicts (`<<<<<<<`, `=======`, `>>>>>>>`), remote repositories (`git clone`, `git remote -v`, `git remote add`), synchronizing (`git fetch`, `git pull`, `git push`) |

---

## 🗂️ Repository Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── Introduction_to_Python_for_Developers_revised.ipynb
├── Intermediate_Python_for_Developers_revised.ipynb
├── Introduction_to_Importing_Data_in_Python_revised.ipynb
├── Intermediate_Importing_Data_in_Python_revised.ipynb
├── Introduction_to_APIs_in_Python_revised.ipynb
├── Cleaning_Data_in_Python_revised.ipynb
├── Writing_Efficient_Python_Code_revised.ipynb
├── Streamlined_Data_Ingestion_with_pandas.ipynb
├── Introduction_to_Git.ipynb
├── Intermediate_Git.ipynb
└── datasets/
    ├── Chinook.sqlite                  # Relational database (Employee, Artist, Album tables)
    ├── a_movie.json                    # Sample OMDb movie metadata JSON
    ├── airlines_final.csv              # Airline survey responses & wait times
    ├── albeck_gene_expression.mat      # MATLAB workspace array data
    ├── api_albums_mock.csv             # Mock albums dataset for API exercises
    ├── api_tracks_mock.json            # Mock paginated tracks JSON payload
    ├── banking_dirty.csv               # Banking records with currency, age, and missing value issues
    ├── baseball_stats.csv              # MLB team runs scored (RS), runs allowed (RA), wins (W), games (G)
    ├── battledeath.xlsx                # Multi-sheet Excel workbook (2002 & 2004 sheets)
    ├── call_counts.csv                 # Daily NYC 311 call counts for DataFrame merging
    ├── categories.csv                  # Ground-truth valid categories lookup table
    ├── data.db                         # SQLite database (weather, hpd311calls, boro_census tables)
    ├── data.pkl                        # Pickled Python dictionary
    ├── dataset.hdf5                    # Hierarchical numerical HDF5 file
    ├── digits.csv                      # 28x28 grayscale handwritten digit pixel rows
    ├── digits_header.txt               # Tab-delimited digit pixel data with header
    ├── disarea.dta                     # Stata disease extent dataset
    ├── fcc_survey.xlsx                 # Multi-sheet developer survey workbook ('2016', '2017') with timestamps
    ├── fcc_survey_booleans.xlsx        # Survey dataset with binary, Yes/No, and TRUE/FALSE columns
    ├── fcc_survey_with_headers.xlsx    # Survey workbook with metadata title rows & wide Excel columns
    ├── hero_funcs.py                   # External helper functions for %mprun memory profiling
    ├── huck_finn.txt                   # Plain text excerpt (Adventures of Huckleberry Finn)
    ├── latitude.xlsx                   # Multi-sheet country latitude Excel workbook ('1700', '1900')
    ├── moby_dick.txt                   # Plain text excerpt (Moby-Dick)
    ├── nyc_death_causes.json           # Split-oriented JSON dataset of NYC leading death causes
    ├── pokemon.csv                     # Pokédex stats (HP, Attack, Defense, Speed, Type, Legendary, Generation)
    ├── restaurants_L2.csv              # Restaurant records for fuzzy matching & linkage (Table A)
    ├── restaurants_L2_dirty.csv        # Partner restaurant records for record linkage (Table B)
    ├── ride_sharing_new.csv            # Ride-sharing logs with duration strings, tire sizes & duplicates
    ├── sales.csv                       # User order values CSV
    ├── seaslug.txt                     # Tab-delimited time vs. percentage of larvae data
    ├── superheroes.csv                 # Superhero heights (cm) and weights (kg) for runtime/memory profiling
    ├── titanic.csv                     # Passenger survival dataset
    ├── titanic_corrupt.txt             # Tab-delimited file with '#' comments and 'Nothing' NaNs
    ├── tweets3.txt                     # Newline-delimited JSON (JSONL) tweet stream
    ├── urbanpop.xlsx                   # Urban population Excel workbook
    ├── us_tax_data_2016.csv            # IRS ZIP-code tax return statistics (CSV)
    ├── us_tax_data_2016.tsv            # IRS ZIP-code tax return statistics (tab-delimited TSV)
    ├── us_tax_data_2016_corrupt.csv    # IRS tax CSV containing a malformed row for ParserError handling
    ├── weather_daily.csv               # Daily NYC temperature records (tmax, tmin) for DataFrame merging
    ├── winequality-red.csv             # Semicolon-delimited red wine physiochemical properties
    └── yelp_bookstores_mock.json       # Nested Yelp Business Search API JSON response payload
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a Virtual Environment & Install Dependencies
Make sure you have **Python 3.10+** and **Git** installed, then install the pinned dependencies using `requirements.txt`:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate        # On Linux/macOS
# .venv\Scripts\activate         # On Windows

# Install all required packages from requirements.txt
pip install -r requirements.txt
```

### 3. Launch Jupyter Lab / Notebook
```bash
jupyter lab
# or
jupyter notebook
```
Open any of the `*.ipynb` files in your browser or VS Code Jupyter extension and run all cells (`Run All`).

---

## 📖 What You Will Find at the End of Every Chapter

Every chapter across all ten notebooks follows a consistent review template designed for quick revision and interview prep:
1. **Key Takeaways**: Concise summary of the most important concepts and gotchas from the chapter.
2. **Step-by-Step Process to Act On**: A numbered checklist showing how to apply the chapter's tools in a real data pipeline.
3. **Glossary & Official Documentation Table**: A quick-reference table listing every module, CLI command, function, method, class, and attribute introduced in that chapter, its accepted parameters, and a direct link to the official documentation (`docs.python.org`, `git-scm.com/docs`, `pandas.pydata.org`, `numpy.org`, `sqlalchemy.org`, `requests.readthedocs.io`, `ipython.readthedocs.io`, etc.).

---

## 🛠️ Built With
* [Python 3](https://docs.python.org/3/) — Core programming language & standard library (`itertools`, `collections`, `timeit`, `sqlite3`, `json`, `subprocess`)
* [Git](https://git-scm.com/doc) — Distributed version control, branching, conflict resolution, and remote synchronization
* [pandas](https://pandas.pydata.org/docs/) & [NumPy](https://numpy.org/doc/) — Data ingestion, manipulation, JSON normalization, and numerical vectorization
* [line_profiler](https://github.com/pyutils/line_profiler) & [memory_profiler](https://pypi.org/project/memory-profiler/) — Line-by-line runtime and RAM profiling
* [Requests](https://requests.readthedocs.io/) & [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) — Web APIs and HTML parsing
* [Matplotlib](https://matplotlib.org/stable/contents.html) & [Seaborn](https://seaborn.pydata.org/) — Data visualization
* [SciPy](https://docs.scipy.org/doc/scipy/) & [h5py](https://docs.h5py.org/) — Scientific & hierarchical file formats
* [SQLAlchemy](https://docs.sqlalchemy.org/) & [SQLite3](https://docs.python.org/3/library/sqlite3.html) — Relational database connections and SQL querying
* [TheFuzz](https://github.com/seatgeek/thefuzz) & [RecordLinkage](https://recordlinkage.readthedocs.io/) — Fuzzy string matching and entity resolution