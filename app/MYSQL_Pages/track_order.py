import streamlit as st
import mysql.connector
from config import DB_CONFIG
import time

def get_order_details(order_id):
    """✅ Fetch order details from the database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM orders WHERE id = %s"
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()

        cursor.close()
        conn.close()
        return order
    
    except Exception as e:
        st.error(f"⚠ Database error: {e}")
        return None

def show_order_tracking():
    """🚀 **Customer Order Tracking Page - Modern UI**"""
    st.markdown("<h1 style='text-align: center; color: #007BFF;'>📦 Track Your Order</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>🔍 Enter your Order ID below to check your order status.</h3>", unsafe_allow_html=True)
    st.divider()

    # ✅ Order ID Input
    order_id = st.text_input("🔢 **Enter Order ID**", placeholder="e.g., 12345").strip()

    if st.button("🚀 Track Order", use_container_width=True):
        if not order_id.isdigit():
            st.warning("⚠ Please enter a **valid numeric Order ID**.")
            return

        st.info("⏳ Fetching order details... Please wait.")
        time.sleep(1.5)  # ⏳ Simulate loading

        order = get_order_details(order_id)

        if order:
            st.success("✅ Order Found! Here are your order details:")
            st.markdown("---")
            st.markdown("<h3 style='text-align: center;'>📝 Order Summary</h3>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📦 **Order ID:** {order['id']}")
                st.write(f"🛒 **Items Ordered:** {order['items']}")
                st.write(f"💰 **Total Price:** ${order['total_price']:.2f}")                

            # ✅ Display Status with Color Codes
            status = order["status"]
            status_colors = {
                "Pending": "⚪ **Pending** - Your order is waiting to be processed.",
                "In Process": "🔵 **In Process** - Your order is being prepared.",
                "Preparing": "🟡 **Preparing** - Your food is being cooked.",
                "Ready": "🟢 **Ready** - Your order is ready for pickup/delivery.",
                "Completed": "✅ **Completed** - Your order has been delivered!",
                "Canceled": "❌ **Canceled** - This order was canceled."
            }

            st.markdown(f"📌 **Current Status:** {status_colors.get(status, '🔘 Unknown Status')}")

        else:
            st.error("⚠ No order found with this **Order ID**. Please check and try again.")

# ✅ Run the Order Tracking Page
if __name__ == "__main__":
    show_order_tracking()
