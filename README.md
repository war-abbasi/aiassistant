# 🧠 AI Chat Assistant with LangChain & OpenAI

<p align="center">
  <img src="banner.png" alt="AI Chat Assistant Banner" width="100%" />
</p>

A command-line AI assistant built using **LangChain**, **LangGraph**, and **OpenAI’s GPT-3.5-Turbo**. This assistant supports natural language interaction and can evaluate complex mathematical expressions through a seamless chat interface.

---

## ✨ Features

* 🤖 Conversational AI assistant powered by OpenAI
* ➗ Supports mathematical calculations like `17 * (4 + 9)`
* 🔁 Continuous chat loop until user types `quit`
* 🛠 Built with **LangChain**, **LangGraph**, and **OpenAI GPT**

---

## 🚀 Getting Started

Follow these simple steps to get your assistant running:

### 1. Clone the Repository

```bash
git clone https://github.com/war-abbasiaiassistant.git
cd aiassistant
```

### 2. Create a Virtual Environment (Recommended)

```bash
# For Linux/macOS
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install manually:

```bash
pip install openai langchain langgraph python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-your-api-key
```

Make sure this file is **not committed** to version control.

---

## 🧪 How to Use

Run the assistant:

```bash
python proj1.py
```

You’ll see:

```
Welcome to your AI assistant
You can tell me to do calculations
```

Now enter prompts like:

```
what is the square root of 625
```

To exit the assistant, type:

```
quit
```

---

## 📂 Project Structure

```
.
├── proj1.py           # Main Python script
├── .env               # Environment file with OpenAI API key (ignored by Git)
├── banner.png         # Project banner (optional but recommended)
├── README.md          # Project documentation
```

---

## 🛠 Technologies Used

* [OpenAI GPT-3.5-Turbo](https://platform.openai.com/docs/models/gpt-3-5)
* [LangChain](https://www.langchain.com/)
* [LangGraph](https://www.langchain.com/langgraph)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

## ❗ Troubleshooting

* **Quota Exceeded?**
  Visit your [OpenAI usage dashboard](https://platform.openai.com/account/usage) to check limits and add billing.

* **API Key Not Loading?**
  Ensure `.env` is present and you're using `load_dotenv()` before initializing the LLM.

---

## 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it as needed.

---

## 👩‍💻 Author

**Wardah Zia Abbasi**
🔗 [GitHub: @war-abbasi](https://github.com/war-abbasi)

---

## 🙌 Contributions

Pull requests are welcome!
Feel free to fork the repo and contribute improvements, new features, or bug fixes.
