class State(object):
    """Represents a potential state of the printing shop, including day, probability of reaching state, and the paper remaining in that state"""
    def __init__(self, day, prob, remaining_paper):
        self.day = day
        self.prob = prob
        self.remaining_paper = remaining_paper
    
    def next_day(self):
        """Given current state, returns list of possible states branching from current state"""
        generate = {0:[-1,1,1,1,1], 1:[0,-1,1,1,1], 2:[0,0,-1,1,1], 3:[0,0,0,-1,1], 4:[0,0,0,0,-1]}
        next_day_states = []
        for index, count in enumerate(self.remaining_paper):
            if count > 0:
                # determine remaining_paper for the new state
                new_paper = [x + y for x,y in zip(self.remaining_paper,generate[index])]
                # determine the probability of reaching the new state
                new_prob = self.prob * ((1.0 * count) / sum(self.remaining_paper))
                # generate a new state object
                new_state = State(self.day + 1, new_prob, new_paper)
                # put state object in the list
                next_day_states.append(new_state)
        return next_day_states

    def check_values(self):
        """Function for debugging - check what is in a State object"""
        print 'day is ' + str(self.day)
        print 'prob is ' + str(self.prob)
        print 'paper is '
        print(self.remaining_paper) 

first_day = State(1, 1, [0,1,1,1,1])

# generate all possible states for days 1-14 and put them in a master list
state_list = [first_day]
# for each day
for i in range(1,14):
    # look at all the current states
    for current_state in filter(lambda state: state.day == i, state_list):
        # generate new states from current state and concatenate onto master list
        state_list += current_state.next_day()

# sum up probabilities for single paper states
sum_prob = 0
single_paper_states = filter(lambda state: sum(state.remaining_paper) == 1, state_list)
for state in single_paper_states:
    sum_prob += state.prob

print sum_prob