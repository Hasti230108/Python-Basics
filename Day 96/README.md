# Day 96 — Streamlit Colour Playground

Today, I explored how to add colours to a Streamlit application using Markdown and theme configuration. I created a Colour Playground to experiment with built-in text colours, custom HEX colours, and a pastel-pink app theme.

## Features

- 🔴 Displays red text using Streamlit Markdown.
- 🔵 Displays blue text using Streamlit Markdown.
- 🟢 Displays green text using Streamlit Markdown.
- 🟣 Displays violet text using Streamlit Markdown.
- 💗 Uses a custom pink text colour with a light-pink background.
- 🎨 Customises the overall app theme using `config.toml`.
- 🌸 Applies a pastel-pink background and secondary background.
- 🖌️ Changes the primary colour and text colour of the app.

## Technologies Used

- Python
- Streamlit
- Markdown
- TOML configuration

## Project Structure

```text
Day 96/
├── .streamlit/
│   └── config.toml
└── colour_playground.py
```

## Concepts Learned

- Using `st.markdown()` to display coloured text.
- Understanding built-in Markdown colour directives.
- Using HEX colour codes for custom colours.
- Applying foreground and background colours to text.
- Creating a `.streamlit` folder for project-specific configuration.
- Customising the app theme using `config.toml`.
- Understanding `primaryColor`, `backgroundColor`, `secondaryBackgroundColor`, and `textColor`.

## Key Learnings

I learned that Markdown can be used to colour individual text elements, while Streamlit's theme configuration can customise the overall appearance of an application.

I also learned the importance of placing `config.toml` inside the `.streamlit` folder in the working directory from which the app is run.

---

Successfully experimented with built-in colours, custom HEX colours, and a pastel-pink Streamlit theme.