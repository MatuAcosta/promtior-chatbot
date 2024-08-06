FROM python:3.9

# 
WORKDIR /app

# 
COPY requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
ADD . .

# 
CMD ["python3", "main.py", "--port", "8000"]