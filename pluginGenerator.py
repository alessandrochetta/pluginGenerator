import os
import shutil
import settings

# TODO create GUID

print('Plug-in generator')

# TODO set plugin name length limit
pluginName = input('\n\tEnter plug-in name: ')
pluginProjectName = 'E2S_' + pluginName
tagProjectDestinationFileName = pluginProjectName + '.vbp'

numberOfParameters = input('\tEnter number of custom parameter (default 2): ')

print('\n\tStarting ' + pluginName + ' plug-in generation...')

print('\n\tGenerating VB project file')

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagProjectSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + tagProjectDestinationFileName)

if not os.path.exists(settings.tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(settings.tagDestinationFolder + pluginProjectName)

tagProjectSource = open(settings.tagSourceFolderPath + settings.tagProjectSourceFileName, 'r')
tagProjectDestination = open(settings.tagDestinationFolder + pluginProjectName + "\\" + tagProjectDestinationFileName, 'w')

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

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaTagTemplateKernelSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaKernelDestinationFileName)

if not os.path.exists(settings.tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath )

shutil.copyfile(settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaTagTemplateKernelSourceFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaKernelDestinationFileName)


tagClaOffsetDestinationFileName = settings.tagClaErrorsOffsetsSourceFileName
print('\n\tGenerating Offset class')

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaErrorsOffsetsSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaOffsetDestinationFileName)

shutil.copyfile(settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaErrorsOffsetsSourceFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaOffsetDestinationFileName)


tagClaDestinationFileName = 'cla' + pluginName + '.cls'
print('\n\tGenerating main class')

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaTagTemplateSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaDestinationFileName)

shutil.copyfile(settings.tagSourceFolderPath + settings.tagClassesFolderPath + settings.tagClaTagTemplateSourceFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagClassesFolderPath + tagClaDestinationFileName)


tagFrmDestinationFileName = 'frm' + pluginName + '.frm'
print('\n\tGenerating Forms')

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagFormsFolderPath + settings.tagFrmTagTemplateSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagFormsFolderPath + tagFrmDestinationFileName)

if not os.path.exists(settings.tagDestinationFolder + tagProjectDestinationFileName):
    os.makedirs(settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagFormsFolderPath)

shutil.copyfile(settings.tagSourceFolderPath + settings.tagFormsFolderPath + settings.tagFrmTagTemplateSourceFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagFormsFolderPath + tagFrmDestinationFileName)


#tagFrmFrxDestinationFileName = 'frm' + pluginName + '.frx'

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagFormsFolderPath + settings.tagFrmTagTemplateFrxSourceFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagFormsFolderPath + settings.tagFrmTagTemplateFrxSourceFileName)

shutil.copyfile(settings.tagSourceFolderPath + settings.tagFormsFolderPath + settings.tagFrmTagTemplateFrxSourceFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagFormsFolderPath + settings.tagFrmTagTemplateFrxSourceFileName)


tagModConstDestinationFileName = settings.tagModConstFileName
print('\n\tGenerating Modules')

print('\t\tSource \t\t\t' + settings.tagSourceFolderPath + settings.tagModulesFolderPath + settings.tagModConstFileName)
print('\t\tDestination \t' + settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagModulesFolderPath + tagModConstDestinationFileName)

if not os.path.exists(settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagModulesFolderPath):
    os.makedirs(settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagModulesFolderPath)

shutil.copyfile(settings.tagSourceFolderPath + settings.tagModulesFolderPath + settings.tagModConstFileName,
                settings.tagDestinationFolder + pluginProjectName + '\\' + settings.tagModulesFolderPath + tagModConstDestinationFileName)