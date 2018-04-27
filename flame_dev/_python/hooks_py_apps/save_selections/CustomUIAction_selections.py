
# (c) Stefan Gaillot
# Venice, CA 90291
# 2017/11/03

from PySide.QtGui import QApplication
import sys

# UI
import save_Load_selections_UI_04c
reload(save_Load_selections_UI_04c)
from save_Load_selections_UI_04c import SelectionsWidget

# inherit absolute part of the path from the __init__.py file
from __init__ import get_absolute_path_part
ROOT_PATH = get_absolute_path_part()

# Modules Paths
#sys.path.append('/opt/flame_dev/_python/modules')
sys.path.append("{root}/_python/modules".format(root=ROOT_PATH))


# Contextuel Menu Entry
def getCustomUIActions():

    action1 = {}
    action1["name"] = "nodes_selection"
    action1["caption"] = "v01"

    appGroup1 = {}
    appGroup1["name"] = "Selections"
    appGroup1["actions"] = (action1,)

    return (appGroup1,)


def customUIAction(info, userData):
    if info['name'] == 'nodes_selection':
        import flame

        def get_selection():
            import flame
            return ["" + s.name + "" for s in flame.batch.selected_nodes.get_value()]

        #yamlpath = '/opt/flame_dev/_python/hooks_py_apps/save_selections/saved_nodes.yaml'
        yamlpath = "{root}/_python/hooks_py_apps/save_selections/saved_nodes.yaml".format(root=ROOT_PATH)

    #############################################

        app = QApplication.activePopupWidget()
        # we call 'save_Load_selections_UI_04c.py' giving it 2 args:
        # -> the path to the yaml file and the selected nodes list
        form = SelectionsWidget(path=yamlpath, graphSelected=get_selection)
        form.show()
        app.exec_()
