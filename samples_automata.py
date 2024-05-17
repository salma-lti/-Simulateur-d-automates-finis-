""" Some input automata useful to check functions
    from the class Automata """

from automata import *
from random import *

# B1: (a+b)^*
Sigma = {'a', 'b'}
states_1 = {0}
ini_1 = {0}
final_1 = {0}
trans_1 = {
    0: {'a': {0}, 'b': {0}},
}
B1 = Automata(Sigma, states_1, trans_1, ini_1, final_1)

# B2: |w|_a = 0 modulo 2
Sigma = {'a', 'b'}
states_2 = {0, 1}
ini_2 = {0}
final_2 = {0}
trans_2 = {
    0: {'a': {1}, 'b': {0}},
    1: {'a': {0}, 'b': {1}}
}
B2 = Automata(Sigma, states_2, trans_2, ini_2, final_2)

# B3: (a+b)^*.b
Sigma = {'a', 'b'}
states_3 = {0, 1}
ini_3 = {0}
final_3 = {1}
trans_3 = {
    0: {'a': {0}, 'b': {1}},
    1: {'a': {0}, 'b': {1}}
}
B3 = Automata(Sigma, states_3, trans_3, ini_3, final_3)
# B4: (a+b)^*.b  (non-deterministic)
Sigma = {'a', 'b'}
states_4 = {0, 1}
ini_4 = {0}
final_4 = {1}
trans_4 = {
    0: {'a': {0}, 'b': {0,1}},
    1: {}
}
B4 = Automata(Sigma, states_4, trans_4, ini_4, final_4)

for B in [B1, B4]:
    print("***   New Automaton  ***")
    #B.text_display()
    print("is deterministic:",B.is_deterministic(True))
    print("is complete:", B.is_complete(True))
    print("is empty:", B.is_empty())
    print("reachable states:",B.reachable_states())
    print("Test acceptance")
    for i in range(10):
        list_symbols = list(B.alphabet)
        word = "".join([choice(list_symbols) for i in range(randrange(10))])
        print("Test",i," : accepte",word,B.accept(word))


for B in [B1, B4]:
    reachable = B.reachable_states()
    assert B.ini.issubset(reachable), "Initial states not reachable"

empty_automaton = Automata(set(),set(),dict(),set(),set())   
assert empty_automaton.is_empty() == True, "Automaton is not empty"

B32 = B3.intersection(B2)
print(B2.ini)
print(B32)
assert B32.accept("aab") == True

print(B3.ini)
print(B32.accept("aaab"))

assert B32.accept("aaab") == False
assert B32.accept("a") == False
assert B32.accept("b") == True
assert B32.accept("bbbbba") == False

b32 = B3.union(B2)
assert b32.accept("aab") == True
assert b32.accept("aaab") == True
assert b32.accept("aa") == True
assert b32.accept("b") == True
assert b32.accept("bbbbba") == False

B3.complement_DFA()
assert B3.accept("aab") == False
assert B3.accept("aa") == True
assert B3.accept("aaba") == True
assert B3.accept("abb") == False
B3.complement_DFA()
for B in [B1, B2, B3, B4]:
    assert B.check_inclusion_DFA(B1)
assert B3.check_equivalence_DFA(B3)

B2.mirror()
assert B2.accept("aa") == True
assert B2.accept("aab") == True
assert B2.accept("aaba") == False
assert B2.accept("bba") == False

B2.mirror()
assert B2.co_reachable_states() == B2.states
assert B3.useful_states() == B3.states

B2.add_state(10)
assert 10 in B2.states
B2.trim()
print(B2.states)
assert 10 not in B2.states