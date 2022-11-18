#!/bin/bash


# docker ps | grep "business3" | awk '{print $1}'
CON_ID=$(docker ps | grep "business3" | awk '{print $1}')


if [[ -n "$CON_ID" ]]
then
    echo "container running and container_id is $CON_ID"
    # docker stop $CON_ID
    # echo $?
else
    echo "business 3 docker container is not running..!"
fi

if [[ ! -n "$CON_ID" ]]
then
    echo "starting business3 container again..!"
    CON_ID=$(docker run --rm -d --name business3 business3:1.0)

    if [[ $? != 0 ]]
    then
        echo "business3 container cant be running. It giving error"
    else
        echo "container running and container_id is $CON_ID"
    fi
fi

echo "Now stoping the container with id $CON_ID to get update, rebuild the image!"

docker stop $CON_ID
if [[ $? ==0]]
then
    echo "container stop successfully...!"
fi
