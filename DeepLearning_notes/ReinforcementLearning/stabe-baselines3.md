# Stable-baselines3

### Monitor
- save the information of the episode
- the location to save a log file has to be generated before using Monitor class
```Python
from stable_baselines3.common.monitor import Monitor
custom_env = Monitor(env, log_dir, info_keywords=(,)) 
# info_keywords : extra information to log, from the information return of env.step()
```
### StopTrainingOnRewardThreshold
- Stop the training once a threshold in episodic reward has been reached
- **must be used with the `EvalCallback`**
```Python
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnRewardThreshold
callback_on_best = StopTrainingOnRewardThreshold(reward_threshold=100, verbose=1)
```
### EvalCallback
- **Evaluate** periodically the **performance** of an agent, using a **separate** test environment
```Python
# Separate evaluation env
eval_env = CustomEnv()
# Use deterministic actions for evaluation
eval_callback = EvalCallback(eval_env, best_model_save_path='./logs/',
                              callback_on_new_best=callback_on_best
                             log_path='./logs/', eval_freq=5000, 
                             deterministic=True, render=False)
model.learn(time_step, callback=eval_callback)
```
## RL algorithms
### A2C
```Python
from stable_baselines3.a2c import A2C
policy_kwargs = dict(activation_fn=torch.nn.Sigmoid,
                net_arch=[64, 128, 256, dict(pi=[32], vf=[32])])
model = A2C('MlpPolicy', env=env, 
        verbose=0, policy_kwargs=policy_kwargs, learning_rate=0.0001, clip_range=0.1)
model.learn(time_step, callback=eval_callback)
model.save('a2c')                
```

### DQN
```Python
from stable_baselines3 import DQN
policy_kwargs = dict(activation_fn=torch.nn.Sigmoid,
                net_arch=[64, 128, 256])
model = DQN('MlpPolicy', env=env, 
        verbose=0, policy_kwargs=policy_kwargs, learning_rate=0.00001, clip_range=0.1)
model.learn(time_step, callback=eval_callback)
model.save('dqn')            
```

### PPO
```Python
from stable_baselines3 import PPO
policy_kwargs = dict(activation_fn=torch.nn.Sigmoid,
                net_arch=[64, 128, 256, dict(pi=[32], vf=[32])])
model = PPO('MlpPolicy', env=custom_env, 
        verbose=0, policy_kwargs=policy_kwargs, learning_rate=0.0025, clip_range=0.1)
model.learn(time_step, callback=eval_callback)
model.save('ppo')
```
