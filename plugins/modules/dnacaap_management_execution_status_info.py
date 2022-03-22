#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dnacaap_management_execution_status_info
short_description: Information module for Dnacaap Management Execution Status
description:
- Get Dnacaap Management Execution Status by id.
- Retrieves the execution details of a Business API.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  executionId:
    description:
    - ExecutionId path parameter. Execution Id of API.
    type: str
requirements:
- dnacentersdk >= 2.4.7
- python >= 3.5
notes:
  - SDK Method used are
    task.Task.get_business_api_execution_details,

  - Paths used are
    get /dna/intent/api/v1/dnacaap/management/execution-status/{executionId},

"""

EXAMPLES = r"""
- name: Get Dnacaap Management Execution Status by id
  cisco.dnac.dnacaap_management_execution_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    executionId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "bapiKey": "string",
      "bapiName": "string",
      "bapiExecutionId": "string",
      "startTime": "string",
      "startTimeEpoch": 0,
      "endTime": "string",
      "endTimeEpoch": 0,
      "timeDuration": 0,
      "status": "string",
      "bapiError": "string",
      "runtimeInstanceId": "string"
    }
"""
