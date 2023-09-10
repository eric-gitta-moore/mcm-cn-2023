import matplotlib.pyplot as plt
import subprocess
import os

inkscapePath = r"inkscape"
savePath = r"~"


def exportEmf(plotName, savePath=None, fig=None, keepSVG=True):
    """Save a figure as an emf file

    Parameters
    ----------
    savePath : str, the path to the directory you want the image saved in
    plotName : str, the name of the image
    fig : matplotlib figure, (optional, default uses gca)
    keepSVG : bool, whether to keep the interim svg file
    """
    if savePath is None:
        savePath = ""
    figFolder = savePath + r"{}.{}"
    svgFile = figFolder.format(plotName, "svg")
    emfFile = figFolder.format(plotName, "emf")
    if fig:
        use = fig
    else:
        use = plt
    use.savefig(svgFile)
    subprocess.run([inkscapePath, svgFile, "-M", emfFile])

    if not keepSVG:
        os.system('rm -f "{}"'.format(svgFile))


def convertEmf(path: str) -> str:
    file_name = os.path.basename(path)
    file_name_without_extension, file_extension = os.path.splitext(file_name)
    dir_name = os.path.dirname(path)
    emfFile = f"{dir_name}/{file_name_without_extension}.emf"
    subprocess.run([inkscapePath, path, "-M", emfFile])
    return emfFile
