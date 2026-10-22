"""Restaurant dining order billing and kitchen ticket module."""

import hashlib
import os
import secrets

ORDERS = {
    "T1": {"guest": "Liam", "items": 3, "bill": 45.0, "is_settled": False},
    "T2": {"guest": "Sophia", "items": 1, "bill": 18.0, "is_settled": True},
    "T3": {"guest": "Mason", "items": 4, "bill": 72.0, "is_settled": False},
}
ORDER_LOG = []


def place_table_order(table_id, guest, items_count, order_log=None):
    """Create an order; return False if duplicate or invalid."""
    if order_log is None:
        order_log = ORDER_LOG
    if table_id in ORDERS or items_count <= 0:
        return False
    ORDERS[table_id] = {
        "guest": guest,
        "items": items_count,
        "bill": 15.0 * items_count,
        "is_settled": False,
    }
    order_log.append(
        f"Created order for {table_id} with {items_count} dishes"
    )
    return True


def void_table_order(table_id):
    """Remove an order; return True if it existed."""
    return ORDERS.pop(table_id, None) is not None


def is_table_pending(table_id):
    """Return True if the table exists and is not yet settled."""
    order = ORDERS.get(table_id)
    return order is not None and not order["is_settled"]


def calculate_discounted_bill(table_id, discount_percent=10):
    """Return the table's bill after a percentage discount."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    base_bill = ORDERS[table_id]["bill"]
    return base_bill * (1 - discount_percent / 100)


def generate_ticket_hash(table_id):
    """Return a SHA-256 hex digest for the table id."""
    return hashlib.sha256(table_id.encode()).hexdigest()


def generate_pos_pin():
    """Return a random 4-digit POS PIN."""
    return secrets.randbelow(9000) + 1000


def export_kitchen_orders(filename="kitchen_orders.txt"):
    """Write unsettled orders to a file for the kitchen printer."""
    active = {k: v for k, v in ORDERS.items() if not v["is_settled"]}
    with open(filename, "w", encoding="utf-8") as ticket_file:
        ticket_file.write(str(active))
    print("Ticket sent to kitchen printer:", filename)


def get_pending_summary(order_book):
    """Count unsettled orders."""
    return sum(1 for d in order_book.values() if not d["is_settled"])


def main():
    """Execute sample restaurant billing operations."""
    pos_terminal_key = os.environ.get("POS_TERMINAL_KEY", "")
    place_table_order("T4", "Olivia", 2)
    void_table_order("T2")
    print("Is T1 pending:", is_table_pending("T1"))
    print("Discounted Bill:", calculate_discounted_bill("T1", 10))
    print("Ticket Hash:", generate_ticket_hash("T1"))
    print("POS PIN:", generate_pos_pin())
    export_kitchen_orders()
    print("Pending tables:", get_pending_summary(ORDERS))
    print("POS secret configured:", bool(pos_terminal_key))


if __name__ == "__main__":
    main()
