Password Generator 📱

A modern, user-friendly password generator application built with Python and Tkinter that creates secure, customizable passwords with strength evaluation.
✨ Features

  Customizable Password Generation

        Adjustable length (8-128 characters)

        Multiple password generation (1-20 at once)

        Character set selection (uppercase, lowercase, numbers, special characters)

  Security Features

        Password strength evaluation (Weak, Medium, Strong)

        Visual strength indicators with color coding

        Hide/Show password toggle

        One-click copy to clipboard

  User Experience

        Clean, modern GUI with blue theme

        Scrollable output area for multiple passwords

        Real-time validation and error handling

        Responsive design

🛠️ Installation

   Prerequisites

        Python 3.6 or higher

        Tkinter (usually included with Python)

Clone the repository
bash

    git clone https://github.com/yourusername/password-generator.git
    cd password-generator

Run the application
bash

    python main.py

or
bash

    python passgen.py

🚀 Usage

    Set your desired password length (8-128 characters)

    Choose how many passwords to generate (1-20)

    Select character types to include

    Click "Generate Passwords"

    Use "Show/Hide" to reveal passwords or "Copy" to clipboard

📁 Project Structure
text

password-generator/
├── main.py              # Main application entry point
├── passgen.py           # Alternative implementation
├── generator.py         # Password generation logic
├── character_sets.py    # Character set definitions
├── widgets.py           # UI component functions
├── requirements.txt     # Project dependencies
└── Password Generator.spec  # PyInstaller configuration

🏗️ Architecture

The application follows a modular architecture:

    UI Layer: main.py, passgen.py, widgets.py

    Business Logic: generator.py, character_sets.py

    Separation of concerns for maintainability and testing
