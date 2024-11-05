# Simple Chatbot Server

This repository contains the Simple Chatbot Server, which uses the OpenAI API for generating conversational responses. It demonstrates a simple implementation of [Langchain](https://python.langchain.com/docs/introduction/), utilizing Conversational Chains and Memory to maintain context across interactions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **OpenAI API Integration:** Utilizes the OpenAI API to generate dynamic and intelligent chat responses.
- **Langchain Integration:** Demonstrates the use of Langchain with Conversational Chain and Memory to persist state.
- **FastAPI Framework:** Built using FastAPI for high-performance and easy-to-use web server implementation.

## Technologies Used

- Python
- Langchain
- FastAPI
- OpenAI API

## Installation

To set up the Simple Chatbot Server locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/softdev629/simple-chatbot-server.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd simple-chatbot-server
   ```

3. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the server:**

   ```bash
   uvicorn main:app --reload
   ```

   This will launch the server on `http://127.0.0.1:8000`.

## Usage

Once the server is running, you can interact with the chatbot via API calls. It leverages Langchain for managing conversational state and OpenAI for generating responses.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Ensure your contributions adhere to the existing code style and include tests for any new functionality.

## License

This project is licensed under the MIT License. Feel free to use and modify the code.

## Contact

For questions, feedback, or more information, please contact Bohdan at [vuongtpv@gmail.com](mailto:vuongtpv@gmail.com).

---

Thank you for exploring the Simple Chatbot Server project! It serves as a practical example of integrating OpenAI API and Langchain for building responsive chat interfaces.