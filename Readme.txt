Group 14

C Vishwesh, 140050031		100%
Saurabh Garg, 140070003		100%
Aviral Kumar, 140070031		100%

Honor Code: 
I pledge on my honour that I have not given or received any unauthorized assistance on this assignment or any previous task. 


Installation Instructions :

For Ubuntu 14.04 :
Open terminal 
(i) Ensure Ubuntu 14.04 is upto date:
	 sudo apt-get update
(ii) Extract the download folder and change current directory to Django_Project which is inside submitted folder	 
(iii)Install python  
   	 sudo apt-get install python-pip
(iv) Install Virtual Enviornment  
	 sudo pip install virtualenv
(v) Type the following command to create virtual env :
	virtualenv .
(vi) Activate virtual enviornment by typing :
	source bin/activate
(vii) Install django in this virtual env by typing the following command :
	pip install django
(viii) Install Third party package Crispy forms by typing following command:
	pip install --upgrade django-crispy-forms


The project is now ready to use :
(i) Change directory to src folder inside this project and run the following commands :
	--- To make all migrations type :
		python manage.py makemigrations
	--- To migrate all changes write 
		python manage.py migrate
	--- Now Create a super user by typing command 
		python manage.py createsuperuser
		(Username should be different from admin)
	--- Now run the server by typing :
		python manage.py runserver 
		Link will be shown on the Terminal 
		(Crlt-click the link to open in Browser)
(ii) The website is now up at the link for testing all features mentioned in Feature_doc.txt

(iii) code is also included in testcases folder



Citations:

https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04
http://stackoverflow.com/questions/19668444/how-to-add-import-a-django-project-into-a-virtualenv
http://django-crispy-forms.readthedocs.org/en/d-0/install.html
https://docs.djangoproject.com/en/1.8/
http://django-crispy-forms.readthedocs.org/en/latest/
https://github.com/axelpale/minimal-django-file-upload-example
http://stackoverflow.com/questions/17663809/deleting-uploaded-files-in-django
https://docs.djangoproject.com/en/dev/ref/contrib/messages/#using-messages-in-views-and-templates
https://docs.python.org/2/library/os.path.html
http://stackoverflow.com/questions/735545/how-to-access-data-when-form-is-valid-is-false
https://groups.google.com/forum/#!topic/django-users/gt79d6ESo8A
http://stackoverflow.com/questions/25253678/django-render-models-into-template
http://stackoverflow.com/questions/15029666/exporting-items-from-a-model-to-csv-django-python
http://stackoverflow.com/questions/2514961/remove-a-sublist-from-a-list-in-python
http://stackoverflow.com/questions/7601691/remove-item-from-dropdown-list-on-page-load-no-jquery
http://stackoverflow.com/questions/11787272/how-to-create-dropdown-menu-that-appears-based-on-answer-from-another-dropdown-m
http://stackoverflow.com/questions/17461411/div-style-display-none-inside-a-table-not-working
http://stackoverflow.com/questions/2237064/passing-arguments-to-a-dynamic-form-in-django
http://stackoverflow.com/questions/7920128/difference-between-django-form-initial-and-bound-data
http://www.ilian.io/django-forms-choicefield-with-dynamic-values/
https://mayukhsaha.wordpress.com/2013/05/09/simple-login-and-user-registration-application-using-django/
http://stackoverflow.com/questions/14919922/select-onchange-not-working-inside-a-form
http://stackoverflow.com/questions/21497497/django-self-cleaned-data-keyerror
http://stackoverflow.com/questions/5083493/is-valid-vs-clean-django-forms
http://stackoverflow.com/questions/2964244/django-meaning-of-leading-underscore-in-list-of-tuples-used-to-define-choice-fi
http://stackoverflow.com/questions/15846743/django-keyerror-at-register
http://stackoverflow.com/questions/10377510/django-checking-to-see-if-filter-returns-anything-in-the-queryset
http://www.effectivedjango.com/forms.html
http://stackoverflow.com/questions/18179960/how-to-add-a-title-to-a-html-select-tag
http://stackoverflow.com/questions/16117393/can-not-iterate-a-choicefield-with-select-as-widget
http://stackoverflow.com/questions/8567455/django-custom-forms-select-tag
http://stackoverflow.com/questions/3090302/in-django-how-do-i-objects-get-but-return-none-when-nothing-is-found
http://gregblogs.com/the-little-things-tlt-django-creating-a-drop-down-list-with-django/
http://stackoverflow.com/questions/2320581/django-redirect-logged-in-users-from-login-page
http://stackoverflow.com/questions/8813674/javascript-popup-alert-on-link-click
https://docs.python.org/2.7
http://stackoverflow.com/questions/22957606/remove-tuple-from-list-of-tuples-if-certain-condition-is-met
http://stackoverflow.com/questions/5516437/django-form-has-no-errors-but-form-is-valid-doesnt-validate
http://joincfe.com
http://trydjango.com
http://w3schools.com
http://stackoverflow.com/questions/16906515/how-can-i-get-the-username-of-the-logged-in-user-in-django
http://stackoverflow.com/questions/732952/get-primary-key-after-saving-a-modelform-in-django
http://stackoverflow.com/questions/2837229/how-do-i-save-data-from-a-modelform-to-database-in-django
http://www.djangobook.com/en/
https://groups.google.com/forum/#!topic/django-users/9KaJEh4pBWo
http://www.tutorialspoint.com/python/os_listdir.htm
https://docs.djangoproject.com/en/1.8/ref/forms/fields/
http://stackoverflow.com/questions/735545/how-to-access-data-when-form-is-valid-is-false
http://stackoverflow.com/questions/11871104/django-generate-download-link
http://stackoverflow.com/questions/15246661/downloading-the-fileswhich-are-uploaded-from-media-folder-in-django-1-4-3
http://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it
http://stackoverflow.com/questions/16849117/html-how-to-do-a-confirmation-popup-to-a-submit-button-and-then-send-the-reque
http://stackoverflow.com/questions/1085801/get-selected-value-in-dropdown-list-using-javascript
http://www.tutorialspoint.com/python/file_close.htm
http://stackoverflow.com/questions/755857/default-value-for-field-in-django-model