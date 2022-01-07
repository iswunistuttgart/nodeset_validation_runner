# OPC UA Nodeset Validation Runner
This is a short script that start a validation of the 
Nodeset Valdation tool (see https://apps.opcfoundation.org/NodeSetValidator/) of the OPC Foundation. 
It is an unofficial python client that should simplify the automated using.


## Dependencies
see requirement.txt

## Installation
pip install -r requirements.txt

## Use 

- copy test/config.json
- modify config.json file (to your own  Companion Specification / nodeset / ...)
- run python main.py --config config.json

## Config Stucture
- nodesetFile: A file to validate that conforms to the UANodeSet schema defined in Part 6 of the OPC UA Specification. 
- supportingNodeSetFiles: Additional NodeSet files which are needed to process the NodeSet that is being validated.
- specificationFile: A Word document that follows the conventions defined for OPC UA specifications.
- email (not needed): An optional email used to send a notification when the processing compeletes.
- ignoreTypes: An optional comma seperated list of type names which will be ignored by the tool.
- suppressErrors: An optional comma seperated list of errors which should be suppressed.
- noDelete: Flag that indicate if the file are removed from the serve automatically 
- checkConformanceUnits (new Feature): Check that the conformance units assigned to nodes exist in the profile database.
