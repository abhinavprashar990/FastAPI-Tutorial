from fastapi import FastAPI # type: ignore
from . import models
from . database import engine
from .routers import blog, user,authentication
from fastapi.templating import Jinja2Templates 
from starlette.requests import Request 
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from .config import CLIENT_ID,CLIENT_SECRET 
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="AbhinavPrashar123")
app.mount("/static", StaticFiles(directory="static"), name='static')
oauth = OAuth()

oauth.register(
    name = 'google',
    server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    client_kwargs = {
        'scope' : 'email oenid profile',                                                                
        'redirect_url': 'http://localhost:8000/auth'
    }
)

templates = Jinja2Templates(directory = "blog/templates")


models.Base.metadata.create_all(engine)

@app.get('/')
def index(request:Request):
    return templates.TemplateResponse(
        name = "home.html",
        context = {"request": request}
    )
    
@app.get("/login")
async def login(request:Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request,url)

app.include_router(authentication.router)

app.include_router(blog.router)

app.include_router(user.router)
