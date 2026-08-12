import streamlit as st
import pandas as pd
import time

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

# --- EXPANDED MASTER DATABASE ACROSS 14+ SECTORS ---
if 'db_data' not in st.session_state:
    st.session_state.db_data = [
        # Logistics & Transport
        {"Company": "DHL Group", "Domain": "dhl.com", "Industry": "Logistics & Supply Chain", "Employees": 590000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.45, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,250,000/yr", "Optimal_Strategy": "Mass Frontline Staging & Buy-and-Rent-Back (BARB) Fleet Modernization", "Partner_Stack": "Samsung / T-Mobile"},
        {"Company": "Deutsche Bahn AG", "Domain": "deutschebahn.com", "Industry": "Logistics & Supply Chain", "Employees": 320000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.40, "Legacy_Lockin": True, "Estimated_Contract_Value": "€950,000/yr", "Optimal_Strategy": "Field-Worker Device Modernization via BARB & 1-Day Swap", "Partner_Stack": "Zebra / Vodafone"},
        {"Company": "Dachser SE", "Domain": "dachser.com", "Industry": "Logistics & Supply Chain", "Employees": 32000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€380,000/yr", "Optimal_Strategy": "Warehouse Handheld Fleet Upgrade & Automated Staging", "Partner_Stack": "Zebra / Samsung"},

        # Manufacturing & Industrial
        {"Company": "Siemens AG", "Domain": "siemens.com", "Industry": "Manufacturing & Industrial", "Employees": 320000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,100,000/yr", "Optimal_Strategy": "Enterprise-Scale BARB Rollout + Blancco Erasure", "Partner_Stack": "HP / Microsoft"},
        {"Company": "Volkswagen Group", "Domain": "volkswagen-group.com", "Industry": "Manufacturing & Industrial", "Employees": 680000, "Current_MDM": "Jamf / Intune", "Device_Density": 0.30, "Legacy_Lockin": True, "Estimated_Contract_Value": "€1,500,000/yr", "Optimal_Strategy": "Multi-Plant Ruggedized DaaS Exchange via BARB", "Partner_Stack": "Samsung Knox / T-Mobile"},
        {"Company": "BMW Group", "Domain": "bmwgroup.com", "Industry": "Manufacturing & Industrial", "Employees": 150000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€600,000/yr", "Optimal_Strategy": "Executive CYOD & Production Line Mobile Security", "Partner_Stack": "Apple / Microsoft"},

        # Chemicals & Materials
        {"Company": "BASF SE", "Domain": "basf.com", "Industry": "Chemicals & Materials", "Employees": 111000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.30, "Legacy_Lockin": True, "Estimated_Contract_Value": "€450,000/yr", "Optimal_Strategy": "Chemical Plant Field Safety Device Lifecycle Management", "Partner_Stack": "Samsung / Vodafone"},
        {"Company": "Bayer AG", "Domain": "bayer.com", "Industry": "Chemicals & Materials", "Employees": 100000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.50, "Legacy_Lockin": False, "Estimated_Contract_Value": "€420,000/yr", "Optimal_Strategy": "Global Pharma Representative Tablet CYOD Program", "Partner_Stack": "Apple / Vodafone"},

        # Retail & E-Commerce
        {"Company": "Zalando SE", "Domain": "zalando.com", "Industry": "Retail & E-Commerce", "Employees": 17000, "Current_MDM": "Jamf", "Device_Density": 0.85, "Legacy_Lockin": False, "Estimated_Contract_Value": "€290,000/yr", "Optimal_Strategy": "Zero-Touch Deployment via Apple DEP & Flexible DaaS", "Partner_Stack": "Apple / AWS"},
        {"Company": "Delivery Hero SE", "Domain": "deliveryhero.com", "Industry": "Retail & E-Commerce", "Employees": 28000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.70, "Legacy_Lockin": False, "Estimated_Contract_Value": "€410,000/yr", "Optimal_Strategy": "Rapid Rider & Corporate Staff Scalable DaaS Rollout", "Partner_Stack": "Samsung / Android Enterprise"},
        {"Company": "REWE Group", "Domain": "rewe-group.com", "Industry": "Retail & E-Commerce", "Employees": 380000, "Current_MDM": "Mobile Device Manager Plus", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€900,000/yr", "Optimal_Strategy": "Supermarket POS Terminal & Handheld Scanner BARB", "Partner_Stack": "Zebra / O2"},

        # Tech & Software (SaaS)
        {"Company": "SAP SE", "Domain": "sap.com", "Industry": "Technology & SaaS", "Employees": 105000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.90, "Legacy_Lockin": False, "Estimated_Contract_Value": "€750,000/yr", "Optimal_Strategy": "Global Corporate CYOD Program with Intune Integration", "Partner_Stack": "Apple / Microsoft"},
        {"Company": "TeamViewer AG", "Domain": "teamviewer.com", "Industry": "Technology & SaaS", "Employees": 1500, "Current_MDM": "Jamf", "Device_Density": 0.95, "Legacy_Lockin": False, "Estimated_Contract_Value": "€95,000/yr", "Optimal_Strategy": "Remote-First Engineering Onboarding & Device Lifecycle", "Partner_Stack": "Apple / Lenovo"},

        # Finance & Insurance
        {"Company": "Allianz SE", "Domain": "allianz.com", "Industry": "Finance & Insurance", "Employees": 159000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.75, "Legacy_Lockin": False, "Estimated_Contract_Value": "€820,000/yr", "Optimal_Strategy": "DSGVO-Compliant Secure Financial Advisory Mobile Enclave", "Partner_Stack": "Apple / Vodafone"},
        {"Company": "Deutsche Bank AG", "Domain": "db.com", "Industry": "Finance & Insurance", "Employees": 85000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.80, "Legacy_Lockin": False, "Estimated_Contract_Value": "€550,000/yr", "Optimal_Strategy": "Secure Investment Banking CYOD & Mobile Threat Defense", "Partner_Stack": "Apple / Microsoft"},

        # Energy & Utilities
        {"Company": "E.ON SE", "Domain": "eon.com", "Industry": "Energy & Utilities", "Employees": 72000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.40, "Legacy_Lockin": True, "Estimated_Contract_Value": "€310,000/yr", "Optimal_Strategy": "Critical Infrastructure Field Technician Ruggedized Swap", "Partner_Stack": "Samsung / T-Mobile"},
        {"Company": "RWE AG", "Domain": "rwe.com", "Industry": "Energy & Utilities", "Employees": 20000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.45, "Legacy_Lockin": True, "Estimated_Contract_Value": "€180,000/yr", "Optimal_Strategy": "Green Energy Power Plant Asset Tracking via BARB", "Partner_Stack": "Zebra / Vodafone"},

        # Telecommunications
        {"Company": "Deutsche Telekom AG", "Domain": "telekom.com", "Industry": "Telecommunications", "Employees": 199000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.80, "Legacy_Lockin": False, "Estimated_Contract_Value": "€890,000/yr", "Optimal_Strategy": "Co-Selling Carrier Bundle DaaS Framework", "Partner_Stack": "Apple / Samsung"},

        # Healthcare & Pharma
        {"Company": "Fresenius SE & Co. KGaA", "Domain": "fresenius.com", "Industry": "Healthcare & Pharmaceuticals", "Employees": 300000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€920,000/yr", "Optimal_Strategy": "Clinical Tablet Rollout & HIPAA/GDPR Secure Wiping", "Partner_Stack": "Samsung Knox / Vodafone"},

        # Aerospace & Defense
        {"Company": "Airbus SE", "Domain": "airbus.com", "Industry": "Aerospace & Defense", "Employees": 134000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€580,000/yr", "Optimal_Strategy": "High-Security Classified Engineering Device Management", "Partner_Stack": "HP / Microsoft"},

        # Media & Entertainment
        {"Company": "RTL Group", "Domain": "rtlgroup.com", "Industry": "Media & Entertainment", "Employees": 17000, "Current_MDM": "Jamf", "Device_Density": 0.85, "Legacy_Lockin": False, "Estimated_Contract_Value": "€140,000/yr", "Optimal_Strategy": "Broadcast Production Mobile Workstation CYOD", "Partner_Stack": "Apple / AWS"},

        # Real Estate & Construction
        {"Company": "Vonovia SE", "Domain": "vonovia.de", "Industry": "Real Estate & Construction", "Employees": 12000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.55, "Legacy_Lockin": True, "Estimated_Contract_Value": "€110,000/yr", "Optimal_Strategy": "Property Management Inspection Tablet Deployment via BARB", "Partner_Stack": "Samsung / O2"},

        # Public Sector & Government
        {"Company": "Federal Agency for Digital (Mock)", "Domain": "bund.de", "Industry": "Public Sector & Government", "Employees": 45000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.60, "Legacy_Lockin": False, "Estimated_Contract_Value": "€210,000/yr", "Optimal_Strategy": "BSI-Compliant Secure Government Mobility Architecture", "Partner_Stack": "Samsung Knox / T-Mobile"},

        # Hospitality & Tourism
        {"Company": "TUI AG", "Domain": "tuigroup.com", "Industry": "Hospitality & Tourism", "Employees": 60000, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.65, "Legacy_Lockin": False, "Estimated_Contract_Value": "€250,000/yr", "Optimal_Strategy": "Global Resort Staff Device Pooling & Seasonal DaaS", "Partner_Stack": "Apple / Vodafone"}
    ]

df_db = pd.DataFrame(st.session_state.db_data)

# Helper function for Dynamic Multi-Tier Classification
def get_target_tier(employees):
    if employees >= 50000:
        return "Tier 1 - Strategic Enterprise (Global)"
    elif employees >= 5000:
        return "Tier 1 - Enterprise"
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
    st.markdown("**Stratix Console v3.0**<br>Enterprise GTM Infrastructure", unsafe_allow_html=True)

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
        search_query = st.text_input("🔍 Enterprise Search Engine:", placeholder="Type any company (e.g. Siemens, DHL, E.ON, Airbus, Vonovia)...")
    with col_s2:
        industry_options = ["All Industries"] + sorted(df_db["Industry"].unique().tolist())
        selected_industry = st.selectbox("Filter Directory by Sector", industry_options)
    
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

    # PROFESSIONAL ERROR HANDLING (Simulated Live API Lookup State)
    if not is_from_db:
        with st.spinner(f"🌐 Querying global firmographic database for '{search_query}'..."):
            time.sleep(0.6) # Simulating API network latency
        
        st.warning(f"⚠️ **Exact match not found in local index for '{search_query}'.** Dynamically synthesized a synthetic enterprise profile below based on sector heuristics.")
        
        matched_account = {
            "Company": search_query.strip().title(),
            "Domain": f"{search_query.strip().lower().replace(' ', '')}.de",
            "Industry": selected_industry if selected_industry != "All Industries" else "Manufacturing & Industrial",
            "Employees": 3500,
            "Current_MDM": "Microsoft Intune",
            "Device_Density": global_density_modifier,
            "Legacy_Lockin": True,
            "Estimated_Contract_Value": "€140,000/yr",
            "Optimal_Strategy": "Automated Fleet Migration (AFM) via BARB & Zero-Touch Deployment",
            "Partner_Stack": "Samsung / T-Mobile"
        }

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

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_strat1, col_strat2 = st.columns(2)
    with col_strat1:
        st.markdown(f"""
            <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%; box-shadow: 0 4px 12px rgba(0,7,93,0.04);">
                <h3 style="margin-top: 0px; margin-bottom: 15px; font-size: 20px !important;">Recommended GTM Strategy</h3>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Optimal Framework:</b><br>{matched_account['Optimal_Strategy']}</p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Corporate Domain:</b> <code>{matched_account['Domain']}</code></p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Current MDM Integration:</b> <code>{matched_account['Current_MDM']}</code></p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Hardware Lock-in Status:</b> <code>{'Yes — BARB Eligible (CapEx Relief)' if matched_account['Legacy_Lockin'] else 'No — Standard DaaS/CYOD'}</code></p>
                <p style="margin-bottom: 0px; font-size: 18px !important;"><b>Ecosystem Partner Stack:</b> <code>{matched_account['Partner_Stack']}</code></p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_strat2:
        st.markdown(f"""
            <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%; box-shadow: 0 4px 12px rgba(0,7,93,0.04);">
                <h3 style="margin-top: 0px; margin-bottom: 15px; font-size: 20px !important;">Tailored B2B Sales Outreach Email</h3>
        """, unsafe_allow_html=True)
        
        realistic_pitch = (
            f"Subject: Streamlining corporate mobile lifecycle at {matched_account['Company']}\n\n"
            f"Hi [First Name],\n\n"
            f"Managing a mobile fleet of ~{calculated_fleet} devices integrated with {matched_account['Current_MDM']} "
            f"often creates heavy administrative overhead for IT teams—from procurement and staging to handling device swaps and secure end-of-life data erasure.\n\n"
            f"Our Device-as-a-Service (DaaS) platform helps enterprise IT leaders transition smoothly. "
            f"Given your infrastructure, utilizing our **{matched_account['Optimal_Strategy']}** allows {matched_account['Company']} "
            f"to unlock immediate balance sheet relief (via Buy-and-Rent-Back) while guaranteeing zero-downtime migration.\n\n"
            f"Would you be open to a brief 10-minute introductory call next Tuesday to review a custom fleet migration blueprint?\n\n"
            f"Best regards,\n"
            f"[Your Name] | Enterprise Business Development"
        )
        st.code(realistic_pitch, language="text")
        
        st.download_button(
            label="Download Pitch as Text File",
            data=realistic_pitch,
            file_name=f"{matched_account['Company'].lower().replace(' ', '_')}_pitch.txt",
            mime="text/plain"
        )
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Master Enterprise Database & CRM Ingestion")
    
    col_db_metrics1, col_db_metrics2 = st.columns(2)
    with col_db_metrics1:
        st.metric("Total Indexed Accounts", len(df_db))
    with col_db_metrics2:
        st.metric("Sectors Covered", df_db["Industry"].nunique())
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Salesforce / HubSpot CRM Export Ingestion")
    uploaded_file = st.file_uploader("Drop your CRM account export (.csv or .xlsx) here", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                upload_df = pd.read_csv(uploaded_file)
            else:
                upload_df = pd.read_excel(uploaded_file)
            
            if 'Company' in upload_df.columns:
                for _, row in upload_df.iterrows():
                    new_rec = {
                        "Company": str(row.get('Company', 'Unknown')),
                        "Domain": str(row.get('Domain', 'company.de')),
                        "Industry": str(row.get('Industry', 'Enterprise')),
                        "Employees": int(row.get('Employees', 1000)),
                        "Current_MDM": str(row.get('Current_MDM', 'Microsoft Intune')),
                        "Device_Density": 0.50,
                        "Legacy_Lockin": True,
                        "Estimated_Contract_Value": "€100,000/yr",
                        "Optimal_Strategy": "Automated Fleet Migration (AFM) via BARB",
                        "Partner_Stack": "Samsung / T-Mobile"
                    }
                    if not any(d['Company'].lower() == new_rec['Company'].lower() for d in st.session_state.db_data):
                        st.session_state.db_data.append(new_rec)
                st.success(f"Successfully processed CRM batch export from `{uploaded_file.name}`!")
            else:
                st.error("Uploaded file must contain a 'Company' column.")
        except Exception as e:
            st.error(f"Error processing file: {e}")

    db_search = st.text_input("Search Database table", "")
    display_df = df_db[df_db['Company'].str.contains(db_search, case=False)] if db_search else df_db
    st.dataframe(display_df, use_container_width=True)
    
    csv_data = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Pipeline Database as CSV",
        data=csv_data,
        file_name="stratix_pipeline_export.csv",
        mime="text/csv"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Pipeline Analytics by Industry Sector")
    industry_summary = df_db.groupby("Industry")["Employees"].sum().reset_index()
    st.bar_chart(industry_summary.set_index("Industry"))
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Append Single Target Account")
    with st.form("add_account_form"):
        c_name = st.text_input("Company Name")
        c_dom = st.text_input("Domain")
        c_ind = st.selectbox("Industry Sector", sorted(df_db["Industry"].unique().tolist()))
        c_emp = st.number_input("Employees", min_value=10, value=1500)
        c_mdm = st.selectbox("MDM Tool", ["Microsoft Intune", "MobileIron / Ivanti", "Jamf", "Mobile Device Manager Plus"])
        submitted = st.form_submit_button("Index Account to Pipeline Database")
        if submitted and c_name:
            new_record = {
                "Company": c_name, "Domain": c_dom if c_dom else f"{c_name.lower().replace(' ', '')}.de",
                "Industry": c_ind, "Employees": c_emp, "Current_MDM": c_mdm, "Device_Density": 0.50,
                "Legacy_Lockin": True, "Estimated_Contract_Value": f"€{int(c_emp * 40):,}/yr",
                "Optimal_Strategy": "Automated Fleet Migration (AFM) via BARB", "Partner_Stack": "Samsung / T-Mobile"
            }
            st.session_state.db_data.append(new_record)
            st.success(f"Successfully recorded {c_name} into pipeline database.")

with tab3:
    st.subheader("Enterprise Ecosystem & Strategic Playbooks")
    st.markdown("Select a hardware or security partner ecosystem below to view specific channel margins, integration specs, and co-selling frameworks.")
    
    selected_partner = st.selectbox(
        "Select Ecosystem Partner",
        ["Samsung Knox & Enterprise", "Apple iOS & DEP Deployment", "Zebra Technologies (Ruggedized)", "Microsoft Surface & Intune Stack"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    
    if selected_partner == "Samsung Knox & Enterprise":
        with col_p1:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Knox Integration & Staging</h3>
                    <p><b>Deployment Method:</b> Knox Mobile Enrollment (KME)</p>
                    <p><b>Security Tier:</b> Hardware-backed root of trust with Knox Guard isolation.</p>
                    <p><b>Target Vertical:</b> Manufacturing, Logistics, Field Healthcare.</p>
                </div>
            """, unsafe_allow_html=True)
        with col_p2:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Commercial & Channel Incentives</h3>
                    <p><b>Partner Margin Tier:</b> Tier 1 Authorized DaaS Distributor</p>
                    <p><b>Buy-and-Rent-Back Eligibility:</b> Full residual value guarantee on Galaxy Enterprise Editions.</p>
                    <p><b>Data Wipe Certification:</b> Integrated Blancco automated audit logging.</p>
                </div>
            """, unsafe_allow_html=True)
            
    elif selected_partner == "Apple iOS & DEP Deployment":
        with col_p1:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Apple Ecosystem & DEP Setup</h3>
                    <p><b>Deployment Method:</b> Automated Device Enrollment via Apple Business Manager (ABM).</p>
                    <p><b>Security Tier:</b> Supervised mode, mandatory MDM profile retention.</p>
                    <p><b>Target Vertical:</b> Finance, Tech/SaaS, Professional Services.</p>
                </div>
            """, unsafe_allow_html=True)
        with col_p2:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Commercial & Channel Incentives</h3>
                    <p><b>Partner Margin Tier:</b> Apple Authorized Enterprise Reseller (AAER)</p>
                    <p><b>Buy-and-Rent-Back Eligibility:</b> High resale valuation retention across iPhone & iPad Pro portfolios.</p>
                    <p><b>Lifecycle Option:</b> 24-month upgrade cycles with zero-touch swap logistics.</p>
                </div>
            """, unsafe_allow_html=True)
            
    elif selected_partner == "Zebra Technologies (Ruggedized)":
        with col_p1:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Ruggedized Handheld Staging</h3>
                    <p><b>Deployment Method:</b> StageNow Enterprise Barcode Provisioning.</p>
                    <p><b>Security Tier:</b> Enterprise Mobility Security Suite with LifeGuard OTA updates.</p>
                    <p><b>Target Vertical:</b> Warehousing, Freight Logistics, Omnichannel Retail.</p>
                </div>
            """, unsafe_allow_html=True)
        with col_p2:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Commercial & Channel Incentives</h3>
                    <p><b>Partner Margin Tier:</b> Zebra Premier Solution Partner</p>
                    <p><b>Buy-and-Rent-Back Eligibility:</b> Heavy-duty asset lifecycle structuring for multi-year warehouse contracts.</p>
                    <p><b>Swap Logistics:</b> 24-hour advance replacement SLA for broken barcode terminals.</p>
                </div>
            """, unsafe_allow_html=True)
            
    else:
        with col_p1:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Microsoft Surface & Intune Integration</h3>
                    <p><b>Deployment Method:</b> Windows Autopilot native cloud enrollment.</p>
                    <p><b>Security Tier:</b> Microsoft Entra ID (Azure AD) conditional access policies.</p>
                    <p><b>Target Vertical:</b> Corporate Headquarters, Public Sector, Enterprise IT.</p>
                </div>
            """, unsafe_allow_html=True)
        with col_p2:
            st.markdown("""
                <div style="background-color: white; padding: 24px; border-radius: 10px; border: 1px solid #e2e8f0; border-top: 4px solid #00075D; height: 100%;">
                    <h3>Commercial & Channel Incentives</h3>
                    <p><b>Partner Margin Tier:</b> Microsoft Cloud Solution Provider (CSP)</p>
                    <p><b>Buy-and-Rent-Back Eligibility:</b> Balance sheet capitalization relief for laptop & tablet fleets.</p>
                    <p><b>Compliance:</b> ISO 27001 & BSI-compliant secure workspace provisioning.</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    partner_playbook_text = (
        f"STRATIX PARTNER ECOSYSTEM PLAYBOOK\n"
        f"Ecosystem Focus: {selected_partner}\n"
        f"Compliance Framework: ISO 27001 Certified, GDPR & NIS-2 Compliant, Blancco Data Erasure Audit Trail."
    )
    st.download_button(
        label="Download Selected Partner Playbook (.txt)",
        data=partner_playbook_text,
        file_name=f"{selected_partner.lower().replace(' ', '_')}_playbook.txt",
        mime="text/plain"
    )
