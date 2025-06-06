from fastapi import FastAPI
from app.routers import arithmetic_parenthesis, graph, string,intervals,monotonic_stack, dp, container_with_most_water
from mangum import Mangum

app = FastAPI()

app.include_router(graph.router)
app.include_router(string.router)
app.include_router(intervals.router)
app.include_router(monotonic_stack.router)
app.include_router(dp.router)
app.include_router(arithmetic_parenthesis.router)
app.include_router(container_with_most_water.router)

handler = Mangum(app)