import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Stratix | Enterprise Mobility & GTM Intelligence Console",
    page_icon="📱",
    layout="wide"
)

# Custom Styling: Enterprise Sidebar, Dark Navy Blue (#00075D) Theme
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
        font-size: 18px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1.5rem !important;
    }
    .stButton>button:hover {
        background-color: #00128a !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header Banner
st.markdown("""
    <div class="stratix-header">
        <h1>Stratix | Enterprise Mobility & GTM Intelligence Console</h1>
        <p>B2B Account Intelligence, Device Fleet Evaluation & BARB Financial Transition Engine</p>
    </div>
""", unsafe_allow_html=True)

# Comprehensive Mock Database with UNIQUE Headcounts, Sectors, and Tech Stacks
@st.cache_data
def load_company_database():
    return pd.DataFrame([
        {
            "Company Name": "LogiTrans Berlin GmbH", 
            "Sector": "Logistics & Supply Chain", 
            "Headcount": 1250, 
            "Target Tier": "Tier 1 - Strategic Enterprise", 
            "Current MDM": "Microsoft Intune", 
            "Renewal Cycle": "Q4 2026",
            "Region": "Berlin, Germany"
        },
        {
            "Company Name": "Bavaria Logistics & Co.", 
            "Sector": "Logistics & Supply Chain", 
            "Headcount": 450, 
            "Target Tier": "Tier 2 - Growth Mid-Market", 
            "Current MDM": "MobileIron", 
            "Renewal Cycle": "Q2 2026",
            "Region": "Munich, Germany"
        },
        {
            "Company Name": "FinScale Solutions AG", 
            "Sector": "Financial Technology", 
            "Headcount": 820, 
            "Target Tier": "Tier 1 - Strategic Enterprise", 
            "Current MDM": "Microsoft Intune", 
            "Renewal Cycle": "Q1 2027",
            "Region": "Frankfurt, Germany"
        },
        {
            "Company Name": "HealthCore Digital", 
            "Sector": "Healthcare & Pharma", 
            "Headcount": 2100, 
            "Target Tier": "Tier 1 - Strategic Enterprise", 
            "Current MDM": "Jamf Pro", 
            "Renewal Cycle": "Q3 2026",
            "Region": "Hamburg, Germany"
        },
        {
            "Company Name": "Rhein-Ruhr Manufacturing", 
            "Sector": "Industrial Manufacturing", 
            "Headcount": 3400, 
            "Target Tier": "Tier 1 - Strategic Enterprise", 
            "Current MDM": "SAP Mobile Secure", 
            "Renewal Cycle": "Q4 2026",
            "Region": "Cologne, Germany"
        },
        {
            "Company Name": "Alpha Retail Group", 
            "Sector": "Retail & E-Commerce", 
            "Headcount": 920, 
            "Target Tier": "Tier 2 - Growth Mid-Market", 
            "Current MDM": "None / Legacy", 
            "Renewal Cycle": "Q2 2026",
            "Region": "Stuttgart, Germany"
        }
    ])

df_companies = load_company_database()

# Sidebar Setup with Global Search & Lookup Feature
st.sidebar.header("🔍 Account Lookup & Filters")
search_query = st.sidebar.text_input("Search Company / Database", placeholder="e.g., LogiTrans, FinScale...")

# Filter database based on search input
if search_query:
    filtered_df = df_companies[df_companies['Company Name'].str.contains(search_query, case=False, na=False) | 
                              df_companies['Sector'].str.contains(search_query, case=False, na=False)]
else:
    filtered_df = df_companies

st.sidebar.markdown("---")
selected_company_name = st.sidebar.selectbox("Select Target Account", filtered_df['Company Name'].tolist() if not filtered_df.empty else ["No matching accounts"])

if selected_company_name != "No matching accounts":
    account_data = df_companies[df_companies['Company Name'] == selected_company_name].iloc[0]
else:
    account_data = None

# Main Layout Tabs
tab1, tab2 = st.tabs(["📊 Account Intelligence & Fleet Scoring", "💼 BARB Financial Transition Engine"])

with tab1:
    st.subheader("Enterprise Account Intelligence Console")
    
    if account_data is not None:
        # Display Account Information in Clean Metrics/Cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Headcount", f"{account_data['Headcount']:,} employees")
        with col2:
            st.metric("Industry Sector", account_data['Sector'])
        with col3:
            st.metric("Target Tier", account_data['Target Tier'])
        with col4:
            st.metric("Current MDM Stack", account_data['Current MDM'])
            
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"**Region Location:** {account_data['Region']}")
            st.write(f"**Contract Renewal Cycle:** {account_data['Renewal Cycle']}")
            st.write("**Account Status:** Qualified Prospect for DaaS Rollout")
        with col_b:
            # Dynamic Fleet Estimation based on individual company headcount
            estimated_mobile_fleet = int(account_data['Headcount'] * 0.65)
            st.write(f"**Estimated Mobile Device Fleet (65% ratio):** ~{estimated_mobile_fleet} devices")
            st.write(f"**Integration Compatibility:** Fully compatible with {account_data['Current MDM']}")
            
        st.markdown("---")
        st.info(f"💡 **Recommendation for {selected_company_name}:** Initiate outbound campaign emphasizing automated device staging and seamless integration with {account_data['Current MDM']}.")
    else:
        st.warning("No accounts found matching your search query. Please broaden your search term in the sidebar.")

with tab2:
    st.subheader("Buy-and-Rent-Back (BARB) Financial Value Pitch")
    
    if account_data is not None:
        st.write(f"Calculating CapEx-to-OpEx transition metrics for **{selected_company_name}** based on their workforce of **{account_data['Headcount']:,}** employees.")
        
        # Financial Calculation inputs
        col_x, col_y = st.columns(2)
        with col_x:
            device_replacement_cost = st.number_input("Average Device Cost (€)", value=850, step=50)
        with col_y:
            fleet_ratio = st.slider("Active Fleet Allocation Ratio (%)", min_value=20, max_value=100, value=60)
            
        target_fleet_size = int(account_data['Headcount'] * (fleet_ratio / 100))
        total_capex_relief = target_fleet_size * device_replacement_cost
        estimated_monthly_opex = total_capex_relief * 0.035 # 3.5% monthly DaaS fee model approximation
        
        st.markdown("---")
        
        f1, f2, f3 = st.columns(3)
        with f1:
            st.metric("Calculated Target Fleet", f"{target_fleet_size} units")
        with f2:
            st.metric("Total CapEx Relief (BARB)", f"€{total_capex_relief:,.0f}")
        with f3:
            st.metric("Est. Monthly OpEx Impact", f"€{estimated_monthly_opex:,.2f} / mo")
            
        st.success(f"✅ **Strategic Value Pitch Ready:** By executing a Buy-and-Rent-Back framework for {selected_company_name}, management unlocks €{total_capex_relief:,.0f} in immediate liquidity while transferring device lifecycle and security management overhead to Everphone.")
    else:
        st.warning("Please select a valid company account from the sidebar lookup filter.")
