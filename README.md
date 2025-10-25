# ☕ CoffeePot (v0.0.1a1)

CoffeePot is a fun, quirky Python module and server that lets you **brew coffee (and other drinks)** via HTTP, CLI, or directly in Python code. Inspired by the HTCPCP “Hyper Text Coffee Pot Control Protocol,” CoffeePot is perfect for programmers who want a cozy, playful local server.

---

## Features

- Start a local **CoffeeServer** with a cozy default HTML page.
- **BREW** endpoint simulating different types of drinks:
  - `coffee`, `espresso`, `latte`, `mocha`, `tea`, `hot chocolate`.
- Each drink type can have **unique effects** (strength, aroma, mood).
- Flexible routing using HTTP methods:
  - `GET /brew` → pull a coffee safely
  - `BREW /brew` → full HTCPCP brew
  - `POST /latte`, `PUT /mocha`, `PATCH /tea`, `BREW /hot-chocolate`
- Fully **programmatic API**: use `brew()` and `run()` in Python scripts.
- Fun ASCII art and cozy startup messages in the terminal.

---

## Installation

```bash
git clone https://github.com/DevHollo/CoffeePot.git
cd CoffeePot
pip install -e .
```

This installs CoffeePot in editable mode so you can modify it while developing.

### Via pip:

`pip install coffeepot-http`

---

## CLI Usage

**Start the server:**

```bash
python -m coffeepot.cli serve --port 2615
```

- Opens `http://127.0.0.1:2615/` with the default cozy homepage.
- Try:
```bash
curl -X BREW http://127.0.0.1:2615/brew
curl http://127.0.0.1:2615/brew?type=espresso
```

**Brew a coffee from CLI:**

```bash
python -m coffeepot.cli brew --type latte
```

---

## Programmatic Usage

```python
from CoffeePot import brew, run

# Brew an espresso programmatically
coffee = brew("espresso")
print(coffee)

# Start CoffeeServer programmatically
run(port=2615)
```

**Sample output from `brew("latte")`:**

```json
{
  "status": "ready",
  "message": "Your latte is brewed!",
  "strength": 4,
  "aroma": "milky"
}
```

---

## Custom HTML

You can provide a custom HTML page for the server:

```bash
python -m CoffeePot.cli serve --html mypage.html
```

- `/` and `/index.html` will serve your custom page.
- All brew routes continue to work normally.

---

## Extend CoffeePot

- Add new drink types with unique effects in `brew.py`.
- Register new routes with `@CoffeeServer.route("/drink", method="POST")`.
- Customize HTML, ASCII art, or responses to make your CoffeePot truly yours.

---

## Fun Facts

- Default server port is `☕` (U+2615, decimal 9749).
- Full HTCPCP-inspired methods make your API feel like a real coffee machine.
- Cozy ASCII art makes even a 404 error a bit more charming.

---

## License

MIT License. Feel free to brew, share, and fork!
