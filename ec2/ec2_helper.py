#!/usr/bin/python

import sys

import connect_ec2

def _get_instance_by_name(conn, name=None):
  for res in conn.get_all_instances():
    for ins in res.instances:
      if 'Name' in ins.tags and ins.tags['Name'] == name:
        instance = ins
  return instance

def start_instance_by_name(name=None):
  conn = connect_ec2.get_connection()
  try:
    instance = _get_instance_by_name(conn, name)
    conn.start_instances([instance.id])
    print 'Done'
  except:
    print 'Failed to start instance'

def stop_instance_by_name(name=None):
  conn = connect_ec2.get_connection()
  try:
    instance = _get_instance_by_name(conn, name)
    conn.stop_instances([instance.id])
    print 'Done'
  except:
    print 'Failed to stop instance'

def get_instance_ip_by_name(name=None):
  conn = connect_ec2.get_connection()
  try:
    instance = _get_instance_by_name(conn, name)
    print instance.public_dns_name
  except:
    print 'Failed to find instance'

if __name__ == '__main__':
  try:
    command = sys.argv[1]
    name = sys.argv[2]
    if command == 'start':
      start_instance_by_name(name)
    elif command == 'stop':
      stop_instance_by_name(name)
    elif command == 'getip':
      get_instance_ip_by_name(name)
    else:
      raise 'no command specified'

  except:
    print 'Usage: %s command instance_name' % sys.argv[0]
    print ' command: start, stop, getip'
