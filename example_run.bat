TASKLIST | FINDSTR globus_connect || START "" "Path\globus_connect_personal.exe"
call activate globus
python PATH_TO_python_subprocess_test.py --svcuser SVC-USER LOCALENDPOINT --localdir /~/C/PATH_TO_LOCALDIR --remotedir PATH_TO_REMOTEDIR
