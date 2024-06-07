# STANDARD IMPORTS
from typing import Optional
from fastapi import Query
from pydantic import BaseModel, Extra


class CourseReportsModel(BaseModel):
    tenant: str
    school_id: Optional[int] = Query(default=None)
    class_id: Optional[int] = Query(default=None)

    class Config:
        # this will not allow to send extra parameters besides the above
        extra = Extra.forbid
