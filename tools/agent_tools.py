import json
from order.order_handler import OrderHandler
import ast
import re

# ✅ Order Handler for in-memory storage
order_handler = OrderHandler()

# ✅ Define tools
def show_menu(_=None):
    """✅ Return available menu items from stored memory."""
    menu = order_handler.menu  # ✅ Now accessing stored menu
    return f"📜 Here's our menu:\n{menu}" if menu else "⚠ Sorry, the menu is currently unavailable."

def extract_items(order_details):
    """✅ Extracts item names and quantities using regex from JSON format."""
    try:
        # Convert JSON string to a dictionary
        order_dict = json.loads(order_details)
        
        # Convert dictionary to a string for regex processing
        order_str = json.dumps(order_dict)

        # ✅ Match item names and quantities using regex
        pattern = r'"([\w\s-]+)"\s*:\s*(\d+)'
        matches = re.findall(pattern, order_str)

        # ✅ Convert extracted data to a structured dictionary
        extracted_order = {item.strip(): int(qty) for item, qty in matches}
        try:
            
            response = order_handler.add_item(extracted_order)
            return response
        except Exception as e:
            return f"��� Error occurred: {str(e)}"

    except json.JSONDecodeError:
        return "⚠ Invalid JSON format. Please use structured order format."

def add_items(order_details):
    return extract_items(order_details)
    

def update_item(item_details: str):
    """✅ Update the quantity of an existing item in the order while correctly extracting item name and quantity."""
    try:
        print(f"🔍 Extracting items from: {item_details}")

        # ✅ Use regex to extract the "item" name and "quantity"
        item_pattern = r'"item"\s*:\s*"([\w\s-]+)"'   # Extract item name
        quantity_pattern = r'"quantity"\s*:\s*(\d+)'  # Extract quantity

        item_match = re.search(item_pattern, item_details)
        quantity_match = re.search(quantity_pattern, item_details)

        if not (item_match and quantity_match):
            return "⚠ No valid items found. Use structured format like: {'item': 'pepsi', 'quantity': 2}"

        # ✅ Extracted values
        item_name = item_match.group(1).strip()
        quantity = int(quantity_match.group(1))

        # ✅ Convert to required dictionary format
        order_dict = {item_name: quantity}
        print(f"✅ Extracted Order Update: {order_dict}")

        # ✅ Pass structured data to order handler
        response = order_handler.update_item(order_dict)
        return response

    except Exception as e:
        return f"⚠ Error processing update: {str(e)}"

def replace_item(replacements):
    """✅ Replace multiple items in the order while keeping quantity and updating the total price."""
    try:
        print("🔄 Replace Request:", replacements)

        # ✅ Convert string representation of list/tuple to actual Python list
        if isinstance(replacements, str):
            try:
                replacements = ast.literal_eval(replacements)  # Convert string to Python list of tuples
            except (SyntaxError, ValueError):
                return "⚠ Invalid format. Expected [(old_item, new_item), (old_item, new_item), ...]"

        # ✅ Ensure replacements is a list of valid (old_item, new_item) tuples
        if not (isinstance(replacements, list) and all(isinstance(pair, tuple) and len(pair) == 2 for pair in replacements)):
            return "⚠ Invalid format. Expected [(old_item, new_item), (old_item, new_item), ...]"

        # ✅ Process all replacements
        responses = []
        for old_item, new_item in replacements:
            response = order_handler.replace_item(old_item, new_item)
            responses.append(response)

        return "\n".join(responses)  # ✅ Return all updates as a single response

    except Exception as e:
        return f"⚠ Error processing replacement: {str(e)}"


def modify_order_after_confirmation(order_details: str):
    """✅ Modify an order after confirmation before preparation starts."""
    try:
        print(order_details)
        order_data = json.loads(order_details)  # Expecting {'order_id': 1, 'updated_items': {'item': quantity}}
        order_id = order_data["order_id"]
        updated_items = order_data["updated_items"]
        return order_handler.modify_order_after_confirmation(order_id, updated_items)
    except json.JSONDecodeError:
        return "⚠ Invalid format. Use JSON: {'order_id': 1, 'updated_items': {'item': quantity}}"

def confirm_order(_=None):
    """✅ Confirms the order and provides an Order ID."""
    confirmation_message = order_handler.confirm_order()
    return confirmation_message  # ✅ Now returns Order ID after confirmation

def check_order_status(order_id: str):
    """✅ Retrieve order status using Order ID."""
    return order_handler.check_order_status(order_id)

def remove_item(item_name: str):
    """✅ Removes an item from the order."""
    return order_handler.remove_item(item_name)

def total_price(_=None):
    return order_handler.total_price

def check_order_items(_=None):
    return order_handler.order_items

def cancel_order_before_confirmation(_=None):
    """�� Cancels the current order and returns the Order ID."""
    return order_handler.cancel_order_before_confirmation()

def cancel_order_after_confirmation(user_id):
    """🚫 Cancels the current order after confirmation using the Order ID."""
    return order_handler.cancel_order_after_confirmation(user_id)

def estimated_delivery_time(order_id: int):
    """✅ Track estimated delivery time of an order."""
    return order_handler.estimated_delivery_time(order_id)