import random
import time


class CantMove(Exception):

    def __init__(self, reason):
        self.__reason = reason

    def __repr__(self):
        return "unable to find a move: {}".format(self.__reason)


class Nim:
    def __init__(self, startstate):
        self.state = startstate

    # Goal is to be unambiguous :

    def __repr__(self):

    # Return sum of all rows:

    def sum(self):

    # Return nimber (xor of all rows):

    def nimber(self):

    # Make a random move, raise a CantMove if
    # there is nothing left to remove.

    def randommove(self):

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

    # Try to find a move that makes the nimber zero.
    # Raise CantMove( "nimber is already zero" ), if the
    # nimber is zero already.

    def makenimberzero(self):

    def optimalmove(self):

    # Let the user make a move. Make sure that the move
    # is correct. This function never crashes, not
    # even with the dumbest user in the world.

    def usermove(self):