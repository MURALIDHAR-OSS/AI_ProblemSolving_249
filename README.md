# 🤖 AI Problem Solving Assignment

## 📌 Project Overview
This repository contains implementations of core Artificial Intelligence problem-solving techniques using Python.  
The project focuses on **Search Algorithms** and **Constraint Satisfaction Problems (CSP)** to solve real-world inspired scenarios.

---

## 🎯 Objectives
- Understand fundamental AI problem-solving techniques  
- Implement search-based and constraint-based algorithms  
- Compare algorithm efficiency and behavior  
- Build structured and modular Python programs  

---

# 🚦 Problem 1: Smart Navigation System (BFS & DFS)

## 📖 Description
A graph-based navigation system that finds a path between a **start node** and a **goal node** using AI search algorithms.

---

## 🧠 Algorithms Used

### 🔹 Breadth-First Search (BFS)
- Explores nodes level by level  
- Uses Queue (FIFO)  
- Guarantees shortest path  

### 🔹 Depth-First Search (DFS)
- Explores nodes deeply first  
- Uses Recursion / Stack  
- Faster but not always optimal  

---

## ⚙️ Working Logic
- Graph is predefined using adjacency list  
- User inputs start and goal nodes  
- BFS and DFS traverse graph differently  
- Paths are generated and displayed  

---

## 🧪 Sample Input

Start Node: A
Goal Node: F


---

## 📊 Sample Output

BFS Path: A → B → D → F
DFS Path: A → C → D → F


---

## 📈 Comparison

| Feature        | BFS                | DFS                |
|----------------|-------------------|--------------------|
| Path Type      | Shortest          | Not guaranteed     |
| Data Structure | Queue             | Stack / Recursion  |
| Speed          | Slower            | Faster             |
| Nodes Explored | More              | Less               |

---

# 🎨 Problem 2: Map Coloring Problem (CSP)

## 📖 Description
Assign colors to regions on a map such that **no two adjacent regions share the same color**.

---

## 🧠 Concept Used
### 🔹 Constraint Satisfaction Problem (CSP)
- Variables → Regions  
- Domains → Colors  
- Constraints → Adjacent regions must differ  

---

## ⚙️ Working Logic
- User defines regions and adjacency  
- System assigns colors using backtracking  
- If conflict occurs → backtrack and retry  
- Final valid assignment is produced  

---

## 🧪 Sample Input

Regions: A, B, C, D
Adjacency:
A → B, C
B → A, C, D
C → A, B, D
D → B, C
Colors: Red, Green, Blue


---

## 📊 Sample Output

A → Red
B → Green
C → Blue
D → Red


---

## 🚀 How to Run

### ▶️ Step 1: Clone Repository

git clone <your-repo-link>


### ▶️ Step 2: Navigate

cd AI_ProblemSolving_249


### ▶️ Step 3: Run Program

python main.py


---

## 📁 Project Structure

AI_ProblemSolving_249/
│
├── bfs_dfs_navigation/
│ ├── main.py
│ └── README.md
│
├── map_coloring_csp/
│ ├── main.py
│ └── README.md
│
└── README.md


---

## 🛠️ Technologies Used
- 🐍 Python  
- 🔍 BFS Algorithm  
- 🌳 DFS Algorithm  
- 🎨 Constraint Satisfaction Problem (CSP)  

---

## ✨ Key Features
- Clean and modular implementation  
- Covers both uninformed search and CSP  
- Easy to understand logic  
- Console-based interaction  
- Beginner-friendly and efficient  

---

## 📌 Assignment Requirements Covered
✔ Two AI problems implemented  
✔ GitHub repository maintained  
✔ Multiple commits included  
✔ Proper folder structure  
✔ README with explanation, steps, and outputs  

---

## 👨‍💻 Author
**Muralidhar**

---

## ⭐ Conclusion
This project demonstrates practical implementation of AI algorithms used in real-world applic
