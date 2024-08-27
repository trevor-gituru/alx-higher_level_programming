title="$(tail -n 1 ./README.md | grep -oP '\[\K[^]]+')"
git add README.md
git commit -m "Added '$title' resource"
