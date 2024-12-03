import streamlit as st
import pandas as pd
import plotly
import plotly.express as px

# Dummy farmer credentials
FARMER_USERNAME = "farmer1"
FARMER_PASSWORD = "123"

# Dummy Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("Farmer Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == FARMER_USERNAME and password == FARMER_PASSWORD:
            st.session_state['logged_in'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
    st.stop()

st.set_page_config(page_title="WineBridge Marketplace", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["Add Wine", "Manage Orders", "Marketing & Promotion", "Dashboard", "Pricing & Forecasting"])

# Initialize or load dummy data
if 'warehouse_data' not in st.session_state:
    st.session_state['warehouse_data'] = pd.DataFrame({
        'Wine Name': ['Red Delight', 'White Wonder', 'Rosé Glow', 'Cabernet Classic', 'Chardonnay Reserve'],
        'Quantity': [50, 30, 20, 40, 25],
        'Quality': ['Premium', 'Standard', 'Luxury', 'Standard', 'Premium'],
        'Selling Price': [20, 15, 50, 25, 30],
        'Export Charges': [5, 3, 10, 7, 6],
        'Customer': ['', '', '', 'John Doe', 'Jane Smith'],
        'Address': ['', '', '', '123 Vine Street, Napa Valley, CA, USA', '45 Grape Road, Adelaide, Australia'],
        'Delivery Partner': ['', '', '', 'FedEx', 'DHL']
    })


# st.set_page_config(page_title="WineBridge Marketplace", layout="wide")

# # Sidebar navigation
# menu = st.sidebar.radio("Navigation", ["Add Wine", "Manage Orders", "Marketing & Promotion", "Dashboard", "Pricing & Forecasting"])

# 1. Add Wine to Virtual Warehouse
if menu == "Add Wine":
    st.title("Add Wine to Virtual Warehouse")

    with st.form("wine_form"):
        wine_name = st.selectbox("Wine Name", ["Red Delight", "White Wonder", "Rosé Glow", "Riesling", "Gewürztraminer", "Spätburgunder", "Silvaner", "Dornfelder"])
        quantity = st.slider("Quantity", 1, 100, 10)
        quality = st.selectbox("Quality", ["Standard", "Premium", "Luxury"])
        selling_price = st.number_input("Selling Price (EUR)", min_value=0.0)
        export_charge = st.number_input("Export Charge (EUR)", min_value=0.0)
        
        generate_description = st.checkbox("Generate AI Description")
        
        if generate_description:
            description = "A delightful wine with rich flavors and subtle undertones, perfect for any occasion. Known for its smooth finish and aromatic profile. Enjoy this premium selection from the finest vineyards."
        else:
            description = st.text_area("Wine Description")
        
        origin = st.text_input("Wine Origin (Region/Country)")
        alcohol_content = st.number_input("Alcohol Content (%)", min_value=0.0, max_value=100.0)
        uploaded_image = st.file_uploader("Upload Wine Image", type=['png', 'jpg', 'jpeg'])

        submitted = st.form_submit_button("Add Wine")

        if submitted:
            new_wine = pd.DataFrame({
                "Wine Name": [wine_name],
                "Quantity": [quantity],
                "Quality": [quality],
                "Selling Price": [selling_price],
                "Export Charges": [export_charge],
                "Description": [description],
                "Origin": [origin],
                "Alcohol Content": [alcohol_content],
                "Customer": [''],
                "Address": [''],
                "Delivery Partner": ['']
            })
            st.session_state['warehouse_data'] = pd.concat([st.session_state['warehouse_data'], new_wine], ignore_index=True)
            st.success(f"{wine_name} added to warehouse!")


# 2. Manage Orders
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
if menu == "Marketing & Promotion":
    st.title("Marketing & Promotion")

    # Email Marketing with AI-Generated Emails
    st.subheader("Send Personalized AI-Generated Emails")

    with st.form("email_form"):
        subject = st.text_input("Email Subject", value="Exciting News: New Wines in Stock!")
        
        # AI-generated email body based on the subject
        if subject:
            ai_generated_message = f"""
            Dear Valued Customer,

            We are excited to share some great news with you! Our latest selection of wines, including premium and luxury options, is now available on our platform. 
            Whether you are looking for a bold Red Delight or a crisp Chardonnay Reserve, we have something for every palate.

            Visit our marketplace today to explore and enjoy exclusive discounts. Don't miss out on the chance to experience these exquisite flavors from top vineyards worldwide!

            Cheers,
            The WineBridge Team
            """
        else:
            ai_generated_message = "Please enter a subject to generate the email content."

        st.text_area("AI-Generated Email Content", value=ai_generated_message, height=200, disabled=True)

        submitted = st.form_submit_button("Send Emails")
        if submitted:
            email_list = ["customer1@example.com", "customer2@example.com", "customer3@example.com"]  # Replace with actual email list
            st.success(f"Emails sent to {len(email_list)} customers!")


    # Influencer Section
    st.subheader("Collaborate with Influencers")
    influencers = pd.DataFrame({
        "Name": ["Christopher Roland", "Thobias Meier", "Egon Maas", "Emilia Watzen", "Selina Groß", "Leonel Meiss"],
        "Followers": ["10K", "21K", "1.1M", "128K", "3K", "25K"],
        "Cost per Post (EUR)": [50, 200, 1000, 150, 80, 900]
    })

    for idx, row in influencers.iterrows():
        st.image(f"placeholder_image_{idx}.jpg", caption=row["Name"], width=150)  # Replace with image paths
        st.write(f"Followers: {row['Followers']}")
        st.write(f"Cost per Post: €{row['Cost per Post (EUR)']}")
        st.button(f"Contact {row['Name']}")

    st.subheader("Podcast Promotion")
    st.image("podcast.jpg", caption="Wine Podcast Banner")
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
        col1.metric("Total Profit (EUR)", f"€{total_profit}")
        col2.metric("Total Orders", total_orders)

        st.subheader("Order Distribution")

        sample_locations = pd.DataFrame({
            'City': ['New York', 'San Francisco', 'Chicago', 'Mumbai', 'Delhi', 'Bangalore', 'Sydney', 'Melbourne', 'Brisbane'],
            'Latitude': [40.7128, 37.7749, 41.8781, 19.0760, 28.7041, 12.9716, -33.8688, -37.8136, -27.4698],
            'Longitude': [-74.0060, -122.4194, -87.6298, 72.8777, 77.1025, 77.5946, 151.2093, 144.9631, 153.0251],
            'Orders': [10, 8, 6, 12, 11, 9, 7, 5, 4],
            'Color': ['#5DADE2', '#58D68D', '#F4D03F', '#5DADE2', '#58D68D', '#F4D03F', '#5DADE2', '#58D68D', '#F4D03F']
        })

        fig = px.scatter_geo(
            sample_locations, 
            lat='Latitude', 
            lon='Longitude', 
            text='City', 
            size='Orders',
            color='Color',  # Add color by specific values
            title="Global Order Distribution", 
            projection="natural earth"
        )

        st.plotly_chart(fig)

# 5. Dynamic Pricing & Sales Forecasting
if menu == "Pricing & Forecasting":
    st.title("Dynamic Pricing & Sales Forecasting")

    # Dynamic Pricing Section
    st.subheader("Price Trends by Wine Type")
    pricing_data = pd.DataFrame({
        'Wine Type': ['Red Delight', 'White Wonder', 'Rosé Glow', 'Cabernet Classic', 'Chardonnay Reserve'],
        'Current Price': [20, 15, 50, 25, 30],
        'Projected Price': [22, 14, 55, 28, 35],
        'Demand': [80, 60, 90, 70, 85]
    })

    fig_pricing = px.bar(
        pricing_data,
        x='Wine Type',
        y=['Current Price', 'Projected Price'],
        title="Current vs Projected Prices",
        barmode='group',
        labels={'value': 'Price (EUR)', 'variable': 'Price Type'},
        color_discrete_sequence=['#3498db', '#e74c3c']
    )
    st.plotly_chart(fig_pricing)

    st.subheader("Demand Analysis")
    fig_demand = px.scatter(
        pricing_data,
        x='Wine Type',
        y='Demand',
        size='Demand',
        color='Wine Type',
        title="Demand Forecast",
        labels={'Demand': 'Projected Demand (Units)'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_demand)

    # Sales Prediction & Forecasting Section
    st.title("Sales Prediction & Forecasting")

    forecast_data = pd.DataFrame({
        'Month': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'Projected Sales': [100, 120, 150, 180, 170, 200, 220, 240, 230, 250, 270, 300]
    })

    fig_forecast = px.line(
        forecast_data,
        x='Month',
        y='Projected Sales',
        title="Sales Forecast for Next 12 Months",
        labels={'Projected Sales': 'Sales (Units)', 'Month': 'Month'},
        markers=True,
        line_shape='spline'
    )
    st.plotly_chart(fig_forecast)

    st.subheader("AI-powered Sales Insights")
    if st.button("Generate Insights"):
        st.write("""
        - **Key Takeaways:**
            - Sales are expected to peak during holiday seasons.
            - Chardonnay Reserve shows a steady increase in demand.
            - Marketing efforts should focus on Red Delight for the next quarter.
        """)
