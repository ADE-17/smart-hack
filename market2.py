import streamlit as st
import pandas as pd
import plotly.express as px

# Dummy data for wines
wines = pd.DataFrame({
    "Name": ["Red Delight", "White Wonder", "Rosé Glow", "Riesling", "Gewürztraminer", "Spätburgunder"],
    "Origin": ["Germany", "France", "Italy", "Germany", "Germany", "Germany"],
    "Quality": ["Premium", "Standard", "Luxury", "DLG Certified", "Standard", "DLG Certified"],
    "Retail Price": [29.9, 20.0, 61.9, 40.9, 34.9, 55.6],
    "Current Price": [19.9, 15.9, 44.6, 34.9, 30.9, 41.9],
    "Alcohol Content": [12, 11, 13, 10, 14, 12],
    "Delivery Cost": [4.9, 7.9, 10.9, 8.9, 6.9, 9.9],
    "Import Cost": [3, 5, 7, 4, 5, 6],
    "Orders in Last 24hrs": [15, 25, 5, 12, 8, 10],
    "Delivery Time": ["5-7 days", "3-5 days", "7-10 days", "5-7 days", "6-8 days", "4-6 days"],
    "Image Path": ["wine1.jpg",
     "wine2.jpg", 
     "wine3.jpg", 
     "wine4.jpg", 
     "wine5.jpg",
      "wine6.jpg"],
    "YouTube Review": [
        "https://youtu.be/sample1",
        "https://youtu.be/sample2",
        "https://youtu.be/sample3",
        "https://youtu.be/sample4",
        "https://youtu.be/sample5",
        "https://youtu.be/sample6"
    ],
    "Description": [
        "A bold red wine with rich flavors.",
        "A light white wine perfect for summer.",
        "A luxurious rosé with hints of berries.",
        "A classic German Riesling with crisp taste.",
        "A flavorful Gewürztraminer with spicy notes.",
        "A smooth Spätburgunder with earthy undertones."
    ]
})

# Dummy past orders
past_orders = pd.DataFrame({
    "Order ID": ["ORD001", "ORD002", "ORD003", "ORD004"],
    "Wine": ["Riesling", "Pinot Noir", "Merlot", "Chardonnay"],
    "Price": [24.69, 30.99, 22.99, 28.69],
    "Status": ["Delivered", "Pending", "Delivered", "Shipped"]
})


# Main Page
def show_main_page():
    st.title("Welcome to the WineBridge")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("team.jpg", width=100, caption="")
    with col2:
        st.image("dlg.png", width=100, caption="DLG Certified")
    with col3:
        st.image("wset.png", width=100, caption="WSET Certified")


    # Filters
    st.sidebar.header("Filters")
    origin_filter = st.sidebar.multiselect("Filter by Origin", wines["Origin"].unique())
    quality_filter = st.sidebar.multiselect("Filter by Quality", wines["Quality"].unique())
    alcohol_filter = st.sidebar.slider("Alcohol Content (%)", 0, 15, (0, 15))

    filtered_wines = wines[
        (wines["Alcohol Content"].between(alcohol_filter[0], alcohol_filter[1])) & 
        (wines["Origin"].isin(origin_filter) if origin_filter else True) & 
        (wines["Quality"].isin(quality_filter) if quality_filter else True)
    ]

    for _, wine in filtered_wines.iterrows():
        st.image(wine["Image Path"], width=300)
        st.markdown(f"### {wine['Name']}")
        st.write(f"**Origin:** {wine['Origin']}")

        # Properly formatted HTML for price display
        st.markdown(
            f"""<p style='margin:0;'>
            <span style='color:red;'>Retail Price: €{wine['Retail Price']}</span> <br>
            <span style='color:green; font-size:24px;'><b>Selling Price: €{wine['Current Price']}</b></span>
            </p>""", 
            unsafe_allow_html=True
        )

        if st.button(f"View Details - {wine['Name']}"):
            show_wine_details(wine)


# Wine Details Page
def show_wine_details(wine):
    st.title(f"{wine['Name']} - Details")
    st.image(wine["Image Path"], width=500)
    st.write(f"**Origin:** {wine['Origin']}")
    st.write(f"**Quality:** {wine['Quality']}")
    st.write(f"**Alcohol Content:** {wine['Alcohol Content']}%")
    st.write(f"**Description:** {wine['Description']}")
    st.write(f"**Price:** €{wine['Current Price']}")
    st.write(f"**Delivery Cost:** €{wine['Delivery Cost']} | **Import Cost:** €{wine['Import Cost']}")
    st.write(f"**Delivery Time:** {wine['Delivery Time']}")
    st.markdown(f"[Watch Review on YouTube]({wine['YouTube Review']})")

    # Payment Section
    st.header("Complete Your Order")
    st.image(r"C:\Users\cbkri\Desktop\smart_hack\paypal_logo.png", width=100)
    if st.button("Pay with PayPal"):
        st.success("Payment successful! Thank you for your order.")

# Customer Dashboard
def show_dashboard():
    st.title("My Orders")
    st.dataframe(past_orders)

    selected_order_id = st.selectbox(
        "Select an Order ID to Reorder:", 
        past_orders["Order ID"]
    )

    # Fetch the selected order details
    selected_order = past_orders[past_orders["Order ID"] == selected_order_id].iloc[0]

    # Display order details
    st.write(f"**Wine:** {selected_order['Wine']}")
    st.write(f"**Price:** €{selected_order['Price']}")
    st.write(f"**Status:** {selected_order['Status']}")

    # Button to reorder the selected order
    if st.button(f"Order Again - {selected_order_id}"):
        st.success(f"Order ID: {selected_order_id} - {selected_order['Wine']} added to cart!")

    st.subheader("Recommended Wine Based on Past Orders")
    recommended_wine = wines.sample(1).iloc[0]
    if st.button("Generate Recommendation"):
        st.markdown(f"### {recommended_wine['Name']}")
        st.image(recommended_wine["Image Path"], width=300)
        st.write(f"**Origin:** {recommended_wine['Origin']}")
        st.write(f"**Quality:** {recommended_wine['Quality']}")
        st.write(f"**AI Review:** A unique blend, perfect for celebrations. Customers love its fruity notes and long-lasting finish. Expertly crafted for a luxurious experience. The wine is golden yellow in the glass. On the nose it has aromas of peach, lemon and lime, accompanied by floral notes. The wine is elegant but at the same time rich in peach fruit, quince and Granny Smith apple. A mineral base with a slightly spicy note rounds off this wine.")
        st.write("**Customer Review:** 'Absolutely delightful! Got this from France for my anniversary and it was the best thing I could've done to make that night special.'")


# World Map for Origin Selection
def show_map():
    st.title("Select Wine by Origin")
    locations = {
        "Germany": [51.1657, 10.4515],
        "France": [46.6034, 1.8883],
        "Italy": [41.8719, 12.5674],
        "Stuttgart": [48.7758, 9.1829],
        "Nuremberg": [49.4521, 11.0767],
        "Kaiserslautern": [49.4447, 7.7694]
    }
    df = pd.DataFrame(locations, index=["Latitude", "Longitude"]).T.reset_index().rename(columns={"index": "Country"})
    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", text="Country", size_max=20, size=[20]*len(df), hover_name="Country", projection="natural earth", opacity=0.7)
    st.plotly_chart(fig)

# Trending and Bestsellers
def show_trending_page():
    st.title("Trending Wines")
    trending_wines = wines.sample(3)  # Dummy trending wines
    for _, wine in trending_wines.iterrows():
        st.image(wine["Image Path"], width=200)
        st.subheader(wine["Name"])
        st.write(f"**Price:** €{wine['Current Price']}")
        st.write(f"**Ordered in Last 24 Hours:** {wine['Orders in Last 24hrs']} orders")


def show_bestsellers_page():
    st.title("Bestsellers")
    bestsellers = wines.nlargest(3, "Current Price")  # Dummy bestsellers
    for _, wine in bestsellers.iterrows():
        st.image(wine["Image Path"], width=300)
        st.subheader(wine["Name"])
        st.write(f"**Price:** €{wine['Current Price']}")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Trending", "Bestsellers", "Dashboard", "Origin Map"])

if page == "Home":
    show_main_page()
elif page == "Dashboard":
    show_dashboard()
elif page == "Origin Map":
    show_map()
elif page == "Trending":
    show_trending_page()
elif page == "Bestsellers":
    show_bestsellers_page()
