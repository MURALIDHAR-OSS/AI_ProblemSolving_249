# 🚦 Smart Navigation System (BFS & DFS)

<p align="center">
  <b>Artificial Intelligence | Graph Search Algorithms | Python Implementation</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/AI-Search%20Algorithms-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Student%20Project-orange?style=for-the-badge">
</p>

---

## 📌 Project Overview
This project implements a **Smart Navigation System** using fundamental Artificial Intelligence search algorithms — **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

The system finds a path between two nodes in a graph and demonstrates how different algorithms behave in terms of **optimality, efficiency, and traversal strategy**.

---

## 🎯 Objectives
- Understand graph-based problem solving  
- Implement BFS and DFS algorithms  
- Compare algorithm performance  
- Demonstrate AI search techniques  

---

## 🧠 Algorithms Explained

### 🔹 Breadth-First Search (BFS)
- Explores nodes **level-by-level**
- Uses **Queue (FIFO)**
- Guarantees **shortest path**
- Explores more nodes  

---

### 🔹 Depth-First Search (DFS)
- Explores nodes **deeply first**
- Uses **Recursion / Stack**
- Faster traversal  
- Does **not guarantee shortest path**

---

## 🗺️ Graph Representation


A → B, C
B → D, E
C → D
D → F
E → F
F → -


---

## ⚙️ Working Principle
1. User inputs start node and goal node  
2. BFS explores neighbors level-wise  
3. DFS explores deep paths first  
4. Both attempt to reach goal node  
5. Paths are displayed and compared  

---

## 🧪 Sample Execution

### 🔸 Input

Enter start node: A
Enter goal node: F


### 🔸 Output

BFS Path: A → B → D → F
DFS Path: A → C → D → F


---

## 📊 Algorithm Comparison

| Feature        | BFS                        | DFS                        |
|----------------|----------------------------|-----------------------------|
| Strategy       | Level-wise                 | Depth-wise                  |
| Data Structure | Queue                      | Stack / Recursion           |
| Optimal Path   | ✅ Yes                     | ❌ Not guaranteed           |
| Speed          | Slower                     | Faster                      |
| Nodes Explored | More                       | Less                        |
| Memory Usage   | High                       | Low                         |

---

## ⏱️ Complexity Analysis

### BFS
- **Time Complexity:** O(V + E)  
- **Space Complexity:** O(V)  

### DFS
- **Time Complexity:** O(V + E)  
- **Space Complexity:** O(V)  

---

## 🚀 How to Run

### ▶️ Step 1: Clone Repository
```bash
git clone <your-repo-link>
▶️ Step 2: Navigate to Folder
cd bfs_dfs_navigation
▶️ Step 3: Run Program
python main.py
▶️ Step 4: Provide Input
Enter start node
Enter goal node
📁 Project Structure
bfs_dfs_navigation/
│
├── main.py
└── README.md
💡 Key Features
Clean and simple implementation
User-driven input system
Demonstrates core AI algorithms
Easy comparison of BFS vs DFS
Beginner-friendly and efficient
🌍 Real-World Applications
🗺️ GPS Navigation Systems
🌐 Network Routing
🎮 Game Pathfinding AI
🤖 Robotics Navigation
🛠️ Technologies Used
🐍 Python
📊 Graph Data Structures
🔍 BFS & DFS Algorithms
📌 Assignment Requirements Covered

✔ AI problem implemented
✔ GitHub repository maintained
✔ Proper folder structure
✔ README with explanation and outputs
✔ Working program with user input

👨‍💻 Author

Sai MuraliDhar . Ch
