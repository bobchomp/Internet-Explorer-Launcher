# IE Launcher

A simple Windows utility that opens URLs in legacy Internet Explorer using COM automation, bypassing the modern redirect to Microsoft Edge.

## Usage

1. Download `IELauncher-Setup.exe` from the [latest release](../../releases/latest) and install it, or grab the portable `IELauncher.exe`
2. Enter a URL in the text box
3. Click **Open in Internet Explorer** (or press Enter)

## Building from source

Requires Python 3.11+ and [Inno Setup](https://jrsoftware.org/isinfo.php).

```
pip install pyinstaller pywin32
pyinstaller --onefile --windowed --name IELauncher ielauncher.py
iscc "/DAppVersion=1.0.0" installer.iss
```

Or trigger the **Build IE Launcher** GitHub Actions workflow with a version number — it will produce both a portable exe and a full installer attached to a GitHub release.

## Requirements

- Windows with Internet Explorer still present (legacy IE is disabled but still ships on Windows 10/11)
- The COM object `InternetExplorer.Application` must be available

## License

MIT — see [LICENSE](LICENSE)
