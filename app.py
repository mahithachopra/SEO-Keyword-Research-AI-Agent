import streamlit as st
from agent import expand_keywords
from googleadds import get_keyword_metrics
from utils import score_keywords
import pandas as pd

st.set_page_config(page_title="SEO Keyword Research AI Agent", layout="wide")
st.title("🔍 SEO Keyword Research AI Agent")

seed = st.text_input("Enter a seed keyword:")

if st.button("Generate Keywords") and seed:
    with st.spinner("Generating and analyzing keywords..."):
        keywords = expand_keywords(seed)
        metrics = [get_keyword_metrics(k) for k in keywords]
        top_keywords = score_keywords(metrics)

        df = pd.DataFrame(top_keywords)
        st.success("Here are your top 50 keyword suggestions:")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download as CSV", csv, "top_keywords.csv", "text/csv")
