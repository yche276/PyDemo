import yaml
# sudo pip install PyYAML


with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)


print(cfg['mysql'])
print(cfg['other'])

print(cfg['mysql']['passwd'])
