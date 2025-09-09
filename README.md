<div align="center">
  <h1 align="center">🔐 Caesar Cipher – Text Encryption Tool</h1>
  <p align="center">
    A simple yet powerful <b>Python-based encryption tool</b> that uses the classical Caesar Cipher algorithm to securely shift text by a specified key value.
  </p>
  <br />


  <!-- Tech Badges -->
  <img src="https://img.shields.io/badge/-Python_3.10-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/-CLI_Tool-black?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Command Line" />
</div>

---

## 📋 Table of Contents

- [🌟 Features](#features)
- [⚙️ Tech Stack](#tech-stack)
- [🚀 Getting Started](#getting-started)
- [📚 Project Structure](#project-structure)
- [🔄 How It Works](#how-it-works)
- [🚢 Deployment](#deployment)
- [🤝 Contributing](#contributing)

---

<a name="features"></a>

## 🌟 Features

### 🔒 Caesar Cipher Encryption & Decryption

- Encrypts plaintext with a customizable shift key
- Decrypts ciphered text back to original
- Handles both **uppercase and lowercase letters**
- Ignores non-alphabetic characters (punctuation, spaces, etc.)

### 🖥️ Command-Line Interface (CLI)

- Simple CLI prompts for user-friendly interaction
- Input your message and choose a shift value
- Option to choose between encryption and decryption modes

### 📂 File Encryption Support *(Optional Enhancement)*

- Easily extendable to support file-based encryption/decryption

---

<a name="tech-stack"></a>

## ⚙️ Tech Stack

- **Language**: Python 3.x
- **Interface**: Command Line (CLI)
- **Libraries**: Built-in Python (no external dependencies)

---

<a name="getting-started"></a>

## 🚀 Getting Started

### **Prerequisites**

- Python 3.6+
- Terminal or command prompt

### **Clone the Repository**

```bash
git clone https://github.com/Krishna-Sharma07/caesar-cipher.git
cd caesar-cipher
````

### **Run the Program**

```bash
python caesar_cipher.py
```

### Example CLI Interaction

```
Welcome to Caesar Cipher!

Choose mode:
1. Encrypt
2. Decrypt
> 1

Enter your message:
> Hello World

Enter shift value:
> 3

Encrypted message:
> Khoor Zruog
```

---

<a name="project-structure"></a>

## 📚 Project Structure

```
caesar-cipher/
├── caesar_cipher.py      # Main Python file containing the logic
├── README.md             # Project documentation
└── examples/             # (Optional) Input/output examples or test cases
```

---

<a name="how-it-works"></a>

## 🔄 How It Works

1. **Input**: User enters text and shift value
2. **Shift Logic**: Each letter is shifted by the key value

   * Wraps around alphabet (`Z` to `A`, `z` to `a`)
3. **Output**: Transformed text is displayed

> Note: Non-letter characters (spaces, numbers, punctuation) are preserved as-is.

---

<a name="deployment"></a>

## 🚢 Deployment

This project runs locally on any machine with Python installed. No deployment or hosting required.

For packaging into an executable:

```bash
pip install pyinstaller
pyinstaller --onefile caesar_cipher.py
```

The resulting binary will be located in the `/dist` folder.

---

<a name="contributing"></a>

## 🤝 Contributing

Contributions are welcome!

1. Fork this repo
2. Create a branch → `git checkout -b feature/your-feature`
3. Commit → `git commit -m "Add new feature"`
4. Push → `git push origin feature/your-feature`
5. Open a pull request 🚀

---

<div align="center">
  🔐 Built with 🧠 and 💻 by Krishna Sharma — using pure <strong>Python</strong> for simple encryption logic.
</div>
```
