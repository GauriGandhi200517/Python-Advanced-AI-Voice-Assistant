# 🐍 Python Advanced AI Voice Assistant — Offline Demo Mock

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An attractive, information-rich README for the demo harness that lets you test the conversational VIN lookup flow locally — no LiveKit or OpenAI required.

---

## ✨ Highlights
- Lightweight offline mock of the AI voice assistant flow (VIN lookup).  
- Great for development, tests, and demos without external APIs.  
- Small SQLite DB for persisting demo auto records. Delete it to reset state.

---

## 📁 What’s in this repo
- `demo_mock.py` — interactive/scripted demo harness (main entrypoint).  
- `prompts.py` — built-in assistant prompts and welcome messages.  
- `db_driver.py` — thin DB abstraction around `demo_auto_db.sqlite`.  
- `.env.example` — example env vars for live demo (redacted).  
- `demo_auto_db.sqlite` — demo SQLite DB (created next to script on first run).  
- `LICENSE` — MIT License (this project is already licensed under MIT). ✅

---

## ⚙️ Requirements
- Python 3.8+  
- (Optional) Virtual environment recommended

---

## 🚀 Quick start

1. Clone the repo and change into the project folder.
2. Create and activate a virtual env (recommended).

PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python .\demo_mock.py --demo    # scripted demo
python .\demo_mock.py           # interactive mode
```

macOS / Linux (bash/zsh):
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 demo_mock.py --demo
python3 demo_mock.py
```

---

## 🧭 Commands (inside demo)
- `lookup <VIN>` — look up a VIN in the demo DB and print details or guidance.  
    Example: `lookup 1HGCM82633A004352`  
- `create <VIN> <make> <model> <year>` — add a demo car entry.  
    Example: `create 1HGCM82633A004352 Honda Accord 2003`  
- `help` — show available commands.  
- `exit` — quit the demo.

---

## 🔍 What the mock does
- Prints a friendly welcome (from `prompts.py`) 🎤  
- Parses simple text commands and returns deterministic responses ✅  
- Reads/writes `demo_auto_db.sqlite` via `db_driver.DatabaseDriver` (safe to delete to reset) 🗃️

---

## 🔐 Real demo vs offline mock
To run the live demo (connect to LiveKit / OpenAI) you must:
- Populate `.env` with valid credentials (see `.env.example`)  
- Run the real agent: `python agent.py`  
This offline mock is intentionally lightweight to avoid third-party dependencies.

---

## 🛠️ Development tips
- To reset the demo DB: stop demo and delete `demo_auto_db.sqlite`.  
- Add sample records with `create` or by prepopulating a small SQLite DB.  
- Use the `--demo` flag to simulate a scripted conversation (useful for CI / demos).

---

## 📦 Packaging & Deployment
This is a local demo harness — packaging is optional. Consider:
- Adding `pyproject.toml` / `setup.cfg` for pip installs.  
- Dockerizing if you want reproducible demo environments.

---

## 🧪 Tests
No formal test suite included. Suggested quick checks:
- Run `python demo_mock.py --demo` and verify scripted output.  
- Manually test `create` + `lookup` round-trip.

---

## 🤝 Contributing
Contributions welcome! Suggested improvements:
- Add unit tests for `db_driver` and CLI parsing.  
- Expand prompt variations or add TTS/ASR stubs for richer demos.

---

## 📄 License & Credits

This project is licensed under the MIT License — see the included `LICENSE` file for full terms.

Copyright (c) 2024-2025 The Project Contributors

Third-party libraries and attribution
- Backend: Flask (BSD-style), python-dotenv, LiveKit Python SDK and related plugins. See each package's own license for details.
- Frontend: React, React DOM, Vite, livekit-client, @livekit/components-react and @livekit/components-styles, react-router-dom. Refer to each dependency's license in `frontend/node_modules` or upstream repositories.

Credits
- This demo harness and UI were inspired by upstream examples (see project history / commit log). Portions of the frontend were adapted from public LiveKit example projects — please retain the upstream attributions when redistributing.

Redistribution notes
- If you redistribute a modified version of this project, include the original `LICENSE` file and retain attributions for third-party libraries that require it.
- Do not commit secrets (API keys, secrets). Use `.env` and environment variables for credentials and provide a `.env.example` with placeholders.

Maintainer / Contact
- Maintainer: Project Owner (see repository metadata). For issues or contributions, please open an issue or pull request on the repository.

If you'd like, I can expand this section further with exact library license lines (SPDX identifiers) or add authorship entries — tell me how detailed you want it.

---

## 🗒️ Notes
- This README focuses on the offline mock — the real agent depends on external services and credentials.  
- Keep secrets out of repo; use `.env` and environment variables.

Happy hacking! 🚀
