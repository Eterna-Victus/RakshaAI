<<<<<<< HEAD
# RakshaAI

RakshaAI is a hackathon-ready mining safety and predictive-maintenance demo combining CoalGuard and Khaan Netra.

## Architecture


The repository uses FastAPI rather than the Express paths described in the original feature brief. REST APIs are authoritative; WebSocket and offline clients degrade gracefully.

## Run Locally

Terminal 1, backend:

```powershell
cd coalguard/backend
python -m pip install -r requirements.txt
python scripts/seed_reset.py
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Terminal 2, React dashboard:

```powershell
cd coalguard/frontend
npm install
npm run dev
```

Open `http://127.0.0.1:4173/`. Demo credentials use password `demo123`; seeded user emails are in `coalguard/backend/scripts/seed_reset.py`.

Terminal 3, Khaan Netra camera PWA (needed for live camera development):

```powershell
cd khaan-netra
python -m http.server 8080
```

Open `http://127.0.0.1:8080/`. The React Vite proxy forwards `/khaan-netra/*` to this server when both servers are running.

For a self-contained production demo, build the dashboard instead:

```powershell
cd coalguard/frontend
npm run build
npm run preview
```

The build copies Khaan Netra to `dist/khaan-netra`, so the dashboard link works without Terminal 3. When Khaan Netra is opened directly on port 8080, its CV and offline-sync bridge targets the FastAPI server on port 8000. Set `window.KHAAN_API_URL` before loading it to use another backend URL.

## Demo Flow

1. Open `/telemetry` and observe live sensor charts.
2. Inject a methane leak or bearing thermal surge.
3. Watch hazards, RUL degradation, and the generated ticket.
4. Open `/tickets` and move the ticket through its workflow.
5. Open `/compliance` to preview Form IV-A/Form B and download the signed demo PDF.
6. Open `/safety-intelligence` for RCA and cited CMR context.
7. Open `/digital-twin` for spatial risk and worker-zone state.
8. Run Khaan Netra, perform a denied PPE scan, and observe the CV bridge/queue behavior.

## Validation

```powershell
cd coalguard/backend
python -m compileall -q main.py models routes services

cd ../frontend
npm run lint
npm run build

cd ../../
node --check khaan-netra/js/app.js
node --check khaan-netra/js/api-bridge.js
node --check khaan-netra/js/sync-queue.js
node --check khaan-netra/js/cv-scanner.js
python -m unittest discover -s coalguard/backend/tests -v
```

## Demo Limitations

Telemetry, platform records, sync receipts, and recent history persist in SQLite. The RUL and regulatory assistant use deterministic offline fallbacks so the demo does not require XGBoost, an external LLM, or cloud hardware. DGMS downloads contain a canonical SHA-256 report signature; this is demo evidence integrity, not a legally valid digital signature. Camera access requires localhost or HTTPS, and the supplied PPE model must be downloaded/cached before first offline inference.
=======
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
>>>>>>> origin/main
