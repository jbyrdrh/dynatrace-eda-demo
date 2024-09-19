**Dynatrace w/ Event-Driven Ansible Demo**

**Prerequisites:**
- In order to set up this lab, you will have to build a decision environment for the Event-Driven Ansible controller.
Decision environments are a container image to run Ansible rulebooks.
- This is the current AAP 2.4 documentation for building a decision environment: https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/eda-decision-environments#eda-decision-environments

# Environment overview
In my example environment, I have 3 RHEL 9.4 VMs which comprise my Ansible Automation Platform test environment: an Automation Controller, a Private Automation Hub, and an Event-Driven Ansible controller. There is a 4th RHEL 9.4 system serving as the managed node running Dynatrace oneagent.
