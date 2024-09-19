**Dynatrace w/ Event-Driven Ansible Demo**

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
