import streamlit as st

# Set page config
st.set_page_config(page_title="Tranquilo", page_icon="logo.png", layout="centered")

# Custom Tranquilo pink styling
st.markdown("""
    <style>
        body {
            background-color: #ffe4ec;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #d6336c;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 24px;
            color: #6c1d45;
            text-align: center;
            margin-bottom: 10px;
        }
        .paragraph {
            font-size: 18px;
            color: #333;
            line-height: 1.6;
            text-align: center;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Welcome to Tranquilo 🌸</div>', unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">Revolutionizing Bipolar Disorder Monitoring</div>', unsafe_allow_html=True)

# About us
st.markdown('<div class="paragraph">Tranquilo is pioneering the future of mental health technology for individuals with bipolar disorder. Our mission is to intervene early, empower users, and create a system of support that spans moments of calm and crisis. Built on cutting-edge research and wearable innovation, Tranquilo helps predict and manage mood episodes before they escalate, transforming how we understand and respond to mental health.</div>', unsafe_allow_html=True)

# What we do
st.markdown('<div class="subtitle">What We Do</div>', unsafe_allow_html=True)

st.markdown('<div class="paragraph">Using our AI-powered mobile app and smart ring, we track physiological markers like heart rate variability (HRV), electrodermal activity (EDA), and daily behavior to detect early signs of distress. We then offer real-time support—from peer connections to personalized insights—helping users take action before a full episode emerges. Our technology doesn’t just monitor; it empowers.</div>', unsafe_allow_html=True)

# Meet the founders
st.markdown('<div class="subtitle">Meet the Founders</div>', unsafe_allow_html=True)

founders = {
    "Kian (CEO)": "Kian is a mental health advocate and researcher with over 10 peer-reviewed publications. He previously led a peer support company that supported over 300 people. He developed Tranquilo from his undergraduate thesis which used wearables to predict mood states in bipolar disorder.",
    "Kauel (COO)": "Kauel brings deep experience in biochemistry, manufacturing, and patent strategy. His work ensures that Tranquilo’s hardware meets the highest standards of innovation, efficiency, and intellectual protection.",
    "Maryjo (Chief Research Officer)": "Maryjo has extensive experience conducting clinical trials and is currently training as a nurse. Her clinical insight ensures that Tranquilo is safe, evidence-based, and built with real-world users in mind."
}

image_files = st.file_uploader("Upload founder images (one at a time)", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])

if image_files:
    for image in image_files:
        st.image(image, caption=image.name, use_column_width=True)
        for name, bio in founders.items():
            if name.split()[0].lower() in image.name.lower():
                st.markdown(f"<div class='paragraph'><strong>{name}</strong><br>{bio}</div>", unsafe_allow_html=True)
                break

# Contact form
st.markdown('<div class="subtitle">Contact Us</div>', unsafe_allow_html=True)

with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        st.success("Thank you for reaching out! We'll get back to you soon.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: #6c1d45;'>
        © 2025 Tranquilo. All rights reserved.
    </p>
""", unsafe_allow_html=True)


