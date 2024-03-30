class Artwork:
    def __init__(self, title, artist, creation_date, significance, location):
        self.title = title
        self.artist = artist
        self.creation_date = creation_date
        self.significance = significance
        self.location = location


class Exhibition(Artwork):
    def __init__(self, title, artist, creation_date, significance, location, start_date, end_date):
        super().__init__(title, artist, creation_date, significance, location)
        self.start_date = start_date
        self.end_date = end_date


class PermanentGallery(Artwork):
    def __init__(self, title, artist, creation_date, significance, location, gallery_number):
        super().__init__(title, artist, creation_date, significance, location)
        self.gallery_number = gallery_number


class OutdoorSpace(Artwork):
    def __init__(self, title, artist, creation_date, significance, location, space_name, capacity):
        super().__init__(title, artist, creation_date, significance, location)
        self.space_name = space_name
        self.capacity = capacity


class Visitor:
    def __init__(self, name, age, visitor_type):
        self.name = name
        self.age = age
        self.visitor_type = visitor_type
        self.tickets = []

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)


class Ticket:
    def __init__(self, base_price, date, event_name, event_type="regular"):
        self.base_price = base_price
        self.date = date
        self.event_name = event_name
        self.event_type = event_type  # Can be "regular", "special", or "tour"

    def calculate_final_price(self, visitor, group_size=1):
        # Check for free tickets
        if (visitor.visitor_type == "student" or
                visitor.visitor_type == "teacher" or
                (visitor.visitor_type == "senior" and visitor.age >= 60) or
                (visitor.age < 5)):
            return 0

        price = self.base_price

        # Apply group discount if applicable
        if group_size >= 10:
            price *= 0.5  # 50% discount

        # Apply VAT if it's not a free ticket
        price *= 1.05  # 5% VAT

        return price


class Event:
    def __init__(self, event_name, location, duration, special_requirements):
        self.event_name = event_name
        self.location = location
        self.duration = duration
        self.special_requirements = special_requirements


class Group:
    def __init__(self, group_size, discount):
        self.group_size = group_size
        self.discount = discount
        self.visitors = []

    def add_visitor(self, visitor):
        self.visitors.append(visitor)
