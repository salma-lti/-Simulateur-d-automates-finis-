"""

A class to deal with finite-state automata
P.-A. Reynier, Feb. 2023

"""

import copy
from itertools import product

class Automata:
    def __init__(self, alphabet, states, trans, ini, final):
        """
        :param alphabet: set of symbols
        :param states: set of states
        :param trans: dictionary giving transitions
        :param ini: set of initial states
        :param final: set of final states
        """
        self.alphabet = alphabet
        self.states = states
        self.trans = trans
        self.ini = ini
        self.final = final


    def add_state(self, state):
        """
        :param state: state to be added
        :return: 1 if state successfuly added, 0 otw
        """
        if state in self.states:
            print("Error while adding state: already present")
            return 0
        try: 
            self.states.add(state)
        except:
            print("Error while adding state: set error")
            return 0
        return 1


    def add_transition(self, source, label, target): 
        """
        :param source: source state
        :param label: label of the transition
        :param target: target state
        :return: 1 if transition successfuly added, 0 otw
        """
        if source not in self.states:
            print("Error while adding transition: source state not in states")
            return 0
        if target not in self.states:
            print("Error while adding transition: target state not in states")
            return 0
        if label not in self.alphabet:
            print("Error while adding transition: label not in alphabet")
            return 0
        # source is not a key of self.trans
        if source not in self.trans:
            self.trans[source] = {}
            self.trans[source][label]={target}
        # source is a key of self.trans
        else:
            # label is not a key of self.trans[source]
            if label not in self.trans[source]:
                self.trans[source][label]={target}
            # label is a key of self.trans[source]
            else:
                self.trans[source][label].add(target)
        return 1               


    def set_initial(self,state):
        """
        :param state: a state
        :return: 1 if modification suceeded, 0 otw
        """
        if state in self.states:
            self.ini.add(state)
            return 1
        else:
            return 0


    def set_final(self,state):
        """
        :param state: a state
        :return: 1 if modification suceeded, 0 otw
        """
        if state in self.states:
            self.final.add(state)
            return 1
        else:
            return 0


    def __str__(self):
        """ Overrides print function """
        res = "Display Automaton\n"
        res += "Alphabet: " + str(self.alphabet) +"\n"
        res += "Set of states: "+str(self.states) +"\n"
        res += "Initial states "+str(self.ini) + "\n"
        res += "Final states "+str(self.final) + "\n"
        res += "Transitions:"+"\n"
        for source in self.trans:
            for label in self.trans[source]:
                for target in self.trans[source][label]:
                    res += "Transition from "+str(source)+" to "+str(target)+" labelled by "+str(label)+"\n"
        return res


    def is_deterministic(self,verbose=False):
        """
        :return: True if the automaton is deterministic, False otherwise
        """
        # Checks the number of initial states
        if len(self.ini) != 1:
            if verbose:
                print("Too many initial states")
            return False
        # Loop over source states
        for source in self.trans:
            # Loop over labels
            for label in self.trans[source]:
                # Check whether there are two transitions with same
                # source state and label
                if len(self.trans[source][label]) > 1:
                    if verbose:
                        print("Too many outgoing transitions from 0 labelled by a")
                    return False
        return True

    def is_complete(self,verbose=False):
        """
        :return: True if the automaton is complete, False otherwise
        """
        for state in self.states:
             for alphabet in self.alphabet:
                if alphabet not in self.trans[state]:
                    return False
                if len(self.trans[state][alphabet]) == 0:
                    return False  
        return True


    def compute_next(self, X, sigma):
        """
        :param X: set of states
        :param sigma: symbol of the alphabet
        :return: a set of states corresponding to one-step successors of X by reading sigma
        """
        res = set()
        for state in X:
            if state not in self.trans:
                continue
            if sigma in self.trans[state]:
                
                res.update(self.trans[state][sigma])
        return res


    def accept(self, word):
        """
        :param word: string on the alphabet
        :return: True if word is accepted, False otw
        """
        X=self.ini.copy()
        for char in word:
            X = self.compute_next(X,char)
        X = X.intersection(self.final)
        if (len(X)==0):
            return False
        return True


    def reachable_states(self):
        """
        Computes the of states reachable from the initial ones
        :return: the set of reachable states
        """
        X = self.ini
        Y = set()
        while (X!=Y):
            Y = X.copy()
            for alphabet in self.alphabet:
                print(X)
                X.update(self.compute_next(X,alphabet))
        return X


    def is_empty(self):
        """
        Checks whether the automaton accepts no word. Proceeds by checking
        whether there exists a final state reachable from an initial one.
        :return: True if the language of the automaton is empty, False otherwise
        """
        if (len(self.reachable_states().intersection(self.final)) ==0):
            return True
        return False

    def intersection(self,other):
        """
        :param other: an automaton
        :return: a new automaton whose language is the intersection
        """
        new_states = set()
        for i in self.states:
            for j in other.states:
                new_states.add((i,j))
        new_alphabet = self.alphabet.intersection(other.alphabet)
        new_ini_states = set(product(self.ini,other.ini))
        print(self.ini,other.ini)
        print(new_ini_states)
        new_final_states = set(product(self.final,other.final))
        new_transitions = dict()
        for letter in new_alphabet:
            for state in new_states:
                states1 = self.compute_next({state[0]},letter)
                states2 = other.compute_next({state[1]},letter)
                new_trans = set(product(states1,states2))
                if state not in new_transitions:
                    new_transitions[state]=dict()
                if letter not in new_transitions[state]:
                    new_transitions[state][letter]=set()
                for trans in new_trans:
                    new_transitions[state][letter].add(trans)
        return Automata(new_alphabet,new_states,new_transitions,new_ini_states,new_final_states)

    def union(self,other):
        """
        :param other: an automaton
        :return: a new automaton whose language is the union
        """
        new_states = set()
        for i in self.states:
            for j in other.states:
                new_states.add((i,j))
        new_alphabet = self.alphabet.union(other.alphabet)
        new_ini_states = set(product(self.ini,other.ini))
        new_final_states = set()
        for final in self.final:
            for state in other.states:
                new_final_states.add((final,state))
        for final in other.final:
            for state in self.states:
                new_final_states.add((state,final))
        new_transitions = dict()
        for letter in new_alphabet:
            for state in new_states:
                states1 = self.compute_next({state[0]},letter)
                states2 = other.compute_next({state[1]},letter)
                new_trans = set(product(states1,states2))
                if state not in new_transitions:
                    new_transitions[state]=dict()
                if letter not in new_transitions[state]:   
                    new_transitions[state][letter]=set()
                for trans in new_trans:
                    new_transitions[state][letter].add(trans)
        return Automata(new_alphabet,new_states,new_transitions,new_ini_states,new_final_states)
    
    def complement_DFA(self):
        """
        Modifies the current automaton to the complement
        """
        self.final= self.states.copy() - self.final

    def check_inclusion_DFA(self, other):
        complement = other.copy()
        complement.complement_DFA()
        return self.copy().intersection(complement).is_empty() 
    
    def check_equivalence_DFA(self, other):
        return self.check_inclusion_DFA(other) and other.check_inclusion_DFA(self)

    def mirror(self):
        new_trans = dict()
        for state in self.states:
            new_trans[state]= {}
            if state not in self.trans:
                continue
            for alph in self.trans[state]:
                new_trans[state][alph] = set()
        for source_state, transitions in self.trans.items():
            for symbol, target_states in transitions.items():
                for target_state in target_states:
                    new_trans[target_state][symbol].add(source_state)
        self.trans = new_trans

    def co_reachable_states(self):
        mirrored = self.copy()
        mirrored.mirror()
        return mirrored.reachable_states() 
    
    def useful_states(self):
        Co_reachable = self.co_reachable_states()
        reachable = self.reachable_states()
        return Co_reachable.intersection(reachable)
    def trim(self):
        unuseful_states = self.states.difference(self.useful_states())
        self.ini -= unuseful_states
        self.final -= unuseful_states
        self.states -= unuseful_states
        new_trans = dict()
        for state in self.useful_states():
            new_trans[state]= {}
            for alph in self.trans[state]:
                new_trans[state][alph] = set()
        for source_state, transitions in self.trans.items():
            for symbol, target_states in transitions.items():
                if source_state not in unuseful_states:
                    for target_state in target_states:
                        if target_state not in unuseful_states:
                            new_trans[target_state][symbol].add(source_state)
        self.trans = new_trans

    def copy(self):
        return Automata(self.alphabet.copy(),self.states.copy(),self.trans.copy(),self.ini.copy(),self.final.copy())

    def make_deterministic(self):
        new_states = [self.ini]
        new_finals = set() 
        new_initial = {0}
        new_trans = dict()
        wait = set()
        for alph in self.alphabet:
            wait.add((0,alph))
        while len(wait) != 0:
            X, alpha = wait.pop()
            reached = self.compute_next(new_states[X],alpha)
            if reached not in new_states:
                new_states.append(reached)
                for alph in self.alphabet:
                    wait.add((len(new_states)-1,alph))
                if len(reached.intersection(self.final)) != 0:
                    new_finals.add(len(new_states)-1)
            if X not in new_trans:
                new_trans[X] = dict()
            if alpha not in new_trans[X]:
                new_trans[X][alpha] = set()
            new_trans[X][alpha].add(new_states.index(reached))
        return Automata(self.alphabet,set(range(0,len(new_states))),new_trans,new_initial,new_finals)

    def check_equivalence(self,B):
        A = self.make_deterministic()
        return A.check_equivalence_DFA(B.make_deterministic())
    
    def check_inclusion(self,B):
        A = self.make_deterministic()
        return A.check_inclusion_DFA(B.make_deterministic())
