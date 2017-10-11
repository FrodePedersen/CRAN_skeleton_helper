from optparse import OptionParser
import subprocess as sp
import re
from itertools import zip_longest

def write_recipe(package, recipe_dir, config=None, force=False, bioc_version=None,
				 pkg_version=None, versioned=False):
	#sp.call(['conda', 'skeleton', 'cran', package], shell=True)
	clean_skeleton_files(package, recipe_dir)
	

def clean_skeleton_files(package, recipe_dir):
	lines = []
	path = 'r-' + package + '/meta.yaml'
	with open(path, 'r') as yaml:
		lines = list(yaml.readlines())
		lines = remove_comments(lines)
		lines = remove_spaces(lines)
	
	print("LINES: " + str(lines))
 
	with open(path, 'w') as yaml:
		yaml.write("".join(lines))	

def remove_comments(lines):
	cleanedYaml = []

	for line in lines:
		#Remove comments
		tempLine = re.sub(r'\s*#.*$', '', line)
		#Append only non-empty lines as a result of a removed comment
		tempLineHasChanged = False
		if tempLine != line:
			tempLineHasChanged = True

		if (tempLineHasChanged and tempLine != '\n' or
			not tempLineHasChanged):
			cleanedYaml.append(tempLine)

	print("new yaml: \n" + str(cleanedYaml))
	return cleanedYaml

def remove_spaces(lines):
	cleanedYaml = []
	for i, j in zip_longest(lines, lines[1:]):
	 	if i.isspace() and j.isspace():
	 		pass
	 	else:
	 		cleanedYaml.append(i)

	return cleanedYaml

def main():
	""" Adding support for arguments here """
	usage = "usage: %prog [options] arg"
	parser = OptionParser(usage)
	parser.add_option('--cran', nargs=2, dest="cran", help='runs the skeleton on a cran package with parameters: <package> <recipe_dir>')

	(options, args) = parser.parse_args()

	if options.cran != None:
		packageName = options.cran[0]
		recipe_dir = options.cran[1]        
		write_recipe(packageName, recipe_dir)


if __name__ == '__main__':
	main()