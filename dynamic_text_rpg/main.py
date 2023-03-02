inventory = {
    'key': False
}

def north_result():
    print('NORTH')

def south_result():
    inventory['key'] = True
    print('OWEN DIED OMG', 'but you did pick up a key! :D')

def run_conditions():
    return inventory['key'] == True

def run_result():
    inventory['key'] = False
    print('YOU RAN AWAY AND CONSUMED YOUR KEY')

prompts = [
    {
        'ask': 'A tall man with dark hair greets you nervously and asks you where you want to go',
        'choices': {
            'north': {
                'result': north_result
            },
            'south': {
                'result': south_result
            }
        }
    },
    {
        'ask': 'A tall man with blond hair attacks you and consumes your friends brain',
        'choices': {
            'run': {
                'conditions': run_conditions,
                'result': run_result,
            }
        }
    }
]

for prompt in prompts:

    selection = 'initial'

    while selection not in prompt['choices']:
        if selection != 'initial': print('Invalid input, try again')
    
        selection = input(prompt['ask'] + ': ')

    choice = prompt['choices'][selection]
    choice['result']()
    
    