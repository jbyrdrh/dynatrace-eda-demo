# Instructions for Dynatrace w/ Event-Driven Ansible Demo

**Prerequisites:**
- In order to set up this lab, you will have to build a decision environment for the Event-Driven Ansible controller.
Decision environments are a container image to run Ansible rulebooks.
- This is the [current AAP 2.4 documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/eda-decision-environments#eda-decision-environments) for building an Event-Driven Ansible Decision Environment.
- [Dynatrace OneAgent](https://www.dynatrace.com/platform/oneagent/) deployed on a VM to serve as the managed node.

# Environment overview
- In my example environment, I have three RHEL 9 VMs for my Ansible Automation Platform test environment:
  - Automation Controller
  - Private Automation Hub
  - Event-Driven Ansible controller
- There is a 4th RHEL 9 VM serving as the managed node running [Dynatrace OneAgent](https://www.dynatrace.com/platform/oneagent/)

# Dynatrace OneAgent Setup
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
