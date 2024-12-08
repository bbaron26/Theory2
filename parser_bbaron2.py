import csv

class NTMParser:
    @staticmethod
    def parse(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            #line 1: machine name
            name = next(reader)[0]
            #line 2: states
            states = set(next(reader))
            #line 3: input alphabet (not directly used)
            _ = next(reader)
            #line 4: tape alphabet (not directly used)
            _ = next(reader)
            #line 5: start state
            start_state = next(reader)[0]
            #line 6: accept state
            accept_state = next(reader)[0]
            #line 7: reject state
            reject_state = next(reader)[0]

            #parse transitions
            transitions = {}
            for row in reader:
                #skip invalid lines
                if not row or len(row) < 5:
                    print(f"Skipping invalid row: {row}")
                    continue
                state, symbol, next_state, write_symbol, move = row
                #append
                transitions.setdefault((state, symbol), []).append((next_state, write_symbol, move))
        
            #return
            return {
                "name": name,
                "states": states,
                "start_state": start_state,
                "accept_state": accept_state,
                "reject_state": reject_state,
                "transitions": transitions
            }

