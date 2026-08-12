import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Stratix | Enterprise Mobility & GTM Intelligence Console",
    page_icon="",
    layout="wide"
)

# Custom Styling: Enterprise Sidebar, Pill Tabs, Dark Navy Blue (#00075D) Theme
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* Global Base Font Override - 18px for Maximum Readability */
    html, body, [class*="css"] {
        font-size: 18px !important;
        color: #1e293b !important;
    }
    
    /* Custom Header Banner Styling with Exact Dark Navy Blue (#00075D) */
    .stratix-header {
        background-color: #00075D;
        padding: 2.5rem 3rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 7, 93, 0.25);
        border-left: 6px solid #00075D;
    }
    .stratix-header h1 { 
        color: #ffffff !important; 
        font-size: 36px !important; 
        font-weight: 700 !important; 
        margin-bottom: 8px !important; 
    }
    .stratix-header p { 
        color: #ffffff !important; 
        font-size: 19px !important; 
        margin: 0px !important; 
        opacity: 0.9;
    }
    
    /* Section & Subheader Scaling */
    h2 { font-size: 24px !important; color: #0f172a !important; font-weight: 700; margin-top: 1.2rem; }
    h3 { font-size: 20px !important; color: #0f172a !important; font-weight: 700; }
    
    /* Form Labels and Inputs */
    label, .stTextInput label, .stSelectbox label, .stNumberInput label, .stFileUploader label, .stSlider label {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #0f172a !important;
    }
    input, select, div[data-baseweb="select"] span {
        font-size: 18px !important;
    }
    
    /* Primary Action Buttons Unified with Exact Dark Navy Blue (#00075D) */
    .stButton>button {
        background-color: #00075D !important; 
        color: white !important; 
        border-radius: 6px; 
        font-weight: 600; 
        font-size: 18px !important;
        border: none; 
        padding: 0.8rem 1.4rem; 
        width: 100%; 
        box-shadow: 0 4px 12px rgba(0, 7, 93, 0.2);
    }
    .stButton>button:hover { 
        background-color: #000542 !important; 
        color: white !important; 
    }
    
    /* Refined Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #ffffff; 
        padding: 22px; 
        border-radius: 10px; 
        border: 1px solid #e2e8f0; 
        border-top: 4px solid #00075D; 
        box-shadow: 0 4px 12px rgba(0,7,93,0.04);
    }
    div[data-testid="stMetricLabel"] { 
        font-size: 15px !important; 
        color: #64748b !important; 
        font-weight: 600 !important; 
        letter-spacing: 0.3px;
    }
    div[data-testid="stMetricValue"] { 
        font-size: 22px !important; 
        color: #00075D !important; 
        font-weight: 600 !important; 
    }

    /* Modern Pill / Card Tab Separation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        background-color: #f1f5f9;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        padding: 0 24px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        background-color: #00075D !important;
        color: #ffffff !important;
        border-color: #00075D !important;
        font-weight: 700;
        font-size: 18px !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="false"] {
        color: #475569 !important;
        font-weight: 600;
        font-size: 18px !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="false"]:hover {
        background-color: #e2e8f0 !important;
        color: #0f172a !important;
    }
    
    /* Dataframe Table Text Scaling */
    div[data-testid="stDataFrame"] {
        font-size: 17px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- EXPANDED REAL-WORLD ENTERPRISE MASTER DATABASE ---
if 'db_data' not in st.session_state:
    st.session_state.db_data = [
        # Logistics & Transport
        {"Company": "DHL Group", "Domain": "dhl.com", "Industry": "Logistics", "Employees": 590000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.45, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,250,000/yr", "Optimal_Strategy": "Mass Frontline Staging & Buy-and-Rent-Back (BARB) Fleet Modernization", "Partner_Stack": "Samsung / T-Mobile"},
        {"Company": "Deutsche Bahn AG", "Domain": "deutschebahn.com", "Industry": "Logistics", "Employees": 320000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.40, "Legacy_Lockin": True, "Estimated_Contract_Value": "€950,000/yr", "Optimal_Strategy": "Field-Worker Device Modernization via BARB & 1-Day Swap", "Partner_Stack": "Zebra / Vodafone"},
        {"Company": "Dachser SE", "Domain": "dachser.com", "Industry": "Logistics", "Employees": 32000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€380,000/yr", "Optimal_Strategy": "Warehouse Handheld Fleet Upgrade & Automated Staging", "Partner_Stack": "Zebra / Samsung"},

        # Manufacturing & Automotive
        {"Company": "Siemens AG", "Domain": "siemens.com", "Industry": "Manufacturing", "Employees": 320000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,100,000/yr", "Optimal_Strategy": "Enterprise-Scale BARB Rollout + Blancco Erasure", "Partner_Stack": "HP / Microsoft"},
        {"Company": "Volkswagen Group", "Domain": "volkswagen-group.com", "Industry": "Manufacturing", "Employees": 680000, "Current_MDM": "Jamf / Intune", "Device_Density": 0.30, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,500,000/yr", "Optimal_Strategy": "Multi-Plant Ruggedized DaaS Exchange via BARB", "Partner_Stack": "Samsung Knox / T-Mobile"},
        {"Company": "BMW Group", "Domain": "bmwgroup.com", "Industry": "Manufacturing", "Employees": 150000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€600,000/yr", "Optimal_Strategy": "Executive CYOD & Production Line Mobile Security", "Partner_Stack": "Apple / Microsoft"},
        {"Company": "BASF SE", "Domain": "basf.com", "Industry": "Manufacturing", "Employees": 111000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.30, "Legacy_Lockin": True, "Estimated_Contract_Value": "€450,000/yr", "Optimal_Strategy": "Chemical Plant Field Safety Device Lifecycle Management", "Partner_Stack": "Samsung / Vodafone"},

        # Retail & E-Commerce
        {"Company": "Zalando SE", "Domain": "zalando.com", "Industry": "Retail", "Employees": 17000, "Current_MDM": "Jamf", "Device_Density": 0.85, "Legacy_Lockin": False, "Estimated_Contract_Value": "€290,000/yr", "Optimal_Strategy": "Zero-Touch Deployment via Apple DEP & Flexible DaaS", "Partner_Stack": "Apple / AWS"},
        {"Company": "Delivery Hero SE", "Domain": "deliveryhero.com", "Industry": "Retail", "Employees": 28000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.70, "Legacy_Lockin": False, "Estimated_Contract_Value": "€410,000/yr", "Optimal_Strategy": "Rapid Rider & Corporate Staff Scalable DaaS Rollout", "Partner_Stack": "Samsung / Android Enterprise"},
        {"Company": "REWE Group", "Domain": "rewe-group.com", "Industry": "Retail", "Employees": 380000, "Current_MDM": "Mobile Device Manager Plus", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€900,000/yr", "Optimal_Strategy": "Supermarket POS Terminal & Handheld Scanner BARB", "Partner_Stack": "Zebra / O2"},

        # Tech & Software
        {"Company": "SAP SE", "Domain": "sap.com", "Industry": "Tech/SaaS", "Employees": 105000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.90, "Legacy_Lockin": False, "Estimated_Contract_Value": "€750,000/yr", "Optimal_Strategy": "Global Corporate CYOD Program with Intune Integration", "Partner_Stack": "Apple / Microsoft"},
        {"Company": "TeamViewer AG", "Domain": "teamviewer.com", "Industry": "Tech/SaaS", "Employees": 1500, "Current_MDM": "Jamf", "Device_Density": 0.95, "Legacy_Lockin": False, "Estimated_Contract_Value": "€95,000/yr", "Optimal_Strategy": "Remote-First Engineering Onboarding & Device Lifecycle", "Partner_Stack": "Apple / Lenovo"},

        # Finance & Insurance
        {"Company": "Allianz SE", "Domain": "allianz.com", "Industry": "Finance", "Employees": 159000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.75, "Legacy_Lockin": False, "Estimated_Contract_Value": "€820,000/yr", "Optimal_Strategy": "DSGVO-Compliant Secure Financial Advisory Mobile Enclave", "Partner_Stack": "Apple / Vodafone"},
        {"Company": "Deutsche Bank AG", "Domain": "db.com", "Industry": "Finance", "Employees": 85000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.80, "Legacy_Lockin": False, "Estimated_Contract_Value": "€550,000/yr", "Optimal_Strategy": "Secure Investment Banking CYOD & Mobile Threat Defense", "Partner_Stack": "Apple / Microsoft"}
    ]

# Ensure df_db is globally available
df_db = pd.DataFrame(st.session_state.db_data)

# Helper function for Dynamic Multi-Tier Classification
def get_target_tier(employees):
    if employees >= 5000:
        return "Tier 1 - Strategic Enterprise"
    elif employees >= 1500:
        return "Tier 2 - Growth Corporate"
    elif employees >= 500:
        return "Tier 3 - Mid-Market"
    else:
        return "SMB / Emerging"

# --- SIDEBAR CONTROL PANEL ---
with st.sidebar:
    st.markdown("### Workspace Controls")
    st.markdown("Configure global account parameters.")
    
    global_density_modifier = st.slider(
        "Global Device Density Ratio", 
        min_value=0.10, 
        max_value=1.00, 
        value=0.50, 
        step=0.05,
        help="Adjusts the baseline mobile penetration rate across enterprise headcounts."
    )
    
    st.markdown("---")
    st.markdown("**Stratix Console v2.9**<br>Enterprise GTM Infrastructure", unsafe_allow_html=True)

# Header Banner
st.markdown("""
    <div class="stratix-header">
        <h1>Stratix</h1>
        <p>Enterprise Mobility & GTM Intelligence Console</p>
    </div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["Account Intelligence & Outreach", "Master Database & CRM Upload", "Partner Ecosystem & Strategy"])

with tab1:
    st.subheader("Target Account Pipeline & Global Search Engine")
    
    col_s1, col_s2 = st.columns([2, 1])
    with col_s1:
        search_query = st.text_input("🔍 Enterprise Search Engine:", placeholder="Type company name (e.g., Siemens, DHL)...")
    with col_s2:
        industry_options = ["All Industries"] + sorted(df_db["Industry"].unique().tolist())
        selected_industry = st.selectbox("Filter Directory", industry_options)
    
    filtered_db = df_db if selected_industry == "All Industries" else df_db[df_db["Industry"] == selected_industry]
    
    matched_account = None
    is_from_db = True

    if search_query.strip():
        q = search_query.strip().lower()
        exact_match = filtered_db[filtered_db["Company"].str.lower() == q]
        partial_match = filtered_db[filtered_db["Company"].str.lower().str.contains(q, na=False)]
        
        if not exact_match.empty:
            matched_account = exact_match.iloc[0].copy()
        elif not partial_match.empty:
            matched_account = partial_match.iloc[0].copy()
        else:
            is_from_db = False
    else:
        selected_company = st.selectbox("Or Select Enterprise from Directory", filtered_db["Company"].tolist() if not filtered_db.empty else ["No accounts available"])
        match = df_db[df_db["Company"].str.lower() == selected_company.lower()]
        matched_account = match.iloc[0].copy() if not match.empty else df_db.iloc[0].copy()

    if not is_from_db:
        st.warning(f"⚠️ **No indexed account found for '{search_query}' in the Stratix Master Database.**")
        st.info("💡 **Pro-Tip:** You can quickly add this company to your pipeline database using the **Master Database & CRM Upload** tab.")
        matched_account = df_db.iloc[0].copy()
        st.markdown("---")
        st.markdown(f"### 📊 Displaying Default View (`{matched_account['Company']}` as reference):")

    matched_account["Device_Density"] = global_density_modifier
    calculated_fleet = int(matched_account["Employees"] * matched_account["Device_Density"])
    dynamic_tier = get_target_tier(matched_account["Employees"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric("Total Headcount", f"{matched_account['Employees']:,}")
    with col_m2:
        st.metric("Estimated Mobile Fleet", f"{calculated_fleet:,} Devices")
    with col_m3:
        st.metric("Target Tier", dynamic_tier)
    with col_m4:
        st.metric("Est. Annual Contract Value", matched_account["Estimated_Contract_Value"])
