## Week 11 Tasks — Introduction to Docker

This week introduces Docker, a platform for containerizing applications. You'll learn the basics of Docker and how to use it for data science workflows. This lab is designed to be beginner-friendly with step-by-step instructions.

### What is Docker?

Docker is a platform that packages applications and their dependencies into containers, ensuring your code runs the same way on any machine. This is especially useful in data science for:
- **Reproducibility**: Your experiments work the same way for everyone
- **Dependency Management**: No more "it works on my machine" problems
- **Collaboration**: Share your entire environment easily

### Prerequisites

1. **Install Docker Desktop** on your machine:
   - **Windows/Mac**: Download from [Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - **Linux**: Install [Docker Engine](https://docs.docker.com/engine/install/)
   
2. **Verify Installation**:
   Open a terminal/command prompt and run:
   ```bash
   docker --version
   ```
   You should see something like: `Docker version 24.0.0, build ...`

### Submission Format

**Important**: You must submit **TWO separate files**:
1. **PDF Report** (`Week11_Report.pdf`) - Contains all tasks with screenshots and explanations
2. **Source Code Zip** (`Week11_SourceCode.zip`) - Contains all your code files

See the "Deliverables" section at the end for detailed requirements.

---

### Task 1 — Hello Docker: Your First Container

Let's start with the simplest possible Docker container to verify everything works.

**Steps:**

1. **Run the hello-world container**:
   ```bash
   docker run hello-world
   ```
   
   **Expected Output**: You should see a welcome message explaining that Docker is working correctly.

2. **List downloaded images**:
   ```bash
   docker images
   ```
   
   You should see the `hello-world` image listed.

3. **List all containers** (including stopped ones):
   ```bash
   docker ps -a
   ```
   
   You should see the hello-world container that just ran.

**Deliverable**: 
- Screenshot of the `docker run hello-world` output
- Screenshot showing `docker images` and `docker ps -a` results

---

### Task 2 — Run Python in a Container

Now let's run Python inside a Docker container without installing Python on your machine!

**Steps:**

1. **Pull the official Python image**:
   ```bash
   docker pull python:3.9-slim
   ```
   
   This downloads a lightweight Python image from Docker Hub.

2. **Run Python interactively**:
   ```bash
   docker run -it python:3.9-slim python --version
   ```
   
   You should see: `Python 3.9.x`

3. **Run a Python command**:
   ```bash
   docker run python:3.9-slim python -c "print('Hello from Docker!')"
   ```
   
   You should see: `Hello from Docker!`

4. **Run Python interactively (like a terminal)**:
   ```bash
   docker run -it python:3.9-slim python
   ```
   
   This opens Python REPL. Type:
   ```python
   print("I'm running Python in Docker!")
   exit()
   ```

**Deliverable**: 
- Screenshots showing:
  - Python version output
  - The "Hello from Docker!" message
  - Python REPL interaction

---

### Task 3 — Create a Simple Python Application

Create a simple Python script that we'll containerize.

**Steps:**

1. **Create a new directory** for your project:
   ```bash
   mkdir docker-lab
   cd docker-lab
   ```

2. **Create a simple Python script** (`app.py`):
   ```python
   # app.py
   print("Hello, Docker!")
   print("This Python script is running inside a container!")
   
   # Simple calculation
   result = 2 + 2
   print(f"2 + 2 = {result}")
   ```

3. **Test it locally** (if you have Python installed):
   ```bash
   python app.py
   ```
   
   Or test it in Docker:
   ```bash
   docker run -v $(pwd):/app -w /app python:3.9-slim python app.py
   ```
   
   The `-v $(pwd):/app` mounts your current directory into the container.

**Deliverable**: 
- Your `app.py` file
- Screenshot of the output when running in Docker

---

### Task 4 — Create Your First Dockerfile

A Dockerfile is a recipe for building a Docker image. Let's create one!

**Steps:**

1. **Create a Dockerfile** in your `docker-lab` directory:
   ```dockerfile
   # Use Python 3.9 as base image
   FROM python:3.9-slim
   
   # Set working directory inside container
   WORKDIR /app
   
   # Copy your Python script into the container
   COPY app.py .
   
   # Run the script when container starts
   CMD ["python", "app.py"]
   ```

2. **Build your Docker image**:
   ```bash
   docker build -t my-python-app .
   ```
   
   The `-t` flag tags (names) your image as `my-python-app`.
   The `.` means "use the current directory".

3. **Run your container**:
   ```bash
   docker run my-python-app
   ```
   
   You should see your script's output!

4. **List your images**:
   ```bash
   docker images
   ```
   
   You should see `my-python-app` in the list.

**Deliverable**: 
- Your `Dockerfile`
- Screenshot of `docker build` output
- Screenshot of `docker run` output

---

### Task 5 — Data Analysis Application with Docker

Now let's create a more useful application that analyzes data.

**Steps:**

1. **Create a simple CSV file** (`data/scores.csv`):
   ```csv
   Name,Score
   Alice,85
   Bob,72
   Charlie,90
   David,65
   Emma,78
   ```

2. **Create a Python script** (`analyze.py`):
   ```python
   import pandas as pd
   import sys
   
   # Read CSV file
   df = pd.read_csv('data/scores.csv')
   
   # Calculate statistics
   print("Score Statistics:")
   print(f"Mean: {df['Score'].mean():.2f}")
   print(f"Max: {df['Score'].max()}")
   print(f"Min: {df['Score'].min()}")
   print(f"Count: {len(df)}")
   ```

3. **Create `requirements.txt`**:
   ```
   pandas>=1.5.0
   ```

4. **Update your Dockerfile**:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   # Copy requirements first (for better caching)
   COPY requirements.txt .
   
   # Install dependencies
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Copy application files
   COPY analyze.py .
   COPY data/ ./data/
   
   # Run the analysis
   CMD ["python", "analyze.py"]
   ```

5. **Build and run**:
   ```bash
   docker build -t data-analyzer .
   docker run data-analyzer
   ```

**Deliverable**: 
- `analyze.py` file
- `requirements.txt` file
- Updated `Dockerfile`
- `data/scores.csv` file
- Screenshot of the analysis output

---

### Task 6 — Working with Volumes (Data Persistence)

Volumes let you share data between your computer and the container.

**Steps:**

1. **Run container with a volume mount**:
   ```bash
   docker run -v $(pwd)/data:/app/data data-analyzer
   ```
   
   This mounts your local `data` folder into the container.

2. **Modify your CSV file** on your computer, then run again:
   ```bash
   # Edit data/scores.csv (add a new row)
   docker run -v $(pwd)/data:/app/data data-analyzer
   ```
   
   The container should see your changes!

3. **Create a new file** in the container and verify it persists:
   ```bash
   docker run -v $(pwd)/output:/app/output -v $(pwd)/data:/app/data \
     data-analyzer python -c "import pandas as pd; df = pd.read_csv('data/scores.csv'); df.to_csv('output/results.csv', index=False); print('File saved!')"
   ```
   
   Check if `output/results.csv` was created on your computer.

**Deliverable**: 
- Screenshot showing volume mount commands
- Screenshot showing the output file created

---

### Task 7 — Run Jupyter Notebook in Docker

Jupyter Notebooks are essential for data science. Let's run one in Docker!

**Steps:**

1. **Run Jupyter Notebook container**:
   ```bash
   docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook
   ```
   
   The `-p 8888:8888` maps port 8888 from container to your computer.

2. **Access Jupyter**:
   - Look for a URL in the output like: `http://127.0.0.1:8888/?token=...`
   - Copy the entire URL and paste it in your browser
   - You should see the Jupyter interface!

3. **Create a notebook**:
   - Click "New" → "Python 3"
   - Try this code:
     ```python
     import pandas as pd
     df = pd.read_csv('work/data/scores.csv')
     print(df.describe())
     ```
   - Run the cell and see the output!

4. **Stop the container**:
   - Press `Ctrl+C` in the terminal
   - Or in another terminal: `docker ps` then `docker stop <container_id>`

**Deliverable**: 
- Screenshot of Jupyter Notebook running in browser
- Screenshot of your notebook with code and output

---

### Task 8 — Docker Compose

Docker Compose makes it easy to run multiple containers together.

**Steps:**

1. **Create `docker-compose.yml`**:
   ```yaml
   version: '3.8'
   
   services:
     jupyter:
       image: jupyter/scipy-notebook
       ports:
         - "8888:8888"
       volumes:
         - .:/home/jovyan/work
   ```

2. **Start the service**:
   ```bash
   docker-compose up
   ```
   
   This starts Jupyter Notebook. Access it in your browser as before.

3. **Stop the service**:
   ```bash
   docker-compose down
   ```

**Deliverable**: 
- Your `docker-compose.yml` file
- Screenshot showing `docker-compose up` running

---

### Task 9 — Container Management

Learn how to manage your containers and images.

**Steps:**

1. **List running containers**:
   ```bash
   docker ps
   ```

2. **View container logs**:
   ```bash
   docker logs <container_id>
   ```
   (Get container_id from `docker ps -a`)

3. **Stop a container**:
   ```bash
   docker stop <container_id>
   ```

4. **Remove a stopped container**:
   ```bash
   docker rm <container_id>
   ```

5. **Remove an image**:
   ```bash
   docker rmi <image_name>
   ```

6. **Clean up everything** (be careful!):
   ```bash
   docker system prune -a
   ```
   This removes all unused containers, images, and networks.

**Deliverable**: 
- Screenshots showing:
  - `docker ps` output
  - Container logs
  - Cleanup commands

---

### Guidelines

**Getting Help:**
- If a command doesn't work, check for typos
- Use `docker --help` or `docker <command> --help` for help
- Check Docker Desktop is running (Windows/Mac)

**Best Practices:**
- Use meaningful names for images (e.g., `data-analyzer` not `my-app`)
- Keep Dockerfiles simple and readable
- Use `.dockerignore` to exclude unnecessary files (we'll cover this later)

**Common Issues:**
- **"Cannot connect to Docker daemon"**: Make sure Docker Desktop is running
- **Port already in use**: Change the port number (e.g., `-p 8889:8888`)
- **Permission denied**: On Linux, you may need `sudo` or add user to docker group

---

### Deliverables

You need to submit **TWO files**:

#### 1. PDF Report (`Week11_Report.pdf`)

A comprehensive PDF document containing:

- **Cover page** with your name, student ID, and date
- **For each task (Tasks 1-9)**:
  - Task number and title
  - Brief description of what you did
  - Screenshots showing:
    - Commands you ran
    - Output/results
    - Any relevant terminal output or browser screenshots
  - Brief explanation (1-2 sentences) of what the task demonstrates
  
- **Required Screenshots**:
  - Task 1: `docker run hello-world` output and `docker images`/`docker ps -a` results
  - Task 2: Python version output, "Hello from Docker!" message, Python REPL interaction
  - Task 3: Running `app.py` in Docker
  - Task 4: `docker build` output, `docker run` output showing your script execution
  - Task 5: Data analysis output from `analyze.py`
  - Task 6: Volume mount commands and output file creation
  - Task 7: Jupyter Notebook interface in browser with your notebook code/output
  - Task 8: `docker-compose up` running and services active
  - Task 9: Container management commands (`docker ps`, logs, cleanup)

- **Summary/Reflection** (1-2 paragraphs):
  - What you learned about Docker
  - Any challenges you faced and how you overcame them
  - How Docker could be useful in your data science projects

**PDF Format Guidelines:**
- Use clear headings for each task
- Ensure screenshots are readable and properly labeled
- Keep the document well-organized and professional
- Maximum 20 pages (typically 10-15 pages is sufficient)

#### 2. Source Code Zip File (`Week11_SourceCode.zip`)

A zip file containing all your source code and project files:

```
Week11_SourceCode/
├── app.py                    # Simple Python script (Task 3)
├── analyze.py                # Data analysis script (Task 5)
├── data/
│   └── scores.csv           # Sample data file
├── Dockerfile                # Your Dockerfile (Task 4)
├── requirements.txt          # Python dependencies (Task 5)
├── docker-compose.yml       # Docker Compose file (Task 8)
└── README.md                # Brief documentation
```

**README.md should include:**
- Project description
- How to build: `docker build -t data-analyzer .`
- How to run: `docker run data-analyzer`
- How to use docker-compose: `docker-compose up`
- Any special instructions or notes

**Important Notes:**
- Make sure all code files are included and complete
- Test that your code works before submitting
- The zip file should extract to a single folder (not multiple files at root level)
- Do NOT include the PDF report in the zip file (submit separately)

---

### Additional Resources

- [Docker for Data Science: An Introduction](https://www.datacamp.com/tutorial/docker-for-data-science-introduction) - Great beginner tutorial
- [Docker for Data Science Tutorial](https://github.com/docker-for-data-science/docker-for-data-science-tutorial) - Exercises and examples
- [Docker Official Documentation](https://docs.docker.com/) - Complete reference
- [Docker Hub](https://hub.docker.com/) - Find pre-built images

---

### Submission Checklist

**Tasks Completed:**
- [ ] Task 1: hello-world container runs successfully
- [ ] Task 2: Python runs in Docker container
- [ ] Task 3: Simple Python script created
- [ ] Task 4: Dockerfile created and image builds successfully
- [ ] Task 5: Data analysis application works in Docker
- [ ] Task 6: Volumes work correctly
- [ ] Task 7: Jupyter Notebook runs in Docker
- [ ] Task 8: Docker Compose works 
- [ ] Task 9: Container management commands demonstrated

**PDF Report:**
- [ ] Cover page with name, student ID, and date
- [ ] All 9 tasks documented with screenshots
- [ ] Screenshots are clear and readable
- [ ] Each task has brief explanation
- [ ] Summary/reflection section included
- [ ] PDF is properly formatted and professional

**Source Code Zip:**
- [ ] All source code files included (app.py, analyze.py, Dockerfile, etc.)
- [ ] data/scores.csv included
- [ ] requirements.txt included
- [ ] docker-compose.yml included
- [ ] README.md with clear instructions
- [ ] Zip file extracts to a single folder
- [ ] All code tested and working

**Final Check:**
- [ ] PDF report submitted separately (not in zip)
- [ ] Source code zip file submitted separately
- [ ] Both files named correctly (Week11_Report.pdf and Week11_SourceCode.zip)

---

**Remember**: Docker is a powerful tool, but it's okay to make mistakes! Experiment, try different commands, and don't be afraid to start over. The goal is to understand the basics, not to be perfect.
