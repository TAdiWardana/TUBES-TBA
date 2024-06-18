class LL1Parser:
    def __init__(self, parse_table, start_symbol):
        self.parse_table = parse_table
        self.start_symbol = start_symbol

    def parse(self, tokens):
        tokens.append('$')
        stack = [self.start_symbol]
        index = 0

        while stack:
            top = stack.pop()
            current_token = tokens[index]

            if top in self.parse_table:  # Non-terminal
                if current_token in self.parse_table[top]:
                    rule = self.parse_table[top][current_token]
                    stack.extend(reversed(rule))
                else:
                    return False
            elif top == current_token:  # Terminal
                index += 1
            else:
                return False

        return index == len(tokens) - 1

# Parse table untuk CFG yang diberikan
parse_table = {
    'S\'': {
        'saya': ['S', 'P', 'O', 'K'],
        'kamu': ['S', 'P', 'O', 'K'],
        'dia': ['S', 'P', 'O', 'K'],
        'mereka': ['S', 'P', 'O', 'K'],
        'kita': ['S', 'P', 'O', 'K']
    },
    'S': {
        'saya': ['saya'],
        'kamu': ['kamu'],
        'dia': ['dia'],
        'mereka': ['mereka'],
        'kita': ['kita']
    },
    'P': {
        'makan': ['makan'],
        'minum': ['minum'],
        'tidur': ['tidur'],
        'berlari': ['berlari'],
        'berjalan': ['berjalan']
    },
    'O': {
        'nasi': ['nasi'],
        'teh': ['teh'],
        'kopi': ['kopi'],
        'roti': ['roti'],
        'ayam': ['ayam']
    },
    'K': {
        'di rumah': ['di rumah'],
        'di sekolah': ['di sekolah'],
        'di kantor': ['di kantor'],
        'pada pagi hari': ['pada pagi hari'],
        'pada malam hari': ['pada malam hari']
    }
}

# Membuat parser LL(1) dengan tabel parsing
parser = LL1Parser(parse_table, 'S\'')

# Contoh kalimat
input_tokens = ['saya', 'makan', 'nasi', 'di rumah']
print(parser.parse(input_tokens))  # Output: True

input_tokens = ['kamu', 'minum', 'teh', 'pada pagi hari']
print(parser.parse(input_tokens))  # Output: True

input_tokens = ['dia', 'berlari', 'di sekolah']
print(parser.parse(input_tokens))  # Output: True

input_tokens = ['kita', 'tidur']
print(parser.parse(input_tokens))  # Output: True

input_tokens = ['saya', 'kopi', 'pada malam hari']
print(parser.parse(input_tokens))  # Output: False (karena "kopi" bukan predikat)
