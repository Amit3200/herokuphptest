Option Explicit
Dim objWMIService, objComputer, colComputer 
Dim strLogonUser, strComputer 

strComputer = "." 

Set objWMIService = GetObject("winmgmts:" _
& "{impersonationLevel=impersonate}!\\" _ 
& strComputer & "\root\cimv2") 
Set colComputer = objWMIService.ExecQuery _
("Select * from Win32_ComputerSystem") 

For Each objComputer in colComputer 
Wscript.Echo "System Name: " & objComputer.Name _
& vbCr & "Total RAM " & objComputer.TotalPhysicalMemory
Next 

WScript.Quit 