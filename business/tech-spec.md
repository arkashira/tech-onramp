 # tech-spec.md

## Stack
- Language: TypeScript for compatibility with Node.js and browser environments.
- Framework: React for building the user interface, and Express.js for the backend API.
- Runtime: Node.js for server-side execution.

## Hosting
- Free-tier-first: AWS Amplify for hosting the application, with a free tier that supports up to 1 million requests per month.
- Specific platforms: Support for deployment on AWS Elastic Beanstalk, Heroku, and Vercel for easy scaling and deployment.

## Data Model
- Tables/Collections:
  - Users (id, name, email, password, created_at, updated_at)
  - Lessons (id, title, description, prerequisites, content, created_by, created_at, updated_at)
  - Exercises (id, title, description, lesson_id, solution, created_by, created_at, updated_at)
  - Progress (id, user_id, lesson_id, exercise_id, score, completed_at)

## API Surface
- Endpoints (Method/Path/Purpose):
  1. POST /auth/register (Register a new user)
  2. POST /auth/login (Login a user)
  3. GET /lessons (Retrieve a list of lessons)
  4. GET /lessons/:id (Retrieve a specific lesson)
  5. POST /lessons (Create a new lesson)
  6. GET /exercises (Retrieve a list of exercises)
  7. GET /exercises/:id (Retrieve a specific exercise)
  8. POST /exercises (Create a new exercise)
  9. POST /progress (Track user progress on lessons and exercises)
  10. GET /progress (Retrieve user progress)

## Security Model
- Auth: JWT-based authentication for user sessions.
- Secrets: AWS Secrets Manager for secure storage of API keys and other sensitive data.
- IAM: AWS IAM for role-based access control and fine-grained permissions.

## Observability
- Logs: AWS CloudWatch for centralized logging and monitoring.
- Metrics: AWS CloudWatch for monitoring key application metrics.
- Traces: AWS X-Ray for distributed tracing and debugging.

## Build/CI
- Continuous Integration: AWS CodePipeline for automating the build, test, and deployment process.
- Testing: Jest for unit testing, and Cypress for end-to-end testing.
- Linting: ESLint for code linting and formatting.
- Code Quality: SonarQube for static code analysis and quality checks.