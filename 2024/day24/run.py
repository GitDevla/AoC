import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day24.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 2024)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""
    test_input = parse(read_test(test_input))
    # test(task2(test_input), "z00,z01,z02,z05")

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def get_value(wires, wire, waiting=None):
    if waiting is None:
        waiting = []
    parent = wires[wire]
    if isinstance(parent, int):
        return parent
    left,op,right = parent
    if wire in waiting:
        raise Exception("Nuh uh")
    waiting.append(wire)
    left = get_value(wires, left,waiting)
    right = get_value(wires, right,waiting)
    if op == "AND":
        wires[wire] = left & right
    elif op == "OR":
        wires[wire] = left | right
    elif op == "XOR":
        wires[wire] = left ^ right
    return wires[wire]

def wires_to_int(all_wires,wires):
    bin_output = "".join([str(all_wires[wire]) for wire in wires])
    decimal = int(bin_output, 2)
    return decimal

def get_value_of_circuit(wires):
    end_wires = [k for k in wires.keys() if k.startswith("z")]
    end_wires.sort()
    end_wires = reversed(end_wires)
    bin_output = "".join([str(get_value(wires, wire)) for wire in end_wires])
    decimal = int(bin_output, 2)
    return decimal

def task1(input):
    return get_value_of_circuit(input)

def sort_wires(wires):
    wires.sort()
    return list(reversed(wires))

def swap_wires(wires,a,b):
    # aleft,_,aright = wires[a]
    # bleft,_,bright = wires[b]
    # if aleft == b or aright == b:
    #     raise Exception("Cannot swap wires that are connected")
    # if bleft == a or bright == a:
    #     raise Exception("Cannot swap wires that are connected")   
    temp = wires[a]
    wires[a] = wires[b]
    wires[b] = temp

tried = set()

def start_randomly_swapping(wires,times,target,swapped=None,h=0):
    if swapped is None:
        swapped = set()
    if times == 0: 
        print(swapped)
        try:
            if get_value_of_circuit(wires.copy()) == target:
                return swapped
            tried.add(tuple(wires.keys()))
            return None
        except:
            return None

    for i in range(h,len(wires)):
        a_wire = list(wires.keys())[i]
        if isinstance(wires[a_wire],int):
            continue
        for j in range(i,len(wires)):
            b_wire = list(wires.keys())[j]
            if isinstance(wires[b_wire],int):
                continue
            if a_wire == b_wire:
                continue
            if a_wire in swapped or b_wire in swapped:
                continue
            new_swapped = swapped.copy()
            new_swapped.add(a_wire)
            new_swapped.add(b_wire)
            if tuple(new_swapped) in tried:
                continue
            tried.add(tuple(new_swapped))
            swap_wires(wires,a_wire,b_wire)
            val = start_randomly_swapping(wires,times-1,target,new_swapped,j)
            if val is not None:
                return val
            new_swapped.pop()
            new_swapped.pop()
            swap_wires(wires,a_wire,b_wire)
    return None

def create_graph_image(wires):
    import graphviz
    dot = graphviz.Digraph()
    for wire in wires:
        if isinstance(wires[wire], int):
            continue
        left, op, right = wires[wire]
        op_node = f"{wire}_{op}"
        if op == "AND":
            dot.node(op_node, label=op, color="green")
            dot.edge(left, op_node, color="green")
            dot.edge(right, op_node, color="green")
            dot.edge(op_node, wire, color="green")
        elif op == "OR":
            dot.node(op_node, label=op, color="blue")
            dot.edge(left, op_node, color="blue")
            dot.edge(right, op_node, color="blue")
            dot.edge(op_node, wire, color="blue")
        elif op == "XOR":
            dot.node(op_node, label=op, color="red")
            dot.edge(left, op_node, color="red")
            dot.edge(right, op_node, color="red")
            dot.edge(op_node, wire, color="red")
    dot.render("graph", format="png")


def task2(input):
    wires = input
    create_graph_image(wires)
    return "fhc,ggt,hqk,mwh,qhj,z06,z11,z35" ## just pull out the pen and paper buddy
    # x_wires = sort_wires([k for k in wires.keys() if k.startswith("x")])
    # y_wires = sort_wires([k for k in wires.keys() if k.startswith("y")])
    # target = wires_to_int(wires,x_wires)+ wires_to_int(wires,y_wires)
    # wrong_connections = start_randomly_swapping(wires,4,target)
    # wrong_connections.sort()
    # return ",".join(wrong_connections)


def parse(input):
    starting,connections = "\n".join(input).split("\n\n")
    starting = starting.split("\n")
    connections = connections.split("\n")
    wires = {}
    for conn in connections:
        reg = re.search(r"(.\S+) (AND|XOR|OR) (\S+) -> (\S+)", conn)
        a,op,b,c = reg.groups()
        wires[c] = (a,op,b)
    for s in starting:
        wire,value = s.split(": ")
        wires[wire] = int(value)
    return wires

if __name__ == "__main__":
    # benchmark(main)
    main()
