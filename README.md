<h1 align="center"><a href="#" alt="cookin">Sales Record App</a></h1>

Load sales record's data into database through text file uploading.

Files should be uploaded in multipart form with name = file.

To run the application using docker-compose, follow the next steps:

1. Run in CLT the following command to build your docker image: docker build -t image_name path_chosen_to_create_image (if you want to create in the actual directory, use .)
2. To persist migrations, run in CLT: docker-compose exec web python manage.py migrate
3. To run the application run in CLT: docker-compose up (Base URL: http://127.0.0.1:8000/)

\*\*Observation:
To run the tests, a variable named TEST should be set in CLT command (tests are supposed to run in SQLite database).
Run in CLT the following to run the tests:
TEST=test python manage.py test

To produce a report with test results, run in CLT:
TEST=test python manage.py test -v 2 &> report.txt
