import eel, os

@eel.expose
def parent_dir(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        os.chdir('..')
        return os.getcwd()
    else:
        return 'Not valid folder'

@eel.expose
def enter_dir_and_list_contents(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        return os.listdir(folder)
    else:
        return 'Not valid folder'

@eel.expose
def list_contents_are_directories(folder):
    if os.path.isdir(folder):
        os.chdir(folder)
        types_list = list(map(os.path.isdir, os.listdir(folder)))
        return types_list
    else:
        return 'Not valid folder'


@eel.expose
def get_cwd():
    return os.getcwd()