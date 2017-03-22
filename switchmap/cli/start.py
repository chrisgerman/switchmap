#!/usr/bin/env python3
"""switchmap CLI functions for 'start'.

Functions to start daemons

"""

# Main python libraries
import sys
import os

# Switchmap-NG imports
from switchmap.utils import general
from switchmap.utils import configuration
from switchmap.utils import log
from switchmap.main.agent import Agent, AgentAPI, AgentDaemon
from switchmap.constants import (
    API_EXECUTABLE, API_GUNICORN_AGENT, POLLER_EXECUTABLE)


def run(args):
    """Process 'start' command.

    Args:
        args: Argparse arguments

    Returns:
        None

    """
    # Show help if no arguments provided
    if args.qualifier is None:
        general.cli_help()

    # Process 'show api' command
    if args.qualifier == 'api':
        api()
    elif args.qualifier == 'poller':
        poller()

    # Show help if there are no matches
    general.cli_help()


def api():
    """Process 'start api' commands.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    config = configuration.Config()

    # Check existence of systemd file
    if general.systemd_exists(API_EXECUTABLE) is True:
        general.systemd_daemon(API_EXECUTABLE, action='start')
    else:
        # Check user
        general.check_user()

        # Create agent objects
        agent_gunicorn = Agent(API_GUNICORN_AGENT)
        agent_api = AgentAPI(API_EXECUTABLE, API_GUNICORN_AGENT)

        # Start daemons (API first, Gunicorn second)
        daemon_api = AgentDaemon(agent_api)
        daemon_api.start()
        daemon_gunicorn = AgentDaemon(agent_gunicorn)
        daemon_gunicorn.start()

    # Change the log file permissions
    os.chmod(config.web_log_file(), 0o0644)
    log.log2info(2222222222222222222, 'boo 2')

    # Done
    sys.exit(0)


def poller():
    """Process 'start poller' commands.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    config = configuration.Config()

    # Check existence of systemd file
    if general.systemd_exists(POLLER_EXECUTABLE) is True:
        general.systemd_daemon(POLLER_EXECUTABLE, action='start')
    else:
        # Check user
        general.check_user()

        # Create agent object
        agent_poller = Agent(POLLER_EXECUTABLE)

        # Start agent
        daemon_poller = AgentDaemon(agent_poller)
        daemon_poller.start()

    # Change the log file permissions
    os.chmod(config.log_file(), 0o0644)
    log.log2info(111111111111111111111111, 'boo 2')

    # Done
    sys.exit(0)
