fission spec init
fission env create --spec --name onb-br-enum-marit-env --image nexus.sigame.com.br/fission-onboarding-br-enum-marit:0.2.0-0 --poolsize 0 --version 3 --imagepullsecret "nexus-v3" --spec
fission fn create --spec --name onb-br-enum-marit-fn --env onb-br-enum-marit-env --code fission.py --targetcpu 80 --executortype newdeploy --maxscale 3 --requestsperpod 10000 --spec
fission route create --spec --name onb-br-enum-marit-rt --method GET --url /enum/marital_status --function onb-br-enum-marit-fn
