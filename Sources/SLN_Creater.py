#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  	: SLN_Creater.py
# Abstract	: To Generate the sln file with the exsited .vcxproj file.
# Author	: Aminor_z
# Date  	: 2020/3/14
import os
from xml.dom.minidom import parse
os.system("title SLN Generator Powered by Aminor_z")
print('请将本程序放置在解决方案文件夹根目录内，\n即按照 【本程序】\\你的项目文件夹\\你的文件.cpp   为标准，\n若您打开本程序未放置在对应目录，关闭即可')
sln_head = """\n
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 16
VisualStudioVersion = 16.0.29806.167
MinimumVisualStudioVersion = 10.0.40219.1"""
sln_end = """
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|x64 = Debug|x64
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(NestedProjects) = preSolution
		{2CE69B07-9F13-4A36-90D6-7A3CC2A1D063} = {84C30512-6E8D-4F12-973C-B5ADE53D44FA}
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {F4A74F44-9BBB-48B2-925E-3F24C6236DD8}
	EndGlobalSection
EndGlobal"""
GUID_project = "{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}"
path=os.path.abspath(os.path.dirname(__file__))
name = input('你想把这个.sln文件叫做什么\n')
if(name==''):
    	print('未读取到生成的文件名，程序退出')
    	exit()
output_position = path+'\\'+name+'.sln'
data = open(output_position, 'w+')
print(sln_head, file=data)
for filename in os.listdir(path):
    _path = path+"\\"+filename+"\\"+filename+".vcxproj"
    if(os.path.exists(_path)):
        _file = open(_path, 'r', encoding='UTF-8')
        domTree = parse(_path)
        rootNode = domTree.documentElement
        _GUID = rootNode.getElementsByTagName(
            "ProjectGuid")[0].childNodes[0].nodeValue
        print('Project("'+GUID_project+'") = "'+filename+'","'+filename +
              '\\'+filename+'.vcxproj"."'+_GUID+'"\nEndProject', file=data)
print(sln_end, file=data)
