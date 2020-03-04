
while true

do

python3 make_index.py --dir .
git add .
date | awk '{print $4}' | xargs git commit -m
git push

sleep 3600

done

