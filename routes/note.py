from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from  schemas.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = [
        {
            "id": str(doc["_id"]), 
            "title": doc["title"],
            "desc": doc["desc"], 
            "important": doc["important"], 
        }
        for doc in docs
    ]
    return templates.TemplateResponse(
        request=request, name="index.html", context={"newDocs": newDocs}
    )

@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    print('incoming form: ',form)
    form_data = dict(form)
    print('form_data: ',form_data)
    form_data["important"] = True if form_data.get("important") == "on" else False 
    print('form_data_updated: ',form_data)

    note = conn.notes.notes.insert_one(form_data)
    return {"Success": True}