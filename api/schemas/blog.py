from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date

class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None  # Allow it to be optional so the validator can populate it
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        title = values.get('title')
        if title and not values.get('slug'):  # Only generate slug if it wasn't provided
            values['slug'] = title.replace(" ", "-").lower()
        return values  # Return the entire dictionary of values, not just slug
    
class UpdateBlog(CreateBlog):
    pass
    
class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date 

    class Config:
        orm_mode = True
