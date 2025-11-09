from pathlib import Path as PLPath
from fastapi import FastAPI, Request, Form, Path as FPath
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import json


BASE_DIR = PLPath(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

TEMPLATES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

hotels_json_path = (BASE_DIR / "hotels.json") # 把檔案存到 hotels_json_path中

with hotels_json_path.open("r", encoding="utf-8") as f:
    hotels = json.load(f) #解析 JSON


hotels_by_id = {}
for item in hotels:
    try:
        key = int(item.get("id"))
        hotels_by_id[key] = item
    except Exception:
        continue

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="test")

# 掛載靜態與模板
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Login Page
@app.post("/login")
async def login(email: str = Form(""), password: str = Form(""), request: Request = None):
    # 清洗輸入值
    e = email.strip().lower()
    p = password.strip()

    if not e or not p:
        return RedirectResponse("/ohoh?msg=請輸入信箱和密碼", status_code=303)

    if e == "abc@abc.com" and p == "abc":
        request.session["LOGGED_IN"] = True
        request.session["EMAIL"] = e
        return RedirectResponse("/member", status_code=303)

    return RedirectResponse("/ohoh?msg=信箱或密碼輸入錯誤", status_code=303)

# Member
@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if not request.session.get("LOGGED_IN", False):
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

# Logout
@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)

# ohoh Page
@app.get("/ohoh", response_class=HTMLResponse)
async def ohoh(request: Request, msg: str = "發生未知錯誤"):
    return templates.TemplateResponse(
        "ohoh.html",{
            "request": request,
            "msg": msg,
        }
    )

# Hotel
@app.get("/hotel/{hotel_id}", response_class=HTMLResponse)
async def show_hotel(
    request: Request,
    hotel_id: int = FPath(..., gt=0)
):
    hotel = hotels_by_id.get(hotel_id)
    return templates.TemplateResponse(
        "hotel.html",
        {"request": request, "hotel": hotel, "hotel_id": hotel_id}
    )
