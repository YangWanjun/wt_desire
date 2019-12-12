## runserver 
docker run -d --name wt_desire --link mysql:mysql -v /home/ec2-user/workspace/wt_desire/:/workspace -p 8001:80 yangwanjun/sales python3 /workspace/manage.py runserver 0.0.0.0:80
