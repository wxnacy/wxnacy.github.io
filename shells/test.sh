

BREW_FILES="git openssl vim"
P=/bin
for i in $BREW_FILES
do 
echo "i is $i"
export P=$i:$P 
done

for i in $(brew --prefix)/opt/*/bin
do
export P=$i:$P
done
