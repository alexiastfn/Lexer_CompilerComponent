from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class DFA[STATE]:
    S: set[str]
    K: set[STATE]
    q0: STATE
    d: dict[tuple[STATE, str], STATE]
    F: set[STATE]

    def __init__(self, S: set[str], K: set[STATE], q0: STATE, d: dict[tuple[STATE, str], STATE], F: set[STATE]):
        self.S = S
        self.K = K
        self.q0 = q0
        self.d = d
        self.F = F

    def accept(self, word: str) -> bool:
        # simulate the dfa on the given word. return true if the dfa accepts the word, false otherwise
        this_state = self.q0

        for w in word:
            key = (this_state, w)
            if not key in self.d:
                return False
            this_state = self.d[(this_state, w)]
        return this_state in self.F

    def remap_states[OTHER_STATE](self, f: Callable[[STATE], 'OTHER_STATE']) -> 'DFA[OTHER_STATE]':
        # optional, but might be useful for subset construction and the lexer to avoid state name conflicts.
        # this method generates a new dfa, with renamed state labels, while keeping the overall structure of the
        # automaton.

        # for example, given this dfa:

        # > (0) -a,b-> (1) ----a----> ((2))
        #               \-b-> (3) <-a,b-/
        #                   /     ⬉
        #                   \-a,b-/

        # applying the x -> x+2 function would create the following dfa:

        # > (2) -a,b-> (3) ----a----> ((4))
        #               \-b-> (5) <-a,b-/
        #                   /     ⬉
        #                   \-a,b-/

        pass

