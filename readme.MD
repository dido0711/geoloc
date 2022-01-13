1. Usage in localhost

-Database setting

set PRODUCTION variable in settings.py to False
-Python  Dependency

pip install requirements.txt


2. Usage in production

-Database setting
set PRODUCTION variable in settings.py to True

-Use gitlab CI pipeline to deploy, see below link for detail
https://docs.gitlab.com/ee/ci/quick_start/
https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html