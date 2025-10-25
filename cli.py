from .vars import DEFAULT_PORT
from .server import run
from .brew import brew
import argparse

def main():
    parser = argparse.ArgumentParser(description="[!] coffeepot command-line tool")
    parser.add_argument("action", choices=["serve", "brew"], help="What to do")
    parser.add_argument("--type", default="coffee", help="What to brew")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Server port")

    args = parser.parse_args()

    if args.action == "serve":
        run(args.port)
    elif args.action == "brew":
        result = brew(args.type)
        print(f"✅ {result['message']} | Aroma: {result['aroma']} | Strength: {result['strength']}")

if __name__ == "__main__":
    main()