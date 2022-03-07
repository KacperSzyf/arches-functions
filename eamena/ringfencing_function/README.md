# Installation

1. `.htm` 

place the `.htm` file in `template -> views -> components -> functions`

2. `.js`

placec the `.js` file in `media -> js -> views -> components -> functions`

3. `.py`

place the `.py` file in `functions`

4. Register function

finally register your function using the following command

```
python manage.py fn register --source '/path/to/function_name.py
```

# Demo
Demo on mature trees, actors Jane, John, admin and annonymous user.

### Scenarios

Rules are set up in the following way:
- Only John and Admin can see mature trees.
![image showing John only being able to see a mature tree](/imags/john.png)
- Only Jane and admin can see juvenile trees.
- Annonymous can't see any trees.
- Admin can see all trees.
