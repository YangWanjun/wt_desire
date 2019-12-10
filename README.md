## runserver 
docker run -d --name wt_desire --link mysql:mysql -v /home/ec2-user/workspace/wt_desire/:/workspace yangwanjun/sales python3 /workspace/manage.py runserver 0.0.0.0:8001
