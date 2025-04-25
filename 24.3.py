class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False

class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, app):
        if app not in self.apps:
            self.apps.append(app)

    def remove_application(self, app):
        if app in self.apps:
            self.apps.remove(app)

    def block_application(self, app):
        if app in self.apps:
            app.blocked = True

    def total_apps(self):
        return len(self.apps)

if __name__ == "__main__":
    store = AppStore()
    app_youtube = Application("Youtube")
    app_telegram = Application("Telegram")

    store.add_application(app_youtube)
    store.add_application(app_telegram)

    print(f"Total apps: {store.total_apps()}")

    store.block_application(app_youtube)
    print(f"Is 'Youtube' blocked? {app_youtube.blocked}")

    store.remove_application(app_telegram)
    print(f"Total apps after removal: {store.total_apps()}")
