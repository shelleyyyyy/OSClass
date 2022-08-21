from numpy import random


class PCB:
    def __init__(self, state, number, counter, memory, open_files):
        self.state = state
        self.number = number
        self.counter = counter
        self.memory = memory
        self.open_files = open_files

    def print_pcb(self):
        print("state: ", self.state)
        print("number: ", self.number)
        print("counter: ", self.counter)
        print("memory: ", self.memory)
        print("open_files: ", self.open_files)


input = input("Enter number of processes: ")

input = int(input)

processes = []

slices = []


def get_random(amt):
    ran = random.randint(amt)
    return ran


def gen_processes(amt):
    for i in range(amt):
        process = PCB("w", i, 0, "N/A", "N/A")
        processes.append(process)


def gen_slices(amt):
    for i in range(20):
        slices.append(get_random(amt))


def find_running():
    proc = 0
    for i in processes:
        if i.state == "r":
            return proc
        proc = proc + 1


def main_loop():
    gen_processes(input)
    gen_slices(input)
    for i in range(len(slices)):
        if i == 0:
            processes[slices[i]].state = "r"

        running = find_running()
        print("-------------- Time Slice: ", i, " process: ", slices[i], "-----------------")
        print("process: ", running, " is running")
        x = processes[running].counter
        processes[running].counter = x + 1
        print("program counter updated")
        print("--------- PCB ----------")
        processes[running].print_pcb()
        processes[running].state = "w"
        print("process: ", running, " is now waiting")
        print("-------------------------------")

        try:
            processes[slices[i + 1]].state = "r"
        except:
            break


if __name__ == '__main__':
    main_loop()
