import torch
import numpy as np
import time
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.base_env import ActionTuple

def stepDiscreteAction(behavior_name, arrlist):
    _discrete = np.array(arrlist, dtype=np.int32)
    action = ActionTuple(discrete=_discrete)
    env.set_actions(behavior_name, action)
    env.step()

def getObservations(behavior_name):
    '''
    The DecisionSteps contains information about the state of the agents that 
    need an action this step and have the behavior behavior_name. 
    The TerminalSteps contains information about the state of the agents whose 
    episode ended and have the behavior behavior_name

    끝났을 당시의 관측 정보를 알고 싶다면 terminal_steps를 사용하고
    끝난 이후에 초기화 되고 관측 정보나, 에피소드 중간의 관측 정보를 알기 위해서는 decision_steps를 사용한다.
    '''
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    vis_obs = []
    vec_obs = []
    tr_vis_obs = []
    tr_vec_obs = []
    for index, shape in enumerate(spec.observation_shapes):
        if len(shape) == 3:
            vis_obs.append(decision_steps.obs[index])
            tr_vis_obs.append(terminal_steps.obs[index])

    for index, shape in enumerate(spec.observation_shapes):
        if len(shape) == 1:
            vec_obs.append(decision_steps.obs[index])
            tr_vec_obs.append(terminal_steps.obs[index])

    return vis_obs, vec_obs, tr_vis_obs, tr_vec_obs

def get_reward(behavior_name):
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    reward = decision_steps.reward
    tr_reward = terminal_steps.reward

    return reward, tr_reward

if __name__ == "__main__":
    game = "/unity-project/FallingStar/Build/FallingStar.exe"

    env = UnityEnvironment(file_name = game)
    env_info=env.reset()

    # We will only consider the first Behavior
    behavior_name = list(env.behavior_specs)[0] 
    print(f"Name of the behavior : {behavior_name}")
    spec = env.behavior_specs[behavior_name]

    # Examine the number of observations per Agent
    print("Number of observations : ", len(spec.observation_shapes))

    # Is there a visual observation ?
    # Visual observation have 3 dimensions: Height, Width and number of channels
    vis_obs_bool = any(len(shape) == 3 for shape in spec.observation_shapes)
    print("Is there a visual observation ?", vis_obs_bool)

    #print action is_discrete
    print("Is action is discrete ?", spec.action_spec.is_discrete())

    #print action is_continuous
    print("Is action is continus ?", spec.action_spec.is_continuous())

    #make continuous action and discrete action with 0 array, and step!
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    n_agents = len(decision_steps)
    _continuous = np.zeros((n_agents, spec.action_spec.continuous_size), dtype=np.float32)
    _discrete = np.zeros((n_agents, spec.action_spec.discrete_size), dtype=np.int32)
    action = ActionTuple(continuous=_continuous, discrete=_discrete)
    env.set_actions(behavior_name, action)
    env.step()


    #make custom discrete action, and step!
    actionarr = [[1]]#list shape(1<num_agents>,1<discrete_size>)
    _discrete = np.array(actionarr, dtype=np.int32)
    action = ActionTuple(discrete=_discrete)
    env.set_actions(behavior_name, action)
    env.step()


    #Get step information to get observation
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    #visual observation
    for index, shape in enumerate(spec.observation_shapes):
        if len(shape) == 3:
            vis_obs = decision_steps.obs[index]
            print("Get vis_obs with shape:", np.shape(vis_obs))
    #vector observation
    for index, shape in enumerate(spec.observation_shapes):
        if len(shape) == 1:
            vec_obs = decision_steps.obs[index]
            print("Get vis_obs with shape:", np.shape(vec_obs))


    #get reward
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    reward = decision_steps.reward
    tr_reward = terminal_steps.reward


    #lets run few episodes!
    print("lets run few episodes!")
    for i in range(100):
        print("\n")
        actionList = []
        actionList.append(np.random.randint(3,size=1))
        actionList=[[1]]
        stepDiscreteAction(behavior_name, actionList)
        vis_obs, vec_obs, tr_vis_obs, tr_vec_obs = getObservations(behavior_name)
        print(np.shape(vis_obs[0]), np.shape(vec_obs[0]))
        print(vec_obs[0])
        print(tr_vec_obs[0])

        reward,tr_reward = get_reward(behavior_name)
        print(reward)
        print(tr_reward)

    env.close()
