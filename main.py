from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "后端部署成功！"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
