# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

myList = {}

def player(prev_play, opponent_history=[]):
  if prev_play in ['R','P','S']:
    opponent_history.append(prev_play)
  guess = 'R'

  depth = 6
  if len(opponent_history)>depth:
    inp = ''.join(opponent_history[-depth:])
    if ''.join(opponent_history[-(depth+1):]) in myList.keys():
      myList[''.join(opponent_history[-(depth+1):])]+=1
    else:
      myList[''.join(opponent_history[-(depth+1):])]=1

    doable = [inp+'R', inp+'P', inp+'S']

    for i in doable:
      if not i in myList.keys():
        myList[i] = 0

    predictions = max(doable, key=lambda key: myList[key])

    if predictions[-1] == 'P':
      guess = 'S'
    if predictions[-1] == 'R':
      guess = 'P'
    if predictions[-1] == 'S':
      guess = 'R'


  return guess
