from pydantic import BaseModel, Field

class DependencyCreate(BaseModel):
    source_id: int
    affected_service: str = Field(min_length=1, max_length=255)
    file_path: str = Field(min_length=1)
    symbol: str | None = None
    method: str = Field(min_length=1, max_length=20)
    path_pattern: str = Field(min_length=1)
