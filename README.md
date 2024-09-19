## Instructions for Dynatrace w/ Event-Driven Ansible Demo

**Prerequisites:**
- In order to set up this lab, you will have to build a decision environment for the Event-Driven Ansible controller.
Decision environments are a container image to run Ansible rulebooks. (See "Setting up the Event-Driven Ansible environment" below.)
- [Dynatrace OneAgent](https://www.dynatrace.com/platform/oneagent/) deployed on a VM to serve as the managed node.

**Environment overview**
- In my example environment, I have three RHEL 9 VMs for my Ansible Automation Platform test environment:
  - Automation Controller
  - Private Automation Hub
  - Event-Driven Ansible controller
- There is a 4th RHEL 9 VM serving as the managed node running [Dynatrace OneAgent](https://www.dynatrace.com/platform/oneagent/)

**Dynatrace OneAgent Setup**
- Once you have at least obtained a trial Dynatrace Instance, on the Dynatrace web UI:
  - Use the Search function to search for "Deploy OneAgent"
  - On the "Download Dynatrace OneAgent" screen, choose the appropriate OS installation instructions.
  - In my example, I chose the Linux option.
  - Chose "Create token"
  - Copy and paste the installation commands into the Linux terminal.

- Next, use the Search function once again to search for "Access Tokens"
  - On the Access tokens page, choose "Generate new token"
  - Give your token an arbitrary name
  - Give your token the following permissions:
    - (API v2 scopes) Ingest events, Read events, Read problems, Write problems, Read security problems
    - (API v1 scopes) Access problem and event feed, metrics, and topology, Read configuration, and Write configuration

**Setting up the Event-Driven Ansible environment**
- This is the [current AAP 2.4 documentation for building an Event-Driven Ansible Decision Environment.](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/eda-decision-environments#eda-decision-environments)

This is an example DE definition file that can be used to build the environment:

~~~
---
version: 3

dependencies:
  galaxy:
    collections:
      - name: ansible.eda
      - name: dynatrace.event_driven_ansible
  system:
    - pkgconf-pkg-config [platform:rpm]
    - systemd-devel [platform:rpm]
    - gcc [platform:rpm]
    - python39-devel [platform:rpm]

options:
  package_manager_path: /usr/bin/microdnf

images:
  base_image:
    name: registry.redhat.io/ansible-automation-platform-24/de-minimal-rhel8:latest
~~~

**Writing a Rulebook to watch for problems on Dynatrace**

Example rulebook:

~~~
---
- name: Watching for Problems on Dynatrace
  hosts: all
  sources:
    - dynatrace.event_driven_ansible.dt_esa_api:
        dt_api_host: "{{ dynatrace_host }}"
        dt_api_token: "{{ dynatrace_token }}"
        delay: "{{ dynatrace_delay }}"

  rules:
    - name: Problem payload Dynatrace for CPU saturation issue
      condition: event.title contains "CPU saturation"
      action:
        debug:
          msg: " CPU saturation"

    - name: Problem payload Dynatrace for Memory saturation issue
      condition: event.title contains "Memory saturation"
      action:
        debug:
          msg: " Memory saturation"
~~~

**The following python script will trigger 100% CPU utilization**

~~~
#!/usr/bin/env python3

import multiprocessing
import time

def cpu_stress():
    while True:
        # Perform intensive calculations
        x = 0
        while True:
            x += 1
            if x > 1e6:
                x = 0  # Reset to avoid overflow

def run_stress_on_all_cores():
    num_cores = multiprocessing.cpu_count()
    print(f"Spawning {num_cores} processes to fully utilize the CPU")
    processes = []
    
    try:
        for _ in range(num_cores):
            p = multiprocessing.Process(target=cpu_stress)
            processes.append(p)
            p.start()

        # Keep the main process alive to allow CPU stress to continue
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Process interrupted by user. Stopping all processes.")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    run_stress_on_all_cores()
~~~
