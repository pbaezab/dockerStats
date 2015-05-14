#! /usr/bin/env python

import argparse
import docker
import json
import logging

class DockerStats():

		def __init__(self, url):

			self.url = url
			self.conn = docker.Client(base_url=self.url, timeout=20)
	
		def stats(self):
			'''

			'''
			
			self.containers = self.conn.containers()
			
			logging.info("action=num_containers total=" + str(len(self.containers)))		

			for container in self.containers:

				#container_name = container["Names"][0].replace('/','')
				container_id = str(container["Id"])
				container_img = str(container["Image"])

				stats = self.conn.stats(container_id)

				for statStr in stats:
					logging.info(self._readStat(statStr,container_id, container_img))
					break
			

		def _readStat(self,stats,container_id, container_img):
			'''
			'''

			statsObj = json.loads(stats)

			summaryData = dict(
				container_id=container_id,
				container_img=container_img,
				memory_usage=str(statsObj["memory_stats"]['usage']),
				memory_limit=str(statsObj["memory_stats"]['limit']),
				cpu_usage=str(statsObj["cpu_stats"]["cpu_usage"]["total_usage"]),
				cpu_total_system=str(statsObj["cpu_stats"]["cpu_usage"]["total_usage"]),
				network_rx_bytes=str(statsObj["network"]["rx_bytes"]),
				network_tx_bytes=str(statsObj["network"]["tx_bytes"]),
				network_rx_dropped=str(statsObj["network"]["rx_dropped"]),
				network_tx_dropped=str(statsObj["network"]["tx_dropped"]),
				network_rx_errors=str(statsObj["network"]["rx_errors"]),
				network_tx_errors=str(statsObj["network"]["tx_errors"]),
				network_rx_packet=str(statsObj["network"]["rx_packets"]),
				network_tx_packet=str(statsObj["network"]["tx_packets"]),
				blkio_io_service_bytes=str(statsObj["blkio_stats"]["io_service_bytes_recursive"]),
				blkio_io_serviced=str(statsObj["blkio_stats"]["io_serviced_recursive"]),
				blkio_io_queue=str(statsObj["blkio_stats"]["io_queue_recursive"])
			)

			summaryStr = "action=stats "
			for key,value in summaryData.items():
				summaryStr += " "+key+"="+value
			return summaryStr

def main():

	argp = argparse.ArgumentParser()
	argp.add_argument('-u', '--url', metavar='URL',
					  help='URL string for Docker service.',
					  default='unix://var/run/docker.sock'),

	args = argp.parse_args()

	logging.basicConfig(level=logging.INFO, filename="/var/log/docker-stats.log", format='%(asctime)s %(message)s')
	docker_stats = DockerStats(args.url)
	docker_stats.stats()



if __name__ == '__main__':
	main()
