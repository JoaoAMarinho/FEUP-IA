# **Optimize a Data Center**

## **Problem**

### **Slots**

A data center is modeled as rows of slots in which servers can be placed, example:

    [Empty, Empty, Empty, Empty, Empty]
    [Empty, Empty, Empty, Unavailable, Empty]
    [Empty, Empty, Empty, Unavailable, Unavailable]


Some of the slots might be unavailable (as seen above).

### **Servers**

Each server is characterized by its size and capacity. 

Size is the number of consecutive slots occupied by the machine.

Capacity is the total amount of CPU resources of the machine (an integer value).

### **Input**

``` py
R S U P M
U (lines)
M (lines)
```
R - number of rows

S - number of slots in each row

U - number of unavailable slots

P - number of pools

M - number of servers

Next U lines describe the pos of unavailable slots (r,s), row and column.

Next M lines describe the size of server and capacity (z, c).

### **Task**

If a shared resource fails (row), we assume that the entire row is lost and all servers in that row become unavailable.

Servers in a data center are also logically **divided into pools**.

The **guaranteed capacity** of a pool is the minimum capacity it will have when at most one data center row goes down.

The goal is to assign servers to **slots within the rows** and to **logical pools** so that the **lowest guaranteed capacity** of all pools is maximized.