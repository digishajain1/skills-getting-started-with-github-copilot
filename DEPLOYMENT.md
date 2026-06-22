# NEET Reach - Nonprofit Volunteer Scheduling Platform

A FastAPI-based web application for education nonprofits that enables teachers to access NEET coaching resources and volunteers to claim 45-minute teaching slots with instant lesson handbooks.

## Features

✨ **Teacher Resource Access**
- View NEET coaching guidance for 11th and 12th standards
- Access Physics, Chemistry, and Biology focus areas
- Review strategic teaching goals for each grade level

✨ **Volunteer Scheduling**
- Browse weekly class slots (3 weekday, 5 weekend classes)
- Claim a 45-minute teaching slot
- Receive complete lesson handbook immediately upon signup

✨ **Production Ready**
- CORS support for cross-origin requests
- Structured logging for monitoring
- Docker containerization for easy deployment
- Health checks built-in
- Life skill emphasis integrated into every lesson plan

## Project Structure

```
.
├── src/
│   ├── app.py                 # FastAPI application
│   ├── static/
│   │   ├── index.html        # Frontend UI
│   │   ├── app.js            # JavaScript logic
│   │   └── styles.css        # Styling
│   └── README.md
├── Dockerfile                 # Production container image
├── docker-compose.yml        # Local development setup
├── .dockerignore             # Files to exclude from Docker
├── requirements.txt          # Python dependencies
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+ (for local development)
- Docker & Docker Compose (for containerized deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd skills-getting-started-with-github-copilot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   cd src
   python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application**
   - Open your browser to `http://localhost:8000`
   - API documentation available at `http://localhost:8000/docs`

### Docker Deployment

#### Using Docker Compose (Recommended for Development)

```bash
# Build and start the application
docker-compose up --build

# Access at http://localhost:8000
```

#### Using Docker (Production)

1. **Build the image**
   ```bash
   docker build -t mergington-school .
   ```

2. **Run the container**
   ```bash
   docker run -d -p 8000:8000 \
     --name mergington-school \
     --health-interval=30s \
     --health-timeout=10s \
     --health-retries=3 \
     mergington-school
   ```

3. **Check application status**
   ```bash
   docker ps
   docker logs mergington-school
   ```

## API Endpoints

### Get Teacher Resources
```http
GET /api/resources
```

### Get Weekly Schedule
```http
GET /api/schedule
```

### Sign Up for a Teaching Slot
```http
POST /api/schedule/{slot_id}/signup?email={volunteer_email}&name={volunteer_name}
```

**Parameters:**
- `slot_id`: Unique slot identifier (e.g., "mon-1")
- `email`: Volunteer email address
- `name`: Volunteer full name

**Success Response (200):**
```json
{
  "message": "Volunteer Name is scheduled for Monday 4:00 PM - 4:45 PM.",
  "slot": { ... },
  "handbook": {
    "course_structure": [ ... ],
    "homework": [ ... ],
    "life_skill_focus": "..."
  }
}
```

**Error Responses:**
- `404 Not Found`: Teaching slot does not exist
- `400 Bad Request`: Volunteer already assigned or slot is taken

## Running Tests

Test endpoints using curl:

```bash
# Get teacher resources
curl http://localhost:8000/api/resources

# Get weekly schedule
curl http://localhost:8000/api/schedule

# Sign up for a teaching slot
curl -X POST "http://localhost:8000/api/schedule/mon-1/signup?email=volunteer@example.org&name=John%20Doe"
```

## Logging

The application logs all important events:

```
INFO:app:Fetching teacher resources
INFO:app:Fetching weekly class schedule
INFO:app:Volunteer volunteer@example.org signed up for mon-1
WARNING:app:Duplicate signup attempt: volunteer@example.org for mon-1
WARNING:app:Signup rejected - slot full: mon-1
```

## Deployment Platforms

### Cloud Deployment

This application can be deployed to:

- **Heroku** (via Docker or buildpack)
  ```bash
  heroku create mergington-school
  git push heroku main
  ```

- **AWS** (ECS, App Runner, Elastic Beanstalk)
  - Push Docker image to ECR
  - Deploy using AWS services

- **Google Cloud** (Cloud Run, App Engine)
  - Deploy Docker image to Cloud Run
  - No infrastructure management needed

- **Azure** (App Service, Container Instances)
  - Push to Azure Container Registry
  - Deploy from ACR

### Environment Configuration

Create a `.env` file for production settings:

```bash
# Logging
LOG_LEVEL=info

# CORS
CORS_ORIGINS=https://yourdomain.com
```

## Key Features

✅ Teacher resource hub for NEET coaching strategy
✅ Weekly scheduling with 3-5 classes per day
✅ Lesson handbooks with course structure, homework, and life skill focus
✅ Duplicate assignment prevention
✅ Slot capacity management
✅ Structured logging and monitoring
✅ CORS support for integration
✅ Docker containerization
✅ Health checks and security best practices

## Contributing

Contributions to NEET Reach are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues or questions, please open an issue on the GitHub repository.

---

Built with ❤️ to support accessible medical entrance exam coaching | Deployed with Docker 🐳
