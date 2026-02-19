# Part 1: Python Environment & Virtual Environments

**Duration:** 2-3 hours | **Level:** Beginner | **Prerequisites:** None

---

## 📚 Overview

Before diving into machine learning, you need a **clean, isolated Python environment**. This Part covers:
- Installing Python correctly
- Creating virtual environments
- Managing dependencies with pip
- Verifying your setup

---

## 🎯 Learning Outcomes

By the end of this Part, you will:
- ✅ Have Python 3.8+ installed on your system
- ✅ Understand why virtual environments matter
- ✅ Create and activate a virtual environment  
- ✅ Install required ML packages
- ✅ Run Python code to verify everything works

---

## 🔧 Part 1: Python Installation

### **Step 1: Check if Python is Installed**

Open your terminal/command prompt and run:

```bash
python --version
```

**Expected Output:**
```
Python 3.8.0  # or higher (3.9, 3.10, 3.11 all fine)
```

### **Step 2: Install Python (if needed)**

#### **Windows:**
1. Go to [python.org](https://www.python.org/downloads/)
2. Click "Download Python 3.11" (or latest stable version)
3. Run the installer
4. **IMPORTANT:** Check "Add Python to PATH" during installation
5. Click "Install Now"
6. Verify: Open Command Prompt and run `python --version`

#### **macOS:**
```bash
# Using Homebrew (recommended)
brew install python3

# Or download from python.org (same as Windows)
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### **Linux (Fedora):**
```bash
sudo dnf install python3 python3-pip
```

---

## 📦 Part 2: Virtual Environments

### **Why Virtual Environments?**

Virtual environments are **isolated Python installations** on your machine.

**Benefits:**
- Different projects can use different package versions
- No conflicts between projects
- Easy to reproduce environments
- Professional standard practice

**Example Problem (without venv):**
```
Project A needs NumPy 1.19
Project B needs NumPy 1.23
Both installed globally → CONFLICT!

With venv: Each has its own NumPy version ✅
```

### **Creating a Virtual Environment**

#### **On Windows:**
```bash
# Create virtual environment named 'ml_internship'
python -m venv ml_internship

# Activate it
ml_internship\Scripts\activate

# You should see: (ml_internship) C:\path\to\directory>
```

#### **On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv ml_internship

# Activate it
source ml_internship/bin/activate

# You should see: (ml_internship) user@machine:~$
```

### **Verifying Virtual Environment is Active**

When activated, you should see:
```
(ml_internship) your_prompt_here>
```

The `(ml_internship)` prefix shows your virtual environment is active.

---

## 💾 Part 3: Installing ML Libraries

Once your virtual environment is **active**, install the required packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

This installs:
- **numpy** - Numerical computing
- **pandas** - Data manipulation
- **matplotlib** - Basic plotting
- **seaborn** - Advanced visualization
- **scikit-learn** - Machine learning library
- **jupyter** - Interactive notebooks

### **Installation Output**

```
Collecting numpy
  Downloading numpy-1.24.3-cp311-cp311-win_amd64.whl (14.6 MB)
Installing collected packages: numpy, pandas, ...
Successfully installed numpy-1.24.3 pandas-2.0.0 ...
```

**This takes 2-5 minutes depending on internet speed.**

### **Verify Installation**

Run this Python script to test everything:

```bash
python -c "
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print('✅ NumPy:', np.__version__)
print('✅ Pandas:', pd.__version__)
print('✅ Matplotlib:', plt.matplotlib.__version__)
print('✅ Seaborn:', sns.__version__)
print('✅ Scikit-learn:', sklearn.__version__)
print()
print('🎉 All packages installed successfully!')
"
```

**Expected Output:**
```
✅ NumPy: 1.24.3
✅ Pandas: 2.0.0
✅ Matplotlib: 3.7.1
✅ Seaborn: 0.12.2
✅ Scikit-learn: 1.2.2

🎉 All packages installed successfully!
```

---

## 🧪 Part 4: Creating Your First Script

Create a file named `test_setup.py`:

```python
#!/usr/bin/env python3
"""
Test script to verify Python environment setup.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

def test_numpy():
    """Test NumPy installation and basic operations."""
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {arr}")
    print(f"Array mean: {np.mean(arr)}")
    print(f"Array std: {np.std(arr)}")
    return True

def test_pandas():
    """Test Pandas installation and basic operations."""
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [95, 87, 92]
    })
    print("\nPandas DataFrame:")
    print(df)
    print(f"Mean score: {df['Score'].mean()}")
    return True

def test_matplotlib():
    """Test Matplotlib plotting."""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.savefig("sine_wave.png")
    print("\n✅ Plot saved as 'sine_wave.png'")
    return True

def test_sklearn():
    """Test Scikit-learn installation."""
    from sklearn.datasets import load_iris
    iris = load_iris()
    print(f"\nLoaded Iris dataset with {len(iris.target)} samples")
    print(f"Number of features: {iris.data.shape[1]}")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("PYTHON ENVIRONMENT TEST SUITE")
    print("=" * 50)
    
    tests = [
        ("NumPy", test_numpy),
        ("Pandas", test_pandas),
        ("Matplotlib", test_matplotlib),
        ("Scikit-learn", test_sklearn)
    ]
    
    passed = 0
    for name, test_func in tests:
        try:
            if test_func():
                print(f"✅ {name} test passed\n")
                passed += 1
        except Exception as e:
            print(f"❌ {name} test failed: {e}\n")
    
    print("=" * 50)
    print(f"RESULTS: {passed}/{len(tests)} tests passed")
    print("=" * 50)
    
    if passed == len(tests):
        print("\n🎉 All systems go! You're ready to start learning ML!")
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
```

**Run it:**
```bash
python test_setup.py
```

**Expected Output:**
```
==================================================
PYTHON ENVIRONMENT TEST SUITE
==================================================
NumPy array: [1 2 3 4 5]
Array mean: 3.0
Array std: 1.4142135623730951
✅ NumPy test passed

Pandas DataFrame:
     Name  Score
0   Alice     95
1     Bob     87
2 Charlie     92
Mean score: 91.33...
✅ Pandas test passed

✅ Plot saved as 'sine_wave.png'
✅ Matplotlib test passed

Loaded Iris dataset with 150 samples
Number of features: 4
✅ Scikit-learn test passed

==================================================
RESULTS: 4/4 tests passed
==================================================

🎉 All systems go! You're ready to start learning ML!
```

---

## 🔄 Part 5: Deactivating Virtual Environment

When you're done working, **deactivate the virtual environment**:

```bash
deactivate
```

The `(ml_internship)` prefix should disappear.

**To reactivate later:**
```bash
# Windows
ml_internship\Scripts\activate

# macOS/Linux
source ml_internship/bin/activate
```

---

## 📖 Troubleshooting

### **Problem: "python command not found"**
- **Solution:** Python is not in your PATH. Reinstall and check "Add Python to PATH"
- On macOS/Linux: Use `python3` instead of `python`

### **Problem: "pip command not found"**
- **Solution:** Make sure virtual environment is activated
- Check: Do you see `(ml_internship)` in your terminal?

### **Problem: "ModuleNotFoundError: No module named 'numpy'"**
- **Solution:** Install packages while virtual environment is active
- Run: `pip install numpy` with `(ml_internship)` visible

### **Problem: Permission denied (macOS/Linux)**
- **Solution:** Use `sudo` or reinstall Python without sudo
- Best practice: Use virtual environments to avoid this

### **Problem: Installation takes forever**
- **Solution:** Your internet might be slow
- Try: `pip install --no-cache-dir numpy` (faster)
- Alternative: Download wheels manually from [PyPA](https://pypa.io/)

---

## 📚 Key Concepts

| Concept | Meaning | Example |
|---------|---------|---------|
| **Virtual Environment** | Isolated Python installation | `ml_internship/` folder |
| **pip** | Python package installer | `pip install numpy` |
| **Requirements.txt** | List of dependencies | `numpy==1.24.3` |
| **Activation** | Enable a venv | `source venv/bin/activate` |
| **Package** | Reusable code library | `numpy`, `pandas` |

---

## 🔗 Additional Resources

### **Python Installation:**
- **Official Python Site:** [python.org](https://www.python.org/)
  - Direct download links for all OS
  - Official documentation

### **Virtual Environments:**
- **Official venv Guide:** [python.org/docs/venv](https://docs.python.org/3/library/venv.html)
  - Deep dive into virtual environment management
  
- **Real Python - Virtual Environments:** [realpython.com/python-virtual-environments](https://realpython.com/python-virtual-environments-a-primer/)
  - Comprehensive guide with examples
  
- **Why Virtual Environments Matter:** [Medium Article](https://medium.com/swlh/why-you-should-use-python-virtual-environments-1f7ed3c34eb)
  - Real-world problems they solve

### **Package Management:**
- **pip Documentation:** [pip.pypa.io](https://pip.pypa.io/)
  - Complete pip command reference
  
- **Writing Requirements Files:** [pip-requirements.txt Guide](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
  - How to create `requirements.txt` for sharing projects

### **Troubleshooting:**
- **Stack Overflow Python Questions:** [stackoverflow.com/questions/tagged/python](https://stackoverflow.com/questions/tagged/python)
  - Answers to common Python setup issues
  
- **Python Error Messages Explained:** [Real Python Error Reference](https://realpython.com/python-keyerror/)
  - Understanding what went wrong

### **Best Practices:**
- **Python Packaging Guide:** [python-packaging.readthedocs.io](https://python-packaging.readthedocs.io/)
  - Professional Python setup practices
  
- **PEP 8 Style Guide:** [pep8.org](https://pep8.org/)
  - Write Pythonic code from the start

---

## ✅ Success Criteria

You've successfully completed Part 1 when:

- [ ] Python 3.8+ is installed (`python --version` shows version)
- [ ] Virtual environment created (`ml_internship/` folder exists)
- [ ] Virtual environment activates (`(ml_internship)` shows in terminal)
- [ ] All packages installed (pip list shows numpy, pandas, etc.)
- [ ] Test script runs successfully (all 4 tests pass)
- [ ] You can write and run Python scripts

---

## 🎓 Next Steps

Once you've completed this Part:
→ Move to **Part 2: Git & GitHub** to set up version control

---

**Part Status:** ✅ Complete  
**Difficulty:** ⭐ (Beginner friendly)  
**Time Estimate:** 2-3 hours  
**Key Takeaway:** A clean Python environment is the foundation for professional ML development.
