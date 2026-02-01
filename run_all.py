import json
from pathlib import Path

def main():
    out = Path("outputs")
    out.mkdir(exist_ok=True)

    # Placeholder outputs — teams replace these with real planning + simulation results
    aircraft = {
        "status": "placeholder",
        "todo": "aircraft mission planning + simulation + constraints + metrics"
    }
    spacecraft = {
        "status": "placeholder",
        "todo": "7-day LEO mission plan + downlink scheduling + constraints + metrics"
    }

    (out / "aircraft_demo_output.json").write_text(json.dumps(aircraft, indent=2))
    (out / "spacecraft_demo_output.json").write_text(json.dumps(spacecraft, indent=2))

    print("Wrote outputs/aircraft_demo_output.json")
    print("Wrote outputs/spacecraft_demo_output.json")

if __name__ == "__main__":
    main()
