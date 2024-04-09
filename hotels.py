hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
  
  if room_number in hotel_rooms:
    if hotel_rooms[room_number]["status"] == "available":
      hotel_rooms[room_number]["status"] = "booked"
      hotel_rooms[room_number]["customer"] = customer_name
      print(f"Room {room_number} booked for {customer_name}.")
    else:
      print(f"Room {room_number} is already booked.")
  else:
    print(f"Room {room_number} does not exist.")

def check_out(room_number):
  
  if room_number in hotel_rooms:
    if hotel_rooms[room_number]["status"] == "booked":
      hotel_rooms[room_number]["status"] = "available"
      hotel_rooms[room_number]["customer"] = ""
      print(f"Customer checked out of room {room_number}.")
    else:
      print(f"Room {room_number} is already available.")
  else:
    print(f"Room {room_number} does not exist.")

def display_room_status():
  
  print("Room Status:")
  for room_number, room_info in hotel_rooms.items():
    print(f"  Room {room_number}: {room_info['status']} - {room_info['customer']}")

book_room("103", "Jane Smith")
display_room_status()
check_out("101")
display_room_status()