# Create a Django admin project
django-admin startproject dcrud (dcrud is project name)

# Create a app inside your django-admin
python3 manage.py startapp crud

# First create method based view:
Steps:
1) Import your app (crud here) in the installed apps in settings.py
2) Go to the views of your app and then create def 
3) In the urls.py import views and set the route

Shortcomings in def based view:
we need to use req.method and then compare it will all the possible types instead of one generic thing


# Now class based views that are used normally

Every class will be child class of VIEW

Note: Django itself provides csrf token authentication and will not any post request if csrf is enable so fro demo purposes comment the csrf token one
For demo one we will comment the csrf token middleware from setting file

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
Mixin:

class which acts as parent class
to provide functionality to child class
only for child class but not itself(parent one)
Mainly for code resusalbility
we can't create object for mixin

Read Durga tutorial 4 from 1:07 to end

DB-Crud: 
created new app sqlcrud
Steps:
1) In model file created a Employee Model, then running makemigrations(to make queries) and migrations to execuet taht queries
python3 manage.py makemigrations
python3 manage.py migrate
2) Then register the model in admin interface to get it viewed on admin panel (admin.py in the same directory)

Create a super user:
python3 manage.py superuser
start the app and login to admin panel (/admin)
create some data for the corresponding model table.

Serialization:
Converting a object from one form to another is called serialization.
dict object to json object is serialization.

DumpData:

python3 manage.py dumpdata sqlcrud.Employee
python3 manage.py dumpdata sqlcrud.Employee --format json --indent 4 
python3 manage.py dumpdata sqlcrud.Employee --format xml --indent 4 

# Commenting csrf token 
1) Method level
2) Class level
3) Project level ( Not Recommmended) [Disable From Middleware]

1) To disable at Method level:
------------------------------
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):

2) To disable at class level:
------------------------------
from django.views.decorator.csrf import csrf_exempt
from djano.utils.decorator import method_decorator

@method_decorator(csrf_exempt,name='dispatch') //name = post if we want to exempt in post only
class EmployeeTest(View):

# Posting data into db
for posting data best thing available is to create forms and then post data
Validations can also be written there

