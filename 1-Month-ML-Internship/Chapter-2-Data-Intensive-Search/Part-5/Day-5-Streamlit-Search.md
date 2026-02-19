# Day 5: Streamlit Web Search Interface

**Date:** Week 2, Day 5 | **Duration:** 7+ hours | **Difficulty:** Intermediate

---

## 🎯 Learning Objectives

By the end of Day 5, you will:

✅ Build interactive web applications with Streamlit
✅ Manage application state and user interactions
✅ Handle file uploads and data processing
✅ Display ranked search results
✅ Deploy a complete search engine web app
✅ Integrate all Week 2 components into one system

---

## 📖 Core Topics

### 1. Streamlit Basics

#### Hello Streamlit
```python
import streamlit as st

st.set_page_config(page_title="Search Engine", layout="wide")

st.title("Search Engine")
st.header("Welcome")
st.write("This is a simple search engine built with Streamlit")

# User input
query = st.text_input("Enter search query:")
if query:
    st.write(f"You searched for: {query}")
```

#### Basic Components
```python
import streamlit as st

# Text input
name = st.text_input("Enter name:")

# Number input
age = st.number_input("Enter age:", min_value=0, max_value=150)

# Select box
option = st.selectbox("Choose category:", ["Tech", "Science", "History"])

# Checkbox
agreed = st.checkbox("I agree")

# Button
if st.button("Submit"):
    st.write("Button clicked!")
```

---

### 2. State Management

#### Session State
```python
import streamlit as st

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Modify state
if st.button("Increment"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")
```

#### Caching for Performance
```python
import streamlit as st

@st.cache_resource
def load_search_index():
    """Load index once, reuse across sessions"""
    engine = SearchEngine()
    engine.load_index('index.json')
    return engine

# Use cached function
search_engine = load_search_index()
```

---

### 3. File Upload & Processing

#### Handle Uploads
```python
import streamlit as st
import pandas as pd

st.sidebar.header("Upload Data")

uploaded_file = st.sidebar.file_uploader("Choose CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data preview:")
    st.dataframe(df.head())
    
    # Process data
    st.write(f"Shape: {df.shape}")
```

---

### 4. Layout and Organization

#### Columns and Tabs
```python
import streamlit as st

# Two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content here")

with col2:
    st.header("Column 2")
    st.write("Content here")

# Tabs
tab1, tab2, tab3 = st.tabs(["Search", "Statistics", "Settings"])

with tab1:
    st.header("Search Tab")

with tab2:
    st.header("Statistics Tab")

with tab3:
    st.header("Settings Tab")
```

#### Sidebar
```python
import streamlit as st

st.sidebar.title("Sidebar Title")
st.sidebar.header("Configuration")

# Sidebar widgets
max_results = st.sidebar.slider("Max Results", 1, 100, 10)
ranking_method = st.sidebar.radio("Ranking", ["TF-IDF", "BM25"])

st.write(f"Settings: {max_results} results, {ranking_method}")
```

---

### 5. Displaying Results

#### Tables and Data
```python
import streamlit as st
import pandas as pd

# Table
data = pd.DataFrame({
    'Document': [1, 2, 3],
    'Score': [0.95, 0.87, 0.76],
    'Preview': ['...text 1...', '...text 2...', '...text 3...']
})

st.dataframe(data)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Documents", 1000)
col2.metric("Total Terms", 5000)
col3.metric("Search Time", "0.05s")
```

---

## 💡 Complete Example: Search Engine Web App

```python
import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Micro Search Engine",
    page_icon="🔍",
    layout="wide"
)

# Load search index (cached)
@st.cache_resource
def load_engine():
    engine = SearchEngine()
    engine.build_index(get_sample_documents())
    return engine

engine = load_engine()

# Header
st.title("🔍 Micro Search Engine")
st.markdown("---")

# Sidebar
st.sidebar.title("Configuration")
max_results = st.sidebar.slider("Max Results", 5, 50, 10)
ranking_method = st.sidebar.select_box("Ranking", ["TF-IDF", "Boolean"])

# Main search area
st.header("Search")
query = st.text_input("Enter your search query:", placeholder="e.g., python machine learning")

# Statistics
col1, col2, col3 = st.columns(3)
stats = engine.get_statistics()
col1.metric("Documents", stats['documents'])
col2.metric("Terms", stats['terms'])
col3.metric("Indexed", "✓")

st.markdown("---")

# Search results
if query:
    st.subheader(f"Results for '{query}'")
    
    with st.spinner("Searching..."):
        if ranking_method == "TF-IDF":
            results = engine.ranked_search(query, top_k=max_results)
        else:
            results = engine.boolean_search(query, top_k=max_results)
    
    if results:
        # Display results
        for i, (doc_id, score) in enumerate(results, 1):
            with st.container():
                col1, col2 = st.columns([0.1, 0.9])
                
                with col1:
                    st.metric("", f"#{i}")
                
                with col2:
                    st.subheader(f"Document {doc_id}")
                    st.write(f"**Score**: {score:.3f}")
                    st.write(engine.get_document(doc_id)[:200] + "...")
                    
            st.markdown("---")
    else:
        st.warning("No results found")
else:
    st.info("Enter a search query to get started!")

# Footer
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
```

---

## 🔗 Running the App

```bash
# Install streamlit
pip install streamlit

# Run the app
streamlit run app.py

# App will open at http://localhost:8501
```

---

## � Additional Resources & Learning Links

### **Streamlit Framework**
- [Streamlit Official Docs](https://docs.streamlit.io/) - Complete official documentation
- [Streamlit Gallery](https://streamlit.io/gallery) - 100+ app examples across domains
- [Get Started with Streamlit](https://docs.streamlit.io/library/get-started) - Quick start guide

### **Building Web Applications**
- [Streamlit Components](https://docs.streamlit.io/library/components) - UI building blocks
- [Advanced Streamlit](https://docs.streamlit.io/library/advanced-features) - Session state, caching, secrets
- [Streamlit Best Practices](https://docs.streamlit.io/library/get-started/main-concepts) - Core concepts guide

### **Deployment & Hosting**
- [Streamlit Cloud](https://streamlit.io/cloud) - Free Streamlit hosting
- [Deploying Apps](https://docs.streamlit.io/library/get-started/installation) - Deployment options
- [Docker Containerization](https://docs.docker.com/get-started/) - Docker for app deployment

### **Backend Frameworks Alternative**
- [Flask Documentation](https://flask.palletsprojects.com/) - Lightweight Python web framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern async web framework
- [Django REST Framework](https://www.django-rest-framework.org/) - Full-featured web framework

### **Frontend Integration**
- [HTML/CSS for Data Apps](https://www.w3schools.com/) - Web fundamentals
- [JavaScript Basics](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) - Client-side scripting
- [REST APIs](https://en.wikipedia.org/wiki/Representational_state_transfer) - API design principles

---

## �🔗 Navigation

**[← Back to Chapter 2](../README.md)** | **[Day 5 Exercises →](./Day-5-Exercises.md)**
