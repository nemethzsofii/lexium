# Lexium

**Version:** 1.0.0  
**Author:** Németh Zsófia Réka  
**GitHub:** [https://github.com/nemethzsofii](https://github.com/nemethzsofii)

Lexium is a lightweight professional case handler desktop application built with Python, Flask, and Webview. It provides a friendly GUI interface and automatically manages its database, as well as backups.

---

## System Requirements

- Windows 10 / 11 (64-bit recommended)
- Minimum 200 MB free disk space
- Internet only needed for optional updates

---

## 💾 Installation Guide

### 1. Download

1. Go to the GitHub releases page:  
   [https://github.com/nemethzsofii/Lexium/releases](https://github.com/nemethzsofii/Lexium/releases)
2. Download the latest installer:
   ```
   LexiumSetup.exe
   ```

---

### 2. Run Installer

1. Double-click `LexiumSetup.exe`
2. Choose installation folder (default: `C:\Program Files\Lexium`)
3. Optional: check **Create Desktop Icon**
4. Click **Install**
5. After installation, Lexium will automatically launch

> ⚠️ Make sure **Lexium is closed** before uninstalling or reinstalling

---

## Backup & Restore

Lexium’s database is stored in AppData to keep your data safe.
It automatically gets copied to another location on your computer on every startup. 10 copies remain
at all times.

### Backup

1. Navigate to `C:\Users\<YourUser>\AppData\Local\Lexium\database.db`
2. Copy the file to a safe location (USB, cloud storage, etc.)

### Restore

1. Close Lexium
2. Replace the `database.db` file in AppData with your backup copy
3. Launch Lexium

> This ensures your data is safe if you ever reinstall or update the app

---

## Uninstallation

1. Open **Add/Remove Programs**
2. Select **Lexium** → Click **Uninstall**
3. **Make sure Lexium is closed** during uninstall

> Lexium.exe and Program Files folder will be removed.  
> The database in AppData remains intact for safety.

---

## Shortcuts & Icons

- Desktop shortcut: `Lexium`
- Start Menu shortcut: `Lexium`
- All shortcuts use the Lexium app icon

---

## Troubleshooting

- **App doesn’t start:** Make sure all files were installed correctly. Reinstall if needed.
- **Database missing:** The database is automatically created on first run. Check AppData folder.
- **Uninstaller fails to remove files:** Make sure Lexium is closed before uninstalling.

---

## Future Updates

- Version upgrades through GitHub releases
- More extensive reporting features
- Automatic bill generation

---

### Optional Notes

Have fun using it:)
