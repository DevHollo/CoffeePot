import random
import time

def brew(kind="coffee"):
    """Simulate brewing something."""
    aromas = ["nutty", "sweet", "dark roast", "earthy", "caramel"]
    print(f"[...] Brewing {kind}...")
    time.sleep(1.5)
    aroma = random.choice(aromas)
    return {
        "status": "ready",
        "message": f"Your {kind} is brewed!",
        "aroma": aroma,
        "strength": f"{random.randint(1, 10)}/10"
    }