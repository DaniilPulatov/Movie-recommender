from pydantic import BaseModel, ConfigDict, Field

class RecommendationRequest(BaseModel):
    query: str
    
class RatingRequest(BaseModel):
    user_id: int
    movie_id: int
    rating: int = Field(gt=0, le=10)

class DefaultResponse(BaseModel):
    msg: str

class RecommendationResponse(BaseModel):
    id: int
    textual_repr: str
    
    model_config = ConfigDict(from_attributes=True)


class RecommendationListResponse(BaseModel):
    movies: list[RecommendationResponse]