cd st2-docker
sudo docker-compose up -d
sudo docker-compose exec st2client bash


nano packs/slack_dilshan/slack_dilshan.yaml
cp packs/slack_dilshan/slack_dilshan.yaml /opt/stackstorm/configs/slack_dilshan.yaml
st2ctl reload --register-configs