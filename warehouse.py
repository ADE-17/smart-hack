import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize or load dummy data
if 'warehouse_data' not in st.session_state:
    st.session_state['warehouse_data'] = pd.DataFrame({
        'Wine Name': ['Red Delight', 'White Wonder', 'Rosé Glow'],
        'Quantity': [50, 30, 20],
        'Quality': ['Premium', 'Standard', 'Luxury'],
        'Selling Price': [20, 15, 50],
        'Export Charges': [5, 3, 10],
        'Customer': ['', '', ''],
        'Address': ['', '', ''],
        'Delivery Partner': ['', '', '']
    })

st.set_page_config(page_title="Wine Marketplace", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["Add Wine", "Manage Orders", "Marketing & Promotion", "Dashboard"])

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
            new_wine = pd.DataFrame({
                "Wine Name": [wine_name],
                "Quantity": [quantity],
                "Quality": [quality],
                "Selling Price": [selling_price],
                "Export Charges": [export_charge],
                "Customer": [''],
                "Address": [''],
                "Delivery Partner": ['']
            })
            st.session_state['warehouse_data'] = pd.concat([st.session_state['warehouse_data'], new_wine], ignore_index=True)
            st.success(f"{wine_name} added to warehouse!")

# 2. Manage Orders (Customer Details and Delivery)
elif menu == "Manage Orders":
    st.title("Manage Orders")
    if not st.session_state['warehouse_data'].empty:
        st.dataframe(st.session_state['warehouse_data'])

        st.subheader("Order Details")
        order_idx = st.selectbox("Select an order to update", st.session_state['warehouse_data'].index)
        customer_name = st.text_input("Customer Name", key="customer")
        customer_address = st.text_area("Customer Address", key="address")
        delivery_partner = st.text_input("Delivery Partner Name", key="partner")

        if st.button("Update Order"):
            st.session_state['warehouse_data'].at[order_idx, 'Customer'] = customer_name
            st.session_state['warehouse_data'].at[order_idx, 'Address'] = customer_address
            st.session_state['warehouse_data'].at[order_idx, 'Delivery Partner'] = delivery_partner
            st.success(f"Order updated with customer and delivery details.")

# 3. Marketing & Promotion
elif menu == "Marketing & Promotion":
    st.title("Marketing & Promotion")
    st.subheader("Promote Wine via Ads")
    st.button("Create Google Ads Campaign")
    st.button("Share on Social Media")

    st.subheader("Collaborate with Influencers")
    influencers = ["@wine_expert", "@tastingshow", "@luxury_wines"]
    selected_influencer = st.selectbox("Choose Influencer", influencers)
    st.button(f"Contact {selected_influencer}")

    st.subheader("Collaborate with Podcasts")
    podcasts = ["Wine Talks", "Grape Expectations", "The Vintner's Voice"]
    selected_podcast = st.selectbox("Choose Podcast", podcasts)
    st.button(f"Contact {selected_podcast}")

# 4. Dashboard
elif menu == "Dashboard":
    st.title("Warehouse Dashboard")

    if not st.session_state['warehouse_data'].empty:
        total_profit = st.session_state['warehouse_data']['Selling Price'].sum()
        total_orders = len(st.session_state['warehouse_data'])
        
        col1, col2 = st.columns(2)
        col1.metric("Total Profit (USD)", f"${total_profit}")
        col2.metric("Total Orders", total_orders)

        st.subheader("Order Distribution")

        sample_locations = pd.DataFrame({
            'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
            'Latitude': [40.7128, 51.5074, 35.6895, 48.8566, -33.8688],
            'Longitude': [-74.0060, -0.1278, 139.6917, 2.3522, 151.2093],
            'Orders': [10, 5, 8, 3, 4]
        })

        fig = px.scatter_geo(sample_locations, lat='Latitude', lon='Longitude', text='City', size='Orders',
                             title="Global Order Distribution", projection="natural earth")
        st.plotly_chart(fig)