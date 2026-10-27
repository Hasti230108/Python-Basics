import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Mystery Data Detective",
    layout="wide"
)

st.title("Mystery Data Detective")
st.write(
    "Investigate a fictional museum mystery "
    "using clues, suspects, and data."
)

st.info(
    "CASE 099: The Missing Sapphire\n\n"
    "A sapphire disappeared from a museum at 8 PM. "
    "Explore the fictional evidence and form your theory."
)

data = {
    "Suspect": ["Karan", "Alfiya", "Rahul", "Nina", "Omkar"],
    "Evidence Found": [3, 5, 2, 4, 1],
    "Alibi Confidence": [80, 45, 90, 60, 75],
    "Clue Matches": [2, 4, 1, 3, 1]
}

df = pd.DataFrame(data)

np.random.seed(42)

df["Evidence Score"] = np.random.randint(40, 96, size=len(df))

st.sidebar.header("Investigation Filters")

minimum_evidence = st.sidebar.slider(
    "Minimum evidence found",
    min_value=1,
    max_value=5,
    value=1
)

filtered_df = df[
    df["Evidence Found"] >= minimum_evidence
]

st.subheader("Case Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Suspects", len(df))
col2.metric("Visible Suspects", len(filtered_df))
col3.metric(
    "Average Evidence",
    round(df["Evidence Found"].mean(), 1)
)

st.subheader("Suspect Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

if filtered_df.empty:
    st.warning("No suspects match this filter.")
else:
    st.subheader("Evidence Comparison")

    chart_data = filtered_df.set_index("Suspect")[
        ["Evidence Found", "Clue Matches"]
    ]

    st.bar_chart(chart_data)

    st.subheader("Investigate a Suspect")

    selected_suspect = st.selectbox(
        "Choose a suspect",
        filtered_df["Suspect"].tolist()
    )

    suspect_data = filtered_df[
        filtered_df["Suspect"] == selected_suspect
    ].iloc[0]

    st.markdown(f"### {selected_suspect}")

    detail1, detail2, detail3 = st.columns(3)

    detail1.metric(
        "Evidence Found",
        int(suspect_data["Evidence Found"])
    )

    detail2.metric(
        "Alibi Confidence",
        f'{int(suspect_data["Alibi Confidence"])}%'
    )

    detail3.metric(
        "Clue Matches",
        int(suspect_data["Clue Matches"])
    )

    st.caption(
        "Alibi confidence is a fictional score, "
        "not proof of guilt or innocence."
    )

st.subheader("Submit Your Theory")

theory = st.selectbox(
    "Who do you currently suspect?",
    df["Suspect"].tolist()
)

reason = st.text_area(
    "Why do you suspect them?",
    placeholder="Explain which evidence supports your theory..."
)

if st.button("Submit Investigation", type="primary"):
    if reason.strip() == "":
        st.warning("Please explain your reasoning first.")
    else:
        st.success("Investigation theory submitted!")
        st.write("**Your selected suspect:**", theory)
        st.write("**Your reasoning:**", reason)
        st.info(
            "Your theory is recorded on this screen for "
            "this session. It is not saved permanently."
        )

st.divider()

st.caption(
    "Day 99 Project | Python • Streamlit • Pandas • NumPy"
)
