# LanXing TV Android

Cloud build repository for LanXing TV v1.16.6 (build 292).

## Upload the source archive

Upload this file to the repository root without renaming it:

`lanxing-tv-1.16.6-b292-json-playlist-agp891.zip`

The archive must contain the project folder `lanxing-tv-1.16.6-b292/`.

## Build from GitHub Actions

1. Open the **Actions** tab.
2. Open **Build LanXing TV APK**.
3. Check the latest workflow run.
4. When the workflow succeeds, open the run's **Artifacts** section and download `lanxing-tv-debug-apk`.

The cloud workflow uses JDK 17, Gradle 8.11.1, Android Gradle Plugin 8.10.1, Android SDK Platform 36, and Build Tools 35.0.0. The project keeps minimum SDK 23 (Android 6.0).

The output is an unsigned debug APK intended for device testing, not a signed production release.
