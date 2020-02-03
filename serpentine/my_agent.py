from pommerman.constants import Action
from pommerman.agents import BaseAgent


class MyAgent(BaseAgent):
    """ Our version of the base agent. """

    def __init__(self):
        # This makes sure that we also have all the functionality of the base agent.
        super(BaseAgent, self).__init__()

    def act(self, obs, action_space):
        # Main event that is being called on every turn.
        return Action.Stop
