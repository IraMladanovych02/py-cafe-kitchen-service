### Cafe Kitchen Service
 - Django-based web application for managing dishes and dish types in a cafe kitchen service.

### Description
- Cafe Kitchen Service is a web application built with Django to help cafes manage their dishes and dish types efficiently. The application provides an easy-to-use interface for adding, updating, and deleting dishes, as well as categorizing them into different types.

### Installation
1. Fork the repo (GitHub repository)
2. Clone the forked repo
`git clone https://github.com/your-username/cafe-kitchen-service.git`
3. If you are using PyCharm - create venv for your project and install requirements in it, but if not:
`python -m venv venv`
`venv\Scripts\activate` (on Windows)
`source venv/bin/activate` (on macOS)
`pip install -r requirements.txt`
4. Create superuser to manage the project:
`python manage.py createsuperuser`
5. Run server to check the website
6. Run pytest to check if your solution is correct 
(from command line, or using PyCharm pytest support)
7. Run flake8 to see if your code follows the flake8 rules
8. Save the solution  `git commit -am 'Explanation to changes'`
9. Push the solution to the repo `git push origin develop`


#
### Explanation to endpoints:
### General
- **`GET /`**  
  **Description**: Displays the main landing page.  
  **View Function**: `index`  
  **Name**: `index`

### Dish Types
- **`GET /dish_types/`**  
  **Description**: Lists all dish types.  
  **View**: `DishTypeListCreateView`  
  **Name**: `dish-types-list`


- **`POST /dish_types/`**  
  **Description**: Submits the form to create a new dish type.  
  **View**: `DishTypeListCreateView`  
  **Name**: `dish-types-list`

- **`GET /dish_types/<int:pk>/update/`**  
  **Description**: Displays a form to update an existing dish type identified by `<int:pk>`.  
  **View**: `DishTypeUpdateView`  
  **Name**: `dish-types-update`

- **`POST /dish_types/<int:pk>/update/`**  
  **Description**: Submits the form to update an existing dish type.  
  **View**: `DishTypeUpdateView`  
  **Name**: `dish-types-update`

- **`POST /dish_types/<int:pk>/delete/`**  
  **Description**: Deletes an existing dish type identified by `<int:pk>`.  
  **View**: `DishTypeDeleteView`  
  **Name**: `dish-types-delete`

### Dishes

- **`GET /dish/`**  
  **Description**: Lists all dishes.  
  **View**: `DishListCreateView`  
  **Name**: `dish-list`

- **`GET /dish/<int:pk>/`**  
  **Description**: Displays details of a specific dish identified by `<int:pk>`.  
  **View**: `DishDetailView`  
  **Name**: `dish-detail`


- **`POST /dish/create/`**  
  **Description**: Submits the form to create a new dish.  
  **View**: `DishListCreateView`  
  **Name**: `dish-list`

- **`GET /dish/<int:pk>/update/`**  
  **Description**: Displays a form to update an existing dish identified by `<int:pk>`.  
  **View**: `DishUpdateView`  
  **Name**: `dish-update`

- **`POST /dish/<int:pk>/update/`**  
  **Description**: Submits the form to update an existing dish.  
  **View**: `DishUpdateView`  
  **Name**: `dish-update`

- **`POST /dish/<int:pk>/delete/`**  
  **Description**: Deletes an existing dish identified by `<int:pk>`.  
  **View**: `DishDeleteView`  
  **Name**: `dish-delete`

### Cooks

- **`GET /cooks/`**  
  **Description**: Lists all cooks.  
  **View**: `CookListCreateView`  
  **Name**: `cook-list`

- **`GET /cooks/<int:pk>/`**  
  **Description**: Displays details of a specific cook identified by `<int:pk>`.  
  **View**: `CookDetailView`  
  **Name**: `cook-detail`


- **`POST /cooks/create/`**  
  **Description**: Submits the form to create a new cook.  
  **View**: `CookListCreateView`  
  **Name**: `cook-list`

- **`GET /cooks/<int:pk>/update/`**  
  **Description**: Displays a form to update the experience of a cook identified by `<int:pk>`.  
  **View**: `CookExperienceUpdateView`  
  **Name**: `cook-update`

- **`POST /cooks/<int:pk>/update/`**  
  **Description**: Submits the form to update the cook's experience.  
  **View**: `CookExperienceUpdateView`  
  **Name**: `cook-update`

- **`POST /cooks/<int:pk>/delete/`**  
  **Description**: Deletes an existing cook identified by `<int:pk>`.  
  **View**: `CookDeleteView`  
  **Name**: `cook-delete`

### Special Actions
- **`POST /dishes/<int:pk>/toggle/`**  
  **Description**: Toggles assignment of a cook to a dish identified by `<int:pk>`.  
  **View Function**: `toggle_assign_to_dish`  
  **Name**: `toggle-assign-to-dish`

---