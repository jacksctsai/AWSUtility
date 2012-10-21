
from boto.ec2.connection import EC2Connection

def get_connection():
  conn = EC2Connection('AKIAIVOKQSWBBGSKDL2A', 'UKUBML2+aXvSa2DLv/cDCrpSTrh/NiswOB5Pberl')
  return conn
