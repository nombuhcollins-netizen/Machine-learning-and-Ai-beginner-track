# Chapter 2: Data Intensive & Search Architecture

**Week:** Week 2 | **Duration:** 5 Days (35+ hours) | **Level:** Foundational → Intermediate

---

## 🎯 Chapter Objective

Master the **"Garbage In, Garbage Out"** principle and build a complete **Information Retrieval (IR) System** from scratch.

By the end of this chapter, you will:
- ✅ Acquire and clean real-world datasets (CSV, JSON, Web)
- ✅ Transform raw data into ML-ready format (encoding & scaling)
- ✅ Perform exploratory data analysis (EDA) with visualizations
- ✅ Build inverted indexes for O(1) keyword search
- ✅ Create a web-based search engine with Streamlit

---

## 📋 Weekly Structure

| Day | Topic | Core Concepts | Capstone |
|-----|-------|---------------|----------|
| **1** | Data Acquisition | CSV/JSON parsing, Web Scraping (BeautifulSoup) | Dirty Data Challenge |
| **2** | Feature Engineering | Label Encoding, One-Hot, Scaling | Feature Pipeline Lab |
| **3** | Data Visualization | Matplotlib, Seaborn, EDA, Correlation | Insights Report |
| **4** | Information Retrieval | Term-Incidence Matrix, Inverted Index, Boolean Search | Index Builder |
| **5** | Web Search Interface | Streamlit, State Mgmt, File Upload | Micro Search Engine |

---

## 🏗️ Architecture Philosophy

**Week 1 (NLP) → Week 2 (Data + Search) → Week 3 (ML Algorithms)**

- **Week 1** taught you to process text and extract meaning (embeddings, similarity)
- **Week 2** extends this to handle any data format, clean it, analyze it, and serve it via search
- **Week 3** will apply ML algorithms on top of this clean data

**Key Principle:** Data quality determines ML success. Spend 80% time on data, 20% on models.

---

## 📂 Directory Structure

```
Chapter-2-Data-Intensive-Search/
├── README.md (this file)
├── Day-1/
│   ├── Day-1-Data-Acquisition.md (module)
│   └── Day-1-Exercises.md (exercises + capstone)
├── Day-2/
│   ├── Day-2-Feature-Engineering.md
│   └── Day-2-Exercises.md
├── Day-3/
│   ├── Day-3-Data-Visualization.md
│   └── Day-3-Exercises.md
├── Day-4/
│   ├── Day-4-Information-Retrieval.md
│   └── Day-4-Exercises.md
└── Day-5/
    ├── Day-5-Streamlit-Search.md
    └── Day-5-Exercises.md
```

---

## 🎓 Learning Outcomes

### By Day 1 (Data Acquisition)
- Understand data sources and formats
- Load CSV, JSON, and HTML data
- Identify and handle missing values, duplicates
- Perform basic data exploration with Pandas

### By Day 2 (Feature Engineering)
- Transform categorical → numerical (encoding)
- Normalize/scale numerical features
- Create feature pipelines
- Prepare data for ML models

### By Day 3 (Data Visualization)
- Create publication-quality charts (Matplotlib/Seaborn)
- Identify correlations and outliers visually
- Communicate data insights
- Generate structured reports

### By Day 4 (Information Retrieval)
- Build term-incidence matrices
- Construct inverted indexes (O(1) lookup)
- Implement boolean search queries
- Query documents with multiple keywords

### By Day 5 (Web Interface)
- Build interactive Streamlit dashboards
- Manage state and file uploads
- Deploy a complete search application
- Create ranked search results

---

## 🔧 Technologies & Libraries

### Core Tools
```python
Pandas          # Data manipulation and analysis
NumPy           # Numerical computing
BeautifulSoup   # Web scraping HTML/XML
Requests        # HTTP library for web fetching
CSV, JSON       # File format handling
```

### Visualization
```python
Matplotlib      # Foundational plotting
Seaborn         # Statistical visualization
```

### Web & Deployment
```python
Streamlit       # Web app framework
```

---

## 💡 Real-World Use Cases

1. **E-commerce Product Search** (Day 5)
   - Users upload product catalogs (CSV)
   - System indexes and searches products
   - Ranked results based on relevance

2. **Document Search Systems** (Day 4-5)
   - Legal document retrieval
   - Medical record search
   - Research paper indexing

3. **Data Pipeline Development** (Day 1-2)
   - ETL (Extract, Transform, Load)
   - Data warehouse preparation
   - API → Database workflows

4. **Analytics & Insights** (Day 3)
   - Business intelligence dashboards
   - Data quality reports
   - Exploratory data analysis for research

---

## 📊 Assessment Criteria

### Daily Exercises (40%)
- Correct implementation of algorithms
- Proper error handling and edge cases
- Code organization and documentation

### Daily Capstones (60%)
- Complete working system
- Handles real-world data messiness
- User-friendly interface/output

### Bonus (Extra Credit)
- Performance optimization (e.g., indexed search speed)
- Extended features (fuzzy matching, ranking algorithms)
- Novel dataset or use case

---

## 🚀 Quick Start

### Prerequisites
```bash
# Install required packages
pip install pandas numpy beautifulsoup4 requests matplotlib seaborn streamlit
```

### Recommended Workflow
1. Read the **Day-X module** file carefully
2. Study the code examples and run them locally
3. Complete **Day-X exercises** progressively
4. Build the **daily capstone** project
5. Test thoroughly before moving to next day

---

## 📚 Core Concepts Map

```
RAW DATA (CSV, JSON, HTML)
    ↓
Day 1: DATA ACQUISITION
  - Load, explore, identify issues
    ↓
Day 2: FEATURE ENGINEERING
  - Clean, encode, scale, normalize
    ↓
CLEAN NUMERICAL DATA (ML-Ready)
    ↓
Day 3: VISUALIZATION & EDA
  - Identify patterns, correlations, outliers
    ↓
Day 4: INFORMATION RETRIEVAL
  - Build indexes for fast search
    ↓
Day 5: WEB INTERFACE
  - Deploy searchable system
```

---

## 🔗 Navigation

- **[← Back to Main](../README.md)** | **[Day 1 →](./Day-1/Day-1-Data-Acquisition.md)**
- **[GitHub Repo](https://github.com)**

---

## 💬 Key Principles

1. **Garbage In, Garbage Out (GIGO)**
   - Quality of input determines quality of output
   - 80% of ML time is spent on data

2. **Exploratory First**
   - Always visualize before modeling
   - Understand data before processing

3. **Pipeline Thinking**
   - Data flows through stages: Raw → Clean → Analyzed → Indexed → Served
   - Each stage is a transformation

4. **Real-World Data is Messy**
   - Missing values, duplicates, inconsistent formats
   - Handle gracefully with clear logic

5. **Search is Central**
   - Information retrieval is core to all systems
   - Fast lookup = Better user experience

---

## � Learning Resources for Chapter 2

### **Data Loading & Manipulation**
- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Kaggle Learn - Pandas](https://www.kaggle.com/learn/pandas)
- [Real Python - Working with Files](https://realpython.com/working-with-files-in-python/)

### **Web Scraping**
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Real Python - Web Scraping Guide](https://realpython.com/beautiful-soup-web-scraper-python/)
- [Requests Library](https://requests.readthedocs.io/)
- [Web Scraping Ethics](https://en.wikipedia.org/wiki/Web_scraping)

### **Data Visualization & EDA**
- [Matplotlib Official Guide](https://matplotlib.org/stable/users/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Kaggle Learn - Data Visualization](https://www.kaggle.com/learn/data-visualization)
- [Exploratory Data Analysis](https://en.wikipedia.org/wiki/Exploratory_data_analysis)

### **Feature Engineering**
- [Real Python - Feature Scaling](https://realpython.com/normalize-data-with-pandas/)
- [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Feature Engineering](https://en.wikipedia.org/wiki/Feature_engineering)

### **Information Retrieval & Search**
- [Stanford IR Book](https://nlp.stanford.edu/IR-book/)
- [Wikipedia - Information Retrieval](https://en.wikipedia.org/wiki/Information_retrieval)
- [Inverted Index Explained](https://en.wikipedia.org/wiki/Inverted_index)
- [TF-IDF Algorithm](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [ElasticSearch Tutorial](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

### **Streamlit & Web Frameworks**
- [Streamlit Official Docs](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Building Data Apps](https://docs.streamlit.io/library/get-started)

---

## 📖 Chapter-Specific Resources

Each Part includes detailed "📚 Additional Resources" sections at the end with links to:
- Official documentation
- Tutorial websites
- Interactive learning platforms
- Research papers and academic resources

---

**Last Updated:** February 19, 2026 | **Status:** Ready for implementation
