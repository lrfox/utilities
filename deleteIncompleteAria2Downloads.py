# Used for aria2 downloads that did not complete
# Goes through directory and subdirectories deleting .aria2 files 
# and corresponding incomplete downloaded file.
import os

totalCount = 0

print("\n")

for root, dirs, files in os.walk("./target"):
    count = 0
    for file in files:
        if file.endswith(".aria2"):
             count += 1
             targetPathFile = os.path.join(root, file)
             os.remove(targetPathFile)
             os.remove(targetPathFile.replace(".aria2",""))
             folderNameWithIncompletes = root.rsplit('\\',1)[-1]
    if (count > 0):
        print('\tPictures deleted: {0} (Files deleted: {1}) for {2}'.format(count, count*2, folderNameWithIncompletes))
        totalCount += count

print("\n\t Total pictures deleted: {0} (Files deleted: {1})".format(totalCount, totalCount*2))
