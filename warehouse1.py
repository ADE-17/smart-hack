import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize data storage
if 'warehouse_data' not in st.session_state:
    st.session_state['warehouse_data'] = pd.DataFrame(columns=['Wine Name', 'Quantity', 'Quality', 'Selling Price', 'Export Charges'])

st.set_page_config(page_title="Wine Marketplace", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["Add Wine", "Manage Export & Delivery", "Marketing & Promotion", "Dashboard"])

# 1. Add Wine to Virtual Warehouse
if menu == "Add Wine":
    st.title("Add Wine to Virtual Warehouse")

    with st.form("wine_form"):
        wine_name = st.text_input("Wine Name")
        quantity = st.number_input("Quantity", min_value=0)
        quality = st.selectbox("Quality", ["Standard", "Premium", "Luxury"])
        selling_price = st.number_input("Selling Price (USD)", min_value=0.0)
        export_charge = st.number_input("Export Charge (USD)", min_value=0.0)

        uploaded_image = st.file_uploader("Upload Wine Image", type=['png', 'jpg', 'jpeg'])

        submitted = st.form_submit_button("Add Wine")

        if submitted:
            new_wine = {
                "Wine Name": wine_name,
                "Quantity": quantity,
                "Quality": quality,
                "Selling Price": selling_price,
                "Export Charges": export_charge
            }
            st.session_state['warehouse_data'] = st.session_state['warehouse_data'].append(new_wine, ignore_index=True)
            st.success(f"{wine_name} added to warehouse!")

# 2. Manage Export & Delivery
elif menu == "Manage Export & Delivery":
    st.title("Manage Export & Delivery")

    if not st.session_state['warehouse_data'].empty:
        st.dataframe(st.session_state['warehouse_data'])

        destination = st.selectbox("Select Destination", ["Domestic", "International"])
        if destination == "International":
            st.info("Note: International deliveries may incur extra taxes and packaging charges.")
            extra_charge = st.number_input("Enter Extra Charge (USD)", min_value=0.0)

# 3. Marketing & Promotion
elif menu == "Marketing & Promotion":
    st.title("Marketing & Promotion")

    st.subheader("Promote Wine via Ads")
    st.write("You can create Google Ads campaigns or share on social media platforms directly.")
    st.button("Create Google Ads Campaign")
    st.button("Share on Social Media")

    st.subheader("Collaborate with Influencers")
    st.write("Connect with influencers or wine reviewers for endorsements.")
    influencers = ["@wine_expert", "@tastingshow", "@luxury_wines"]
    selected_influencer = st.selectbox("Choose Influencer", influencers)
    st.button(f"Contact {selected_influencer}")

    st.write("Or collaborate with wine podcasts:")
    podcasts = ["Wine Talks", "Grape Expectations", "The Vintner's Voice"]
    selected_podcast = st.selectbox("Choose Podcast", podcasts)
    st.button(f"Contact {selected_podcast}")

# 4. Dashboard
elif menu == "Dashboard":
    st.title("Warehouse Dashboard")

    if not st.session_state['warehouse_data'].empty:
        # Display metrics
        total_profit = st.session_state['warehouse_data']['Selling Price'].sum()
        total_orders = len(st.session_state['warehouse_data'])

        col1, col2 = st.columns(2)
        col1.metric("Total Profit (USD)", f"${total_profit}")
        col2.metric("Total Orders", total_orders)

        # World Map Visualization
        st.subheader("Order Distribution")
        # Placeholder: Generate sample order locations for map visualization
        sample_locations = pd.DataFrame({
            'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
            'Latitude': [40.7128, 51.5074, 35.6895, 48.8566, -33.8688],
            'Longitude': [-74.0060, -0.1278, 139.6917, 2.3522, 151.2093]
        })
        fig = px.scatter_geo(sample_locations, lat='Latitude', lon='Longitude', text='City', title="Global Order Distribution")
        st.plotly_chart(fig)
