#Name: Nicholas Vickery
#Date: 3/6/2024
#project: Linked List pt2


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node=node(data)
        cur=self.head #address of head node of the list
        while cur.next != None:
            cur=cur.next
        cur.next=new_node

    def insert(self, data):
        new_node = node(data)
        cur = self.head
        # Find the correct position for the new node
        while cur.next != None and cur.next.data < data:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def length(self):
        cur=self.head
        total = 0
        while cur.next !=None:
            total+=1
            cur=cur.next
        return total
    
    def delete(self, data):
        cur = self.head
        while cur.next is not None:
            if cur.next.data == data:
                cur.next = cur.next.next
                return  # Stops after removing the first occurrence
            cur = cur.next

    def remove(self, data):
        cur = self.head
        while cur.next is not None:
            if cur.next.data == data:
                cur.next = cur.next.next
            else:
                cur = cur.next
    def display(self):
        elems= []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)



mylist = linked_list()

# Function to handle user input for inserting numbers
def handle_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = user_input.split()
        
        if all(number.isdigit() for number in numbers):  # Check if all inputs are numbers
            valid_input = True  # Exit the loop if all inputs are valid numbers
            for number in numbers:
                mylist.insert(int(number))
        else:
            print("Error: Please enter numbers only.")

handle_user_input()
mylist.display()

# Function to handle deletion of a single node
def delete_single_node():
    try:
        data_to_delete = int(input("Enter a value to delete (first occurrence): "))
        mylist.delete(data_to_delete)
    except ValueError:
        print("Please enter a valid number.")

delete_single_node()
mylist.display()

# Function to handle removal of nodes with matching data
def remove_nodes():
    try:
        data_to_remove = int(input("Enter a value to remove (all occurrences): "))
        mylist.remove(data_to_remove)
    except ValueError:
        print("Please enter a valid number.")

remove_nodes()
mylist.display()

# Display the length of the list
print("Length:", mylist.length())