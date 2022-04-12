class Row:
    def __init__(self, slots):
        self.max_available_slots = slots
        self.slots = [-1 for _ in range(slots)]

    def set_unavailable(self, slot):
        self.slots[slot] = -2

    def set_server(self, slot, server):
        for i in range(server.size):
            self.slots[slot + i] = server.id
        self.calculate_slots()

    def allocate_server(self, server):
        n_slots = len(self.slots)

        if server.size > len(self.slots):
            return False

        # 1st fit
        for slot in range(0, n_slots-server.size+1):
            if any(x != -1 for x in self.slots[slot:slot+server.size]):
                continue
            self.set_server(slot, server)
            return True

        return False

    def calculate_slots(self):
        available_slots = 0
        max_available_slots = 0

        for slot in self.slots:
            if slot == -1:
                available_slots += 1
            else:
                if available_slots > max_available_slots:
                    max_available_slots = available_slots
                available_slots = 0

        if available_slots > max_available_slots:
            max_available_slots = available_slots
        self.max_available_slots = max_available_slots

    def __repr__(self):
        return print(*self.slots, sep=", ")

    def __str__(self):
        return print(*self.slots, sep=", ")
