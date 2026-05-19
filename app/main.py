import fastapi
from fastapi import Depends


from app.dependencies import get_rec_srv
from app.services import RecommendationSrv
from app.schemas import DefaultResponse, RecommendationRequest


from sqlalchemy.orm import Session
app = fastapi.FastAPI()




@app.get("/ping")
def ping():
    return DefaultResponse(msg="PING")

@app.post("/recommend")
def get_recommendation(
    request: RecommendationRequest, rec_srv: RecommendationSrv = Depends(get_rec_srv),
    ):
    q = request.query

    return rec_srv.recommend(q, K=5)
    