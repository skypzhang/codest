import argparse
import settings





def reading_conf(conf_file):
    param_list = []
    with open(conf_file) as f:
        for line in f:
            if line.startswith('#'):
                continue
            if ',' in line:
                l = map(lambda x:x.strip(), line.split(','))
                t = tuple(l)
                param_list.append(t)
    return param_list

def get_params():
    params = reading_conf(conf_file)
    return params

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf', dest='conf', type=str, required=True)
    args = parser.parse_args()

    conf_file = args.conf
#    print(reading_conf(conf_file))


