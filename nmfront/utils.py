import yaml


def read_file(path):
    with open(path,mode='r') as f:
        return f.read()

def read_yaml(path):
    return yaml.load(read_file(path),Loader=yaml.FullLoader)
def write_yaml(path,data):
    with open(path, "w") as f:
        yaml.dump(data, f)

# # print(read_yaml('./nmconfig.yaml'))
# configinfo=read_yaml('./nmconfig.yaml')
# print(configinfo['DISK_LARM_THRESHOLD'])
# configinfo['DISK_LARM_THRESHOLD']=50
# write_yaml('./nmconfig.yaml',configinfo)
# print(configinfo)
