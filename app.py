import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt
import io
import requests

# --- SLIDE CONTENT DATABASE ---
SLIDES = [
    {"title": "Digital Activism: Social Action & Movements", "subtitle": "M.A. Social Work | University of Delhi\nPresented to: Dr. Pushpanjali Jha", "img": "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=800"},
    {"author": "Monika R.", "title": "The Emergence of Digital Activism", "content": "• Historical reconfiguration of collective action.\n• Influenced by globalization and neoliberal capitalism.\n• Key Marker: 1990s Zapatista uprising.", "img": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800"},
    {"author": "Aniruddh Singh", "title": "Trajectories and Milestones", "content": "• 1994: The first 'informational guerrilla' movement.\n• 2004+: Web 2.0 and the rise of 'Prosumption'.\n• 2011: 'Year of the Protester' (Arab Spring, Occupy).", "img": "https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=800"},
    {"author": "Suhail Khan", "title": "Key Concepts & Terminologies", "content": "• Cyberactivism vs. Hacktivism.\n• Electronic Civil Disobedience (ECD).\n• Transitioning from Cyberspace to 'Cyberplace'.", "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800"},
    {"author": "Suhail Khan", "title": "Choreography of Assembly", "content": "• Social media sets the stage for physical assemblies.\n• 'Choreographic Leadership': consensual influence by elites.\n• Smart Mobs: Online organization, offline action.", "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=800"},
    {"author": "Shambhavi Mishra", "title": "Ideological Foundations", "content": "• Commitment to Participatory Democracy.\n• Anti-Corporate and Anti-Neoliberal framing.\n• Focus on Horizontalism and Decentralization.", "img": "https://images.unsplash.com/photo-1540910419892-f0c74b0e896a?w=800"},
    {"author": "Bhawna Sharma", "title": "Issues Highlighted Globally", "content": "• Social/Human Rights: #BlackLivesMatter.\n• Gender Justice: #MeToo Movement.\n• Environment: Fridays for Future strikes.", "img": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=800"},
    {"author": "Drisya V.", "title": "Strategies for Change", "content": "• Awareness-raising and issue-framing.\n• Mobilization: Moving people from 'likes' to action.\n• Resource Mobilization: Crowdfunding and data activism.", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800"},
    {"author": "Drisya V.", "title": "Tactics in Practice", "content": "• Hashtag Activism and Social Media campaigns.\n• Content creation and Viral Storytelling.\n• Disruptive Hacktivism (Virtual Sit-ins).", "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800"},
    {"author": "Ankit & Sayna", "title": "Organizational Structures", "content": "• Shift from rigid hierarchies to flexible networks.\n• Role of messaging apps (WhatsApp, Telegram).\n• Coalitions between NGOs, students, and citizens.", "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800"},
    {"author": "Tannu & Gaurav", "title": "Achievements and Outcomes", "content": "• Rapid mobilization beyond state media.\n• Lower barriers to participation (Connective Action).\n• Policy and institutional changes (e.g., #MeToo laws).", "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800"},
    {"author": "Tannu & Gaurav", "title": "Limitations and Challenges", "content": "• Slacktivism: Low-effort online engagement.\n• The Digital Divide and State Surveillance.\n• Sustainability and algorithmic bias.", "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800"}
]

def generate_ppt():
    prs = Presentation()
    for item in SLIDES:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = item["title"]
        
        # Text Frame
        body = slide.placeholders[1].text_frame
        if "author" in item:
            p = body.add_paragraph()
            p.text = f"Contributor: {item['author']}"
            p.font.bold = True
        
        if "content" in item:
            body.add_paragraph().text = item["content"]
        elif "subtitle" in item:
            body.add_paragraph().text = item["subtitle"]

        # Add Image from URL
        try:
            response = requests.get(item["img"])
            img_stream = io.BytesIO(response.content)
            slide.shapes.add_picture(img_stream, Inches(6), Inches(1.5), height=Inches(4))
        except:
            pass

    ppt_io = io.BytesIO()
    prs.save(ppt_io)
    ppt_io.seek(0)
    return ppt_io

# --- STREAMLIT UI ---
st.set_page_config(page_title="Digital Activism Tool", page_icon="✊")

st.markdown("<h1 style='text-align: center;'>✊ Digital Activism PPT Generator</h1>", unsafe_allow_html=True)
st.write("---")

st.info("This interactive tool generates a professional presentation based on the Group 401 Assignment.")

if st.button("🚀 Generate & Download Presentation"):
    with st.spinner("Fetching images and building slides..."):
        ppt_data = generate_ppt()
        st.success("Done!")
        st.download_button(
            label="📂 Download PPTX",
            data=ppt_data,
            file_name="Digital_Activism_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

# Animated Preview Section
st.subheader("Interactive Content Preview")
cols = st.columns(2)
for i, slide in enumerate(SLIDES[1:5]): # Showing a few as preview
    with cols[i%2]:
        with st.expander(f"Slide: {slide['title']}"):
            st.image(slide['img'])
            st.write(slide['content'])
