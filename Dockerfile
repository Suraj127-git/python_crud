FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container's working directory
COPY . .
COPY requirements.txt .

# Install the required Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 (if needed)
EXPOSE 8000

# Command to run the application
CMD ["python", "main.py"]
