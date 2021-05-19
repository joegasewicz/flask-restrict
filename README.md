![flask restrict](assets/fr_logo.png?raw=true, "Flask Restrict")
Permission based view authorization Flask extension library

Flask-Restrict does not interfere with your existing database tables
so at anytime it's easy to opt out from using Flask-Restrict.

## 🌱 Currently still in development

## Installation
```
pip install flask-restrict
```

# Quick Start

Setup your existing modals

```python
@restrict.modal
class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    super = restrict.Role("all")
    admin = restrict.Role(["can_view", "can_update", "can_delete"])
    user = restrict.Role(["can_view", "can_post"])


@restrict.modal
class CatModel(db.Model):
    __tablename__ = "cats"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    super = restrict.Role("all")
    admin = restrict.Role(["can_view", "can_update", "can_delete"])
    user = restrict.Role(["can_view", "can_post"])

```
And Create a user with the new permissions
```python
restrict.create_user(user, perm_name="admin")
```

Update a user with the new permissions
```python
restrict.update_user(user, perm_name="admin")
```

Remove a user with the new permissions
```python
restrict.remove_user(user, perm_name="admin")
```


Create an entity with user permissions
```python
restrict.create_entity(entity_model, perm_name="admin")
```

Update an entity with user permissions
```python
restrict.update_entity(entity_model, perm_name="admin")
```

Remove an entity with user permissionss
```python
restrict.remove_entity(entity_model, perm_name="admin")



```python
@restrict.permissions
@test_app.route("/")
def home():
    return {
        "data": "results",
    }, 200
    
```

## Contribute
Grab an issue, Fork, include tests, create a PR.
If you wish to add a feature then open an issue and wait for confirmation before
submitting a PR.