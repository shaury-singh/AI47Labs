import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Backend"))
)

from wrapper import generateAdvertisment

st.set_page_config(
    page_title="AI Advertisement Generator",
    layout="wide"
)

st.title("AI Advertisement Generator")
option = st.selectbox(
    "Choose Input Method",
    ("Single URL", "Batch Processing (CSV)")
)

if option == "Single URL":
    name = st.text_input("Brand Name")
    url = st.text_input(
        "Product URL",
        placeholder="https://example.com"
    )
    if st.button("Generate Advertisements"):
        if name and url:
            with st.spinner("Generating AI creatives..."):
                generated_images = generateAdvertisment(url, name)
            st.success("Advertisements Generated!")
            cols = st.columns(2)
            for i, image_path in enumerate(generated_images):
                with cols[i % 2]:
                    st.image(
                        image_path,
                        caption=f"{name} Ad {i+1}",
                        use_container_width=True
                    )
if option == "Batch Processing (CSV)":
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("CSV Preview")
        st.dataframe(df)
        if st.button("Process Batch"):
            total_rows = len(df)
            progress_bar = st.progress(0)
            status_text = st.empty()
            completed_container = st.container()
            completed_jobs = []
            for index, row in df.iterrows():
                name = row["name"]
                url = row["url"]
                status_text.info(
                    f"Processing {index + 1}/{total_rows}: {name}"
                )
                with st.spinner(f"Generating creatives for {name}..."):
                    generated_images = generateAdvertisment(url, name)
                completed_jobs.append(name)
                with completed_container:
                    st.success(f"Completed: {name}")
                    cols = st.columns(2)
                    for i, image_path in enumerate(generated_images):
                        with cols[i % 2]:
                            st.image(
                            image_path,
                            caption=f"{name} Ad {i+1}",
                            use_container_width=True
                            )
                progress = int(((index + 1) / total_rows) * 100)
                progress_bar.progress(progress)
            status_text.success("All batch jobs completed!")