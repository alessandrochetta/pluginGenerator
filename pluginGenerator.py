import os

# Settings - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# - - - Source
# - - - - - - Tag Template Source
#
tagSourceFolderPath = 'Templates\E2S_TagTemplate\\'
tagProjectSourceFileName = 'E2S_TagTemplate.vbp'
#
# - - - - - - - - - Classes
#
tagClassesFolderPath = 'Classes\\'
tagClaErrorsOffsetsSourceFileName = 'claErrorsOffsets.cls'
tagClaTagTemplateSourceFileName = 'claTagTemplate.cls'
tagClaTagTemplateKernelSourceFileName = 'claTagTemplateKernel.cls'
#
# - - - - - - - - - Forms
#
tagFormsFolderPath = 'Forms\\'
tagFrmTagTemplateSourceFileName = 'frmTagTemplate.frm'
tagFrmTagTemplateFrxSourceFileName = 'frmTagTemplate.frx'
#
# - - - - - - - - - Modules
#
tagModulesFolderPath = 'Modules\\'
tagModConstFileName = 'ModConst.bas'
#
# - - - Destination
#
tagDestinationFolder = 'generated_plug-ins\\tags\\'

print('Plug-in generator')

# TODO set plugin name length limit
pluginName = input('\n\tEnter plug-in name: ')
pluginProjectName = 'E2S_' + pluginName
tagProjectDestinationFileName = pluginProjectName + '.vbp'

numberOfParameters = input('\tEnter number of custom parameter (default 2): ')

print('\n\tStarting ' + pluginName + ' plug-in generation...')

print('\n\tGenerating VB project file plug-in generation...')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagProjectSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + tagProjectDestinationFileName)

if not os.path.exists(tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(tagDestinationFolder + pluginProjectName)

tagProjectSource = open(tagSourceFolderPath + tagProjectSourceFileName, 'r')
tagProjectDestination = open(tagDestinationFolder + pluginProjectName + "\\" + tagProjectDestinationFileName, 'w')

while True:
    line = tagProjectSource.readline()
    print(line)

    if line == '':
        break

    if line.strip() == '{classes}':
        tagProjectDestination.write('Class = cla' + pluginProjectName + 'Kernel; Classes\cla' + pluginProjectName + 'Kernel.cls\n')
        tagProjectDestination.write('Class = claErrorsOffsets; Classes\claErrorsOffsets.cls\n')
        tagProjectDestination.write('Class = cla' + pluginProjectName + '; Classes\cla' + pluginProjectName + '.cls\n')
        continue

    if line.strip() == '{forms}':
        tagProjectDestination.write('Form = Forms\\frm' + pluginProjectName + '.frm\n')
        continue

    if line.strip() == '{title}':
        tagProjectDestination.write('Title = "' + pluginProjectName + '"\n')
        continue

    tagProjectDestination.write(line)

tagProjectSource.close()
tagProjectDestination.close()




