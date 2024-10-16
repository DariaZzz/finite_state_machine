class Queue:

    def __init__(self):
        self.queue = list()

    def add_element(self, val):
        # Insert method to add element
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False

    def __getitem__(self, item):
        return self.queue[item]

    # Pop method to remove element
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty")

    def size(self):
        return len(self.queue)


print("Enter set of states: ")
set_of_states = set(input().split())
# # print(set_of_states)
#
print("Enter the input alphabet: ")
alphabet = input().split()
# print(alphabet)

print("Enter state-transitions function (current state, input character, next state):")
state_transition = input().split()
state_transition = [i.split(',') for i in state_transition]
for g in range(len(state_transition)):
    state_transition[g] = [i.replace('(', '').replace(')', '') for i in state_transition[g]]
# print(state_transition)

print("Enter a set of initial states: ")
initial_states = input().split()

print("Enter a set of final states:")
final_states = input().split()


new_set_of_states = set(initial_states)
states = Queue()
for el in initial_states:
    states.add_element(el)
k = 0
res = {}

while states.size() > 0:
    state = states[-1]
    for letter in alphabet:
        new_state = set()
        for g in state_transition:
            if g[1] == letter and g[0] in str(state):
                new_state.add(g[2])
        new_state = sorted(new_state)
        if new_state:
            if ''.join(new_state) not in new_set_of_states:
                states.add_element(''.join(new_state))
                new_set_of_states.add(''.join(new_state))
            if state not in res:
                res[str(state)] = [[letter, new_state]]
            else:
                res[str(state)].append([letter, new_state])
    states.pop()

new_final_states = set()
for a in sorted(new_set_of_states):
    for b in sorted(final_states):
        if b in a:
            new_final_states.add(a)

print("DFA")
print("Set of states: ", end="")
print(", ".join(sorted(new_set_of_states)))

print("Input alphabet: ", end="")
print(", ".join(alphabet))

print("State-transitions function:")
for key in sorted(res.keys()):
    for g in res[key]:
        print(f"D({key}, {g[0]}) = {''.join(g[1])}")

print("Initial states: ")
print(", ".join(initial_states))

print("Final states: ")
print(", ".join(sorted(new_final_states)))


