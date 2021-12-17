import json
import time
import re
import requests
import argparse


def request_validation(data, files):
    url = 'https://apps.opcfoundation.org/NodeSetValidator/Home/Upload'
    response = requests.post(url, files=files, data=data)
    job_id = get_job_id(response.text)
    print(f"Get response {response} of ther server: ")
    print(f"Validation Job started with numver {job_id}")
    # print(response.text)
    return job_id


def prepare_input_data_from_config(config_path):
    with open(config_path, "r") as json_file:
        config = json.loads(json_file.read())

        files = [("nodesetFile", open(config['nodesetFile'], 'rb'))]
        for support_node_set in config['supportingNodeSetFiles']:
            files.append(("supportingNodeSetFiles", open(support_node_set, 'rb')))
        files.append(("specificationFile", open(config['specificationFile'], 'rb')))
        data = {
            "email": config['email'],
            "ignoreTypes": config['ignoreTypes'],
            "suppressErrors": config['suppressErrors'],
            "noDelete": config['noDelete'],
            "checkConformanceUnits": config['checkConformanceUnits']
        }
    return prepare_input_data(config["nodesetFile"],
                              config["supportingNodeSetFiles"],
                              config["specificationFile"],
                              config["email"],
                              config["ignoreTypes"],
                              config["suppressErrors"],
                              config["noDelete"],
                              config["checkConformanceUnits"])

def prepare_input_data_from_cli(args):
    return prepare_input_data(args["nodesetfile"],
                              args["supportingNodeSetFiles"],
                              args["specificationFile"],
                              args["email"],
                              args["ignoreTypes"],
                              args["suppressErrors"],
                              args["noDelete"],
                              args["checkConformanceUnits"])

def prepare_input_data(nodesetfile,
                       supporting_node_set_files,
                       specificationFile,
                       email,
                       ignoreTypes,
                       suppressErrors,
                       noDelete,
                       checkConformanceUnits):
    files = [("nodesetFile", open(nodesetfile, 'rb'))]
    for support_node_set in supporting_node_set_files:
        files.append(("supportingNodeSetFiles", open(support_node_set, 'rb')))
    files.append(("specificationFile", open(specificationFile, 'rb')))
    data = {
        "email": email,
        "ignoreTypes": ignoreTypes,
        "suppressErrors": suppressErrors,
        "noDelete": noDelete,
        "checkConformanceUnits": checkConformanceUnits
    }
    return data, files


def get_job_id(text):
    regex = r"\/NodeSetValidator\/Home\/Results\/([0-9]+)\""
    job_id = re.findall(regex, text)
    return job_id[0]


def get_validation_result(timeout, job_id):
    result_url = f"https://apps.opcfoundation.org/NodeSetValidator/Home/DownloadResults/{job_id}?filename=results.csv"
    for x in range(10):
        print(f"try load results {x} /10")
        time.sleep(timeout / 10)
        response = requests.post(result_url)
        if "html" in response.text:
            continue
        else:
            print(response.text)
            break


def main():
    args = argument_parser()
    if 'config' in args:
        data, files = prepare_input_data_from_config(args.config)
    else:
        data, files = prepare_input_data_from_cli(args)
    job_id = request_validation(data, files)
    get_validation_result(timeout=(10 * 60), job_id=job_id)


def argument_parser():
    """
    Generate an ArgumentParser menu and parse the arguments
    see main.py -h for all options
    :return: args
    """
    parser = argparse.ArgumentParser(description='Nodeset Validation Runner')
    parser.add_argument('--config', metavar='c', type=str, nargs='?',
                        help='path to a json config file. Which contain all of the other args')
    parser.add_argument('--nodesetfile', metavar='n', type=str, nargs='?',
                        help='A file to validate that conforms to the UANodeSet schema defined in Part 6 of the OPC '
                             'UA Specification. ')
    parser.add_argument('--supportingNodeSetFiles', type=str, nargs='*',
                        help='Additional NodeSet files which are needed to process the NodeSet that is being validated.')
    parser.add_argument('--document', metavar='d', type=str, nargs='?',
                        help='A Word document that follows the conventions defined for OPC UA specifications.')
    parser.add_argument('--email', type=str, nargs='?',
                        help='An optional email used to send a notification when the processing compeletes.')
    parser.add_argument('--ignoreTitels', metavar='s', type=str, nargs='*',
                        help='An optional comma seperated list of type names which will be ignored by the tool')
    parser.add_argument('--supressError', metavar='e', type=str, nargs='*',
                        help='An optional comma seperated list of type names which will be ignored by the tool')
    args = parser.parse_args()
    return args


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
