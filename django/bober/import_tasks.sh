#!/bin/sh

# Import tasks from git repository.

cd /home/j/bober-naloge

for competition in $(ls -d */); do
    cd $competition;
    bash -c '\
        ls skupine;\
        for skupina in skupine/* ; do\
            echo $skupina;\
            python3 /home/bober/bober/manage.py import_question_dir $skupina;\
    done'
    cd ..
done
