from govhack_app import create_app

application = create_app('config.production')

if __name__ == "__main__":
    application.run()
