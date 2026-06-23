import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    text = text.lower()

    skills = [
        "python",
        "machine learning",
        "sql",
        "excel",
        "aws",
        "data analysis"
    ]

    skill_count = 0

    for skill in skills:
        if skill in text:
            skill_count += 1

    skills_score = min(skill_count * 15, 100)

    education_score = 80 if (
        "bachelor" in text
        or "bs" in text
        or "university" in text
    ) else 40

    experience_score = 80 if (
        "experience" in text
        or "internship" in text
    ) else 40

    overall = (
        skills_score
        + education_score
        + experience_score
    ) / 3

    st.write(f"### Overall Score: {overall:.1f}%")

    categories = [
        "Skills",
        "Education",
        "Experience"
    ]

    scores = [
        skills_score,
        education_score,
        experience_score
    ]

    fig, ax = plt.subplots()

    ax.bar(categories, scores)

    st.pyplot(fig)