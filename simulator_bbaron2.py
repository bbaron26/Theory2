from collections import deque

class NTM:
    def __init__(self, name, states, start_state, accept_state, reject_state, transitions):
        self.name = name
        self.states = states
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.transitions = transitions

class NTMSimulator:
    def __init__(self, ntm, input_string, max_depth=100):
        self.ntm = ntm
        self.input_string = input_string
        self.max_depth = max_depth

    def simulate(self):
        #queue for bfs
        queue = deque([([""], self.ntm.start_state, list(self.input_string), [])])
        #track current depth
        depth = 0
        #track total number of configurations explored
        total_configurations = 0

        while queue:
            #if max depth reached
            if depth > self.max_depth:
                return "Timed out", depth, total_configurations

            #number of configurations at this level
            current_level = len(queue)
            #update total configurations
            total_configurations += current_level
        
            #process all configurations at current depth
            for _ in range(current_level):
                left, state, right, path = queue.popleft()

                #if accept state, accept
                if state == self.ntm.accept_state:
                    return "Accepted", depth, total_configurations
                #if reject state, skip it
                elif state == self.ntm.reject_state:
                    continue

                #get current symbol from the right tape
                current_symbol = right[0] if right else '_'
                transitions = self.ntm.transitions.get((state, current_symbol), [])

                #explore all possible configurations
                for next_state, write_symbol, move in transitions:
                    new_left = left[:]
                    new_right = right[:]

                    #write the symbol on the tape, replacing it
                    if write_symbol != '_':
                        if new_right:
                            new_right[0] = write_symbol
                        else:
                            new_right.append(write_symbol)

                    #move the tape right or left (whichever is specified)
                    if move == 'R':
                        if new_right:
                            new_left.append(new_right.pop(0))
                        else:
                            new_left.append('_')
                    elif move == 'L':
                        new_right.insert(0, new_left.pop() if new_left else '_')

                    #append the new configuration to the path
                    new_path = path[:]
                    new_path.append((state, current_symbol, next_state, write_symbol, move))

                    #add new configuration to queue for further exploration
                    queue.append((new_left, next_state, new_right, new_path))

            #increment depthfor next iteration
            depth += 1

        return "Rejected", depth, total_configurations
