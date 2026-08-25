from fastapi import FastAPI
app = FastAPI(
    title="Techlog Solutions Kanban API",
    description="Sistema de gerenciamento de projetos e tarefas baseado na metodologia Kanban para a Techlog Solutions.",
    version="1.0.0"
)
@app.get("/")
async def health_check():
    return {"status": "OK"}