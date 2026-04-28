import streamlit as st

# --- DETAILED SLIDE CONTENT DATABASE ---
SLIDES = [
    {
        "title": "Social Action and Social Movements",
        "subtitle": "Course Code 401, M.A. Social Work, Semester IV\nUniversity of Delhi\nPresented to: Dr. Pushpanjali Jha\nGroup Members: Monika R., Aniruddh Singh, Suhail Khan, Shambhavi Mishra, Drisya, Bhawna Sharma, Tannu Tanwar, Sayna Choudhary, Gaurav Nishad, Ankit Kumar",
        "img": "https://images.unsplash.com/photo-1573164713988-8665fc963095?w=800"
    },
    {
        "author": "Monika R.",
        "title": "The Emergence of Digital Activism",
        "content": "• <b>Historical Continuity:</b> Digital activism is a reconfiguration of long-standing practices of collective action rather than a sudden rupture.<br><br>• <b>Technological Evolution:</b> Activism has shifted through print, radio, and television, with each shift redefining the scale and visibility of movements.<br><br>• <b>The Internet’s Dimension:</b> Unlike previous media, the internet enables immediacy, interactivity, and transnational connectivity.<br><br>• <b>Structural Markers:</b> The 1990s Zapatista uprising is a critical historical marker for using early digital networks to mobilize global solidarity.",
        "img": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800"
    },
    {
        "author": "Aniruddh Singh",
        "title": "Trajectories and Milestones",
        "content": "• <b>1994 - The Informational Guerrilla:</b> The EZLN (Zapatistas) achieved international reach despite primitive infrastructure.<br><br>• <b>2004 - The Rise of Web 2.0:</b> The era of 'prosumption' began, where users simultaneously produce and consume activist content.<br><br>• <b>2011 - The Year of the Protester:</b> Time Magazine designated 2011 as such due to the Arab Spring, Spanish Indignados, and Occupy Wall Street movements.<br><br>• <b>Case Study:</b> Invisible Children utilized YouTube in 2006 to mobilize 80,000 people for the 'Night Commute'.",
        "img": "https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=800"
    },
    {
        "author": "Suhail Khan",
        "title": "Foundational Concepts",
        "content": "• <b>Cyberactivism:</b> The use of internet technologies specifically for progressive political purposes.<br><br>• <b>Hacktivism:</b> A subset of cyberactivism involving technical exploits like disrupting servers for political ends.<br><br>• <b>Electronic Civil Disobedience (ECD):</b> Translates nonviolent rule-breaking into the virtual sphere (e.g., 'virtual sit-ins').<br><br>• <b>Performative Vocabulary:</b> Digital protest acts are often scripted, staged, and enacted for multiple audiences simultaneously.",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800"
    },
    {
        "author": "Suhail Khan",
        "title": "The Choreography of Assembly",
        "content": "• <b>Cyberspace vs. Cyberplace:</b> While cyberspace is abstract, 'Cyberplace' is socially embedded and creates meaningful places for gathering.<br><br>• <b>Choreography of Assembly:</b> The process of using social media to emotionally prepare and symbolically direct physical gatherings.<br><br>• <b>Choreographic Leadership:</b> Indirect, consensual influence exercised by activist elites who 'propose' scripts rather than command.<br><br>• <b>Smart Mobs:</b> Impromptu gatherings organized online, realized physically, and disseminated back into digital spaces.",
        "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=800"
    },
    {
        "author": "Shambhavi Mishra",
        "title": "Ideological Orientation",
        "content": "• <b>Participatory Democracy:</b> The belief that technology can democratize communication by bypassing corporate gatekeepers.<br><br>• <b>Anti-Corporate Foundations:</b> Protest must move into the digital infrastructures where 'nomadic' corporate power now resides.<br><br>• <b>Horizontalism:</b> The ideal of leaderless, self-organizing networks where no single individual commands the movement.<br><br>• <b>The Public Sphere:</b> Seeking to create online spaces for rational deliberation free from state and market distortions.",
        "img": "https://images.unsplash.com/photo-1540910419892-f0c74b0e896a?w=800"
    },
    {
        "author": "Bhawna Sharma",
        "title": "Global Issues in Focus",
        "content": "• <b>Human Rights:</b> Movements like Black Lives Matter use digital tools to expose localized police brutality to a global audience.<br><br>• <b>Gender Justice:</b> The #MeToo movement empowered survivors to challenge patriarchal norms through visibility.<br><br>• <b>Environmental Justice:</b> Fridays for Future mobilized global youth through digital networks to demand ecological accountability.<br><br>• <b>Digital Sphere Concerns:</b> Activism now includes critiques of data privacy, surveillance, and corporate control over the internet.",
        "img": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=800"
    },
    {
        "author": "Drisya V.",
        "title": "Strategies for Social Change",
        "content": "• <b>Issue-Framing:</b> Using personal stories and visuals to shape narratives and build public empathy.<br><br>• <b>Mobilization:</b> Bridging the online-offline divide to move people from 'liking' a post to attending a physical protest.<br><br>• <b>Advocacy:</b> Directly targeting institutions by flooding inboxes or trending topics to demand policy change.<br><br>• <b>The Quadruple 'A' Approach:</b> Abstaining from platforms, Attacking them, building Alternative tools, or Adapting via clever usage.",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800"
    },
    {
        "author": "Drisya V.",
        "title": "Tactics in Practice",
        "content": "• <b>Hashtag Activism:</b> Uniting disparate voices into a global chorus, such as #BlackLivesMatter or #MeToo.<br><br>• <b>Citizen Journalism:</b> Bypassing traditional media during confrontations, such as Facebook Live during Standing Rock.<br><br>• <b>Viral Storytelling:</b> Explaining complex issues through relatable memes, infographics, or short-form videos.<br><br>• <b>Data Activism:</b> Crowdsourcing satellite imagery or citizen reports to expose corporate or environmental wrongdoing.",
        "img": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800"
    },
    {
        "author": "Ankit Kumar & Sayna Choudhary",
        "title": "Organizational Structures",
        "content": "• <b>Flexible Networks:</b> A shift from rigid hierarchies to fluid, horizontal networks where participants join or leave easily.<br><br>• <b>Key Features:</b> Characterized by decentralization, connectivity across platforms, and an absence of formal bureaucratic rules.<br><br>• <b>Coalitions:</b> Alliances between NGOs, students, and citizens that facilitate resource sharing and wider impact.<br><br>• <b>Technological Structuring:</b> Messaging apps like WhatsApp and Telegram are now central to real-time coordination and planning.",
        "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800"
    },
    {
        "author": "Tannu Tanwar & Gaurav Nishad",
        "title": "Achievements",
        "content": "• <b>Rapid Mobilization:</b> The ability to organize mass protests and campaigns within hours, as seen during the Arab Spring.<br><br>• <b>Connective Action:</b> Personalized forms of engagement replace hierarchical organizational membership.<br><br>• <b>Creating Counter-Publics:</b> Digital platforms allow marginalized groups to articulate alternative narratives and challenge news hierarchies.<br><br>• <b>Policy Impact:</b> Translating online narratives into offline change, such as new workplace harassment laws resulting from #MeToo.",
        "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800"
    },
    {
        "author": "Tannu Tanwar & Gaurav Nishad",
        "title": "Outcomes and Limitations",
        "content": "• <b>Slacktivism:</b> The risk that low-effort online actions create an illusion of participation without meaningful change.<br><br>• <b>The Digital Divide:</b> Participation is constrained by socioeconomic status, gender, and geographic location.<br><br>• <b>The Double-Edged Sword:</b> The same tools that enable activism also facilitate state surveillance and repression.<br><br>• <b>Sustainability:</b> Digital movements often face rapid cycles of attention where issues are quickly visible but just as quickly forgotten.",
        "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800"
    }
]

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Activism", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR DARK THEME & BIG TEXT ---
st.markdown("""
    <style>
    /* Global Font adjustments for dark theme appeal */
    html, body, [class*="css"] {
        color: #E0E0E0;
    }
    
    /* Main Title Styling */
    .main-title {
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8E53);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: -1rem;
        margin-bottom: 2rem;
        letter-spacing: 2px;
    }

    /* Slide Card Container with Glassmorphism */
    .slide-card {
        background: rgba(30, 30, 34, 0.7);
        border: 1px solid rgba(255, 75, 75, 0.2);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        animation: slideUp 0.6s ease-out forwards;
        margin-bottom: 2rem;
    }

    /* Slide Headers */
    .slide-title {
        font-size: 3rem !important;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid #FF4B4B;
        padding-bottom: 10px;
        display: inline-block;
    }

    /* Author Tag */
    .slide-author {
        font-size: 1.5rem;
        color: #FF8E53;
        font-weight: 600;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }

    /* Big, readable body text */
    .slide-text {
        font-size: 1.6rem;
        line-height: 1.8;
        color: #D1D5DB;
    }

    /* Subtitle text for the intro slide */
    .intro-subtitle {
        font-size: 1.8rem;
        line-height: 2;
        color: #A0AEC0;
        text-align: left;
    }

    /* Animation Keyframes */
    @keyframes slideUp {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Hide Streamlit Branding for cleaner look */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='main-title'>Digital Activism</div>", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION (Acts as presentation clicker) ---
st.sidebar.markdown("<h2 style='font-size: 2rem; color: #FF4B4B;'>Navigation</h2>", unsafe_allow_html=True)
st.sidebar.write("---")

# Create a list of titles for the radio buttons
slide_options = [f"{i+1}. {s['title']}" for i, s in enumerate(SLIDES)]
selected_slide_str = st.sidebar.radio("Select a slide to view:", slide_options)

# Get the index of the selected slide
selected_index = slide_options.index(selected_slide_str)
current_slide = SLIDES[selected_index]

# --- RENDER THE SELECTED SLIDE ---
# We wrap it in our custom CSS class for the animated, dark-theme card look
st.markdown("<div class='slide-card'>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2], gap="large")

with col1:
    st.markdown(f"<div class='slide-title'>{current_slide['title']}</div>", unsafe_allow_html=True)
    
    if "author" in current_slide:
        st.markdown(f"<div class='slide-author'>👤 {current_slide['author']}</div>", unsafe_allow_html=True)
    
    st.write("") # Spacer
    
    if "content" in current_slide:
        st.markdown(f"<div class='slide-text'>{current_slide['content']}</div>", unsafe_allow_html=True)
    elif "subtitle" in current_slide:
        # Formatting the intro slide specifically so it looks like a title page
        formatted_subtitle = current_slide['subtitle'].replace('\n', '<br>')
        st.markdown(f"<div class='intro-subtitle'>{formatted_subtitle}</div>", unsafe_allow_html=True)

with col2:
    # Adding a slight vertical margin to center the image alongside the big text
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.image(current_slide['img'], use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
