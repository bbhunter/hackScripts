import json
import requests


def getRepos(user):
	headers = {"Travis-API-Version":"3",
		   "User-Agent":"API Explorer"}
	publicData = requests.get("https://api.travis-ci.com/owner/"+user+"/repos", headers=headers)
	privData = requests.get("https://api.travis-ci.org/owner/"+user+"/repos", headers=headers)
        if "repositories" in privData.json():
            return privData.json()['repositories']
        else:
            return []

def getJobLog(jobId):
	headers = {"Travis-API-Version":"3",
		   "User-Agent":"API Explorer"}
	publicData = requests.get("https://api.travis-ci.com/v3/job/"+str(jobId)+"/log.txt", headers=headers)
	privData = requests.get("https://api.travis-ci.org/job/"+str(jobId)+"/log.txt", headers=headers)
	return privData.text

def getBuilds(repoId):
	headers = {"Travis-API-Version":"3",
		   "User-Agent":"API Explorer"}
	publicData = requests.get("https://api.travis-ci.com/repo/"+str(repoId)+"/builds?include=job.config", headers=headers)
	privData = requests.get("https://api.travis-ci.org/repo/"+str(repoId)+"/builds?include=job.config", headers=headers)
        if "builds" in privData.json():
            return privData.json()['builds']
        else:
            return []




user="linode"
for repo in getRepos(user):
    builds = getBuilds(repo['id'])
    buildDescriptors = []
    for build in builds:
        buildDescriptor = {"key":build['repository']['slug']+"/"+str(build['id']), "message":build['commit']['message'], "configs":[], "logs":[]} # Contains job config, job log, and job commit message
        for job in build['jobs']:
            if job['config'] not in buildDescriptor['configs']:
                buildDescriptor['configs'].append(job['config'])
            log = getJobLog(job['id']).split("Network availability confirmed.")[1]
            buildDescriptor['logs'].append(log)
        buildDescriptors.append(buildDescriptor)
    exit()
