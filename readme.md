# Semantic search on products 
This project implements a semantic search engine for product data using Elasticsearch and SentenceTransformers. By converting product descriptions  into high-dimensional dense vectors, the system enables more accurate and relevant search results compared to traditional keyword-based searches.
### Key Features
- **Elasticsearch Integration**: Leverages Elasticsearch for efficient indexing and searching.
- **SentenceTransformers**: Utilizes pre-trained SentenceTransformers models to encode text into vectors.
- **Enhanced Search Accuracy**: Provides more accurate search results through semantic understanding of product descriptions and queries.
## Steps to run the program on Windows
1. Download elasticsearch from the [link](https://www.elastic.co/downloads/elasticsearch) and run the program using the command given in the website.
2. Create a virtual environment 
```
python -m venv "environment name"
```
3. Activate the virtual environment
```
"environment name"\Scripts\activate
```
4. Install all required libraries
```
pip install -r requirements.txt
```
5. Run all the cells in data preparation.ipynb

6. Run the program
```
streamlit run app.py
```

## Demo
![Alt text](<Demo.gif>)

