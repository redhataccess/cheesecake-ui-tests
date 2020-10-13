import os.path
from lemoncheesecake.project import Project
import sys

project_dir = os.path.dirname(__file__)
sys.path.append(project_dir)
project = Project(project_dir)
