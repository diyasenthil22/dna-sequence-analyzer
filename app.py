import streamlit as st

st.set_page_config(
    page_title="DNA Sequence Analyzer",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 DNA Sequence Analyzer")

st.write(
    "Analyze DNA sequences by calculating sequence length, nucleotide counts, "
    "and GC content."
)

sequence = st.text_area(
    "Paste a DNA sequence:",
    height=200,
    placeholder="Example: ATGCGATCGTAGCTAGCTA"
)

if st.button("🔬 Analyze Sequence"):

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    c = sequence.count("C")
    g = sequence.count("G")

    if length > 0:
        gc_content = ((g + c) / length) * 100
    else:
        gc_content = 0

    st.header("Results")

    st.metric("Sequence Length", f"{length} bases")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("A", a)
        st.metric("T", t)

    with col2:
        st.metric("C", c)
        st.metric("G", g)

    st.metric("GC Content", f"{gc_content:.2f}%")
