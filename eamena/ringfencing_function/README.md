# The function

The function will only apply the rules on newly created resrouces.

To make the function work on pre-existing resrouces run the included `resave_all_resource` command.

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

5. Add a view

Place `userandgroups.py` in `project_name -> views`

6. Urls

In `urls.py` add the following import at the top of the page
```
from .views.userandgroups import getUsers
```
Finally add the following url pattern to at the top of the `urlpatterns` array
```
url(r"^get/users", getUsers.as_view(), name="getUsers"),
```

## Optional `resave_all_resrouces` command

Copy the `resave_all_resrouces` to 
```
your/arches/installtion/managment/commands/
```

and run the following 
```
python manage.py resave_all_resrouces
```

# Demo
Demo on mature trees, actors Jane, John, admin and annonymous user.

### Scenarios

Rules are set up in the following way:
- Only John can see mature trees.
![image showing John only being able to see a mature tree](https://github.com/KacperSzyf/arches_functions/blob/main/eamena/ringfencing_function/imags/john.png)
- Only Jane can see juvenile trees.
![image showing Jane only being able to see a majuvenile tree](https://github.com/KacperSzyf/arches_functions/blob/main/eamena/ringfencing_function/imags/jane.png)
- Annonymous can't see any trees.
![image showing no results for anonymous users](https://github.com/KacperSzyf/arches_functions/blob/main/eamena/ringfencing_function/imags/anonymo.png)
- Admin can see all trees.
![image showing all trees for admin](https://github.com/KacperSzyf/arches_functions/blob/main/eamena/ringfencing_function/imags/admin.png)
