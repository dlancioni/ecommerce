class Base():
    def __init__(self, db, session, request, form):
        self.db = db
        self.session = session
        self.request = request
        self.form = form