# File Maker

A professional and platform-independent Python utility for effortless file management and manipulation.  
**File Maker** allows you to perform reading, writing, and appending operations on files, automatically handling the file's current path with precision.

---

## 🚀 Features

- **Cross-Platform Support**: Runs smoothly on **Windows**, **Linux**, and **Mac**.
- **Python 3.6+ Compatible**: Harnesses the power of modern Python for optimal performance.
- **Three Robust Modes**: Work with files in **Read**, **Write**, and **Append** modes.
- **Automatic File Path Detection**: Seamlessly uses the current path where the file is located.

---

## 🛠️ Requirements

- **Python**: Version **3.6** or higher  
  _Installation: [Get Python here](https://www.python.org/downloads/)_

---

## 📦 Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/file-maker.git
cd file-maker
```

---

## ⚙️ Usage

Simply invoke the script and specify your desired mode of operation:

```bash
python file_maker.py
```

---

## 📖 File Handling Modes in Python

Python provides flexible modes for file handling. **File Maker** supports the following three essential modes:

| Mode     | Syntax | Description                                                                                         |
|----------|--------|-----------------------------------------------------------------------------------------------------|
| Read     | `'r'`  | Opens the file for **reading only**. The file must exist. The file pointer is placed at the beginning of the file. |
| Write    | `'w'`  | Opens the file for **writing only**. If the file exists, its contents are **overwritten**. If it does not exist, a new file is created. |
| Append   | `'a'`  | Opens the file for **appending**. New data will be written at the end of the file. If the file does not exist, it creates a new one. |

### Detailed Explanation

#### 1. Read Mode (`'r'`)
- **Purpose**: To read the contents of an existing file.
- **Behavior**:  
  - File must already exist or an error will be raised (`FileNotFoundError`).
  - Cursor is set at the start.
- **Typical Usage**:
    ```python
    with open('example.txt', 'r') as file:
        content = file.read()
    ```

#### 2. Write Mode (`'w'`)
- **Purpose**: To create a new file or overwrite an existing file.
- **Behavior**:  
  - If the file exists, all existing data is **deleted**.
  - If the file does not exist, a new file is created.
- **Typical Usage**:
    ```python
    with open('example.txt', 'w') as file:
        file.write("Hello, World!")
    ```

#### 3. Append Mode (`'a'`)
- **Purpose**: To **add** data to the end of the file without removing existing content.
- **Behavior**:  
  - If the file does not exist, it is created.
  - The file pointer is set at the end.
  - New data is added after existing content.
- **Typical Usage**:
    ```python
    with open('example.txt', 'a') as file:
        file.write("\nNew line added!")
    ```

---

## 🌐 Platform Compatibility

- **Windows**
- **Linux**
- **Mac OS**

This project is fully tested and supported on all major operating systems.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Author
**Youcef Shaaban**

---
## 💥 Note:
Main Code Made By **Youcef Shaaban**
Imporoved Code By **Copilot**

Developed by [Youcef Shaaban](https://github.com/youcefshaaban)

---

_Professional. Reliable. Cross-Platform. That's File Maker._
