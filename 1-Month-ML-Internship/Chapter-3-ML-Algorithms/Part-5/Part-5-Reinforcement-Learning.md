# Part 5: Reinforcement Learning & Q-Learning

**Week:** Week 3, Part 5 | **Duration:** 7+ Hours | **Difficulty:** Intermediate → Advanced

---

## 🎯 Learning Objectives

By the end of Part 5, you will:

✅ Understand agents, environments, and rewards
✅ Implement Markov Decision Processes (MDPs)
✅ Build Q-Learning algorithm from scratch
✅ Create gym-like environments
✅ Train agents to solve navigation problems
✅ Understand exploration vs. exploitation trade-off
✅ Implement epsilon-greedy strategy

---

## 📖 Core Topics

### 1. Reinforcement Learning Fundamentals

#### Agents and Environments
```python
class Environment:
    """Simple grid-based environment"""
    
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.agent_pos = (0, 0)
        self.goal_pos = (grid_size - 1, grid_size - 1)
        self.steps = 0
        self.max_steps = 100
    
    def reset(self):
        """Reset environment to initial state"""
        self.agent_pos = (0, 0)
        self.steps = 0
        return self._get_state()
    
    def _get_state(self):
        """Return current state"""
        return self.agent_pos
    
    def _get_reward(self):
        """Return reward for current position"""
        if self.agent_pos == self.goal_pos:
            return 100  # Goal reward
        else:
            return -1   # Step penalty
    
    def step(self, action):
        """
        Execute action in environment
        
        Actions: 0=up, 1=down, 2=left, 3=right
        """
        x, y = self.agent_pos
        
        # Move based on action
        if action == 0:    # Up
            x = max(0, x - 1)
        elif action == 1:  # Down
            x = min(self.grid_size - 1, x + 1)
        elif action == 2:  # Left
            y = max(0, y - 1)
        elif action == 3:  # Right
            y = min(self.grid_size - 1, y + 1)
        
        self.agent_pos = (x, y)
        self.steps += 1
        
        reward = self._get_reward()
        done = (self.agent_pos == self.goal_pos) or (self.steps >= self.max_steps)
        
        return self._get_state(), reward, done
    
    def render(self):
        """Display current state"""
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        x, y = self.agent_pos
        gx, gy = self.goal_pos
        
        grid[x][y] = 'A'  # Agent
        grid[gx][gy] = 'G'  # Goal
        
        for row in grid:
            print(' '.join(row))
        print()

# Usage
env = Environment(grid_size=5)
state = env.reset()
for _ in range(10):
    action = env.env.action_space.sample()  # Random action
    next_state, reward, done = env.step(action)
    if done:
        break
```

---

### 2. Q-Learning Algorithm

#### Q-Table and Updates
```python
import numpy as np

class QLearning:
    """Q-Learning agent"""
    
    def __init__(self, env, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
        self.env = env
        self.lr = learning_rate      # How fast to learn
        self.gamma = discount_factor # How much to value future rewards
        self.epsilon = epsilon       # Exploration rate
        
        # Initialize Q-table
        state_size = env.grid_size * env.grid_size
        action_size = 4  # 4 possible actions
        self.Q = np.zeros((state_size, action_size))
    
    def _state_to_index(self, state):
        """Convert state tuple to Q-table index"""
        x, y = state
        return x * self.env.grid_size + y
    
    def _index_to_state(self, index):
        """Convert Q-table index back to state"""
        x = index // self.env.grid_size
        y = index % self.env.grid_size
        return (x, y)
    
    def _select_action_epsilon_greedy(self, state):
        """
        Epsilon-greedy action selection
        - With probability epsilon: random action (explore)
        - Otherwise: best known action (exploit)
        """
        if np.random.random() < self.epsilon:
            return np.random.randint(0, 4)  # Explore
        else:
            state_idx = self._state_to_index(state)
            return np.argmax(self.Q[state_idx])  # Exploit
    
    def _update_q(self, state, action, reward, next_state, done):
        """Update Q-value using Bellman equation"""
        state_idx = self._state_to_index(state)
        next_state_idx = self._state_to_index(next_state)
        
        # Q-learning update rule
        current_q = self.Q[state_idx, action]
        max_next_q = np.max(self.Q[next_state_idx]) if not done else 0
        
        new_q = current_q + self.lr * (reward + self.gamma * max_next_q - current_q)
        self.Q[state_idx, action] = new_q
    
    def train(self, episodes=100):
        """Train agent for multiple episodes"""
        rewards_history = []
        
        for episode in range(episodes):
            state = self.env.reset()
            total_reward = 0
            
            while True:
                # Select and execute action
                action = self._select_action_epsilon_greedy(state)
                next_state, reward, done = self.env.step(action)
                
                # Update Q-values
                self._update_q(state, action, reward, next_state, done)
                
                total_reward += reward
                state = next_state
                
                if done:
                    break
            
            rewards_history.append(total_reward)
            
            if (episode + 1) % 10 == 0:
                avg_reward = np.mean(rewards_history[-10:])
                print(f"Episode {episode + 1}, Avg Reward: {avg_reward:.2f}")
        
        return rewards_history
    
    def play(self, render=True):
        """Play one episode using learned policy"""
        state = self.env.reset()
        total_reward = 0
        
        while True:
            if render:
                self.env.render()
            
            # Always exploit (no exploration)
            state_idx = self._state_to_index(state)
            action = np.argmax(self.Q[state_idx])
            
            next_state, reward, done = self.env.step(action)
            total_reward += reward
            state = next_state
            
            if done:
                break
        
        return total_reward

# Usage
env = Environment(grid_size=5)
agent = QLearning(env)

# Train
rewards = agent.train(episodes=100)

# Play learned policy
final_reward = agent.play(render=True)
print(f"Final reward: {final_reward}")
```

---

### 3. Exploration vs. Exploitation

#### Epsilon-Greedy Strategy
```python
class EpsilonScheduler:
    """Decay epsilon over time"""
    
    def __init__(self, initial_epsilon=1.0, final_epsilon=0.01, decay_rate=0.995):
        self.initial = initial_epsilon
        self.final = final_epsilon
        self.decay = decay_rate
        self.current = initial_epsilon
    
    def get_epsilon(self, episode):
        """Get epsilon for current episode"""
        self.current = self.final + (self.initial - self.final) * (self.decay ** episode)
        return self.current

# Usage
scheduler = EpsilonScheduler()
for episode in range(100):
    eps = scheduler.get_epsilon(episode)
    print(f"Episode {episode}: epsilon = {eps:.3f}")
```

---

### 4. Complete Navigation Example

#### Campus Navigation Agent
```python
class CampusEnvironment(Environment):
    """Campus with multiple buildings"""
    
    def __init__(self):
        super().__init__(grid_size=10)
        self.buildings = {
            'library': (2, 2),
            'cafe': (5, 5),
            'dorm': (8, 2),
            'classroom': (8, 8)
        }
    
    def _get_reward(self):
        """Reward structure"""
        base_reward = -0.1  # Step cost
        
        # Bonus for reaching specific buildings
        if self.agent_pos == self.buildings['library']:
            return base_reward + 10
        elif self.agent_pos == self.buildings['cafe']:
            return base_reward + 5
        elif self.agent_pos == self.buildings['classroom']:
            return base_reward + 20
        
        return base_reward

# Usage
campus = CampusEnvironment()
agent = QLearning(campus, learning_rate=0.1, epsilon=0.1)
agent.train(episodes=200)
agent.play(render=True)
```

---

## 💡 Complete Example: Multi-Goal Navigation

```python
class MultiGoalAgent:
    """Agent learning to navigate to multiple goals"""
    
    def __init__(self, env, n_goals=3):
        self.env = env
        self.n_goals = n_goals
        self.agents = []
        
        # Train separate agents for each goal
        for goal_idx in range(n_goals):
            agent = QLearning(env)
            self.agents.append(agent)
    
    def train_all(self, episodes=100):
        """Train all agents"""
        for idx, agent in enumerate(self.agents):
            print(f"Training agent {idx + 1}/{self.n_goals}...")
            agent.train(episodes=episodes)
    
    def solve_sequence(self):
        """Visit all goals in sequence"""
        state = self.env.reset()
        total_reward = 0
        
        for agent in self.agents:
            # Use this agent until goal reached
            # Reset for next goal
            pass
        
        return total_reward

# Usage
env = CampusEnvironment()
multi_agent = MultiGoalAgent(env, n_goals=3)
multi_agent.train_all(episodes=100)
reward = multi_agent.solve_sequence()
```

---

## 🔗 Navigation

**[← Back to Chapter 3](../README.md)** | **[Part 5 Exercises →](./Part-5-Exercises.md)**
