import os
import shutil

# TODO create GUID

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

print('\n\tGenerating VB project file')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagProjectSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagProjectDestinationFileName)

if not os.path.exists(tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(tagDestinationFolder + pluginProjectName)

tagProjectSource = open(tagSourceFolderPath + tagProjectSourceFileName, 'r')
tagProjectDestination = open(tagDestinationFolder + pluginProjectName + "\\" + tagProjectDestinationFileName, 'w')

while True:
    line = tagProjectSource.readline()

    if line == '':
        break

    if line.strip() == '{classes}':
        tagProjectDestination.write('Class=cla' + pluginName + 'Kernel; Classes\cla' + pluginName + 'Kernel.cls\n')
        tagProjectDestination.write('Class=claErrorsOffsets; Classes\claErrorsOffsets.cls\n')
        tagProjectDestination.write('Class=cla' + pluginName + '; Classes\cla' + pluginName + '.cls\n')
        continue

    if line.strip() == '{forms}':
        tagProjectDestination.write('Form=Forms\\frm' + pluginName + '.frm\n')
        continue

    if line.strip() == '{title}':
        tagProjectDestination.write('Title="' + pluginProjectName + '"\n')
        continue

    if line.strip() == '{exeName}':
        tagProjectDestination.write('ExeName32="' + pluginProjectName + '.dll"\n')
        continue

    if line.strip() == '{name}':
        tagProjectDestination.write('Name="' + pluginProjectName + '"\n')
        continue

    if line.strip() == '{description}':
        tagProjectDestination.write('Description="' + pluginProjectName + '_V1"\n')
        continue

    if line.strip() == '{CompatibleEXE32}':
        tagProjectDestination.write('CompatibleEXE32="..\..\BIN\\' + pluginProjectName + '.dll"\n')
        continue

    if line.strip() == '{VersionFileDescription}':
        tagProjectDestination.write('VersionFileDescription="' + pluginProjectName + '_V1"\n')
        continue

    if line.strip() == '{VersionProductName}':
        tagProjectDestination.write('VersionProductName="' + pluginName + ' Plugin"\n')
        continue

    tagProjectDestination.write(line)

tagProjectSource.close()
tagProjectDestination.close()


tagClaKernelDestinationFileName = 'cla' + pluginName + 'Kernel.cls'
print('\n\tGenerating Kernel class')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagClassesFolderPath + tagClaTagTemplateKernelSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaKernelDestinationFileName)

if not os.path.exists(tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath )

shutil.copyfile(tagSourceFolderPath + tagClassesFolderPath + tagClaTagTemplateKernelSourceFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaKernelDestinationFileName)


tagClaOffsetDestinationFileName = tagClaErrorsOffsetsSourceFileName
print('\n\tGenerating Offset class')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagClassesFolderPath + tagClaErrorsOffsetsSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaOffsetDestinationFileName)

shutil.copyfile(tagSourceFolderPath + tagClassesFolderPath + tagClaErrorsOffsetsSourceFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaOffsetDestinationFileName)


tagClaDestinationFileName = 'cla' + pluginName + '.cls'
print('\n\tGenerating main class')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagClassesFolderPath + tagClaTagTemplateSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaDestinationFileName)

shutil.copyfile(tagSourceFolderPath + tagClassesFolderPath + tagClaTagTemplateSourceFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagClassesFolderPath + tagClaDestinationFileName)


tagFrmDestinationFileName = 'frm' + pluginName + '.frm'
print('\n\tGenerating Forms')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagFormsFolderPath + tagFrmTagTemplateSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagFormsFolderPath + tagFrmDestinationFileName)

if not os.path.exists(tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(tagDestinationFolder + pluginProjectName + '\\' + tagFormsFolderPath)

shutil.copyfile(tagSourceFolderPath + tagFormsFolderPath + tagFrmTagTemplateSourceFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagFormsFolderPath + tagFrmDestinationFileName)


#tagFrmFrxDestinationFileName = 'frm' + pluginName + '.frx'

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagFormsFolderPath + tagFrmTagTemplateFrxSourceFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagFormsFolderPath + tagFrmTagTemplateFrxSourceFileName)

shutil.copyfile(tagSourceFolderPath + tagFormsFolderPath + tagFrmTagTemplateFrxSourceFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagFormsFolderPath + tagFrmTagTemplateFrxSourceFileName)


tagModConstDestinationFileName = tagModConstFileName
print('\n\tGenerating Modules')

print('\t\tSource \t\t\t' + tagSourceFolderPath + tagModulesFolderPath + tagModConstFileName)
print('\t\tDestination \t' + tagDestinationFolder + pluginProjectName + '\\' + tagModulesFolderPath + tagModConstDestinationFileName)

if not os.path.exists(tagDestinationFolder + pluginProjectName + '\\' + tagModulesFolderPath):
    os.makedirs(tagDestinationFolder + pluginProjectName + '\\' + tagModulesFolderPath)

shutil.copyfile(tagSourceFolderPath + tagModulesFolderPath + tagModConstFileName,
                tagDestinationFolder + pluginProjectName + '\\' + tagModulesFolderPath + tagModConstDestinationFileName)