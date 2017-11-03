import skeleton_helper as sh
import subprocess as sp
def main():
    with open('packages_to_process.txt', 'r') as file:
        for line in file.readlines():
            try:
                sh.write_recipe(line[2:-1], 'recipes')
                handleGithub(line)
            except FileNotFoundError as e:
                print("Could not find {} on cran".format(line))

def handleGithub(package):
    sp.call('git pull upstream master', shell=True)
    sp.call('git checkout -b ' + package)
    sp.call('git add recipes/' + package)
    sp.call('git commit -m \"added ' + package + '\"')
    sp.call('git push origin ' + package)


if __name__=="__main__":
    main()

