DCS-Website
===========

Django-based website for the Department of Computer Science in the University of the Philippines.

Everything's in the tutorial :bd  
https://docs.djangoproject.com/en/1.6/intro/tutorial01/

Once you've pulled the files, open the command prompt, go to the directory where you've placed the files (cd .../DCS_Website) and enter "manage.py runserver".  
Using your browser, go to http://127.0.0.1:8000 to view the page (it's pretty empty so far).  
The admin page (http://127.0.0.1:8000/admin) can be accessed through all of the accounts: superadmin, admin, faculty, and student. Their passwords are the same as the usernames. They have different permissions based on the group they are in. The admin capability of approving changes made by student accounts is yet to be added.