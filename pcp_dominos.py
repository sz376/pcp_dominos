import sys

domino_dict = {}
trailing_dict = {}
domino_count = 0
open_queue = []
visited = []
max_states = 0
max_queue_length = 0
goal_state_found = False
deepening_count = 0
print_sequence_flag = 0


class Node:
    def __init__(self, top, bottom, parentNode=None, parent_index=0):
        self.top = top
        self.bottom = bottom
        self.parentNode = parentNode
        self.parent_index = parent_index

    def is_valid_state(self, print_sequence_flag):
        if self in visited or self in open_queue:
            return False
        top = self.top
        bottom = self.bottom
        if top.startswith(bottom):
            trailing = "+" + top.replace(bottom, "", 1)
            if trailing not in trailing_dict:
                if print_sequence_flag == 1:
                    print("Adding State to Frontier:" + trailing)
                trailing_dict[trailing] = 1
                return True
            else:
                return False
        elif bottom.startswith(top):
            trailing = "-" + bottom.replace(top, "", 1)
            if trailing not in trailing_dict:
                if print_sequence_flag == 1:
                    print("Adding State to Frontier:" + trailing)
                trailing_dict[trailing] = 1
                return True
            else:
                return False
        else:
            return False

    def is_goal_state(self):
        top = self.top
        bottom = self.bottom
        if top == bottom:
            return True
            goal_state_found = True

    def generate_child_nodes(self, searchtypeflag, print_sequence_flag):
        visited.append(self)
        if searchtypeflag == 0:
            top = open_queue[0].top
            bottom = open_queue[0].bottom
            if top.startswith(bottom):
                trailing = "+" + top.replace(bottom, "", 1)
                if trailing in trailing_dict:
                    if print_sequence_flag == 1:
                        print("Removing State from Frontier:" + trailing)
                    trailing_dict[trailing] = 0
            elif bottom.startswith(top):
                trailing = "-" + bottom.replace(top, "", 1)
                if trailing in trailing_dict:
                    if print_sequence_flag == 1:
                        print("Removing State from Frontier:" + trailing)
                    trailing_dict[trailing] = 0
            open_queue.pop(0)
        elif searchtypeflag == 1:
            top = open_queue[0].top
            bottom = open_queue[0].bottom
            if top.startswith(bottom):
                trailing = "+" + top.replace(bottom, "", 1)
                if trailing in trailing_dict:
                    if print_sequence_flag == 1:
                        print("Popping State from Stack:" + trailing)
                    trailing_dict[trailing] = 0
            elif bottom.startswith(top):
                trailing = "-" + bottom.replace(top, "", 1)
                if trailing in trailing_dict:
                    trailing_dict[trailing] = 0
                    if print_sequence_flag == 1:
                        print("Popping State from Stack:" + trailing)
            global deepening_count
            deepening_count += 1
            open_queue.pop(0)
        for index in domino_dict.keys():
            current_top = self.top
            current_bottom = self.bottom
            first_string = domino_dict[index][0]
            second_string = domino_dict[index][1]
            new_node = Node(
                current_top + first_string, current_bottom + second_string, self, index
            )
            if new_node.is_valid_state(print_sequence_flag):
                if new_node.is_goal_state():
                    if searchtypeflag == 0 and print_sequence_flag == 1:
                        print("----- Part 1 (BFS) Ending -----")
                    elif searchtypeflag == 1 and print_sequence_flag == 1:
                        print("----- Part 2 (Iterative Deepening) Ending -----")
                    print_results(1, new_node, 1, print_sequence_flag)

                if len(open_queue) < max_queue_length:
                    if searchtypeflag == 0:
                        open_queue.append(new_node)
                        if len(open_queue) == max_queue_length:
                            print("----- Frontier Complete -----")
                            print("----- Part 2 (Iterative Deepening) Starting -----")
                            print(
                                "Starting DFS with max queue length set to: "
                                + str(max_queue_length)
                            )
	# end node class #

    def print_solution_sequence(self):
        sequence = []
        while self.parentNode:
            sequence.append("D" + str(self.parent_index))
            self = self.parentNode
        print("The solution sequence is: %s" % sequence[::-1])


def graph_search(self):
    states = 0
    while (
        states < max_states
        and goal_state_found == False
        and len(open_queue) < max_queue_length
    ):
        if open_queue == []:
            print_results(0, None, 0, print_sequence_flag)
        open_queue[0].generate_child_nodes(0, print_sequence_flag)
        states += 1
	# Iterative deeping start
    while states < max_states and goal_state_found == False:
        if open_queue == []:
            print_results(0, None, 0, print_sequence_flag)
        open_queue[0].generate_child_nodes(1, print_sequence_flag)
        states += 1
    print_results(0, None, 1, print_sequence_flag)


def initialize_graph():
    initial_state = Node('', '')
    open_queue.append(initial_state)
    initial_state.generate_child_nodes(0, print_sequence_flag)
    graph_search(initial_state)


def print_results(solutionFound, Node, solutionExists, printSequenceFlag):
    if solutionFound == 0 and solutionExists == 1:
        print("No solution found within bounds")
    elif solutionFound == 1:
        print("Solution Size (# of dominoes): " + str(domino_count))
        print(
            "The top and bottom of the sequence looks like: "
            + Node.top
            + "/"
            + Node.bottom
        )
        Node.print_solution_sequence()
    elif solutionExists == 0:
        print("No solution exists")
    sys.exit()


def main():

    input = open("input1.txt", "r")
    # input = open("input2.txt", "r")
    # input = open("input3.txt", "r")
    # input = open("input4.txt", "r")
    input_lines = input.readlines()

    global max_queue_length
    max_queue_length = int(input_lines[0])
    global max_states
    max_states = int(input_lines[1])
    global print_sequence_flag
    print_sequence_flag = int(input_lines[2])
    global domino_count
    domino_count = int(input_lines[3])
    dominos = input_lines[4:]
    for domino in dominos:
        index = domino.split()[0]
        top_string = domino.split()[1]
        bottom_string = domino.split()[2]
        domino_dict[index] = [top_string, bottom_string]

    initialize_graph()


if __name__ == "__main__":
    main()
