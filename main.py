import joblib
import pandas as pd
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import httpx # Using httpx for async API calls

# Define the data model for our input data
class StockFeatures(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: int
    MA50: float
    MA200: float
    MA_Spread: float
    Volatility_20D: float
    ROC_5D: float

# Create our FastAPI application
app = FastAPI()

# Configure the templates directory
templates = Jinja2Templates(directory="templates")

# Load our trained scaler and model
try:
    scaler = joblib.load('model/scaler.joblib')
    model = joblib.load('model/xgb_model.joblib')
except FileNotFoundError:
    scaler = None
    model = None

# Define a root endpoint that serves our HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define the prediction endpoint
@app.post("/predict")
def predict_trend(features: StockFeatures):
    if not scaler or not model:
         return JSONResponse(status_code=500, content={"error": "Model or scaler not loaded."})
    
    try:
        input_df = pd.DataFrame([features.dict()])
        input_scaled = scaler.transform(input_df)
        prediction_raw = model.predict(input_scaled)
        prediction = int(prediction_raw[0])
        prediction_label = "Up" if prediction == 1 else "Down"
        return {"prediction": prediction, "prediction_label": prediction_label}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Prediction failed: {str(e)}"})

# --- ✨ New Gemini API Endpoint ---
@app.post("/analyze")
async def analyze_with_gemini(features: StockFeatures):
    # Construct a detailed prompt for the Gemini API
    prompt = f"""
    Act as a senior quantitative financial analyst providing a brief market commentary.
    Based on the following daily technical indicators for a stock, provide a concise, insightful analysis (2-3 sentences)
    of the current market sentiment. Mention potential implications.
    Use Google Search to incorporate any relevant, recent market context if available.

    Technical Data:
    - Close Price: {features.Close}
    - 50-Day Moving Average: {features.MA50}
    - 200-Day Moving Average: {features.MA200}
    - 20-Day Volatility: {features.Volatility_20D}
    - 5-Day Rate of Change: {features.ROC_5D}%
    """

    # This is the NEW line in main.py
    api_key = os.environ.get("GEMINI_API_KEY")
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search": {}}], # Enable search grounding
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(api_url, json=payload)
            response.raise_for_status() # Raise an exception for bad status codes
            result = response.json()
            
            candidate = result.get("candidates", [{}])[0]
            content = candidate.get("content", {}).get("parts", [{}])[0]
            analysis_text = content.get("text", "No analysis available.")

            return {"analysis": analysis_text}

    except httpx.RequestError as e:
        return JSONResponse(status_code=500, content={"error": f"API request failed: {str(e)}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"An unexpected error occurred: {str(e)}"})


# Block to run the API directly for local testing
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)