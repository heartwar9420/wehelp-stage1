# 準備資料庫連線
import mysql.connector
con = mysql.connector.connect(
    user="root",
    password="12345678",
    host="localhost",
    database="website"
)
print("Database Ready")

from pathlib import Path as PLPath
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

BASE_DIR = PLPath(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

TEMPLATES_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="test")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Task1:首頁
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Task2:/signup
@app.post("/signup")
async def signup(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    cursor = con.cursor()
    cursor.execute("SELECT id FROM member WHERE email=%s", [email])
    result = cursor.fetchone()

    if result:
        return RedirectResponse("/ohoh?msg=重複的電子郵件", status_code=303)

    cursor.execute(
        "INSERT INTO member(name, email, password) VALUES (%s, %s, %s)",
        [name, email, password]
    )
    con.commit()

    return RedirectResponse("/", status_code=303)

# Task3:/login
@app.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    cursor = con.cursor()
    cursor.execute(
        "SELECT id, name, email FROM member WHERE email=%s AND password=%s",
        [email, password]
    )
    row = cursor.fetchone()

    if not row:
        # 帳號或密碼錯誤 → 錯誤頁
        return RedirectResponse("/ohoh?msg=電子郵件或密碼輸入錯誤", status_code=303)

    member_id, member_name, member_email = row
    # 設定登入狀態
    request.session["member"] = {
        "id": member_id,
        "name": member_name,
        "email": member_email
    }
    return RedirectResponse("/member", status_code=303)

# /member
@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    member = request.session.get("member")
    if not member:
        return RedirectResponse("/", status_code=303)

    cursor = con.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT message.id, member.name, message.content
        FROM message
        JOIN member ON message.member_id = member.id
        ORDER BY message.id DESC
        """
    )
    messages = cursor.fetchall()

    return templates.TemplateResponse(
        "member.html",
        {
            "request": request,
            "name": member["name"],   # 登入者的名字（頁面上方）
            "messages": messages      # 留言列表（下面）
        }
    )

# Task4:/logout
@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)

# /ohoh
@app.get("/ohoh", response_class=HTMLResponse)
async def ohoh(request: Request, msg: str = "發生未知錯誤"):
    return templates.TemplateResponse(
        "ohoh.html",
        {"request": request, "msg": msg}
    )

# Task5: /createMessage
@app.post("/createMessage")
async def create_message(
    request: Request,
    content: str = Form(...)
):
    member = request.session.get("member")
    if not member:
        return RedirectResponse("/", status_code=303)

    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO message (member_id, content) VALUES (%s, %s)",
        [member["id"], content]   # 用登入者的 id 當作者
    )
    con.commit()

    return RedirectResponse("/member", status_code=303)

# Task6: /deleteMessage
@app.post("/deleteMessage/{msg_id}")
async def delete_message(request: Request, msg_id: int):
    member = request.session.get("member")
    if not member:
        return RedirectResponse("/", status_code=303)

    cursor = con.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s AND member_id=%s", [msg_id, member["id"]])
    con.commit()

    return RedirectResponse("/member", status_code=303)