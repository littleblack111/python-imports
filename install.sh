pushd ./dist
printf installing 
ls | grep *.whl
pip install *.whl && echo install succesful || echo install failed; $0 $@
popd
