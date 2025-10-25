from .vars import VERSION, FAVICON_BASE64, DEFAULT_PORT
from urllib.parse import urlparse, parse_qs
from .ascii import COFFEEPOT_LOGO
from .brew import brew
import http.server
import json

DEFAULT_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CoffeePot Server v{VERSION}</title>
    <link rel="icon" type="image/png" href="{FAVICON_BASE64}">
    <style>
        body {{
            font-family: system-ui, sans-serif;
            background: linear-gradient(135deg, #f2e6d9, #d1bfa7);
            color: #3e2723;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            flex-direction: column;
        }}
        pre {{
            background: #f7f3ef;
            padding: 1em;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.15);
        }}
        h1 {{
            font-size: 2rem;
            margin-bottom: 0.2em;
        }}
        .note {{
            margin-top: 1em;
            opacity: 0.7;
        }}
        code {{
            background: #eee;
            padding: 2px 4px;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <h1>☕ CoffeePot Server is Brewing</h1>
    <pre>{COFFEEPOT_LOGO}</pre>
    <p>Welcome to your CoffeePot server. It's up and running!</p>
    <p class="note">Try <code>curl -X BREW http://127.0.0.1:{DEFAULT_PORT}/brew</code> or <code>curl http://127.0.0.1:{DEFAULT_PORT}/brew</code></p>
</body>
</html>
"""

class CoffeeServer(http.server.BaseHTTPRequestHandler):
    routes = {}

    @classmethod
    def route(cls, path, method="GET"):
        """Register a route."""
        def decorator(func):
            cls.routes[(path, method.upper())] = func
            return func
        return decorator

    def do_GET(self):
        self._handle_request("GET")

    def do_POST(self):
        self._handle_request("POST")

    def do_PUT(self):
        self._handle_request("PUT")

    def do_PATCH(self):
        self._handle_request("PATCH")

    def do_BREW(self):
        """Custom HTCPCP BREW method."""
        self._handle_request("BREW")

    def _handle_request(self, method):
        parsed = urlparse(self.path)
        if parsed.path in ["/", "/index.html"]:
            self._send_html(DEFAULT_HTML)
            return
        route_key = (parsed.path, method)
        handler = self.routes.get(route_key)
        if handler:
            params = parse_qs(parsed.query)
            result = handler(params)
            self._send_json(result)
        else:
            self._send_json({"error": "Unknown route or method"}, code=404)

    def _send_json(self, data, code=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html, code=200):
        body = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

@CoffeeServer.route("/brew", method="GET")
def default_brew_get(params):
    """GET /brew returns a coffee without modifying anything."""
    brew_type = params.get("type", ["coffee"])[0]
    return brew(brew_type)

@CoffeeServer.route("/brew", method="BREW")
def default_brew_brew(params):
    """BREW method simulates a full HTCPCP brew."""
    brew_type = params.get("type", ["coffee"])[0]
    return brew(brew_type)

@CoffeeServer.route("/latte", method="POST")
def latte_post(params):
    return brew("latte")

@CoffeeServer.route("/mocha", method="PUT")
def mocha_put(params):
    return brew("mocha")

@CoffeeServer.route("/tea", method="PATCH")
def tea_patch(params):
    return brew("tea")

@CoffeeServer.route("/hot-chocolate", method="BREW")
def chocolate_brew(params):
    return brew("hot chocolate")

def run(port=DEFAULT_PORT):
    print(COFFEEPOT_LOGO)
    print(f"[!] CoffeeServer running on http://127.0.0.1:{port}")
    server = http.server.HTTPServer(("0.0.0.0", port), CoffeeServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nCoffeeServer shutting down...")
        server.server_close()
