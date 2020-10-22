py.test -s -v -m "sanity" -n=2 --html=Reports\reports3.html --browser Chrome testCases
rem pytest -s -v -m "sanity and regression" --html=Reports\reports3.html --browser Chrome testCases
rem pytest -v -s -m "sanity or regression" --html=Reports\Reports4.html --browser Chrome testCases
rem pytest -v -s -m "regression" --html=Reports\Reports5.html --browser Chrome testCases

