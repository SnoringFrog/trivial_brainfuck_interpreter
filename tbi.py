import re
import sys

#TODO:
#   arguments for common bf trivial substitutions
#   option to supply string to represent all commands
#   options to toggle wrapping/negative cells/etc
#   debugging options?
#       print tape, at least

cells = 30000
cell_bits = 8

tape = [0]*cells
ptr = 0

loop_idx_stack = {}

commands = ['<', '>', '+', '-', '.', ',', '[', ']']

### Core brainfuck commands
def lft():
    #move pointer left
    global ptr
    if ptr > 0:
        ptr-=1

def rht():
    #move pointer right
    global ptr
    if ptr < cells:
        ptr+=1

def inc():
    #increment
    val(1)

def dec():
    #decrement
    val(-1)

def out():
    #output
    global ptr
    print(chr(tape[ptr]))

def ipt():
    #input
    global ptr
    tape[ptr] = ord(sys.stdin.read(1))


### Helper commands
def val(dir=1):
    #change cell value
    # dir should be 1 or -1
    global ptr
    tape[ptr] = (tape[ptr] + dir) % (2**cell_bits)

def cmd(new_commands):
    #set list of commands
    a=1

def trm():
    #remove comment characters (regex)
    global source

    source = re.sub("[^"+re.escape(''.join(commands))+"]", '', source)

def trs():
    #translate to bf 
    a=1

def bal():
    #check loop balance
    a=1

def qbl():
    #quick loop balance pre-check
    if source.count(commands[6]) != source.count(commands[7]):
        print("Unbalanced loops")
        sys.exit(1)

def prs(source):
    #parse the source code
    a=1

### Main 

# Handle args
#   tbi -[args] file
#       -c list of commands to replace default bf
#           if 8 characters, read one for one
#           if <8, fail
#           if >8 and < 15, fail
#           if >15, assume comma separated unless -f was used
#       -f set command separator
#       -w turn off cell value wrapping
#       -l make tape loop (instead of just sitting at the start
#       -b change cell bit size
#       -t change tape size
#       -e change how EOF is handled for in-code input?


# Set up command list


# Get input (stdin, stream, file (mainly file)
with open('aa', 'r') as bf_file:
    source=bf_file.read()
bf_file.closed
    
qbl()
trm()
print(source)

