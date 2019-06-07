#!/bin/bash -eu

sizeof() { wc -c $1 | awk '{print $1}'; }  # size, in bytes
same-size() (( $(sizeof $1) == $(sizeof $2) ))  # size, in bytes
same-size-1_23() (( $(sizeof $1) == $(sizeof $2) + $(sizeof $3) ))  # size of the first == sum of sizes of second two

# create sandbox
mkdir testappends; pushd $_ >/dev/null
trap 'popd > /dev/null; rm -rf testappends' EXIT
trap 'echo FAIL' ERR

t=$(which true)
f=$(which false)
same-size $t $f # same size

# tandem duplications of true and false
cat $t $f > true_false
cat $f $t  > false_true
same-size true_false false_true
same-size-1_23 true_false $t $t

# append bash to {true,false}
b=$(which bash)
cat $t $b > true_bash
cat $f $b > false_bash
same-size-1_23 true_bash $b $f
same-size-1_23 false_bash $b $f

chmod +x *
true_false && echo true_false is true
false_true || echo false_true is false
true_bash && echo true_bash is true
false_bash || echo false_bash is false

# finally, just for the heck of it, append stuff to bash
cat $b $f > bash_false
cat $b $t > bash_true
cat $b $b > bash_bash
chmod +x bash_*
bash_false <<< 'echo bash_false is bash'
bash_true <<< 'echo bash_true is bash'
bash_bash <<< 'echo Even bash_bash is bash!'

echo
echo SUCCESS
