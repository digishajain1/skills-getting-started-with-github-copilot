# NEET Reach

NEET Reach is an education nonprofit scheduling app for volunteers and teachers supporting 11th and 12th standard NEET coaching.

Teachers can review resource priorities for Physics, Chemistry, and Biology. Volunteers can claim a 45-minute class slot and immediately receive a lesson handbook with:
- the course structure for that session
- homework to assign
- a last-5-minute life skill focus to improve study habits

## What the app does

- Shows a weekly schedule with 3 classes every weekday
- Shows 5 classes each day on weekends
- Lets one volunteer claim each class slot
- Returns the teaching handbook immediately after signup
- Exposes teacher resource guidance for 11th and 12th standard coaching

## Run locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
cd src
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

3. Open the app:

```text
http://localhost:8000
```

## Free hosting to share with someone

The simplest free hosted option for this app is Render, using a free web service if it is available on your account.

1. Push this repository to GitHub.
2. Sign in to Render and create a new Web Service from the repo.
3. Use these settings:

```text
Environment: Python
Build Command: pip install -r requirements.txt
Start Command: cd src && uvicorn app:app --host 0.0.0.0 --port $PORT
```

4. After deploy completes, share the public URL Render gives you.

If a free web service is not available on your Render account, the fallback free-sharing option is to run locally and expose it with a tunnel such as Cloudflare Tunnel or ngrok.

## API endpoints

- `GET /api/resources`
- `GET /api/schedule`
- `POST /api/schedule/{slot_id}/signup?email=...&name=...`
- `GET /health`

## Deployment notes

- The repository includes a Dockerfile for container-based hosts.
- The health check uses `/health`.
- Static frontend files are served by FastAPI from `src/static`.

