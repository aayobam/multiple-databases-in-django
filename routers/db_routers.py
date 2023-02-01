class AuthRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    # allows for objects to read from the db
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    # allows for object to be written on the db
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'users_db'
        return None

    # allows for tables or objects to access database relations (ForeignKey, Many-Many etc)
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    # determines if the migrations/migrate is allowed to run on the database and what apps can be migrated on the database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "users_db"
        return None


class BlueRouter:
    route_app_labels = {'blue'}

    # allows for objects to read from the db
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    # allows for object to be written on the db
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'blue_db'
        return None

    # allows for tables or objects to access database relations (ForeignKey, Many-Many etc)
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    # determines if the migrations/migrate is allowed to run on the database and what apps can be migrated on the database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "blue_db"
        return None


class AquaRouter:
    route_app_labels = {'aqua'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'aqua_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db=="aqua_db"
        return None