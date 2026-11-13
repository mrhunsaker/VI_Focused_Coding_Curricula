import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_and_search(user: User) -> None:
    await user.open("/")
    await user.should_see("No records to show.")
    for title, description, category in [("Notebook", "Course notes", "supplies"), ("Pencil", "Box of 10", "supplies")]:
        user.find("Record title").type(title)
        user.find("Record description").type(description)
        user.find("Record category").type(category)
        user.find("Add record").click()
    await user.should_see("2. Pencil [supplies] (not done)")
    user.find("Search title or description").type("note")
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_not_see("2. Pencil [supplies] (not done)")
    user.find("Add record").click()
    await user.should_see("A title is required.")
