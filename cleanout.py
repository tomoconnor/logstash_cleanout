from pyes import *
import datetime
import logging
import argparse
DAYS_OLD = 5

logger = logging.getLogger('elastic_rotate')
logger.setLevel(logging.INFO)
lh = logging.StreamHandler()
lh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
lh.setFormatter(formatter)
logger.addHandler(lh)


try:
    parser = argparse.ArgumentParser(description = 'Clean out old ElasticSearch indexes for Logstash')
    parser.add_argument('--noop', help="Doesn't actually delete anything", action='store_true')
    parser.add_argument('--days', help="The number of days older than Today to delete",default=DAYS_OLD)
    args = parser.parse_args()
except Exception, e:
    logger.error(e.message)

try:
    logger.info("Deleting indices older than %s days"%args.days)
    conn = ES('127.0.0.1:9200')
    indices = conn.indices.get_indices()
    index_rotate_threshold = datetime.datetime.now() - datetime.timedelta(days=int(args.days))
    index_counter = 0
    
    for index in indices:
        datestring = index.split('-')[1]
        date_object = datetime.datetime.strptime(datestring,'%Y.%m.%d')
        if date_object < index_rotate_threshold:
            logger.info("DELETE INDEX %s"%index)
    	if not args.noop:
                conn.indices.delete_index(index)
                index_counter += 1
    
    logger.info("Deleted %s indices" % index_counter)
    
except Exception, e:
   logger.error(e.message)

 
