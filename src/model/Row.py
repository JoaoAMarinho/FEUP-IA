class Row:
    """
    Row class model
    """

    def __init__(self, slots):
        self.max_available_slots = slots
        self.slots = [-1 for _ in range(slots)]

    def __str__(self):
        return f"\n{self.slots}"

    def __repr__(self): 
        return self.__str__()

    def set_unavailable(self, slot):
        """
        Sets the specified slot to an unavailable state, and recalculates the maximum number of consecutive slots
        """
        self.slots[slot] = -2
        self.calculate_slots()

    def set_server(self, slot, server):
        """
        Fills the slots with the server id starting from 'slot', and recalculates the maximum number of consecutive slots
        """
        for i in range(server.size):
            self.slots[slot + i] = server.id
        self.calculate_slots()

    def unset_server(self, server):
        """
        Empties the slots which are occupied by the server, and recalculates the maximum number of consecutive slots
        """
        for i in range(server.size):
            self.slots[server.slot + i] = -1
        self.calculate_slots()

    def allocate_server(self, server):
        """
        Tries to allocate the server in the row
        ...
        Returns:
            Slot number in case the server is allocated
            -1 otherwise
        """
        n_slots = len(self.slots)

        if server.size > self.max_available_slots:
            return -1

        for slot in range(0, n_slots-server.size+1):
            if any(val != -1 for val in self.slots[slot:slot+server.size]):
                continue
            self.set_server(slot, server)
            return slot

        return -1

    def allocate_server_to_slot(self, server, slot):
        """
        Tries to allocate the server in the row in a given slot
        ...
        Returns:
            True in case the server is successfully allocated
            False otherwise
        """
        if server.size > self.max_available_slots: 
            return False
        
        if len(self.slots)-slot < server.size:
            return False
            
        if any(val != -1 for val in self.slots[slot:slot+server.size]): 
            return False
        self.set_server(slot, server)
        return True


    def calculate_slots(self):
        """
        Calculates the maximum number of consecutive slots
        """
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
