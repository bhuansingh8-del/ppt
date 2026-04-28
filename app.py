import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import io

# --- PPT GENERATION LOGIC ---
def generate_ppt():
    prs = Presentation()
    
    # Define Slide Data (Extracted from PDF)
    slides_data = [
        {"title": "Digital Activism", "content": "M.A. Social Work - Semester IV\nUniversity of Delhi\nPresented to: Dr. Pushpanjali Jha"},
        {"title": "Historical Emergence (Monika R.)", "content": "* Reconfiguration of long-standing collective action.\n* Key Marker: 1990s Zapatista uprising used early digital networks.\n* Transition from 'tweets to the streets'."},
        {"title": "Trajectories of Activism (Aniruddh Singh)", "content": "* 1994: First informational guerrilla movement (EZLN).\n* 2004: Rise of Web 2.0 and 'Prosumption'.\n* 2011: The 'Year of the Protester' (Arab Spring, Occupy)."},
        {"title": "Concepts & Terminologies (Suhail Khan)", "content": "* Cyberactivism: Internet for progressive political purposes.\n* Hacktivism: Technical exploits for political ends.\n* Electronic Civil Disobedience (ECD): Non-violent virtual sit-ins."},
        {"title": "The Choreography of Assembly (Suhail Khan)", "content": "* Cyberspace vs. Cyberplace (socially embedded interaction).\n* Choreographic Leadership: Activist elites setting the emotional tone.\n* Smart Mobs: Organized online, realized physically."},
        {"title": "Ideological Foundations (Shambhavi Mishra)", "content": "* Participatory Democracy: Circumventing corporate media gatekeepers.\n* Anti-Corporate/Anti-Neoliberal framing.\n* Decentralization and horizontalism."},
        {"title": "Issues Highlighted (Bhawna Sharma)", "content": "* Social Justice: #BlackLivesMatter making injustices visible.\n* Gender Justice: #MeToo creating spaces for survivors.\n* Environment: Fridays for Future mobilizing global youth."},
        {"title": "Strategies for Change (Drisya V.)", "content": "* Awareness-raising and issue-framing.\n* Mobilization: Moving people from 'likes' to real-world action.\n* Resource Mobilization: Crowdfunding for legal/travel fees."},
        {"title": "Tactics in Practice (Drisya V.)", "content": "* Hashtag Activism: #MeToo and #BlackLivesMatter.\n* Content Creation: Viral storytelling and citizen journalism.\n* Data Activism: Crowdsourcing satellite imagery to expose wrongdoing."},
        {"title": "Organizational Structure (Ankit & Sayna)", "content": "* Shift from hierarchies to decentralized networks.\n* Key Features: Fluidity, connectivity, and informality.\n* Role of messaging apps in planning and coordination."},
        {"title": "Achievements & Outcomes (Tannu & Gaurav)", "content": "* Rapid mobilization beyond state-controlled media.\n* Lower barriers to participation (Connective Action).\n* Tangible policy shifts (e.g., workplace harassment laws)."},
        {"title": "Limitations & Challenges (Tannu & Gaurav)", "content": "* Slacktivism: Low-effort online actions.\n* Digital Divide: Uneven access based on socioeconomics.\n* State Surveillance: The 'double-edged sword' of digital tools."}
    ]

    for data in slides_data:
        slide_layout = prs.slide_layouts[1] # Title and Content
        slide = prs.slides.add_slide(slide_layout)
        
        # Style Title
        title_shape = slide.shapes.title
        title_shape.text = data["title"]
        
        # Style Body
        body_shape = slide.placeholders[1]
        tf = body_shape.text_frame
        tf.text = data["content"]

    # Save to a byte stream
    ppt_io = io.BytesIO()
    prs.save(ppt_io)
    ppt_io.seek(0)
    return ppt_io

# --- STREAMLIT UI ---
st.set_page_config(page_title="Digital Activism PPT Tool", layout="wide")

# Animated Header with CSS
st.markdown("""
    <style>
    .main-title { font-size: 50px; font-weight: bold; color: #FF4B4B; text-align: center; animation: fadeIn 2s; }
    @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
    </style>
    <div class="main-title">🚀 Digital Activism PPT Generator</div>
    """, unsafe_allow_html=True)

st.write("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Presentation Overview")
    st.info("This app generates a professional 12-slide PowerPoint based on the 'Digital Activism' assignment content.")
    
    if st.button("🛠️ Build PowerPoint Now"):
        ppt_file = generate_ppt()
        st.success("PowerPoint Created Successfully!")
        st.download_button(
            label="📥 Download Presentation",
            data=ppt_file,
            file_name="Digital_Activism_Assignment.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

with col2:
    st.subheader("Interactive Preview")
    tab1, tab2, tab3 = st.tabs(["History", "Tactics", "Structures"])
    with tab1:
        st.write("**Key Milestone:** The 1994 Zapatista uprising in Mexico.")
        st.image("https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&q=80&w=800", caption="Digital Connectivity")
    with tab2:
        st.write("**Hashtag Power:** #MeToo and #BlackLivesMatter.")
        st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&q=80&w=800", caption="Global Social Change")
    with tab3:
        st.write("**Networking:** Moving from hierarchies to flexible coalitions.")