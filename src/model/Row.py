class Row:
    def __init__(self, slots):
        self.max_available_slots = slots
        self.slots = [-1 for _ in range(slots)]

    def __str__(self):
        return f"\n{self.slots}"

    def __repr__(self): 
        return self.__str__()

    def set_unavailable(self, slot):
        self.slots[slot] = -2
        self.calculate_slots()

    def set_server(self, slot, server):
        for i in range(server.size):
            self.slots[slot + i] = server.id
        self.calculate_slots()

    def unset_server(self, server):
        for i in range(server.size):
            self.slots[server.slot + i] = -1
        self.calculate_slots()

    def allocate_server(self, server):
        n_slots = len(self.slots)

        if server.size > self.max_available_slots:
            return -1

        # 1st fit
        for slot in range(0, n_slots-server.size+1):
            if any(val != -1 for val in self.slots[slot:slot+server.size]):
                continue
            self.set_server(slot, server)
            return slot

        return -1

    def allocate_server_to_slot(self, server, slot):
        if server.size > self.max_available_slots: 
            return False
        if any(val != -1 for val in self.slots[slot:slot+server.size]): 
            return False
        self.set_server(slot, server)
        return True


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
