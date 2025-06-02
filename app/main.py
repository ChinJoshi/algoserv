from fastapi import FastAPI
from app.routers import graph, string,intervals,monotonic_stack, dp, arithmetic_paranthesis

app = FastAPI()

app.include_router(graph.router)
app.include_router(string.router)
app.include_router(intervals.router)
app.include_router(monotonic_stack.router)
app.include_router(dp.router)
app.include_router(arithmetic_paranthesis.router)


