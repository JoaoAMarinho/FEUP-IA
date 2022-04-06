class Row:
  def __init__(self, slots):
    self.slots = [ -1 for _ in range(slots) ]

  def set_unavailable(self, slot):
    self.slots[slot] = -2

  def set_server(self, slot, server):
    for i in range(server.size):
      self.slots[slot + i] = server.id

  def allocate_server(self, server):
    n_slots = len(self.slots)

    if server.size > len(self.slots): return False
    
    # for slot desde 0 até slots-size
    for slot in range(0, n_slots-server.size+1):
      if any(x != -1 for x in self.slots[slot:slot+server.size]): continue
      
      self.set_server(self, slot, server)
      