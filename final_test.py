from automata import Automata


Sigma = {'a', 'b'}
states = {0, 1, 2}
trans = {
    0: {'a': {0},'b': {1}},
    1: {'b': {1, 2} , 'a': {0}},
    2: {'a': {1},'b': {2}}
}
ini = {1}
final = {1,2}
A = Automata(Sigma, states, trans, ini, final)
B = A.make_deterministic()
print(B)


statesC={0,1}
transC= {
    0: {'a': {0},'b':{0,1}}
}
iniC = {0}
finalC = {1}
C = Automata(Sigma, statesC, transC, iniC, finalC)
C2= C.make_deterministic()
print(C2)
assert(C.accept("abb") == True)
assert(C2.accept("abb") == True)
assert(C.accept("a") == False)
assert(C2.accept("a") == False)

statesD={0,1,2,3}
transD= {
    0: {'a':{0},'b':{0,1}},
    1: {'a':{2}},
    2: {'b':{3}},
    3: {'a':{3},'b':{3}},
}
iniD = {0}
finalD ={3}
D = Automata(Sigma, statesD, transD, iniD, finalD)
D2= D.make_deterministic()
print(D2)
assert(D.accept("ababb") == True)
assert(D2.accept("ababb") == True)
assert(D.accept("abb") == False)
assert(D2.accept("abb") == False)

statesM={0,1,2,3,4}
transM= {
    0: {'a':{0,1},'b':{0}},
    1: {'a':{2},'b':{2}},
    2: {'a':{3},'b':{3}},
    3: {'a':{4},'b':{4}},
}
iniM={0}
finalM={4}
M = Automata(Sigma, statesM, transM, iniM, finalM)
M2= M.make_deterministic()
print(M2)
assert(M.accept("ababab") == True)
assert(M2.accept("ababab") == True)
assert(M.accept("abb") == False)
assert(M2.accept("abb") == False)

statesE={0,1,2,3,4,5}
transE= {
    0: {'a':{0,1},'b':{0}},
    1: {'a':{2},'b':{2}},
    2: {'a':{3},'b':{3}},
    3: {'a':{4},'b':{4}},
    4: {'a':{5},'b':{5}}
}
iniE={0}
finalE={5}
E = Automata(Sigma, statesE, transE, iniE, finalE)
E2= E.make_deterministic()
print(E2)
assert(E.accept("abababa") == True)
assert(E2.accept("abababa") == True)
assert(E.accept("abb") == False)
assert(E2.accept("abb") == False)