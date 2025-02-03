import math
import uuid

receipts = {}

def points_from_retailer_name(retailer):
    # 1 point for every alphanumeric character in the retailer name.
    sum = 0
    for ch in retailer:
        if ch.isalnum():
            sum += 1
    return sum

def points_from_round_total(total):
    # 50 points if the total is a round dollar amount with no cents.
    return 50 if total.isdigit() or total.endswith('.00') else 0

def points_from_multiple_of_25(total):
    # 25 points if the total is a multiple of 0.25.
    return 25 if float(total) % 0.25 == 0 else 0

def points_from_item_count(items):
    # 5 points for every 2 items.
    return (len(items) // 2) * 5

def points_from_item_description(items):
    # If an item's trimmed description length is a multiple of 3, add 20% of price (rounded up).
    points = 0
    for item in items:
        if len(item['shortDescription'].strip()) % 3 == 0:
            points += math.ceil(float(item['price']) * 0.2)
    return points

def points_from_purchase_date(purchase_date):
    # 6 points if the purchase date is an odd number.
    day = int(purchase_date.split('-')[2])
    return 6 if day % 2 != 0 else 0

def points_from_purchase_time(purchase_time):
    # 10 points if the purchase time is between 2:00 PM and 4:00 PM.
    time_float = float('.'.join(purchase_time.split(':')))
    return 10 if 14.00 < time_float < 16.00 else 0

def calculate_points(receipt_data):
    # Calculate total points.    
    points = 0
    points += points_from_retailer_name(receipt_data['retailer'])
    points += points_from_round_total(receipt_data['total'])
    points += points_from_multiple_of_25(receipt_data['total'])
    points += points_from_item_count(receipt_data['items'])
    points += points_from_item_description(receipt_data['items'])
    points += points_from_purchase_date(receipt_data['purchaseDate'])
    points += points_from_purchase_time(receipt_data['purchaseTime'])
    return points


def generate_receipt_id():
    # Generates a unique receipt ID."""
    return str(uuid.uuid4())

def process_receipt(receipt_data):

    # Generate ID
    receipt_id = generate_receipt_id()
    
    # Calculate points
    points = calculate_points(receipt_data)

    # Store receipt details with points
    receipts[receipt_id] = {'data': receipt_data, 'points': points}

    # Return receipt ID
    return receipt_id

def get_receipt_points(receipt_id):
    return receipts.get(receipt_id, {}).get('points', None)

def get_receipt_details(receipt_id):
    # Fetch receipt details using the receipt ID.
    receipt = receipts.get(receipt_id, None)

    if receipt:
        return {
            'receipt': receipt['data'],
            'points': receipt['points']
        }
    else:
        return None
