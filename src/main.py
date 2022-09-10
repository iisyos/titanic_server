from pydantic import BaseModel
from fastapi import FastAPI
from machineLearning.titanic import PredictOnAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=["*"],
    allow_headers=["*"]
)


class SchemaOfTitanicFeaturesRequest(BaseModel):
    Sex: str
    Pclass: str
    Age: int
    Parch: int
    SibSp: int


class SchemaOfSurvivalProbabilityResponse(BaseModel):
    survival_probability: float


@app.post('/api/titanic', response_model=SchemaOfSurvivalProbabilityResponse)
def derive_score(request_body: SchemaOfTitanicFeaturesRequest):
    # 辞書形式に変更
    features_dict = request_body.__dict__
    # **<辞書オブジェクト>とすることで引数として自動的にバラして与えることが可能
    survival_probability = PredictOnAPI.derive_survival_probability(
        **features_dict)
    return {'survival_probability': survival_probability}
