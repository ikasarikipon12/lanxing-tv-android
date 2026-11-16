# LanXing TV Android

Cloud build repository for LanXing TV v1.16.6.

## Source archive

The original project archive is kept unchanged at the repository root:

`lanxing-tv-1.16.6-b292-json-playlist-agp891.zip`

## English test build

The GitHub Actions workflow applies an English localization patch during the cloud build. It translates the app's default strings, visible layout labels, and Kotlin/Java UI messages, and forces the app locale to English.

The English test APK uses a separate application ID suffix (`.english`) so it can be installed alongside the previous Chinese test app without uninstalling it. Its app label is **LanXing TV English**.

If you want to move playlist settings from the older app, export a backup from the old app to shared storage, then use **Settings → Backup / Restore → Restore Settings** in the English app. App-private settings are not copied automatically between the two package IDs.

## Build environment

- JDK 17
- Gradle 8.11.1
- Android Gradle Plugin 8.10.1
- Android SDK Platform 36
- Android Build Tools 35.0.0
- Minimum Android version: 6.0 (API 23)

The workflow produces a debug-signed APK for testing, not a production-signed release.
