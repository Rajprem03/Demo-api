from pydantic import BaseModel, Field, model_validator

class SourceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    spec_url: str | None = None
    spec_path: str | None = None
    repo_path: str | None = None

    @model_validator(mode="after")
    def require_location(self):
        if not self.spec_url and not self.spec_path:
            raise ValueError("spec_url or spec_path is required")
        return self

class SourceResponse(BaseModel):
    id: int
    name: str
    spec_url: str | None
    spec_path: str | None
    repo_path: str | None
    active: bool
    model_config = {"from_attributes": True}

class SpecPathUpdate(BaseModel):
    spec_path: str = Field(min_length=1)
