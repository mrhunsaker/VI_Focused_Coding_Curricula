"""User-level tests for app.py. They need: pip install nicegui pytest pytest-asyncio"""
import os
import tempfile

from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]
os.environ["PDM_DATA_FILE"] = os.path.join(tempfile.mkdtemp(), "data.json")


async def test_add_search_complete_delete(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    await user.should_see("No records to show.")

    user.find("Record title").type("Notebook")
    user.find("Record description").type("Course notes")
    user.find("Record category").type("supplies")
    user.find("Add record").click()
    await user.should_see("1. Notebook [supplies] (not done)")
    await user.should_see("Added record 1: Notebook.")

    user.find("Add record").click()
    await user.should_see("A title is required.")

    user.find("Choose a record").click()
    user.find("1. Notebook [supplies] (not done)").click()
    user.find("Mark selected record done").click()
    await user.should_see("1. Notebook [supplies] (done)")

    user.find("Delete selected record").click()
    await user.should_see("Deleted record 1.")
    await user.should_see("No records to show.")
