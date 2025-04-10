# 📝 StoryBuilder — A Wikipedia-Based AI Story Game

Welcome to **StoryBuilder**, an interactive terminal-based storytelling game powered by **Wikipedia** and **AI**! In this game, you'll choose a famous character, define a story genre, and then build a unique story through Wikipedia links and GPT-generated storytelling.

---

## 🏆 Hackathon Background

This project was built during a **4-day hackathon** as part of the **MasterSchool** software development program. The hackathon's theme was:

> 🎮 *"Create a game using Wikipedia."*

It was our **first hackathon experience** — and **we WON!** 🥇🚀

---

## 🎮 How the Game Works

1. **Choose a category**: Superheroes, Politicians, Cartoons, or Actors.
2. **Pick your character**: You'll be given 4 random characters from the category.
3. **Select a genre**: Romance, Sci-fi, Horror, Comedy or Fantasy.
4. **Set the number of articles**: Choose how many Wikipedia links to explore in your story.
5. **Build your story**:
   - Each chapter continues using the content from the selected Wikipedia article.
   - The story is generated step-by-step by GPT, in a fun and thematic tone.
6. **Keep going or finish**: After the chosen number of articles, you can either continue exploring or ask for a satisfying ending.

---

## 🧠 Tech Stack

- Python 🐍
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [OpenAI GPT API](https://platform.openai.com/)
- dotenv for API key management
- emoji for fun terminal visuals

---

## 🖼️ Game Design

You can view the game design [here](https://www.example.com/game-design-doc) 📄

---

## 🚀 Getting Started

1. Clone the repo:
```bash
git clone https://github.com/your-username/storybuilder.git
cd storybuilder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key in a `.env` file:
```
API_KEY=your_openai_api_key_here
```

4. Run the game:
```bash
python main.py
```

---

## 🤝 Team Credits

Made with ❤️ by the team  **String of Life** during our first hackathon!

---

## 📜 License

This project is licensed under the MIT License.
