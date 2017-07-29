from govhack_app import create_app

if __name__ == "__main__":
    application = create_app('config.production')
    application.run()
