"""
 A rough sketch of the API

    actions:
        creates a flask_restrict table

        columns:
            perm_type:
                - can_view
                - can_create
                - can_update # patch / put
                - can_delete
            resource_tablename:
                - the name of the table to match against
            user_id:
            user_tablename:
                - e.g 'users'


    API:

        restrict.create_user(user, **{
                "all": true, # Sets all permissions
                "perm_name": "admin",
                "perm_types=["can_view", "can_post"] # declare individual access types
        })


        class UserModel(db.Model, RestrictMixin):
            class RestrictMeta:
                super = "all"
                admin = ["can_view", "can_update", "can_delete"]
                user = ["can_view", "can_post"]

        class BlogsModel(db.Model, RestrictMixin):
            class RestrictMeta:
                super = "all"
                admin = ["can_view", "can_update", "can_delete"]
                user = ["can_view", "can_post"]

    # How does this work?

    - If there are no other libraries adding the incoming user object
    to Flask's global context then do:
        flask_restrict.init_app(db, models=[UserModel, ..])

    - Otherwise, if there are other libraries or the user is already on the global context
    then do:
        flask_restrict.init_app(db, tablenames=["users"...])


    - user is on the global context
        -
    @restrict
    @app.route("/user", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
    def home():
        pass
"""