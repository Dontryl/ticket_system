import heapq
import itertools


class TicketQueue:
    def __init__(self):
        self.queue = []
        self.counter = itertools.count()

    def add_ticket(self, ticket):
        priority = self.calculate_priority(ticket)
        count = next(self.counter)
        heapq.heappush(self.queue, (priority, count, ticket))

    def calculate_priority(self, ticket):
        urgency_score = {'alta': 3, 'média': 2, 'baixa': 1}
        client_score = {'vip': 3, 'regular': 1}
        urgency = urgency_score.get(ticket.urgency.lower(), 1)
        client = client_score.get(ticket.client_type.lower(), 1)
        return -(urgency * 2 + client)

    def get_next_ticket(self):
        if self.queue:
            priority, count, ticket = heapq.heappop(self.queue)
            return ticket
        return None

    def view_all_tickets(self):
        return sorted(self.queue)
