logstash_cleanout
=================

Deletes old elasticsearch/logstash indices to free up disk space

Usage:
------
    usage: cleanout.py [-h] [--noop] [--days DAYS]
    
    Clean out old ElasticSearch indexes for Logstash
    optional arguments:
      -h, --help   show this help message and exit
      --noop       Doesn't actually delete anything
      --days DAYS  The number of days older than Today to delete - Default is 5
      

--noop will mean nothing is actually deleted.. it's a handy dry-run.

--days defaults to 5 if not set.

