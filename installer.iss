[Setup]
AppName=IE Launcher
AppVersion={#AppVersion}
AppPublisher=Ross Mackenzie
DefaultDirName={autopf}\IELauncher
DefaultGroupName=IE Launcher
OutputBaseFilename=IELauncher-Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\IELauncher.exe

[Files]
Source: "dist\IELauncher.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\IE Launcher"; Filename: "{app}\IELauncher.exe"
Name: "{commondesktop}\IE Launcher"; Filename: "{app}\IELauncher.exe"

[Run]
Filename: "{app}\IELauncher.exe"; Description: "Launch IE Launcher"; Flags: nowait postinstall skipifsilent
