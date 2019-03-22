####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Reuben' # Only 10 chars displayed.
strategy_name = 'Genius'
strategy_description = 'Use their history and their score to decide'

def prob_of_b(their_history):
    if their_history.count('b') > len(their_history)/2:
        return 'b'
    else:
        return 'c'
    
def compare_scores(my_score, their_score):
    if their_score > my_score:
        return 'b'
    else:
        return 'c'
        
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if prob_of_b(their_history) == compare_scores(my_score, their_score):
        return prob_of_b(their_history)
    else:
        return 'b'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray if history of betraying and their score > mine
    if test_move(my_history='ccc',
              their_history='bbb', 
              my_score=0,
              their_score=100,
              result='b'):
         print 'Test passed'
     # Test 2: collude if they don't have a history of betraying and their score < mine
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')
      # Test 3: Betray if history and score comparison return different answers
    if test_move(my_history='ccc',
              their_history='bbb', 
              my_score=200,
              their_score=100,
              result='b'):
         print 'Test passed'             