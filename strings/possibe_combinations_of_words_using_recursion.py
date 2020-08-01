def get_combinations_of_words(keyboard, inputs, index=0, comp=""):
    if index==len(inputs):
        if comp!=None:
            print(comp)
        return
    words=keyboard[inputs[index]]
    for i in words:
        get_combinations_of_words(keyboard, inputs, index+1, comp+i)

    
    
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
get_combinations_of_words(keyboard, inputs)
