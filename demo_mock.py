"""Offline mock demo that reproduces the VIN lookup / assistant flow from the video.

Usage:
  - Interactive mode: python demo_mock.py
  - Demo script: python demo_mock.py --demo

The script uses the project's `db_driver.DatabaseDriver` and `prompts` to keep behavior consistent.
"""
from __future__ import annotations
import argparse
import time
from db_driver import DatabaseDriver
from prompts import WELCOME_MESSAGE, LOOKUP_VIN_MESSAGE

DB = DatabaseDriver("demo_auto_db.sqlite")


class MockAssistant:
    def __init__(self, db: DatabaseDriver):
        self.db = db

    def lookup_car(self, vin: str) -> str:
        vin = vin.strip()
        print(f"[assistant] looking up VIN: {vin}")
        result = self.db.get_car_by_vin(vin)
        if result is None:
            # Follow prompt guidance from prompts.py
            return f"Car not found. {LOOKUP_VIN_MESSAGE(vin)}"

        return (
            f"The car details are:\n"
            f"VIN: {result.vin}\n"
            f"Make: {result.make}\n"
            f"Model: {result.model}\n"
            f"Year: {result.year}"
        )

    def create_car(self, vin: str, make: str, model: str, year: int) -> str:
        print(f"[assistant] creating car: {vin}, {make}, {model}, {year}")
        try:
            self.db.create_car(vin, make, model, year)
        except Exception as e:
            return f"Failed to create car: {e}"
        return "car created!"


def run_interactive():
    assistant = MockAssistant(DB)
    print(WELCOME_MESSAGE)
    print("(type 'help' for commands)")

    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting demo.")
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()

        if cmd in ("quit", "exit"):
            print("Goodbye")
            break
        if cmd == "help":
            print("Commands:\n  lookup <vin>\n  create <vin> <make> <model> <year>\n  exit")
            continue
        if cmd == "lookup":
            if len(parts) < 2:
                print("Usage: lookup <vin>")
                continue
            vin = parts[1]
            out = assistant.lookup_car(vin)
            print(out)
            continue
        if cmd == "create":
            if len(parts) < 5:
                print("Usage: create <vin> <make> <model> <year>")
                continue
            vin, make, model, year = parts[1], parts[2], parts[3], parts[4]
            try:
                year_i = int(year)
            except ValueError:
                print("year must be an integer")
                continue
            out = assistant.create_car(vin, make, model, year_i)
            print(out)
            continue

        print("Unknown command. Type 'help'.")


def run_demo_script():
    assistant = MockAssistant(DB)
    vin = "1HGCM82633A004352"
    print(WELCOME_MESSAGE)
    time.sleep(0.5)
    print(f"\n[user] lookup {vin}")
    out = assistant.lookup_car(vin)
    print(f"[assistant] {out}")

    # create the car
    time.sleep(0.5)
    print(f"\n[user] create {vin} Honda Accord 2003")
    out = assistant.create_car(vin, "Honda", "Accord", 2003)
    print(f"[assistant] {out}")

    # lookup again
    time.sleep(0.5)
    print(f"\n[user] lookup {vin}")
    out = assistant.lookup_car(vin)
    print(f"[assistant] {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run the scripted demo and exit")
    args = parser.parse_args()

    if args.demo:
        run_demo_script()
    else:
        run_interactive()
