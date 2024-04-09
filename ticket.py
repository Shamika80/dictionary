service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def generate_ticket_id():

  global ticket_counter
  ticket_counter += 1
  return f"Ticket{ticket_counter:03d}"  

ticket_counter = 0  

def open_ticket(customer_name, issue_description):
  
  ticket_id = generate_ticket_id()
  service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
  print(f"Ticket {ticket_id} opened for {customer_name}.")

def update_ticket_status(ticket_id, new_status):

  if ticket_id in service_tickets:
    valid_statuses = ["open", "closed"]
    if new_status.lower() in valid_statuses:
      service_tickets[ticket_id]["Status"] = new_status
      print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
      print(f"Invalid status. Please enter 'open' or 'closed'.")
  else:
    print(f"Ticket {ticket_id} not found.")

def display_tickets(status=None):
  
  if status:
    print(f"Tickets with status '{status.upper()}':")
  else:
    print("All Tickets:")
  for ticket_id, ticket_info in service_tickets.items():
    if status is None or ticket_info["Status"] == status.lower():
      print(f"  - ID: {ticket_id}")
      print(f"    Customer: {ticket_info['Customer']}")
      print(f"    Issue: {ticket_info['Issue']}")
      print(f"    Status: {ticket_info['Status']}")
      print("")

open_ticket("Charlie", "Order not received")
display_tickets()
update_ticket_status("Ticket001", "closed")
display_tickets("open")