def get_combinations_of_words(keyboard, inputs):
    l=[i for i in keyboard[inputs[0]]]
    for j in range(1, len(inputs)):
        l=[p+c for p in l for c in keyboard[inputs[j]]]
    return l
keyboard=[
    [],
    [],
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
    ]
inputs=[2, 3, 4]
print(get_combinations_of_words(keyboard, inputs))
