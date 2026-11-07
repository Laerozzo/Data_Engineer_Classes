Python Data Engineering & Data Science Study Notes 🐍📊A curated collection of interactive Jupyter Notebooks (.ipynb) containing structured study notes, runnable code examples, and offline-ready mock datasets from seven DataCamp Python courses.Each notebook has been standardized for readability and enhanced with:Key Takeaways at the end of every chapter.Actionable Step-by-Step Workflows to apply the concepts in real-world projects.Comprehensive Glossaries detailing every package, function, method, and attribute covered—complete with accepted arguments and direct links to official documentation.Self-Contained Mock Datasets (./datasets/) so every code cell runs offline without broken file paths or external server dependencies.📚 Course Notebooks Overview#Notebook FileCourse TitleChapters & Core Topics Covered01Introduction_to_Python_for_Developers_revised.ipynbIntroduction to Python for DevelopersCh 1: Syntax, variables, scalar types (str, int, float, bool), string methodsCh 2: Lists, indexing/slicing, Dictionaries (.keys(), .values(), .items()), Sets, TuplesCh 3: Conditional statements (if/elif/else), for & while loops, safe dictionary workflows02Intermediate_Python_for_Developers_revised.ipynbIntermediate Python for DevelopersCh 1: Built-in functions (min, max, sum, len, round, sorted), os & string modules, pandas basicsCh 2: Custom functions (def), default/keyword arguments, docstrings (__doc__), *args & **kwargsCh 3: Anonymous lambda functions, map(), Tracebacks, Error Handling (try/except, raise)03Introduction_to_Importing_Data_in_Python_revised.ipynbIntroduction to Importing Data in PythonCh 1: Plain text files (with open()), flat files with NumPy (np.loadtxt) and pandas (pd.read_csv)Ch 2: Pickled files (.pkl), Excel (pd.ExcelFile), SAS (.sas7bdat), Stata (.dta), HDF5 (h5py), MATLAB (scipy.io)Ch 3: Relational Databases (SQLite, SQLAlchemy), SELECT/WHERE/INNER JOIN, pd.read_sql_query04Intermediate_Importing_Data_in_Python_revised.ipynbIntermediate Importing Data in PythonCh 1: Web file downloads (urllib.request.urlretrieve), HTTP GET requests (urllib vs requests), HTML scraping with BeautifulSoupCh 2: Web APIs, loading & traversing nested JSON payloads (json.load, r.json())Ch 3: Streaming APIs (tweepy), parsing JSON-lines (tweets3.txt), regex text analysis (re.search), seaborn plots05Introduction_to_APIs_in_Python_revised.ipynbIntroduction to APIs in PythonCh 1: SOAP vs REST vs GraphQL, URL anatomy, automatic query parameter encoding (params=)Ch 2: HTTP verbs (GET, POST, PUT, DELETE), HTTP status codes (requests.codes), Headers, Basic & Bearer Token AuthCh 3: JSON serialization (dumps/loads, json=), ConnectionError & HTTPError (raise_for_status()), rate-limit throttling (time.sleep)06Cleaning_Data_in_Python_revised.ipynbCleaning Data in PythonCh 1: Data type constraints (.astype), range capping (.loc[]), exact & partial deduplication (.duplicated, .groupby().agg())Ch 2: Membership constraints (set.difference, .isin), categorical binning (pd.cut, pd.qcut), text cleaningCh 3: Currency & date uniformity (errors='coerce'), cross-field validation, missingness (MCAR/MAR/MNAR, dropna, fillna)Ch 4: Fuzzy string matching (thefuzz / Levenshtein distance) and Record Linkage (recordlinkage blocking, scoring, linking)07Writing_Efficient_Python_Code_revised.ipynbWriting Efficient Python CodeCh 1: Pythonic idioms (import this), built-ins (range, enumerate, map), NumPy array broadcasting & boolean indexingCh 2: Runtime benchmarking (%timeit, %%timeit), line-by-line profiling (line_profiler / %lprun), memory profiling (sys.getsizeof, memory_profiler / %mprun)Ch 3: Combining & counting (zip, collections.Counter, itertools.combinations), Set theory ($O(1)$ membership, intersection, difference, symmetric_difference, union), eliminating & optimizing loopsCh 4: pandas iteration hierarchy (.iloc vs .iterrows() vs .itertuples() vs .apply() vs .values NumPy vectorization)🗂️ Repository Structure.
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
└── datasets/
    ├── Chinook.sqlite                # Relational database (Employee, Artist, Album tables)
    ├── a_movie.json                  # Sample OMDb movie metadata JSON
    ├── airlines_final.csv            # Airline survey responses & wait times
    ├── albeck_gene_expression.mat    # MATLAB workspace array data
    ├── api_albums_mock.csv           # Mock albums dataset for API exercises
    ├── api_tracks_mock.json          # Mock paginated tracks JSON payload
    ├── banking_dirty.csv             # Banking records with currency, age, and missing value issues
    ├── baseball_stats.csv            # MLB team runs scored (RS), runs allowed (RA), wins (W), games (G)
    ├── battledeath.xlsx              # Multi-sheet Excel workbook (2002 & 2004 sheets)
    ├── categories.csv                # Ground-truth valid categories lookup table
    ├── data.pkl                      # Pickled Python dictionary
    ├── dataset.hdf5                  # Hierarchical numerical HDF5 file
    ├── digits.csv                    # 28x28 grayscale handwritten digit pixel rows
    ├── digits_header.txt             # Tab-delimited digit pixel data with header
    ├── disarea.dta                   # Stata disease extent dataset
    ├── hero_funcs.py                 # External helper functions for %mprun memory profiling
    ├── huck_finn.txt                 # Plain text excerpt (Adventures of Huckleberry Finn)
    ├── latitude.xlsx                 # Multi-sheet country latitude Excel workbook ('1700', '1900')
    ├── moby_dick.txt                 # Plain text excerpt (Moby-Dick)
    ├── pokemon.csv                   # Pokédex stats (HP, Attack, Defense, Speed, Type, Legendary, Generation)
    ├── restaurants_L2.csv            # Restaurant records for fuzzy matching & linkage (Table A)
    ├── restaurants_L2_dirty.csv      # Partner restaurant records for record linkage (Table B)
    ├── ride_sharing_new.csv          # Ride-sharing logs with duration strings, tire sizes & duplicates
    ├── sales.csv                     # User order values CSV
    ├── seaslug.txt                   # Tab-delimited time vs. percentage of larvae data
    ├── superheroes.csv               # Superhero heights (cm) and weights (kg) for runtime/memory profiling
    ├── titanic.csv                   # Passenger survival dataset
    ├── titanic_corrupt.txt           # Tab-delimited file with '#' comments and 'Nothing' NaNs
    ├── tweets3.txt                   # Newline-delimited JSON (JSONL) tweet stream
    ├── urbanpop.xlsx                 # Urban population Excel workbook
    └── winequality-red.csv           # Semicolon-delimited red wine physiochemical properties
🚀 Getting Started1. Clone the Repositorygit clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2. Create a Virtual Environment & Install DependenciesMake sure you have Python 3.10+ installed, then install the pinned dependencies using requirements.txt:# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate        # On Linux/macOS
# .venv\Scripts\activate         # On Windows

# Install all required packages from requirements.txt
pip install -r requirements.txt
3. Launch Jupyter Lab / Notebookjupyter lab
# or
jupyter notebook
Open any of the *_revised.ipynb files in your browser or VS Code Jupyter extension and run all cells (Run All).📖 What You Will Find at the End of Every ChapterEvery chapter across all seven notebooks follows a consistent review template designed for quick revision and interview prep:Key Takeaways: Concise summary of the most important concepts and gotchas from the chapter.Step-by-Step Process to Act On: A numbered checklist showing how to apply the chapter's tools in a real data pipeline.Glossary & Official Documentation Table: A quick-reference table listing every module, function, method, class, and attribute introduced in that chapter, its accepted parameters, and a direct link to the official documentation (docs.python.org, pandas.pydata.org, numpy.org, requests.readthedocs.io, ipython.readthedocs.io, etc.).🛠️ Built WithPython 3 — Core programming language & standard library (itertools, collections, timeit)pandas & NumPy — Data manipulation and numerical vectorizationline_profiler & memory_profiler — Line-by-line runtime and RAM profilingRequests & BeautifulSoup4 — Web APIs and HTML parsingMatplotlib & Seaborn — Data visualizationSciPy & h5py — Scientific & hierarchical file formatsSQLAlchemy & SQLite3 — Relational database queryingTheFuzz & RecordLinkage — Fuzzy string matching and entity resolution
