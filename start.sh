cd st2-docker
sudo docker-compose up -d
sudo docker-compose exec st2client bash

#stop st2
sudo docker-compose stop

###edit and move

nano packs/slack_dilshan/slack_dilshan.yaml
cp packs/slack_dilshan/slack_dilshan.yaml /opt/stackstorm/configs/slack_dilshan.yaml


## reload
st2ctl reload --register-configs

st2ctl reload --register-rules

st2ctl reload --register-actions