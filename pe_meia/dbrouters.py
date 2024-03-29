class DbRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    app_labels = {'sig': 'sigaa', 'sigaa': 'sigaa'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read remote models go to remote database.
        """
        return self.app_labels.get(model._meta.app_label, None)

    def db_for_write(self, model, **hints):
        """
        Attempts to write remote models go to the remote database.
        """
        return self.app_labels.get(model._meta.app_label, None)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Do not allow relations involving the remote database
        """
        if obj1._meta.app_label in ['sig', 'sigaa'] and \
                obj2._meta.app_label in ['sig', 'sigaa']:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Do not allow migrations on the remote database
        """
        if app_label in ['sig', 'sigaa'] or db in ['sig', 'sigaa']:
            return False
        return True
