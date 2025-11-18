#!/usr/bin/env python3
"""
Emergency Preparedness AI Agent - Enhanced User-Friendly Edition
An interactive Streamlit application for disaster preparedness

Run with: streamlit run emergency_prep_app_enhanced.py
"""

import streamlit as st
from datetime import datetime
import time

# Try to import folium, but make it optional
try:
    import folium
    from streamlit_folium import st_folium

    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False

# Page configuration - MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Emergency Preparedness Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with beautiful, interactive design
st.markdown("""
    <style>
    /* Import Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .main {
        background: linear-gradient(to bottom, #f0f4f8 0%, #e8eef3 100%);
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Beautiful Header with Animation */
    .professional-header {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
        padding: 3rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.25);
        position: relative;
        overflow: hidden;
    }

    .professional-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 3s infinite;
    }

    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    .professional-header h1 {
        margin: 0;
        font-size: 2.25rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .professional-header p {
        margin: 1rem 0 0 0;
        opacity: 0.95;
        font-size: 1.125rem;
        font-weight: 400;
    }

    /* Main Menu Box with Cards */
    .main-menu-box {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 2rem;
    }

    .main-menu-box h2 {
        margin: 0 0 2rem 0;
        color: #0f172a;
        font-size: 1.75rem;
        font-weight: 700;
        text-align: center;
    }

    /* Card Grid for Services */
    .service-card {
        background: linear-gradient(to bottom right, #ffffff, #f8fafc);
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
        position: relative;
        overflow: hidden;
    }

    .service-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.15);
        transform: translateY(-4px);
    }

    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(to bottom, #3b82f6, #60a5fa);
        transform: scaleY(0);
        transition: transform 0.3s ease;
    }

    .service-card:hover::before {
        transform: scaleY(1);
    }

    /* Info Cards with Icons */
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
        border-left: 4px solid #3b82f6;
    }

    .info-card h3 {
        color: #1e40af;
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .info-card-success {
        border-left-color: #10b981;
    }

    .info-card-warning {
        border-left-color: #f59e0b;
    }

    .info-card-danger {
        border-left-color: #ef4444;
    }

    /* Checklist Items */
    .checklist-item {
        background: #f8fafc;
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #cbd5e1;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .checklist-item:hover {
        background: #f1f5f9;
        border-left-color: #3b82f6;
        transform: translateX(4px);
    }

    /* Image Container */
    .image-container {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin: 1.5rem 0;
        text-align: center;
    }

    .image-container img {
        max-width: 100%;
        border-radius: 8px;
    }

    .image-caption {
        margin-top: 1rem;
        color: #64748b;
        font-size: 0.875rem;
        font-style: italic;
    }

    /* Progress Steps */
    .progress-steps {
        display: flex;
        justify-content: space-between;
        margin: 2rem 0;
        position: relative;
    }

    .progress-step {
        flex: 1;
        text-align: center;
        position: relative;
    }

    .progress-step-circle {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #e2e8f0;
        color: #64748b;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .progress-step-circle.active {
        background: #3b82f6;
        color: white;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }

    .progress-step-label {
        font-size: 0.875rem;
        color: #64748b;
    }

    /* Message Styling - Enhanced */
    .message-container {
        margin: 1.5rem 0;
        animation: slideIn 0.3s ease;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .message-user {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        padding: 1.25rem 1.5rem;
        border-radius: 12px;
        margin-left: 15%;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
        font-size: 1rem;
        line-height: 1.6;
    }

    .message-assistant {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        margin-right: 15%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        font-size: 1rem;
        line-height: 1.8;
        color: #1e293b;
    }

    .message-assistant h2 {
        color: #0f172a;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid #e2e8f0;
    }

    .message-assistant h3 {
        color: #1e40af;
        margin: 1.5rem 0 1rem 0;
        font-size: 1.125rem;
        font-weight: 600;
    }

    /* Better Lists */
    .message-assistant ul {
        margin: 1rem 0;
        padding-left: 0;
        list-style: none;
    }

    .message-assistant li {
        margin: 0.75rem 0;
        padding-left: 1.75rem;
        position: relative;
        color: #475569;
        line-height: 1.7;
    }

    .message-assistant li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #10b981;
        font-weight: bold;
    }

    /* Highlight Boxes */
    .highlight-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 4px solid #3b82f6;
        border-radius: 8px;
        padding: 1.25rem;
        margin: 1.5rem 0;
    }

    .highlight-box-success {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left-color: #10b981;
    }

    .highlight-box-warning {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border-left-color: #f59e0b;
    }

    /* Contact Cards - Enhanced */
    .contact-card {
        background: white;
        padding: 1.25rem;
        border-radius: 12px;
        margin: 0.75rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border-left: 4px solid #10b981;
        transition: all 0.2s ease;
    }

    .contact-card:hover {
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    .contact-card-emergency {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border-left-color: #ef4444;
    }

    /* Sidebar Enhancements */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 100%);
        border-right: 1px solid #e2e8f0;
    }

    [data-testid="stSidebar"] .stButton>button {
        background: white;
        color: #1e293b;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        font-weight: 600;
        font-size: 0.9375rem;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        width: 100%;
    }

    [data-testid="stSidebar"] .stButton>button:hover {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border-color: #3b82f6;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
    }

    /* Input Styling - Enhanced */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 0.875rem 1rem;
        font-size: 1rem;
        transition: all 0.2s ease;
    }

    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
    }

    /* Buttons - Enhanced */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.875rem 1.75rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.2s ease;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.35);
    }

    /* Thinking Animation - Enhanced */
    .thinking-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin: 1.5rem 0;
        border-left: 4px solid #3b82f6;
    }

    .thinking-dots {
        display: inline-flex;
        gap: 0.5rem;
        align-items: center;
    }

    .thinking-dot {
        width: 10px;
        height: 10px;
        background: #3b82f6;
        border-radius: 50%;
        animation: bounce 1.4s infinite ease-in-out both;
    }

    .thinking-dot:nth-child(1) { animation-delay: -0.32s; }
    .thinking-dot:nth-child(2) { animation-delay: -0.16s; }

    @keyframes bounce {
        0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
        40% { transform: scale(1.2); opacity: 1; }
    }

    /* Stats/Metrics Cards */
    .stat-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border-top: 4px solid #3b82f6;
        text-align: center;
    }

    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #3b82f6;
        margin: 0.5rem 0;
    }

    .stat-label {
        color: #64748b;
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }

    /* Section Headers */
    .section-header {
        color: #0f172a;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 3px solid #e2e8f0;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    /* Dividers */
    hr {
        border: none;
        border-top: 2px solid #e2e8f0;
        margin: 2rem 0;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .message-user, .message-assistant {
            margin-left: 0;
            margin-right: 0;
        }

        .professional-header h1 {
            font-size: 1.75rem;
        }

        .progress-steps {
            flex-direction: column;
        }

        .progress-step {
            margin-bottom: 1rem;
        }
    }

    /* Tooltips */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
        color: #3b82f6;
    }

    .tooltip:hover::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: #1e293b;
        color: white;
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        font-size: 0.875rem;
        white-space: nowrap;
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# Data structures (same as before but will be used differently)
FEMA_DATA = {
    "eligibility": [
        "Disaster must be federally declared",
        "Property is your primary residence",
        "Losses not fully covered by insurance",
        "Valid U.S. citizenship or residency"
    ],
    "process": [
        "Register online at DisasterAssistance.gov or call 1-800-621-FEMA",
        "Provide damage details and insurance information",
        "FEMA inspector assesses damage within 10 days",
        "Decision made and funds distributed"
    ]
}

SHELTER_DATA = {
    "Sunnyvale, CA": [
        {
            "name": "Sunnyvale Community Center",
            "address": "550 E Remington Dr",
            "distance": "1.2 miles",
            "capacity": "500 people",
            "services": "Food, water, medical",
            "phone": "(408) 730-7350",
            "lat": 37.3688,
            "lon": -122.0363
        },
        {
            "name": "Fremont High School Gymnasium",
            "address": "765 W Fremont Ave",
            "distance": "2.1 miles",
            "capacity": "800 people",
            "services": "Food, water, medical, pet-friendly",
            "phone": "(408) 522-8200",
            "lat": 37.3541,
            "lon": -122.0443
        },
        {
            "name": "Red Cross Emergency Shelter",
            "address": "2731 N First St, San Jose",
            "distance": "5.3 miles",
            "capacity": "1200 people",
            "services": "Food, water, medical, mental health",
            "phone": "(408) 577-1000",
            "lat": 37.3894,
            "lon": -121.9439
        }
    ]
}

GO_BAG_ESSENTIALS = {
    "base": [
        "Water (1 gallon per person per day for 3 days)",
        "Non-perishable food (3-day supply)",
        "Battery-powered or hand-crank radio",
        "Flashlight and extra batteries",
        "First aid kit",
        "Medications (7-day supply)",
        "Copies of important documents",
        "Cash and credit cards",
        "Emergency contact list",
        "Phone charger and backup battery"
    ],
    "per_adult": [
        "Personal medications",
        "Eyeglasses or contacts",
        "Hygiene items",
        "Change of clothes",
        "Sturdy shoes"
    ],
    "per_child": [
        "Diapers and wipes",
        "Formula and bottles",
        "Comfort items",
        "Snacks",
        "Extra clothing"
    ],
    "per_pet": [
        "Pet food (3-day supply)",
        "Water bowls",
        "Leash and collar with ID",
        "Pet medications",
        "Carrier or crate",
        "Recent photo"
    ]
}

# Go-bag image URL (using a placeholder service)
GO_BAG_IMAGE = "https://images.unsplash.com/photo-1622260614927-2c7ec90445f0?w=800&q=80"


def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'reasoning_visible' not in st.session_state:
        st.session_state.reasoning_visible = False

    if 'is_thinking' not in st.session_state:
        st.session_state.is_thinking = False

    if 'household_info' not in st.session_state:
        st.session_state.household_info = None

    if 'user_address' not in st.session_state:
        st.session_state.user_address = None


def create_shelter_map(shelters, center_lat=None, center_lon=None):
    """Create an interactive map with shelter markers"""
    if not FOLIUM_AVAILABLE:
        return None

    if center_lat and center_lon:
        map_center = [center_lat, center_lon]
    else:
        map_center = [sum(s['lat'] for s in shelters) / len(shelters),
                      sum(s['lon'] for s in shelters) / len(shelters)]

    m = folium.Map(
        location=map_center,
        zoom_start=11,
        tiles='OpenStreetMap'
    )

    if center_lat and center_lon:
        folium.Marker(
            location=[center_lat, center_lon],
            popup="Your Location",
            tooltip="You are here",
            icon=folium.Icon(color='red', icon='home', prefix='glyphicon')
        ).add_to(m)

    for idx, shelter in enumerate(shelters, 1):
        popup_html = f"""
        <div style="font-family: Inter, sans-serif; width: 250px; padding: 8px;">
            <h4 style="color: #1e40af; margin: 0 0 8px 0; font-size: 14px;">{shelter['name']}</h4>
            <p style="margin: 4px 0; font-size: 13px;"><strong>Address:</strong><br>{shelter['address']}</p>
            <p style="margin: 4px 0; font-size: 13px;"><strong>Distance:</strong> {shelter['distance']}</p>
            <p style="margin: 4px 0; font-size: 13px;"><strong>Capacity:</strong> {shelter['capacity']}</p>
            <p style="margin: 4px 0; font-size: 13px;"><strong>Services:</strong> {shelter['services']}</p>
            <p style="margin: 4px 0; font-size: 13px;"><strong>Phone:</strong> {shelter['phone']}</p>
        </div>
        """

        distance_val = float(shelter['distance'].split()[0])
        if distance_val < 2:
            marker_color = 'green'
        elif distance_val < 4:
            marker_color = 'blue'
        else:
            marker_color = 'orange'

        folium.Marker(
            location=[shelter['lat'], shelter['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=shelter['name'],
            icon=folium.Icon(color=marker_color, icon='info-sign', prefix='glyphicon')
        ).add_to(m)

    return m


def simulate_thinking(query, context=None):
    """Simulate agent reasoning process"""
    reasoning = []
    tools_used = []

    reasoning.append({
        "step": "Query Analysis",
        "thought": f"Analyzing: '{query}'"
    })
    time.sleep(0.2)

    response = ""
    show_map = False
    needs_input = None

    # FEMA queries
    if any(word in query.lower() for word in ['fema', 'funding', 'financial', 'assistance', 'apply']):
        reasoning.append({
            "step": "Tool Selection",
            "thought": "Accessing FEMA database"
        })

        tools_used.append({
            "tool": "FEMA Assistance Database",
            "query": "Eligibility and process"
        })
        time.sleep(0.2)

        response = """<div class="info-card">
<h3>💰 FEMA Individual Assistance</h3>
<p>Financial help for disaster-affected homeowners and renters</p>
</div>

<div class="highlight-box">
<strong>✓ Eligibility Requirements</strong><br><br>
"""
        for item in FEMA_DATA['eligibility']:
            response += f"• {item}<br>"

        response += """</div>

<div class="info-card info-card-success">
<h3>📋 How to Apply</h3>
"""
        for idx, step in enumerate(FEMA_DATA['process'], 1):
            response += f"<strong>Step {idx}:</strong> {step}<br><br>"

        response += """</div>

<div class="highlight-box-success">
<strong>💵 Available Assistance (Up to $38,000)</strong><br><br>
• Home repairs and replacements<br>
• Temporary housing<br>
• Medical and dental expenses<br>
• Personal property replacement<br>
</div>

<div class="highlight-box-warning">
<strong>⚠️ Important</strong><br><br>
Apply within 60 days • Document all damage • Keep receipts
</div>

<strong>📞 Contact:</strong> 1-800-621-FEMA (3362) | <a href="https://www.disasterassistance.gov" target="_blank" style="color: #3b82f6; text-decoration: underline;">DisasterAssistance.gov</a>"""

    # Shelter queries
    elif any(word in query.lower() for word in ['shelter', 'evacuation']):
        if not st.session_state.user_address:
            response = """<div class="info-card">
<h3>🏠 Find Emergency Shelters</h3>
<p>Locate safe havens within 50 miles of your location</p>
</div>

<div class="highlight-box">
Enter your address or ZIP code below to see all available emergency shelters on an interactive map.
</div>"""
            needs_input = "address"
        else:
            reasoning.append({
                "step": "Tool Selection",
                "thought": "Searching 50-mile radius"
            })

            tools_used.append({
                "tool": "Emergency Shelter Database",
                "query": f"Near {st.session_state.user_address}"
            })
            time.sleep(0.2)

            show_map = True

            response = f"""<div class="info-card info-card-success">
<h3>🏠 Emergency Shelters Found</h3>
<p><strong>Your Location:</strong> {st.session_state.user_address}<br>
<strong>Search Radius:</strong> 50 miles</p>
</div>

"""
            for idx, shelter in enumerate(SHELTER_DATA["Sunnyvale, CA"], 1):
                response += f"""<div class="checklist-item">
<strong>{idx}. {shelter['name']}</strong><br>
📍 {shelter['address']} • 📏 {shelter['distance']}<br>
📞 {shelter['phone']} • 👥 {shelter['capacity']}<br>
🏥 Services: {shelter['services']}
</div>

"""

            response += """<div class="highlight-box-warning">
<strong>What to Bring to Shelter</strong><br><br>
Photo ID • Medications • Bedding • Toiletries • Phone charger • Cash
</div>

<strong>📱 Resources:</strong> Call 211 for real-time availability • <a href="https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html" target="_blank" style="color: #3b82f6; text-decoration: underline;">redcross.org/shelter</a>"""

    # Go-bag queries
    elif any(word in query.lower() for word in ['go bag', 'go-bag', 'emergency kit', 'prepare', 'pack', 'kit']):
        if not st.session_state.household_info:
            response = f"""<div class="info-card">
<h3>🎒 Build Your Emergency Kit</h3>
<p>Personalized checklist for your household</p>
</div>

<div class="image-container">
<img src="{GO_BAG_IMAGE}" alt="Emergency Go-Bag" style="max-width: 600px; border-radius: 12px;">
<p class="image-caption">A well-stocked emergency go-bag ready for any situation</p>
</div>

<div class="highlight-box">
<strong>Tell us about your household</strong><br><br>
Enter the number of adults, children, and pets below to get a customized emergency kit checklist.
</div>"""
            needs_input = "household"
        else:
            reasoning.append({
                "step": "Personalization",
                "thought": "Generating custom checklist"
            })

            tools_used.append({
                "tool": "Emergency Kit Generator",
                "query": f"Household: {st.session_state.household_info}"
            })
            time.sleep(0.2)

            info = st.session_state.household_info
            total_people = info['adults'] + info['children']

            response = f"""<div class="info-card info-card-success">
<h3>🎒 Your Personalized Emergency Kit</h3>
<p><strong>Household:</strong> {info['adults']} adults • {info['children']} children • {info['pets']} pets<br>
<strong>Total Items:</strong> {len(GO_BAG_ESSENTIALS['base']) + (info['adults'] * len(GO_BAG_ESSENTIALS['per_adult'])) + (info['children'] * len(GO_BAG_ESSENTIALS['per_child'])) + (info['pets'] * len(GO_BAG_ESSENTIALS['per_pet']))} items</p>
</div>

<div class="image-container">
<img src="{GO_BAG_IMAGE}" alt="Emergency Go-Bag" style="max-width: 600px; border-radius: 12px;">
<p class="image-caption">Example of a well-organized emergency go-bag</p>
</div>

<div class="highlight-box">
<strong>📦 Base Essentials (Everyone)</strong><br><br>
"""
            for idx, item in enumerate(GO_BAG_ESSENTIALS['base'], 1):
                response += f"{idx}. {item}<br>"

            response += "</div>"

            if info['adults'] > 0:
                response += f"""

<div class="highlight-box-success">
<strong>👤 For {info['adults']} Adult(s)</strong><br><br>
"""
                for item in GO_BAG_ESSENTIALS['per_adult']:
                    response += f"• {item}<br>"
                response += "</div>"

            if info['children'] > 0:
                response += f"""

<div class="highlight-box-success">
<strong>👶 For {info['children']} Child(ren)</strong><br><br>
"""
                for item in GO_BAG_ESSENTIALS['per_child']:
                    response += f"• {item}<br>"
                response += "</div>"

            if info['pets'] > 0:
                response += f"""

<div class="highlight-box-success">
<strong>🐾 For {info['pets']} Pet(s)</strong><br><br>
"""
                for item in GO_BAG_ESSENTIALS['per_pet']:
                    response += f"• {item}<br>"
                response += "</div>"

            response += """

<div class="highlight-box-warning">
<strong>💡 Pro Tips</strong><br><br>
Store near exit • Check every 6 months • Keep lightweight • Use waterproof containers
</div>

<strong>📄 Download Checklist:</strong> <a href="https://www.ready.gov/kit" target="_blank" style="color: #3b82f6; text-decoration: underline;">Ready.gov/kit</a>"""

    # Emergency Planning
    elif any(word in query.lower() for word in ['plan', 'planning', 'communication']):
        reasoning.append({
            "step": "Tool Selection",
            "thought": "Loading planning templates"
        })

        tools_used.append({
            "tool": "Emergency Planning Database",
            "query": "Family plans"
        })
        time.sleep(0.2)

        response = """<div class="info-card">
<h3>📋 Family Emergency Plan</h3>
<p>Create a comprehensive communication and response strategy</p>
</div>

<div class="highlight-box">
<strong>📞 Communication Plan</strong><br><br>
• Designate out-of-state contact person<br>
• Share contact list with all family members<br>
• Establish text messaging protocols<br>
• Document everyone's work/school info
</div>

<div class="info-card info-card-success">
<h3>📍 Meeting Locations</h3>
<p><strong>Primary:</strong> Near home (neighbor's house, nearby landmark)<br>
<strong>Secondary:</strong> Outside neighborhood (library, community center)</p>
</div>

<div class="highlight-box-success">
<strong>🎯 Practice Drills</strong><br><br>
• Home evacuation: Quarterly<br>
• Earthquake drill: Twice yearly<br>
• Fire escape: Monthly review
</div>

<div class="highlight-box-warning">
<strong>📄 Important Documents</strong><br><br>
Insurance • Medical records • IDs • Financial documents • Property deeds
</div>

<strong>📚 Resource:</strong> <a href="https://www.ready.gov/plan" target="_blank" style="color: #3b82f6; text-decoration: underline;">Ready.gov/plan</a>"""

    # Alert System
    elif any(word in query.lower() for word in ['alert', 'warning', 'notification']):
        reasoning.append({
            "step": "Tool Selection",
            "thought": "Checking alert systems"
        })

        tools_used.append({
            "tool": "Emergency Alert System",
            "query": "Current status"
        })
        time.sleep(0.2)

        response = """<div class="info-card info-card-success">
<h3>⚠️ Emergency Alert Status</h3>
<p><strong>Location:</strong> Sunnyvale, CA<br>
<strong>Status:</strong> ✓ No Active Alerts<br>
<strong>Risk Level:</strong> Low</p>
</div>

<div class="highlight-box">
<strong>📱 Sign Up for Alerts</strong><br><br>
<strong>Wireless Emergency Alerts (WEA)</strong> – Automatic on all phones<br>
<strong>Local System:</strong> <a href="https://alertscc.org" target="_blank" style="color: #3b82f6; text-decoration: underline;">alertscc.org</a><br>
<strong>NOAA Weather Radio:</strong> <a href="https://www.weather.gov" target="_blank" style="color: #3b82f6; text-decoration: underline;">weather.gov</a><br>
<strong>FEMA App:</strong> Download for notifications
</div>

<div class="info-card">
<h3>🔔 What to Do During Alert</h3>
<p>1. Follow official instructions immediately<br>
2. Check on neighbors<br>
3. Have go-bag ready<br>
4. Monitor official channels</p>
</div>"""

    # Disaster-specific
    elif any(word in query.lower() for word in ['earthquake', 'fire', 'flood', 'disaster']):
        disaster = next((d for d in ['earthquake', 'fire', 'flood'] if d in query.lower()), 'earthquake')

        response = f"""<div class="info-card info-card-warning">
<h3>🚨 {disaster.title()} Preparedness</h3>
<p>Essential safety information</p>
</div>

<div class="highlight-box-warning">
<strong>Immediate Actions</strong><br><br>
"""
        if disaster == 'earthquake':
            response += "🛡️ <strong>Drop, Cover, Hold On</strong><br>Get under sturdy furniture • Stay away from windows • If outdoors, move to open area"
        elif disaster == 'fire':
            response += "🔥 <strong>Get Out, Stay Out</strong><br>Exit immediately • Crawl under smoke • Feel doors before opening • Never use elevators"
        elif disaster == 'flood':
            response += "🌊 <strong>Move to Higher Ground</strong><br>Never drive through water • 6\" knocks you down • 12\" moves cars • Avoid floodwaters"

        response += """</div>

<div class="highlight-box">
<strong>Before Disaster</strong><br><br>
• Secure furniture and appliances<br>
• Know utility shut-offs<br>
• Maintain emergency supplies<br>
• Practice safety drills
</div>

<div class="info-card">
<h3>After the Disaster</h3>
<p>Check for injuries • Inspect for damage • Avoid hazard areas • Document losses • Contact FEMA if needed</p>
</div>

<strong>📚 Learn More:</strong> <a href="https://www.ready.gov/{disaster}" target="_blank" style="color: #3b82f6; text-decoration: underline;">Ready.gov/{disaster}</a>"""

    else:
        response = """<div class="info-card">
<h3>How Can I Help?</h3>
<p>Choose a service from the menu above or ask me about emergency preparedness topics.</p>
</div>"""

    return response, reasoning, tools_used, show_map, needs_input


def display_message(msg):
    """Display a chat message"""
    with st.container():
        if msg['role'] == 'user':
            st.markdown(f'<div class="message-container"><div class="message-user">{msg["content"]}</div></div>',
                        unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message-container"><div class="message-assistant">{msg["content"]}</div></div>',
                        unsafe_allow_html=True)

            if msg.get('show_map') and FOLIUM_AVAILABLE:
                st.markdown("---")
                shelter_map = create_shelter_map(SHELTER_DATA["Sunnyvale, CA"])
                if shelter_map:
                    st_folium(shelter_map, width=700, height=500)
                st.markdown("---")

            if msg.get('tools_used') and st.session_state.reasoning_visible:
                with st.expander("🔧 Tools Used", expanded=False):
                    for tool in msg['tools_used']:
                        st.info(f"**{tool['tool']}**\nQuery: {tool['query']}")

            if msg.get('reasoning') and st.session_state.reasoning_visible:
                with st.expander("🧠 Agent Reasoning", expanded=False):
                    for step in msg['reasoning']:
                        st.success(f"**{step['step']}:** {step['thought']}")


def handle_user_input(query):
    """Handle user input"""
    if not st.session_state.is_thinking:
        st.session_state.messages.append({
            "role": "user",
            "content": query,
            "timestamp": datetime.now()
        })
        st.session_state.is_thinking = True


def show_main_menu():
    """Display main menu"""
    st.markdown("""
        <div class="main-menu-box">
            <h2>Emergency Services</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("**💰 FEMA Assistance**\nFinancial aid and applications",
                     use_container_width=True, key="menu_fema"):
            handle_user_input("How do I apply for FEMA assistance?")
            st.rerun()

        if st.button("**🎒 Emergency Kits**\nPersonalized go-bag checklists",
                     use_container_width=True, key="menu_kit"):
            handle_user_input("Help me build an emergency kit")
            st.rerun()

    with col2:
        if st.button("**🏠 Shelter Locations**\nFind nearby safe havens",
                     use_container_width=True, key="menu_shelter"):
            handle_user_input("Find emergency shelters near me")
            st.rerun()

        if st.button("**📋 Emergency Planning**\nFamily communication plans",
                     use_container_width=True, key="menu_planning"):
            handle_user_input("Help me create an emergency plan")
            st.rerun()

    with col3:
        if st.button("**⚠️ Alert System**\nCurrent warnings and notifications",
                     use_container_width=True, key="menu_alerts"):
            handle_user_input("What are the current emergency alerts?")
            st.rerun()

        if st.button("**🚨 Disaster Guides**\nEarthquake, fire, flood safety",
                     use_container_width=True, key="menu_disasters"):
            handle_user_input("Tell me about earthquake preparedness")
            st.rerun()


def main():
    """Main application"""
    initialize_session_state()

    # Beautiful Header
    st.markdown("""
        <div class="professional-header">
            <h1>Emergency Preparedness Assistant</h1>
            <p>Your intelligent guide for disaster readiness and safety</p>
        </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### 🚀 QUICK ACCESS")
        st.markdown("")

        if st.button("💰 FEMA Assistance", use_container_width=True, key="sidebar_fema"):
            handle_user_input("How do I apply for FEMA assistance?")
            st.rerun()

        if st.button("🏠 Shelter Locator", use_container_width=True, key="sidebar_shelter"):
            handle_user_input("Find emergency shelters near me")
            st.rerun()

        if st.button("🎒 Emergency Kit", use_container_width=True, key="sidebar_gobag"):
            handle_user_input("Help me build an emergency kit")
            st.rerun()

        if st.button("📋 Emergency Planning", use_container_width=True, key="sidebar_planning"):
            handle_user_input("Help me create an emergency plan")
            st.rerun()

        if st.button("⚠️ Alert System", use_container_width=True, key="sidebar_alerts"):
            handle_user_input("What are the current emergency alerts?")
            st.rerun()

        if st.button("🚨 Disaster Guides", use_container_width=True, key="sidebar_disasters"):
            handle_user_input("Tell me about earthquake preparedness")
            st.rerun()

        st.markdown("---")
        st.markdown("### 📞 EMERGENCY CONTACTS")

        st.markdown("""
        <div class="contact-card contact-card-emergency">
            <strong>🚨 Emergency: 911</strong><br>
            <small>Police • Fire • Medical</small>
        </div>
        """, unsafe_allow_html=True)

        contacts = [
            ("💰 FEMA", "1-800-621-3362", "Disaster assistance"),
            ("❤️ Red Cross", "1-800-733-2767", "Disaster relief"),
            ("ℹ️ 211", "Dial 211", "Community resources")
        ]

        for icon_name, number, desc in contacts:
            st.markdown(f"""
            <div class="contact-card">
                <strong>{icon_name}: {number}</strong><br>
                <small>{desc}</small>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        st.session_state.reasoning_visible = st.checkbox(
            "Show AI reasoning",
            value=False
        )

        if st.button("🔄 Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.is_thinking = False
            st.session_state.household_info = None
            st.session_state.user_address = None
            st.rerun()

    # Main menu - always visible
    show_main_menu()

    # Conversation area
    if len(st.session_state.messages) > 0:
        st.markdown('<div class="section-header">💬 Conversation</div>', unsafe_allow_html=True)

        for message in st.session_state.messages:
            display_message(message)

        # Handle input requests
        if len(st.session_state.messages) > 0:
            last_msg = st.session_state.messages[-1]
            if last_msg['role'] == 'assistant' and last_msg.get('needs_input'):
                if last_msg['needs_input'] == 'household':
                    st.markdown("---")
                    st.markdown("### 👨‍👩‍👧‍👦 Tell Us About Your Household")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        adults = st.number_input("👤 Adults", min_value=0, max_value=20, value=2)
                    with col2:
                        children = st.number_input("👶 Children", min_value=0, max_value=20, value=0)
                    with col3:
                        pets = st.number_input("🐾 Pets", min_value=0, max_value=20, value=0)

                    if st.button("✨ Generate My Checklist", use_container_width=True):
                        st.session_state.household_info = {
                            'adults': adults,
                            'children': children,
                            'pets': pets
                        }
                        handle_user_input(f"Create kit for {adults} adults, {children} children, {pets} pets")
                        st.rerun()

                elif last_msg['needs_input'] == 'address':
                    st.markdown("---")
                    st.markdown("### 📍 Enter Your Location")
                    address = st.text_input("Address or ZIP code", placeholder="e.g., 123 Main St, Sunnyvale, CA 94086")
                    if st.button("🔍 Find Shelters", use_container_width=True):
                        if address:
                            st.session_state.user_address = address
                            handle_user_input(f"Find shelters near {address}")
                            st.rerun()

        if st.session_state.is_thinking:
            st.markdown("""
            <div class="thinking-container">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div class="thinking-dots">
                        <div class="thinking-dot"></div>
                        <div class="thinking-dot"></div>
                        <div class="thinking-dot"></div>
                    </div>
                    <span style="color: #475569; font-weight: 600; font-size: 1rem;">Processing your request...</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            query = st.session_state.messages[-1]['content']
            response, reasoning, tools, show_map, needs_input = simulate_thinking(query)

            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now(),
                "reasoning": reasoning,
                "tools_used": tools,
                "show_map": show_map,
                "needs_input": needs_input
            })

            st.session_state.is_thinking = False
            st.rerun()

        # Chat input
        st.markdown("---")
        user_input = st.text_input(
            "💬 Ask a question...",
            placeholder="E.g., How do I prepare for an earthquake?",
            label_visibility="collapsed",
            key="user_input_field"
        )

        if user_input and not st.session_state.is_thinking:
            handle_user_input(user_input)
            st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="info-card">
        <h3>ℹ️ About This Assistant</h3>
        <p>This AI assistant provides expert emergency preparedness guidance based on FEMA guidelines, Red Cross protocols, and emergency management best practices. For life-threatening emergencies, always call 911.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
