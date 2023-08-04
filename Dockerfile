FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container's working directory
COPY . .

# Install the required Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 9090
EXPOSE 9090

# Command to run the application
CMD ["python", "main.py"]
