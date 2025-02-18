from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from .. import models,schemas
from ..oauth2 import get_current_user



def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


# current__user=Depends(get_current_user)\

def create(request: schemas.Blog, db:Session, current_user:schemas.User=Depends(get_current_user)):
    print(current_user)
    new_blog = models.Blog(title= request.title, body = request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'



def update(id:int, request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated successfully'



def show(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not available"}
    
    return blog
