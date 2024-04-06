import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import pandas as pd
embedder = SentenceTransformer("all-mpnet-base-v2")
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", password),  # enter Password for the elastic user
    ca_certs="Elasticsearch\elasticsearch-8.13.1\config\certs\http_ca.crt"
)

st.title("Semantic search on products")
user_input = st.text_area("Enter the description")
if st.button('Search'):
    user_input = user_input.strip()
    if user_input != "":
        encoded_input = embedder.encode(user_input)
        query = {
            "field": "EncodedDescription",
            "query_vector": encoded_input,
            "k": 5,
            "num_candidates": 10000,
        }

        res = es.knn_search(index="products", knn=query, source=[
            "ProductName", "Description", "PrimaryColor", "Price (INR)", "Gender"])
        data_df = pd.DataFrame()
        for i in res["hits"]["hits"]:
            d = {'Product Name': i['_source']['ProductName'], 'Gender': i['_source']['Gender'],
                 'Price (INR)': i['_source']['Price (INR)'], 'Description': i['_source']['Description'], 'Color': i['_source']['PrimaryColor']}
            temp = pd.DataFrame.from_dict([d])
            data_df = pd.concat([data_df, temp], ignore_index=True)
        st.dataframe(data_df, hide_index=True)
