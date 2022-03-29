
while true

do

 find ../../farshidfarhat.github.io/URLs/ -type f -name "*.html" -exec cp {} . \; -print

 python3 make_index.py --dir .

 git add .
 date | awk '{print "\"chore: URLs updated "$0".\""}' | xargs git commit -m

 OUTPUT=$(git push | tail -1)
 while [ "$OUTPUT" = "fatal: The remote end hung up unexpectedly" ]
 do
  OUTPUT=$(git push | tail -1)
 done

 sleep $((RANDOM % 20011))
 sleep $((RANDOM % 20011))

done

