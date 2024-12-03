import streamlit as st
import pandas as pd
import plotly.express as px

# Dummy data for wines
wines = pd.DataFrame({
    "Name": ["Château Margaux", "Sassicaia", "Penfolds Grange", "Dom Pérignon", "Opus One", "Châteauneuf-du-Pape"],
    "Origin": ["France", "Italy", "Australia", "France", "USA", "France"],
    "Grape Type": ["Cabernet Sauvignon, Merlot", "Cabernet Sauvignon", "Shiraz", "Chardonnay, Pinot Noir", "Cabernet Sauvignon, Merlot", "Grenache, Syrah"],
    "Vintage": [2015, 2018, 2017, 2013, 2019, 2020],
    "Alcohol Content": [13.5, 14, 14.5, 12.5, 14, 13],
    "Body": ["Full-bodied", "Medium-bodied", "Full-bodied", "Light-bodied", "Full-bodied", "Full-bodied"],
    "Food Pairing": [
        "Red meats, truffle dishes",
        "Grilled meats, aged cheese",
        "Barbecue, roasted lamb",
        "Seafood, caviar",
        "Steak, braised short ribs",
        "Duck, lamb, grilled vegetables"
    ],
    "Tasting Notes": [
        "Complex aromas of blackcurrant, cedar, and violets with a long finish.",
        "Notes of red berries, tobacco, and spices with elegant tannins.",
        "Rich flavors of dark chocolate, black pepper, and plum.",
        "Hints of citrus, brioche, and almond with fine bubbles.",
        "Opulent with dark fruit, vanilla, and a touch of oak.",
        "Spicy with notes of black cherry, licorice, and herbs."
    ],
    "Current Price": [950, 300, 850, 200, 350, 100],
    "Delivery Cost": [20, 15, 25, 10, 18, 12],
    "Import Cost": [30, 25, 35, 20, 28, 22],
    "Orders in Last 24hrs": [8, 5, 3, 10, 4, 6],
    "Delivery Time": ["7-10 days", "5-8 days", "8-12 days", "6-9 days", "7-10 days", "5-7 days"],
    "Image Path": [
        "wine1.jpg",
        "wine2.jpg",
        "wine3.jpg",
        "wine4.jpg",
        "wine5.jpg",
        "wine6.jpg"
    ],
    "YouTube Review": [
        "https://www.youtube.com/shorts/rlNSxImnnSk",
        "https://www.youtube.com/shorts/rlNSxImnnSk",
        "https://youtu.be/penfolds_review",
        "https://youtu.be/dom_review",
        "https://youtu.be/opusone_review",
        "https://youtu.be/chateauneuf_review"
    ]
})

# Dummy past orders
past_orders = pd.DataFrame({
    "Order ID": ["ORD001", "ORD002", "ORD003", "ORD004"],
    "Wine": ["Riesling", "Pinot Noir", "Merlot", "Chardonnay"],
    "Price": [24.69, 30.99, 22.99, 28.69],
    "Status": ["Delivered", "Pending", "Delivered", "Shipped"]
})


def display_wine_horizontal_main(wine):
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"### {wine['Name']} ({wine['Vintage']})")
        st.write(f"**Origin:** {wine['Origin']}")
        st.write(f"**Grape Type:** {wine['Grape Type']}")
        st.write(f"**Body:** {wine['Body']}")
        st.write(f"**Alcohol Content:** {wine['Alcohol Content']}%")
        st.write(f"**Food Pairing:** {wine['Food Pairing']}")
        st.write(f"**Delivery Time:** {wine['Delivery Time']}")
        
        st.markdown(
            f"""<p style='margin:0;'>
            <span style='text-decoration: line-through; color:red;'>Retail Price: €{wine['Current Price'] * 1.2:.2f}</span><br>
            <span style='color:green; font-size:20px;'><b>Selling Price: €{wine['Current Price']}</b></span>
            </p>""",
            unsafe_allow_html=True
        )
        # st.write(f"**Orders in Last 24hrs:** {wine['Orders in Last 24hrs']} orders")

    with col2:
        st.image(wine["Image Path"], width=200, caption=wine['Name'])

def display_wine_horizontal_main_t(wine):
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"### {wine['Name']} ({wine['Vintage']})")
        st.write(f"**Origin:** {wine['Origin']}")
        st.write(f"**Grape Type:** {wine['Grape Type']}")
        # st.write(f"**Body:** {wine['Body']}")
        # st.write(f"**Alcohol Content:** {wine['Alcohol Content']}%")
        # st.write(f"**Food Pairing:** {wine['Food Pairing']}")
        # st.write(f"**Delivery Time:** {wine['Delivery Time']}")
        
        st.markdown(
            f"""<p style='margin:0;'>
            <span style='text-decoration: line-through; color:red;'>Retail Price: €{wine['Current Price'] * 1.2:.2f}</span><br>
            <span style='color:green; font-size:20px;'><b>Selling Price: €{wine['Current Price']}</b></span>
            </p>""",
            unsafe_allow_html=True
        )
        st.write(f"**Orders in Last 24hrs:** {wine['Orders in Last 24hrs']} orders")

    with col2:
        st.image(wine["Image Path"], width=200, caption=wine['Name'])

def display_wine_horizontal_main_b(wine):
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"### {wine['Name']} ({wine['Vintage']})")
        st.write(f"**Origin:** {wine['Origin']}")
        st.write(f"**Grape Type:** {wine['Grape Type']}")
        st.write(f"**Body:** {wine['Body']}")
        st.write(f"**Review by Expert:** {wine["YouTube Review"]}")
        # st.write(f"**Alcohol Content:** {wine['Alcohol Content']}%")
        # st.write(f"**Food Pairing:** {wine['Food Pairing']}")
        # st.write(f"**Delivery Time:** {wine['Delivery Time']}")
        
        st.markdown(
            f"""<p style='margin:0;'>
            <span style='text-decoration: line-through; color:red;'>Retail Price: €{wine['Current Price'] * 1.2:.2f}</span><br>
            <span style='color:green; font-size:20px;'><b>Selling Price: €{wine['Current Price']}</b></span>
            </p>""",
            unsafe_allow_html=True
        )
        st.write(f"**Orders in Last 24hrs:** {wine['Orders in Last 24hrs']} orders")

    with col2:
        st.image(wine["Image Path"], width=200, caption=wine['Name'])

# Home Page with Horizontal Layout
def show_main_page():
    st.title("Welcome to the WineBridge")

    # Display filters on the sidebar
    st.sidebar.header("Filters")
    origin_filter = st.sidebar.multiselect("Filter by Origin", wines["Origin"].unique())
    quality_filter = st.sidebar.multiselect("Filter by Grape Type", wines["Grape Type"].unique())
    alcohol_filter = st.sidebar.slider("Alcohol Content (%)", 0, 15, (0, 15))

    # Filter wines based on sidebar inputs
    filtered_wines = wines[
        (wines["Alcohol Content"].between(alcohol_filter[0], alcohol_filter[1])) &
        (wines["Origin"].isin(origin_filter) if origin_filter else True) &
        (wines["Grape Type"].isin(quality_filter) if quality_filter else True)
    ]

    # Display each wine horizontally on the main page
    for _, wine in filtered_wines.iterrows():
        display_wine_horizontal_main(wine)
        st.markdown("---")  # Divider line for clarity between items


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

def show_trending_page():
    st.title("Trending Wines")
    trending_wines = wines.sample(3)  # Dummy trending wines

    for _, wine in trending_wines.iterrows():
        display_wine_horizontal_main_t(wine)
        st.markdown("---")  # Divider line for clarity

def show_bestsellers_page():
    st.title("Bestsellers")
    bestsellers = wines.nlargest(3, "Current Price")  # Dummy bestsellers

    for _, wine in bestsellers.iterrows():
        display_wine_horizontal_main_b(wine)
        st.markdown("---")  # Divider line for clarity


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
        st.write(f"**Grape Type:** {recommended_wine['Grape Type']}")
        st.write(f"**AI Review:** A unique blend, perfect for celebrations. Customers love its fruity notes and long-lasting finish. Expertly crafted for a luxurious experience. The wine is golden yellow in the glass. On the nose it has aromas of peach, lemon and lime, accompanied by floral notes. The wine is elegant but at the same time rich in peach fruit, quince and Granny Smith apple. A mineral base with a slightly spicy note rounds off this wine.")
        st.write("**Customer Review:** 'Absolutely delightful! Got this from France for my anniversary and it was the best thing I could've done to make that night special.'")

        st.header("Complete Your Order")
        st.image(r"C:\Users\cbkri\Desktop\smart_hack\paypal_logo.png", width=100)
        if st.button("Pay with PayPal"):
            st.success("Payment successful! Thank you for your order.")

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

# # Trending and Bestsellers
# def show_trending_page():
#     st.title("Trending Wines")
#     trending_wines = wines.sample(3)  # Dummy trending wines
#     for _, wine in trending_wines.iterrows():
#         st.image(wine["Image Path"], width=200)
#         st.subheader(wine["Name"])
#         st.write(f"**Price:** €{wine['Current Price']}")
#         st.write(f"**Ordered in Last 24 Hours:** {wine['Orders in Last 24hrs']} orders")


# def show_bestsellers_page():
#     st.title("Bestsellers")
#     bestsellers = wines.nlargest(3, "Current Price")  # Dummy bestsellers
#     for _, wine in bestsellers.iterrows():
#         st.image(wine["Image Path"], width=300)
#         st.subheader(wine["Name"])
#         st.write(f"**Price:** €{wine['Current Price']}")

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
