from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculate")
async def calculate(operation: str, x: float, y: float):
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = x / y
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"operation": operation, "x": x, "y": y, "result": result}

# Access end point using: http://localhost:8000/calculate?operation=subtract&x=10&y=15