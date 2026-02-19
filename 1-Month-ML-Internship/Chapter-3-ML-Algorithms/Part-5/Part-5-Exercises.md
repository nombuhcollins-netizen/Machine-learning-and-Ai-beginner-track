# Part 5: Reinforcement Learning - Exercises

**Difficulty:** Intermediate → Advanced | **Time:** 6-7 hours | **Capstone:** Campus Navigation Simulation

---

## 📝 Exercise Set 1: Environments

### Exercise 1.1: Simple Grid Environment
Create basic grid environment:
- Grid size (e.g., 5×5)
- Agent position
- Goal position
- Can move up/down/left/right

**File:** `simple_grid_env.py`

---

### Exercise 1.2: Add Obstacles
Extend environment with:
- Walls that block movement
- Penalty for hitting walls
- Visualization with ASCII art

**File:** `env_with_obstacles.py`

---

### Exercise 1.3: Multiple Goals
Create environment with:
- Multiple goal positions
- Different rewards for each goal
- Agent must visit goals in order

**File:** `multi_goal_env.py`

---

## 📝 Exercise Set 2: Q-Learning Basics

### Exercise 2.1: Q-Table Initialization
Create Q-table structure:
- Map states to indices
- Initialize all Q-values to 0
- Handle state-action pairs

**File:** `q_table_basics.py`

---

### Exercise 2.2: Q-Value Update
Implement Q-learning update rule:
- Bellman equation: Q(s,a) ← Q(s,a) + α[R + γ·max(Q(s',a')) - Q(s,a)]
- Learning rate α
- Discount factor γ

**File:** `q_value_update.py`

---

### Exercise 2.3: Action Selection
Implement epsilon-greedy strategy:
- Explore: random action with probability ε
- Exploit: best known action with probability 1-ε
- Allow epsilon decay

**File:** `epsilon_greedy.py`

---

## 📝 Exercise Set 3: Training

### Exercise 3.1: Train Single Episode
Create function to:
- Reset environment
- Run episode until done
- Update Q-values
- Track rewards

**File:** `train_single_episode.py`

---

### Exercise 3.2: Multi-Episode Training
Extend to train multiple episodes:
- Track reward history
- Monitor convergence
- Plot reward over episodes

**File:** `multi_episode_training.py`

---

### Exercise 3.3: Learning Curves
Analyze training progress:
- Average reward every N episodes
- Plot smoothed rewards
- Identify when agent "learned"

**File:** `learning_curves.py`

---

## 📝 Exercise Set 4: Analysis and Visualization

### Exercise 4.1: Policy Visualization
Visualize learned policy:
- Show action for each state (arrows)
- Show Q-values as heatmap
- Identify policy convergence

**File:** `policy_visualization.py`

---

### Exercise 4.2: Q-Value Heatmaps
Create heatmaps:
- Max Q-value per state
- Separate heatmap for each action
- Show value landscape

**File:** `qvalue_heatmaps.py`

---

### Exercise 4.3: Replay Learned Policy
Agent plays episode using learned policy:
- No exploration (epsilon=0)
- Render path to goal
- Show cumulative reward

**File:** `replay_policy.py`

---

## 📝 Exercise Set 5: Advanced Scenarios

### Exercise 5.1: Stochastic Environment
Add randomness to environment:
- Action doesn't always work as intended
- Wind/noise affects movement
- Agent must handle uncertainty

**File:** `stochastic_env.py`

---

### Exercise 5.2: Larger State Spaces
Scale up environment:
- Bigger grid (e.g., 20×20)
- More actions
- Measure training time
- Analyze scalability

**File:** `large_grid_training.py`

---

### Exercise 5.3: Function Approximation (Optional)
Use neural network instead of Q-table:
- Approximate Q-values with network
- Deep Q-Learning basics
- More scalable to large spaces

**File:** `dqn_basics.py` (advanced)

---

## 🎯 Capstone: Campus Navigation Simulation

### Project: Train Agent to Navigate Campus

**Scenario:**
Build a simulation where an agent learns to navigate a campus with:
- Multiple buildings (library, cafe, dorm, classroom)
- Paths and obstacles
- Different rewards for different locations

**Deliverables:**

#### Part 1: Campus Environment (`part1_environment.py`)
```python
class CampusEnvironment:
    def __init__(self):
        self.grid_size = 10
        self.buildings = {
            'library': (2, 2),
            'cafe': (5, 5),
            'dorm': (8, 2),
            'classroom': (8, 8)
        }
        self.obstacles = [(3, 3), (4, 4), (6, 6)]  # Walls
    
    def render(self):
        # Visualize campus with buildings, obstacles, agent
        pass
```

#### Part 2: Q-Learning Agent (`part2_agent.py`)
```python
class CampusAgent(QLearning):
    def __init__(self, env):
        super().__init__(env)
        self.target_building = 'library'
    
    def _get_reward(self):
        # Reward for reaching target building
        # Penalty for hitting obstacles
        pass
```

#### Part 3: Training (`part3_training.py`)
```python
def train_campus_agent():
    env = CampusEnvironment()
    agent = CampusAgent(env)
    
    # Train to location 1
    agent.target_building = 'library'
    agent.train(episodes=100)
    
    # Train to location 2
    agent.target_building = 'cafe'
    agent.train(episodes=100)
    
    # Etc for other buildings
    
    return agent
```

#### Part 4: Visualization (`part4_visualization.py`)
Show:
- Learned policy (arrows showing best action)
- Value map (how good each state is)
- Training progress (reward curve)
- Example playthrough to each building

#### Part 5: Evaluation (`part5_evaluation.py`)
```python
def evaluate_agent(agent):
    results = {}
    
    for building in agent.env.buildings.keys():
        agent.target_building = building
        
        # Test 10 times
        rewards = []
        for _ in range(10):
            reward = agent.play(render=False)
            rewards.append(reward)
        
        results[building] = {
            'avg_reward': np.mean(rewards),
            'success_rate': sum(r > 50 for r in rewards) / len(rewards),
            'avg_steps': ...  # Track steps to goal
        }
    
    return results
```

#### Part 6: Report Generation (`part6_report.py`)
```
CAMPUS NAVIGATION TRAINING REPORT
==================================

Environment:
- Grid size: 10×10
- Buildings: 4 (Library, Cafe, Dorm, Classroom)
- Obstacles: 3 walls

Training Results:
- Episodes: 100 per building
- Learning rate: 0.1
- Discount factor: 0.99

Performance by Target:
- Library: 95 avg reward, 100% success rate, 12 steps avg
- Cafe:    87 avg reward, 90% success rate, 15 steps avg
- Dorm:    92 avg reward, 95% success rate, 13 steps avg
- Class:   88 avg reward, 92% success rate, 16 steps avg

Policy Visualization:
[Show learned actions for each state]

Observations:
- Agent successfully learned navigation
- Performance improved over episodes
- Obstacle avoidance learned naturally
```

**Success Criteria:**
- [ ] Environment works correctly
- [ ] Q-Learning trains successfully
- [ ] Agent navigates to goals
- [ ] Reward curves show learning
- [ ] Policy visualization makes sense
- [ ] Report generated with analysis
- [ ] Code is well-documented

**Bonus Challenges:**
- [ ] Add multiple goals agent must visit in sequence
- [ ] Implement epsilon decay for better convergence
- [ ] Add energy/fuel constraint
- [ ] Implement different agent types
- [ ] Compare with random policy baseline

---

## 🔗 Navigation

**[← Back to Part 5 Module](./Part-5-Reinforcement-Learning.md)** | **[Chapter 3 Complete! →](../README.md)**
