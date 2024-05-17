from automata import Automata

# Construction d'un premier automate
Sigma = {'a', 'b'}
states = {0, 1, 2}
trans = {
    0: {'a': {1}},
    1: {'b': {1, 2}, 'a': {1}}
}
ini = {0}
final = {2}
# A l'aide du constructeur de la classe
A = Automata(Sigma, states, trans, ini, final)
#print(A)

# Construction du même automate
# à l'aide des méthodes de la classe
Abis = Automata(Sigma, set(), {}, set(), set())
#print(Abis)
'''Abis.add_state(0)
Abis.add_state(1)
Abis.add_state(2)
Abis.set_initial(0)
Abis.set_final(2)
Abis.add_transition(0, 'a', 1)
Abis.add_transition(1, 'a', 1)
Abis.add_transition(1, 'b', 1)
Abis.add_transition(1, 'b', 2)
print(Abis)'''

#construction de l'automate de la figure 2
Auto1 = Automata(Sigma, set(), {},set(),set() )
Auto1.add_state(0)
Auto1.add_state(1)
Auto1.add_state(2)
Auto1.add_state(3)
Auto1.set_initial(0)
Auto1.set_final(3)
Auto1.add_transition(0, 'b', 1)
Auto1.add_transition(0, 'a', 0)
Auto1.add_transition(0, 'b', 0)
Auto1.add_transition(1, 'a', 2)
Auto1.add_transition(2, 'b', 3)
Auto1.add_transition(3, 'a', 3)
Auto1.add_transition(3, 'b', 3)
#print(Auto1)
#print(Abis.is_deterministic())

Abis.add_state(0)
Abis.add_state(1)
Abis.add_state((1,2))
Abis.set_initial(0)
Abis.set_final((1,2))
Abis.add_transition(0, 'a', 1)
Abis.add_transition(1, 'a', 1)
Abis.add_transition(1, 'b', (1,2))
Abis.add_transition((1,2), 'a', 1)
Abis.add_transition((1,2), 'b', (1,2))
#print(Abis)
#print(Abis.is_deterministic())
#print(Auto1.is_deterministic(True))
#print(Abis.is_complete())
#first=Abis.states
#print(Abis.compute_next(first,'b'))
#print(Abis.accept('b'))

#print(Auto1.reachable_states())

#print(Auto1.final)
#Auto1.complement_DFA()
#print(Auto1.final)






