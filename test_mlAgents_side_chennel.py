'''
This code is test code to use side_channel method that provided by unity ml_agents
You can convey custom data to mlAgents or change mlAgent Unity environment By using this method
'''

from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.side_channel.side_channel import (
    SideChannel,
    IncomingMessage,
    OutgoingMessage,
)
import numpy as np
import uuid


# Create the StringLogChannel class
class StringLogChannel(SideChannel):

    def __init__(self) -> None:
        super().__init__(uuid.UUID("621f0a70-4f87-11ea-a6bf-784f4387d1f7"))

    def on_message_received(self, msg: IncomingMessage) -> None:
        """
        Note: We must implement this method of the SideChannel interface to
        receive messages from Unity
        """
        # We simply read a string from the message and print it.
        print(msg.read_string())

    def send_string(self, data: str) -> None:
        # Add the string to an OutgoingMessage
        msg = OutgoingMessage()
        msg.write_string(data)
        # We call this method to queue the data we want to send
        super().queue_message_to_send(msg)


# Create the channel
string_log = StringLogChannel()

# We start the communication with the Unity Editor and pass the string_log side channel as input
game = "/unity-project/FallingStar/Build/FallingStar.exe"
env = UnityEnvironment(file_name= game, side_channels=[string_log])
env.reset()
string_log.send_string("The environment was reset")

behavior_name = list(env.behavior_specs)[0]  # Get the first group_name
for i in range(1000):
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    n_agents = len(decision_steps)
    # We send data to Unity : A string with the number of Agent at each
    string_log.send_string(
        "Step " + str(i) + " occurred with " + str(n_agents) + " agents."
    )
    env.step()  # Move the simulation forward

env.close()