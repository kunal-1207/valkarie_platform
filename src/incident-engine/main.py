from fastapi import FastAPI, Request
import httpx
import os
import json
import logging

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "phi3")

@app.post("/webhook")
async def receive_alert(request: Request):
    payload = await request.json()
    logger.info(f"Received alert payload: {json.dumps(payload)}")
    
    # Extract alerts
    alerts = payload.get("alerts", [])
    if not alerts:
        return {"status": "ignored", "reason": "no alerts found in payload"}
        
    for alert in alerts:
        alert_name = alert.get("labels", {}).get("alertname", "Unknown Alert")
        status = alert.get("status", "unknown")
        annotations = alert.get("annotations", {})
        
        # Construct the prompt for the LLM
        prompt = f"""
You are an expert DevOps AI assistant. An incident has occurred in our Kubernetes cluster.
Please analyze the following Prometheus alert data and provide a concise, human-readable summary of the problem and 3 immediate steps an engineer should take to troubleshoot or remediate the issue.

Alert Name: {alert_name}
Status: {status}
Details: {json.dumps(annotations)}
Labels: {json.dumps(alert.get("labels", {}))}

Format your response as:
**Incident Summary**: ...
**Recommended Actions**: ...
"""
        
        logger.info(f"Sending prompt to Ollama model {MODEL_NAME} at {OLLAMA_URL}...")
        
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": MODEL_NAME,
                        "prompt": prompt,
                        "stream": False
                    }
                )
                
            if response.status_code == 200:
                result = response.json()
                summary = result.get("response", "No response generated.")
                logger.info("================ AI INCIDENT SUMMARY ================")
                logger.info(summary)
                logger.info("=====================================================")
            else:
                logger.error(f"Ollama API returned status {response.status_code}: {response.text}")
                
        except Exception as e:
            logger.error(f"Error communicating with Ollama: {str(e)}")
            
    return {"status": "success", "processed_alerts": len(alerts)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
