# 🧠 Sorting Algorithms Cheat Sheet

## 💬 Overview
Sorting algorithms are essential for understanding efficiency, data manipulation, and algorithmic thinking.  
Below is a summary of the most common ones — including when to use them and their time complexities.

---

## ⚙️ Comparison Table

| 🧩 Algorithm | 💡 Core Idea | ⏱️ Time Complexity | ⚙️ When to Use | 🧮 Type |
|---------------|--------------|-------------------|----------------|--------|
| **Bubble Sort** 💨 | Compare adjacent elements and swap if they’re in the wrong order. Each pass “bubbles” the largest to the end. | **O(n²)** time<br>**O(1)** space | Educational purposes or very small datasets. | **Comparative**, stable |
| **Selection Sort** 🎯 | Find the smallest element and place it at the beginning, repeat for the rest. | **O(n²)** time<br>**O(1)** space | When swaps are costly but comparisons are cheap. | **Comparative**, not stable |
| **Insertion Sort** 🧩 | Insert each element into its correct place in the sorted part of the list. | **O(n²)** worst<br>**O(n)** best<br>**O(1)** space | Great for **small** or **almost sorted** lists. | **Comparative**, stable |
| **Quick Sort** ⚡ | Pick a pivot, split the list into smaller and larger parts, then sort recursively. | **O(n log n)** average<br>**O(n²)** worst<br>**O(log n)** space | Best general-purpose sort for large datasets. | **Divide & Conquer**, not stable |
| **Merge Sort** 🪄 | Divide the list in halves, sort each half, then merge them back together. | **O(n log n)** time<br>**O(n)** space | When **stability** matters and memory isn’t a constraint. | **Divide & Conquer**, stable |

---

## 📊 Interview Highlights

- **Bubble vs Selection:** Bubble makes many swaps; Selection does only one per pass.  
- **Insertion Sort:** Fast for nearly sorted data.  
- **Quick Sort:** Usually fastest in practice, thanks to recursion and partitioning.  
- **Stable Algorithm:** Keeps equal elements in the same relative order.  
- **Python’s `.sort()` and `sorted()` use:** 🧠 **Timsort** → hybrid of Merge Sort + Insertion Sort.  

---

> 🧩 **Tip:** Even though modern programming languages have built-in sorting functions,  
> understanding these algorithms shows strong problem-solving and algorithmic thinking skills — a must in technical interviews.