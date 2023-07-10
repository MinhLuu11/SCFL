import argparse
import datetime
import gym
import numpy as np
import itertools
import torch
# from torch.utils.tensorboard import SummaryWriter
from agents.sac.agent_sac import *
from agents.ddpg.agent import *

from agents.sac.modules.replay_memory import *
from envs_DM.environment import *
from envs.env_utils import *
from envs.env_agent_utils import *
from utils.setting_setup import *
from utils.result_utils import *



args = get_arguments()

env = FL_env(args)

if args.algo == "DDPG":
    agent = DDPGAgent(
        args,
        env
    )
elif args.algo == "SAC":
    agent = SAC(
        args,
        env
    )
agent.train(args)