#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_performance_info
short_description: Information module for System Performance
description:
- Get all System Performance.
- This API gives the aggregated performance indicators. The data can be retrieved for the last 3 months.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  kpi:
    description:
    - Kpi query parameter. Valid values cpu,memory,network.
    type: str
  function:
    description:
    - Function query parameter. Valid values sum,average,max.
    type: str
  startTime:
    description:
    - >
      StartTime query parameter. This is the epoch start time in milliseconds from which performance indicator
      need to be fetched.
    type: int
  endTime:
    description:
    - >
      EndTime query parameter. This is the epoch end time in milliseconds upto which performance indicator need to
      be fetched.
    type: int
requirements:
- dnacentersdk >= 2.4.7
- python >= 3.5
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.system_performance,

  - Paths used are
    get /dna/intent/api/v1/diagnostics/system/performance,

"""

EXAMPLES = r"""
- name: Get all System Performance
  cisco.dnac.system_performance_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    kpi: string
    function: string
    startTime: 0
    endTime: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostName": "string",
      "version": "string",
      "kpis": {
        "cpu": {
          "units": "string",
          "utilization": "string"
        },
        "memory": {
          "units": "string",
          "utilization": "string"
        },
        "network tx_rate": {
          "units": "string",
          "utilization": "string"
        },
        "network rx_rate": {
          "units": "string",
          "utilization": "string"
        }
      }
    }
"""
