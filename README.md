# 8-Puzzle Solver 🧩

![GitHub Repo Stars](https://img.shields.io/github/stars/yourusername/8-puzzle-solver?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/8-puzzle-solver?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/8-puzzle-solver)

This project solves the **8-Puzzle Problem** using six different AI search algorithms. The goal is to move tiles in a 3×3 grid to reach the correct configuration using **optimal and heuristic-based search strategies**.

## 🎯 Goal State
```
[1, 0, 3]
[8, 2, 4]
[7, 6, 5]
```

## 🚀 Implemented Algorithms
1️⃣ **[Breadth-First Search (BFS)](Algorithms/8_puzzle_solver.py)** – Guarantees shortest path but uses more memory.  
2️⃣ **[Depth-First Search (DFS)](Algorithms/8_puzzle_solver.py)** – Explores deep paths first but may not be optimal.  
3️⃣ **[Uniform Cost Search (UCS)](Algorithms/8_puzzle_solver.py)** – Expands the least-cost path first, guaranteeing optimality.  
4️⃣ **[Greedy Best-First Search](Algorithms/8_puzzle_solver.py)** – Uses heuristics but can get stuck in bad paths.  
5️⃣ **[Hill Climbing](Algorithms/8_puzzle_solver.py)** – Chooses best local move, but may get stuck in local optima.  
6️⃣ **[A* Search (A-Star)](Algorithms/8_puzzle_solver.py)** – Uses cost and heuristics for an optimal solution.  

```

## 🎮 Live Demo (Google Colab)
[![Run in Google Colab](
## 📂 Project Structure
```
📦 8-Puzzle-Solver
├── 📜 README.md
├── 📂 Algorithms
│   ├── 8_puzzle_solver.py
├── 📂 Docs
│   ├── algorithms_explanation.md
│   ├── installation_guide.md
└── 📂 LiveDemo
    ├── 8_puzzle_demo.ipynb
```

## 📜 References
- **Artificial Intelligence: A Modern Approach** - Stuart Russell & Peter Norvig  
- **GeeksforGeeks: 8-Puzzle Problem Explanation**  

🚀 **Solve the 8-Puzzle problem with AI!** 🧠🔥

