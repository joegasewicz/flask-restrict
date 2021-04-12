"""
 A rough sketch of the API

    actions:
        creates a flask_restrict table

        columns:
            perm_type:
                - can_view
                - can_create
                - can_update
                - can_delete
            resource_tablename:
                - the name of the table to match against
            user_id:
            user_tablename:
                - e.g 'users'


    API:

        restrict.create_user(db,
            **{
                "all": true, # Sets all permissions
                "perm_types=["can_view", "can_post"] # declare individual access types
            },
        )

        OR

        class UserModel(db.Model):
            __tablename__ = "users"
            id = db.Column()

            class RestrictMeta:
                super = "all"
                admin = ["can_view", "can_update", "can_delete"]
                user = ["can_view", "can_post"]


    @restrict(tablename="users")
    @app.route("/user", methods=["GET", "POST", "DELETE", "PATCH", "PUT"])
    def home():
        pass
"""