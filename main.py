from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

class BMIOutput(BaseModel):
    bmi: float
    message: str

@app.get("/")
def Hi():
    return {"message": "Hello World"}

@app.get("/bmi")
def bmi(
        weight: float = Query(..., description="الوزن بالكيلوغرام", gt=20, lt=200),
        height: float = Query(..., description="الطول بالمتر", gt=1.0, lt=2.0)
    ):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "أنت تعاني من نقص الوزن."
    elif 18.5 <= bmi < 24.9:
        message = "وزنك طبيعي."
    elif 25 <= bmi < 29.9:
        message = "أنت تعاني من زيادة الوزن."
    else:
        message = "أنت تعاني من السمنة."

    return BMIOutput(bmi=bmi, message=message)
