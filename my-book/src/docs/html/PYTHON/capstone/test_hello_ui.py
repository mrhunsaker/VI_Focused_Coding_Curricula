from nicegui.testing import User

pytest_plugins = ["nicegui.testing.user_plugin"]


async def test_greeting(user: User) -> None:
    await user.open("/")
    await user.should_see("Personal Data Manager")
    user.find("Greet").click()
    await user.should_see("Please enter a name.")
    user.find("Your name").type("Avery")
    user.find("Greet").click()
    await user.should_see("Hello, Avery!")
