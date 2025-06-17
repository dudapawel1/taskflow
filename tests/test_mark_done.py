from app.models import Task
from datetime import datetime

def test_mark_done():
    t = Task("T", "D", datetime.now())
    t.mark_done()
    assert t.completed
