import streamlit as st
import pandas as pd

# Dummy data for wines
wines = pd.DataFrame({
    "Name": ["Red Delight", "White Wonder", "Rosé Glow", "Riesling", "Gewürztraminer", "Spätburgunder"],
    "Origin": ["Germany", "France", "Italy", "Germany", "Germany", "Germany"],
    "Quality": ["Premium", "Standard", "Luxury", "DLG Certified", "Standard", "DLG Certified"],
    "Retail Price": [25, 20, 60, 40, 35, 55],
    "Current Price": [20, 15, 50, 35, 30, 45],
    "Delivery Cost": [5, 7, 10, 8, 6, 9],
    "Import Cost": [3, 5, 7, 4, 5, 6],
    "Delivery Time": ["5-7 days", "3-5 days", "7-10 days", "5-7 days", "6-8 days", "4-6 days"],
    "Image Path": [r"C:\Users\cbkri\Desktop\smart_hack\wine1.jpg",
     r"C:\Users\cbkri\Desktop\smart_hack\wine2.jpg", 
     r"C:\Users\cbkri\Desktop\smart_hack\wine3.jpg", 
     r"C:\Users\cbkri\Desktop\smart_hack\wine4.jpg", 
     r"C:\Users\cbkri\Desktop\smart_hack\wine5.jpg",
      r"C:\Users\cbkri\Desktop\smart_hack\wine6.jpg"],
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

# Main Page
def show_main_page():
    st.title("Welcome to the Wine Marketplace")
    st.sidebar.header("Filters")

    # Filters
    origin_filter = st.sidebar.multiselect("Filter by Origin", wines["Origin"].unique())
    quality_filter = st.sidebar.multiselect("Filter by Quality", wines["Quality"].unique())

    filtered_wines = wines
    if origin_filter:
        filtered_wines = filtered_wines[filtered_wines["Origin"].isin(origin_filter)]
    if quality_filter:
        filtered_wines = filtered_wines[filtered_wines["Quality"].isin(quality_filter)]

    # Display wines
    for _, wine in filtered_wines.iterrows():
        st.image(wine["Image Path"], width=300)
        st.subheader(wine["Name"])
        st.write(f"**Origin:** {wine['Origin']}")
        st.write(f"**Retail Price:** ${wine['Retail Price']} | **Current Price:** ${wine['Current Price']}")
        st.write(f"**Delivery Cost:** ${wine['Delivery Cost']} | **Import Cost:** ${wine['Import Cost']}")
        st.write(f"**Delivery Time:** {wine['Delivery Time']}")

        st.markdown(f"[Watch Review on YouTube]({wine['YouTube Review']})")

        if st.button(f"View Details - {wine['Name']}"):
            show_wine_details(wine)

# Wine Details Page
def show_wine_details(wine):
    st.title(f"{wine['Name']} - Details")
    st.image(wine["Image Path"], width=500)
    st.write(f"**Origin:** {wine['Origin']}")
    st.write(f"**Quality:** {wine['Quality']}")
    st.write(f"**Description:** {wine['Description']}")
    st.write(f"**Price:** ${wine['Current Price']}")
    st.write(f"**Delivery Cost:** ${wine['Delivery Cost']} | **Import Cost:** ${wine['Import Cost']}")
    st.write(f"**Delivery Time:** {wine['Delivery Time']}")

    st.markdown(f"[Watch Review on YouTube]({wine['YouTube Review']})")

    # Dummy Payment Gateway
    st.header("Complete Your Order")
    st.write("Select your payment method:")
    st.image(r"C:\Users\cbkri\Desktop\smart_hack\paypal_logo.png", width=100)  # Add PayPal image path

    if st.button("Pay with PayPal"):
        st.success("Payment successful! Thank you for your order.")

# Trending and Bestsellers
def show_trending_page():
    st.title("Trending Wines")
    trending_wines = wines.sample(3)  # Dummy trending wines
    for _, wine in trending_wines.iterrows():
        st.image(wine["Image Path"], width=300)
        st.subheader(wine["Name"])
        st.write(f"**Price:** ${wine['Current Price']}")

def show_bestsellers_page():
    st.title("Bestsellers")
    bestsellers = wines.nlargest(3, "Current Price")  # Dummy bestsellers
    for _, wine in bestsellers.iterrows():
        st.image(wine["Image Path"], width=300)
        st.subheader(wine["Name"])
        st.write(f"**Price:** ${wine['Current Price']}")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Trending", "Bestsellers"])

if page == "Home":
    show_main_page()
elif page == "Trending":
    show_trending_page()
elif page == "Bestsellers":
    show_bestsellers_page()
