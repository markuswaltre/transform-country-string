import json

# name file sv.json, etc
# https://github.com/cobalteam/zsite/tree/4bfe0c042a2f5676bc3de5b12a1da7bb025bd058/vendor/symfony/symfony/src/Symfony/Component/Intl/Resources/data/regions
country = 'sv'

json_data=open('codes.json')
codes = json.load(json_data)["one"]

json_data=open('%s.json' % country)
lang = json.load(json_data, encoding='utf-8')

def getName(code):
	for x in codes:
		if x["code"] == code:
			return x["name"]

data = {}
for code in lang:
	data[getName(code)] = lang[code].encode('utf-8')

with open('%s_done.json' % country, 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4, sort_keys=True)


