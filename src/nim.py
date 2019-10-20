import random
import time


class CantMove(Exception):

    def __init__(self, reason):
        self.__reason = reason

    def __repr__(self):
        return f"unable to find a move: {self.__reason}"


class Nim:
    def __init__(self, startstate):
        self.state = startstate

    # Goal is to be unambiguous :

    def __repr__(self):
        my_string = ""
        for a in range(len(self.state)):
            my_string = my_string + f"{a + 1}  : "
            for b in range(self.state[a]):
                my_string = my_string + "1 "
            my_string = my_string + "\n"
        return my_string

    # Return sum of all rows:

    def sum(self):
        return sum(self.state)

    # Return nimber (xor of all rows):

    def nimber(self):
        c = self.state[0]
        for a in range(1, len(self.state)):
            c = c ^ self.state[a]
        return c

    # Make a random move, raise a CantMove if
    # there is nothing left to remove.

    def randommove(self):
        if self.sum() == 0:
            raise CantMove("there is nothing to remove")
        else:
            row = random.randrange(len(self.state))
            while self.state[row] == 0:
                row = random.randrange(len(self.state))
            stick = random.randrange(self.state[row])
            self.state[row] = stick


    # Try to force a win with misere strategy.
    # This functions make a move, if there is exactly
    # one row that contains more than one stick.
    # In that case, it makes a move that will leave
    # an odd number of rows containing 1 stick.
    # This will eventually force the opponent to take the
    # last stick.
    # If it cannot obtain this state, it should raise
    # CantMove( "more than one row has more than one stick" )

    def removelastmorethantwo(self):
        more_than_two = 0
        my_index = 0
        counter = 0
        for a in self.state:
            if a > 0:
                counter += 1
            if a > 1:
                more_than_two += 1
                my_index = self.state.index(a)
        if more_than_two != 1:
            raise CantMove("more than one row has more than one stick")

        self.state[my_index] = 0 if counter % 2 == 0 else 1

    # Try to find a move that makes the nimber zero.
    # Raise CantMove( "nimber is already zero" ), if the
    # nimber is zero already.

    def makenimberzero(self):
        if self.nimber() == 0:
            raise CantMove("nimber is already zero")
        chosen_row = random.randrange(len(self.state))
        while not (self.state[chosen_row] ^ self.nimber()) < self.state[chosen_row]:
            chosen_row = random.randrange(len(self.state))
        self.state[chosen_row] = self.state[chosen_row] ^ self.nimber()

    def optimalmove(self):
        try:
            self.removelastmorethantwo()
        except CantMove:
            try:
                self.makenimberzero()
            except CantMove:
                self.randommove()

    # Let the user make a move. Make sure that the move
    # is correct. This function never crashes, not
    # even with the dumbest user in the world.

    def usermove(self):
        try:
            chosen_row = input("Choose a row: ")
            while int(chosen_row) > len(self.state) or int(chosen_row) == 0:
                print("Such row doesn't exist")
                chosen_row = input("Choose a row: ")
            num_sticks = input("How many sticks to leave: ")
            while int(num_sticks) >= self.state[int(chosen_row) - 1] or int(num_sticks) < 0:
                print("There is not as many sticks as you think")
                num_sticks = input("How many sticks to leave: ")
            self.state[int(chosen_row) - 1] = int(num_sticks)
        except ValueError:
            print("Enter the correct values!")


def play():
    st = Nim([1, 2, 3, 4, 5, 6])

    turn = 'user'
    while st.sum() > 1:
        if turn == 'user':
            print("\n")
            print(st)
            print("hello, user, please make a move")
            st.usermove()
            turn = 'computer'
        else:
            print("\n")
            print(st)
            print("now i will make a move\n")
            print("thinking")
            for r in range(15):
                print(".", end="", flush=True)
                time.sleep(0.1)
            print("\n")
            st.optimalmove()
            turn = 'user'
    print("\n")
    if turn == 'user':
        print("you lost\n")
    else:
        print("you won\n")
