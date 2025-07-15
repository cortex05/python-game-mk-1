grid = [
    [
        {
            'description': 'Can only go south\n',
            'options': [2]
        }, {
            'description': 'This is the castle, but you aren\'nt supposed to behere yet.\n',
            'options': [0, 2]
        }, {
            'description': "HOLDER",
            'options': []
        }],
    [
        {
            'description': "Can only go north or east",
            'options': [0, 1]
        }, {
            'description': 'To the Northeast you see a shed, to the west you see something shiny. Where will you go?\n',
            'random_battle': True,
            'options': [1, 3]
        }, {
            'description': "Monster and a dead end",
            'options': [3]
        }],
    [
        {
            'description': "Null",
            'options': "Null"
        }, {
            'description': 'You stand before a forest. The only way is through. What do you do?\n',
            'options': [0]
        }, {
            'description': "Null",
            'options': "Null"
        }
    ]
]
