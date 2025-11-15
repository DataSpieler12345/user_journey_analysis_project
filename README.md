<p align="center">
  <img src="images/the_project.PNG" alt="User Journey Analysis Banner" width="100%">
</p>

<h1 align="center">📊 User Journey Analysis in Python</h1>

<p align="center">
  <b>Analyze user navigation patterns, identify most visited pages, discover common journeys, and extract behavioral insights from raw web logs.</b>
  <br>
  <br>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas">
  <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

## 🚀 Overview

This project processes raw page-view logs and transforms them into **meaningful behavioral insights** about how users navigate across a website.

You will uncover:

- ⭐ **Most visited pages**
- 🔁 **Most frequent next pages (follow-up navigation)**
- 🔗 **Most common user journey sequences (N-grams)**
- 📏 **Average journey length**
- 🎯 **Insights to optimize conversions & user flows**

---

## 📌 Key Insights (Examples)

### **1️⃣ Most Popular Pages**
{'Total pages': 3282, 'Homepage': 634, 'Sign up': 480, 'Other': 417, 'Courses': 344, ...}

---

### **2️⃣ Most Frequent Follow-Ups (after Homepage)**
{'Pricing': 133, 'Sign up': 124, 'Career tracks': 123, 'Courses': 90, ...}

---

### **3️⃣ Most Common 3-Page Journeys**
{('Homepage', 'Career tracks', 'Sign up'): 34,
('Homepage', 'Pricing', 'Checkout'): 24,
('Homepage', 'Courses', 'Sign up'): 23, ... }

---

### **4️⃣ Average Journey Length**
📏 **2.43 pages per journey**  
Indicates quick user drop-off or highly efficient navigation depending on context.

---

## 🧱 Project Structure

user_journey_analysis_project/
│── notebooks/
│ ├── User_journey_analysis.ipynb
│ └── User_journey_preprocessing.ipynb
│
│── src/
│ ├── preprocessing.py
│ └── analysis.py
│
│── images/ ← place your project screenshots here
│── requirements.txt
│── README.md


---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| 🐍 **Python** | Core programming language |
| 📊 **Pandas** | Data manipulation & exploration |
| 🔢 **NumPy** | Sequence & numeric operations |
| 📓 **Jupyter** | Interactive analysis environment |
| 🧾 **Git** | Version control |

---

## 🖼️ Project Images / Visualizations

Place your images in:  
`/images/`  

### 📌 Example placeholders (you can replace with your own)

1. **Most Popular Pages**
2. **Navigation Follow-Ups**
3. **User Journey Sequences**

```md
<p align="center">
  <img src="images/placeholder1.png" width="70%">
  <br>
  <em>Most Popular Pages</em>
</p>

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/user_journey_analysis_project.git
cd user_journey_analysis_project

Install required libraries:

pip install -r requirements.txt

Run the main notebook:

jupyter notebook notebooks/User_journey_analysis.ipynb

📬 Contact

Author: DataSpieler
🌐 GitHub: https://github.com/dataspieler
