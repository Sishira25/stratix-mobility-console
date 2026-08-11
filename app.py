import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Stratix | Enterprise Mobility & GTM Intelligence Console",
    page_icon="⚡",
    layout="wide"
)

# Custom Styling with Dark Midnight Banner and Complementary Muted, Sophisticated Tones
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    
    /* Global Base Font Override - 18px for Maximum Readability */
    html, body, [class*="css"] {
        font-size: 18px !important;
        color: #1e293b !important;
    }
    
    /* Custom Header Banner Styling matching the exact midnight blue gradient */
    .stratix-header {
        background: linear-gradient(135deg, #070e1c 0%, #0b1736 50%, #061129 100%);
        padding: 2.5rem 3rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(7, 14, 28, 0.35);
        border-left: 6px solid #334155;
        border-top: 1px solid rgba(51, 65, 85, 0.3);
        border-right: 1px solid rgba(51, 65, 85, 0.3);
        border-bottom: 1px solid rgba(51, 65, 85, 0.3);
    }
    .stratix-header h1 { 
        color: #ffffff !important; 
        font-size: 36px !important; 
        font-weight: 700 !important; 
        margin-bottom: 8px !important; 
    }
    .stratix-header p { 
        color: #94a3b8 !important; 
        font-size: 19px !important; 
        margin: 0px !important; 
    }
    
    /* Section & Subheader Scaling */
    h2 { font-size: 24px !important; color: #0f172a !important; font-weight: 700; margin-top: 1.2rem; }
    h3 { font-size: 20px !important; color: #0f172a !important; font-weight: 700; }
    
    /* Form Labels and Inputs */
    label, .stTextInput label, .stSelectbox label, .stNumberInput label, .stFileUploader label {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #0f172a !important;
    }
    input, select, div[data-baseweb="select"] span {
        font-size: 18px !important;
    }
    
    /* Complementary Slate-Navy Action Buttons */
    .stButton>button {
        background-color: #1e293b !important; 
        color: white !important; 
        border-radius: 6px; 
        font-weight: 600; 
        font-size: 18px !important;
        border: none; 
        padding: 0.8rem 1.4rem; 
        width: 100%; 
        box-shadow: 0 2px 4px rgba(30,41,59,0.2);
    }
    .stButton>button:hover { 
        background-color: #0f172a !important; 
        color: white !important; 
    }
    
    /* Metric Cards Overhaul with Slate Accent */
    div[data-testid="stMetric"] {
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 8px; 
        border: 1px solid #e2e8f0; 
        border-top: 4px solid #334155; 
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    div[data-testid="stMetricLabel"] { font-size: 16px !important; color: #64748b !important; font-weight: 600 !important; }
    div[data-testid="stMetricValue"] { font-size: 28px !important; color: #0f172a !important; font-weight: 700 !important; }

    /* Tab Label Typography with Subtle Slate Accent */
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #1e293b !important; 
        border-bottom-color: #1e293b !important; 
        font-weight: 700;
        font-size: 18px !important;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #475569 !important;
    }
    
    /* Dataframe Table Text Scaling */
    div[data-testid="stDataFrame"] {
        font-size: 17px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- EXPANDED MASTER DATABASE (32 Enterprise Accounts Across All Sectors) ---
if 'db_data' not in st.session_state:
    st.session_state.db_data = [
        # Logistics
        {"Company": "Global Logistics GmbH", "Domain": "global-logistics.de", "Industry": "Logistics", "Employees": 4500, "Current_MDM": "Microsoft Intune", "Device_Density": 0.45, "Legacy_Lockin": True, "Estimated_Contract_Value": "€180,000/yr", "Optimal_Strategy": "Buy-and-Rent-Back (BARB) + Frontline Staging", "Partner_Stack": "Samsung / T-Mobile"},
        {"Company": "Hamburg Maritime Freight", "Domain": "hamburg-freight.de", "Industry": "Logistics", "Employees": 2800, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.50, "Legacy_Lockin": False, "Estimated_Contract_Value": "€115,000/yr", "Optimal_Strategy": "DaaS Deployment with Multi-Carrier SIMs", "Partner_Stack": "Verizon / Samsung"},
        {"Company": "Baden-Württemberg Logistics", "Domain": "bw-logistics.de", "Industry": "Logistics", "Employees": 5100, "Current_MDM": "Microsoft Intune", "Device_Density": 0.45, "Legacy_Lockin": True, "Estimated_Contract_Value": "€210,000/yr", "Optimal_Strategy": "Mass Fleet Modernization via BARB & 1-Day Swap", "Partner_Stack": "T-Mobile / Samsung"},
        {"Company": "Bremen Shipping Logistics", "Domain": "bremen-shipping.de", "Industry": "Logistics", "Employees": 3900, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.50, "Legacy_Lockin": True, "Estimated_Contract_Value": "€160,000/yr", "Optimal_Strategy": "Port Operations Fleet Replacement via BARB", "Partner_Stack": "Zebra / T-Mobile"},
        
        # Finance
        {"Company": "Bavaria Finance AG", "Domain": "bavaria-finance.de", "Industry": "Finance", "Employees": 1200, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.70, "Legacy_Lockin": False, "Estimated_Contract_Value": "€95,000/yr", "Optimal_Strategy": "Choose-Your-Own-Device (CYOD) + MTD", "Partner_Stack": "Apple / Microsoft"},
        {"Company": "Frankfurt Capital Partners", "Domain": "frankfurt-capital.de", "Industry": "Finance", "Employees": 890, "Current_MDM": "Jamf", "Device_Density": 0.80, "Legacy_Lockin": False, "Estimated_Contract_Value": "€85,000/yr", "Optimal_Strategy": "Executive CYOD Premium Tier Setup", "Partner_Stack": "Apple / Microsoft"},
        {"Company": "Rhein Main Asset Management", "Domain": "rhein-asset.de", "Industry": "Finance", "Employees": 640, "Current_MDM": "Microsoft Intune", "Device_Density": 0.75, "Legacy_Lockin": False, "Estimated_Contract_Value": "€55,000/yr", "Optimal_Strategy": "Secure Mobile Enclave with Intune Integration", "Partner_Stack": "Apple / Vodafone"},
        
        # Manufacturing
        {"Company": "Rhein-Ruhr Manufacturing SE", "Domain": "rhein-ruhr-mfg.de", "Industry": "Manufacturing", "Employees": 8500, "Current_MDM": "Jamf", "Device_Density": 0.30, "Legacy_Lockin": True, "Estimated_Contract_Value": "€240,000/yr", "Optimal_Strategy": "Ruggedized DaaS Fleet Modernization via BARB", "Partner_Stack": "Lenovo / Samsung Knox"},
        {"Company": "Stuttgart Automotive Solutions", "Domain": "stuttgart-auto.de", "Industry": "Manufacturing", "Employees": 11000, "Current_MDM": "Microsoft Intune", "Device_Density": 0.25, "Legacy_Lockin": True, "Estimated_Contract_Value": "€310,000/yr", "Optimal_Strategy": "Enterprise-Scale BARB Rollout + Blancco Erasure", "Partner_Stack": "HP / Microsoft"},
        {"Company": "Saxon Precision Engineering", "Domain": "saxon-precision.de", "Industry": "Manufacturing", "Employees": 1850, "Current_MDM": "Mobile Device Manager Plus", "Device_Density": 0.30, "Legacy_Lockin": False, "Estimated_Contract_Value": "€70,000/yr", "Optimal_Strategy": "Standard DaaS Lifecycle Management", "Partner_Stack": "Samsung / Android Enterprise"},
        {"Company": "Hannover AgriTech SE", "Domain": "hannover-agritech.de", "Industry": "Manufacturing", "Employees": 1600, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€65,000/yr", "Optimal_Strategy": "Field-Worker Device Modernization via BARB", "Partner_Stack": "Samsung / Vodafone"},
        {"Company": "Westphalia Steel Works", "Domain": "westphalia-steel.de", "Industry": "Manufacturing", "Employees": 4300, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.28, "Legacy_Lockin": True, "Estimated_Contract_Value": "€140,000/yr", "Optimal_Strategy": "Heavy-Duty Ruggedized DaaS Exchange", "Partner_Stack": "Zebra / T-Mobile"},

        # Healthcare
        {"Company": "Berlin HealthTech Labs", "Domain": "berlin-healthtech.de", "Industry": "Healthcare", "Employees": 650, "Current_MDM": "Microsoft Intune", "Device_Density": 0.55, "Legacy_Lockin": False, "Estimated_Contract_Value": "€45,000/yr", "Optimal_Strategy": "DSGVO-Compliant DaaS with Data Partitioning", "Partner_Stack": "Samsung / Android Enterprise"},
        {"Company": "Munich Pharma Group", "Domain": "munich-pharma.de", "Industry": "Healthcare", "Employees": 6200, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.40, "Legacy_Lockin": True, "Estimated_Contract_Value": "€195,000/yr", "Optimal_Strategy": "NIS-2 Compliant Secure Fleet Migration via BARB", "Partner_Stack": "Samsung Knox / T-Mobile"},
        {"Company": "Charité Clinical Research", "Domain": "charite-research.de", "Industry": "Healthcare", "Employees": 2100, "Current_MDM": "Microsoft Intune", "Device_Density": 0.50, "Legacy_Lockin": False, "Estimated_Contract_Value": "€90,000/yr", "Optimal_Strategy": "HIPAA/GDPR Compliant Clinical Tablet Rollout", "Partner_Stack": "Apple / Vodafone"},

        # Retail
        {"Company": "Nordic Retail Group", "Domain": "nordic-retail.de", "Industry": "Retail", "Employees": 3200, "Current_MDM": "Mobile Device Manager Plus", "Device_Density": 0.60, "Legacy_Lockin": True, "Estimated_Contract_Value": "€130,000/yr", "Optimal_Strategy": "BARB Migration for POS Terminals & Scanners", "Partner_Stack": "Zebra / Samsung"},
        {"Company": "Bavarian Department Stores", "Domain": "bavaria-retail.de", "Industry": "Retail", "Employees": 5400, "Current_MDM": "Microsoft Intune", "Device_Density": 0.55, "Legacy_Lockin": True, "Estimated_Contract_Value": "€200,000/yr", "Optimal_Strategy": "Omnichannel POS & Handheld Fleet Upgrade", "Partner_Stack": "Samsung / O2"},

        # Tech / SaaS
        {"Company": "Cologne Media Systems", "Domain": "cologne-media.de", "Industry": "Tech/SaaS", "Employees": 540, "Current_MDM": "Microsoft Intune", "Device_Density": 0.90, "Legacy_Lockin": False, "Estimated_Contract_Value": "€60,000/yr", "Optimal_Strategy": "Flexible DaaS Scaling for Remote Teams", "Partner_Stack": "Lenovo / Apple"},
        {"Company": "Leipzig Web Solutions", "Domain": "leipzig-web.de", "Industry": "Tech/SaaS", "Employees": 420, "Current_MDM": "None", "Device_Density": 0.95, "Legacy_Lockin": False, "Estimated_Contract_Value": "€40,000/yr", "Optimal_Strategy": "Instant Onboarding DaaS for Engineering Teams", "Partner_Stack": "Apple / Lenovo"},
        {"Company": "Berlin Cloud Systems", "Domain": "berlin-cloud.de", "Industry": "Tech/SaaS", "Employees": 980, "Current_MDM": "Jamf", "Device_Density": 0.85, "Legacy_Lockin": False, "Estimated_Contract_Value": "€95,000/yr", "Optimal_Strategy": "Zero-Touch Deployment via Apple DEP & DaaS", "Partner_Stack": "Apple / AWS"},

        # Energy & Utilities
        {"Company": "Ruhr Valley Energy", "Domain": "ruhr-energy.de", "Industry": "Energy/Utilities", "Employees": 4100, "Current_MDM": "Microsoft Intune", "Device_Density": 0.35, "Legacy_Lockin": True, "Estimated_Contract_Value": "€150,000/yr", "Optimal_Strategy": "Critical Infrastructure DaaS & Swap Logistics", "Partner_Stack": "Dell / Microsoft"},
        {"Company": "NordGrid Power AG", "Domain": "nordgrid.de", "Industry": "Energy/Utilities", "Employees": 2900, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.38, "Legacy_Lockin": True, "Estimated_Contract_Value": "€110,000/yr", "Optimal_Strategy": "Field-Technician Secure Device Lifecycle Management", "Partner_Stack": "Samsung / T-Mobile"},

        # Professional Services
        {"Company": "Düsseldorf Consulting Group", "Domain": "duesseldorf-consult.de", "Industry": "Professional Services", "Employees": 2400, "Current_MDM": "Jamf", "Device_Density": 0.75, "Legacy_Lockin": False, "Estimated_Contract_Value": "€110,000/yr", "Optimal_Strategy": "CYOD Program Design with Integrated MTD", "Partner_Stack": "Apple / Microsoft Surface"},
        {"Company": "Hanseatic Advisory Partners", "Domain": "hanseatic-advisory.de", "Industry": "Professional Services", "Employees": 1150, "Current_MDM": "Microsoft Intune", "Device_Density": 0.80, "Legacy_Lockin": False, "Estimated_Contract_Value": "€75,000/yr", "Optimal_Strategy": "Executive Mobile Security & Rapid Replacement", "Partner_Stack": "Apple / Microsoft"},

        # Public Sector
        {"Company": "Federal Digital Agency (Mock)", "Domain": "bund-digital.de", "Industry": "Public Sector", "Employees": 3500, "Current_MDM": "Microsoft Intune", "Device_Density": 0.60, "Legacy_Lockin": False, "Estimated_Contract_Value": "€125,000/yr", "Optimal_Strategy": "BSI-Compliant Secure Government Mobility Framework", "Partner_Stack": "Samsung Knox / T-Mobile"},
        
        # Telecommunications
        {"Company": "Alps Telecom Solutions", "Domain": "alps-telecom.de", "Industry": "Telecommunications", "Employees": 4800, "Current_MDM": "MobileIron / Ivanti", "Device_Density": 0.70, "Legacy_Lockin": False, "Estimated_Contract_Value": "€190,000/yr", "Optimal_Strategy": "Carrier-Integrated DaaS Tiered Deployment", "Partner_Stack": "Ericsson / Samsung"}
    ]

df_db = pd.DataFrame(st.session_state.db_data)

# Header Banner with the custom midnight blue styling
st.markdown("""
    <div class="stratix-header">
        <h1>⚡ Stratix</h1>
        <p>Enterprise Mobility & GTM Intelligence Console</p>
    </div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Account Intelligence & Outreach", "📊 Master Database & CRM Upload", "⚙️ Partner Ecosystem & Strategy"])

with tab1:
    st.subheader("Target Account Pipeline & Instant Lookup")
    
    search_input = st.text_input("🔍 Type any target company name (e.g., 'Siemens', 'Adidas'):", "")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        selected_industry = st.selectbox("Filter by Industry Vertical", ["All"] + sorted(df_db["Industry"].unique().tolist()))
    
    filtered_df = df_db if selected_industry == "All" else df_db[df_db["Industry"] == selected_industry]
    
    with col_f2:
        selected_company = st.selectbox("Or Select Enterprise from Database", filtered_df["Company"].tolist())
    
    target_name = search_input.strip() if search_input else selected_company
    
    match = df_db[df_db["Company"].str.lower() == target_name.lower()]
    
    if not match.empty:
        account_row = match.iloc[0]
    else:
        account_row = {
            "Company": target_name,
            "Domain": f"{target_name.lower().replace(' ', '')}.de",
            "Industry": selected_industry if selected_industry != "All" else "Manufacturing/Enterprise",
            "Employees": 2500,
            "Current_MDM": "Microsoft Intune",
            "Device_Density": 0.50,
            "Legacy_Lockin": True,
            "Estimated_Contract_Value": "€120,000/yr",
            "Optimal_Strategy": "Automated Fleet Migration (AFM) via BARB & Zero-Touch Deployment",
            "Partner_Stack": "Samsung / T-Mobile"
        }
    
    st.markdown("<br>", unsafe_allow_html=True)
    calculated_fleet = int(account_row["Employees"] * account_row["Device_Density"])
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric("Total Headcount", f"{account_row['Employees']:,}")
    with col_m2:
        st.metric("Estimated Mobile Fleet", f"{calculated_fleet:,} Devices")
    with col_m3:
        st.metric("Target Tier", "Enterprise (Tier 1)" if calculated_fleet >= 500 else "SMB")
    with col_m4:
        st.metric("Est. Annual Contract Value", account_row["Estimated_Contract_Value"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_strat1, col_strat2 = st.columns(2)
    with col_strat1:
        st.markdown(f"""
            <div style="background-color: white; padding: 24px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #1e293b; height: 100%;">
                <h3 style="margin-top: 0px; margin-bottom: 15px; font-size: 20px !important;">🎯 Recommended GTM Strategy</h3>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Optimal Framework:</b><br>{account_row['Optimal_Strategy']}</p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Corporate Domain:</b> <code>{account_row['Domain']}</code></p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Current MDM Integration:</b> <code>{account_row['Current_MDM']}</code></p>
                <p style="margin-bottom: 14px; font-size: 18px !important;"><b>Hardware Lock-in Status:</b> <code>{'Yes — BARB Eligible (CapEx Relief)' if account_row['Legacy_Lockin'] else 'No — Standard DaaS/CYOD'}</code></p>
                <p style="margin-bottom: 0px; font-size: 18px !important;"><b>Ecosystem Partner Stack:</b> <code>{account_row['Partner_Stack']}</code></p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_strat2:
        st.markdown(f"""
            <div style="background-color: white; padding: 24px; border-radius: 8px; border: 1px solid #e2e8f0; border-top: 4px solid #1e293b; height: 100%;">
                <h3 style="margin-top: 0px; margin-bottom: 15px; font-size: 20px !important;">✉️ Tailored B2B Sales Outreach Email</h3>
        """, unsafe_allow_html=True)
        
        realistic_pitch = (
            f"Subject: Streamlining corporate mobile lifecycle at {account_row['Company']}\n\n"
            f"Hi [First Name],\n\n"
            f"Managing a mobile fleet of ~{calculated_fleet} devices integrated with {account_row['Current_MDM']} "
            f"often creates heavy administrative overhead for IT teams—from procurement and staging to handling device swaps and secure end-of-life data erasure.\n\n"
            f"Our Device-as-a-Service (DaaS) platform helps enterprise IT leaders transition smoothly. "
            f"Given your infrastructure, utilizing our **{account_row['Optimal_Strategy']}** allows {account_row['Company']} "
            f"to unlock immediate balance sheet relief (via Buy-and-Rent-Back) while guaranteeing zero-downtime migration.\n\n"
            f"Would you be open to a brief 10-minute introductory call next Tuesday to review a custom fleet migration blueprint?\n\n"
            f"Best regards,\n"
            f"[Your Name] | Enterprise Business Development"
        )
        st.code(realistic_pitch, language="text")
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("🗄️ Master Enterprise Database & CRM Ingestion")
    
    st.markdown("### 📁 Salesforce / HubSpot CRM Export Ingestion")
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
    
    st.markdown("### ➕ Append Single Target Account")
    with st.form("add_account_form"):
        c_name = st.text_input("Company Name")
        c_dom = st.text_input("Domain")
        c_ind = st.selectbox("Industry", ["Logistics", "Finance", "Manufacturing", "Healthcare", "Retail", "Tech/SaaS", "Energy/Utilities", "Professional Services", "Public Sector", "Telecommunications"])
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
    st.subheader("⚙️ Enterprise Ecosystem & Strategic Parameters")
    eco1, eco2 = st.columns(2)
    with eco1:
        st.markdown("**Supported Hardware Partners:**\n- Samsung Knox\n- Apple iOS Enterprise\n- Lenovo & Microsoft Surface")
    with eco2:
        st.markdown("**Compliance & Security Standards:**\n- ISO 27001 Certified\n- GDPR & NIS-2 Compliant\n- Blancco Data Erasure Audit Trail")
