class Base():
    def __init__(self, db, session, request):
        self.db = db
        self.session = session
        self.request = request