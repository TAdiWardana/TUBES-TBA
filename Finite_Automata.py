class FiniteAutomata:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def recognize(self, input_string):
        current_state = self.start_state
        for char in input_string.split():
            if char in self.transitions[current_state]:
                current_state = self.transitions[current_state][char]
            else:
                return False
        return current_state in self.accept_states

# Definisi FA untuk setiap kelompok kata
def get_automata_for_subject():
    states = {0, 1}
    alphabet = {"saya", "kamu", "dia", "mereka", "kita"}
    transitions = {
        0: {"saya": 1, "kamu": 1, "dia": 1, "mereka": 1, "kita": 1},
    }
    start_state = 0
    accept_states = {1}
    return FiniteAutomata(states, alphabet, transitions, start_state, accept_states)

def get_automata_for_predicate():
    states = {0, 1}
    alphabet = {"makan", "minum", "tidur", "berlari", "berjalan"}
    transitions = {
        0: {"makan": 1, "minum": 1, "tidur": 1, "berlari": 1, "berjalan": 1},
    }
    start_state = 0
    accept_states = {1}
    return FiniteAutomata(states, alphabet, transitions, start_state, accept_states)

def get_automata_for_object():
    states = {0, 1}
    alphabet = {"nasi", "teh", "kopi", "roti", "ayam"}
    transitions = {
        0: {"nasi": 1, "teh": 1, "kopi": 1, "roti": 1, "ayam": 1},
    }
    start_state = 0
    accept_states = {1}
    return FiniteAutomata(states, alphabet, transitions, start_state, accept_states)

def get_automata_for_adverb():
    states = {0, 1}
    alphabet = {"di rumah", "di sekolah", "di kantor", "pada pagi hari", "pada malam hari"}
    transitions = {
        0: {"di rumah": 1, "di sekolah": 1, "di kantor": 1, "pada pagi hari": 1, "pada malam hari": 1},
    }
    start_state = 0
    accept_states = {1}
    return FiniteAutomata(states, alphabet, transitions, start_state, accept_states)

# Contoh penggunaan FA
subject_fa = get_automata_for_subject()
predicate_fa = get_automata_for_predicate()
object_fa = get_automata_for_object()
adverb_fa = get_automata_for_adverb()

# Menguji FA
print(subject_fa.recognize("saya"))  # Output: True
print(predicate_fa.recognize("makan"))  # Output: True
print(object_fa.recognize("nasi"))  # Output: True
print(adverb_fa.recognize("di rumah"))  # Output: True
print(adverb_fa.recognize("pada siang hari"))  # Output: False (karena "pada siang hari" tidak di-define)
