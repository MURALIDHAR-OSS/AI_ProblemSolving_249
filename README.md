# 🚦 Smart Navigation System using BFS & DFS

<p align="center">
  <b>Artificial Intelligence | Graph Traversal | Pathfinding System</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Algorithm-BFS%20%7C%20DFS-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-AI%20Assignment-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---

## 📌 Project Overview
This project demonstrates a **Smart Navigation System** built using fundamental Artificial Intelligence search algorithms.

It simulates how systems like **Google Maps and GPS navigation** determine paths between locations using graph traversal techniques.

---

## 🎯 Objectives
- Implement core AI search algorithms  
- Understand graph traversal techniques  
- Compare BFS and DFS performance  
- Demonstrate pathfinding logic  

---

## 🧠 Algorithms Used

### 🔹 Breadth-First Search (BFS)
- Explores nodes **level-by-level**
- Uses **Queue (FIFO)**
- Guarantees **shortest path**
- Suitable for optimal solutions  

---

### 🔹 Depth-First Search (DFS)
- Explores nodes **deep-first**
- Uses **Recursion / Stack**
- Faster in some cases  
- Does **not guarantee shortest path**

---

## 🗺️ Graph Representation

The system uses a predefined graph:


A → B, C
B → D, E
C → D
D → F
E → F
F → -


---

## ⚙️ Working Principle
1. User enters start node and goal node  
2. BFS explores all nearby nodes first  
3. DFS explores deeper paths first  
4. Both algorithms attempt to reach the goal  
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
- Time Complexity: **O(V + E)**  
- Space Complexity: **O(V)**  

### DFS
- Time Complexity: **O(V + E)**  
- Space Complexity: **O(V)**  

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
Clean and structured implementation
Interactive user input
Demonstrates core AI search algorithms
Easy comparison between BFS and DFS
Beginner-friendly and efficient
🌍 Real-World Applications
🗺️ GPS Navigation Systems
🌐 Network Routing
🎮 Game Pathfinding
🤖 Robotics Navigation
🛠️ Technologies Used
🐍 Python
📊 Graph Data Structures
🔍 BFS & DFS Algorithms
📌 Assignment Requirements Covered

✔ AI problem implemented
✔ GitHub repository created
✔ Proper folder structure
✔ Multiple commits
✔ README with explanation and outputs
✔ Working program with user input

👨‍💻 Author

Muralidhar

⭐ Conclusion

This project successfully demonstrates how Artificial Intelligence search algorithms can be used to solve real-world navigation problems. It highlights the trade-offs between optimality and efficiency, forming a strong foundation in AI problem-solving techniques.

<p align="center"> 🚀 <b>Project Completed Successfully</b> 🚀 </p> ```
