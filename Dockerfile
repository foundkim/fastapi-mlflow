
FROM python:3.10

# Set Working Directory
WORKDIR /app

# Copy requirements file
COPY requirement.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

#
COPY . .
# COPY api /app/
# COPY core /app/
# COPY models /app/
# COPY services /app/
# COPY utils /app/        

# Expose the port FastAPI will run on
EXPOSE 5000


# Command to run the application
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ,"--port", "5000", "--workers", "3" ]
