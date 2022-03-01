# Stable-baselines3


### StopTrainingOnRewardThreshold
- Stop the training once a threshold in episodic reward has been reached
- **must be used with the `EvalCallback`**
```Python
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
