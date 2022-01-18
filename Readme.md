# OPC UA Nodeset Validation Runner

This is a short script that starts a validation of the
Nodeset Validation tool (see <https://apps.opcfoundation.org/NodeSetValidator/>) of the OPC Foundation.
It is an unofficial python client that should simplify the automated validation.

## Dependencies

see `requirements.txt`

## Installation

`pip install -r requirements.txt`

## Use

- copy test/config.json
- modify config.json file (to your own  Companion Specification / nodeset / ...)
- run `python3 main.py --config config.json`

## Config Stucture

- nodesetFile: A file to validate that conforms to the UANodeSet schema defined in Part 6 of the OPC UA Specification.
- supportingNodeSetFiles: Additional `unreleased` NodeSet files which are needed to process the NodeSet that is being validated.
- specificationFile: A Word document that follows the conventions defined by the [OPC 11020 - UA Companion Specification Template](https://opcfoundation.org/Guidelines-And-Templates/).
- email (not needed): An optional email used to send a notification when the processing completes.
- ignoreTypes: An optional comma seperated list of type names which will be ignored by the tool.
- suppressErrors: An optional comma seperated list of errors which should be suppressed.
- noDelete: Flag that indicates if the files are removed from the server automatically
- checkConformanceUnits (new feature): Check that the conformance units assigned to nodes exist in the profile database.
