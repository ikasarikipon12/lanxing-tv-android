# LanXing TV Android

Cloud build repository for LanXing TV v1.16.6 (build 292).

## Build from GitHub Actions

1. Upload `lanxing-tv-1.16.6-b292-json-playlist-agp891.zip` to the repository root.
2. Open the **Actions** tab.
3. Open **Build LanXing TV APK** and check the latest run.
4. When the workflow succeeds, open the run's **Artifacts** section and download `lanxing-tv-debug-apk`.

The workflow builds the debug APK for Android devices with minimum SDK 23 (Android 6.0), using JDK 17, Gradle 8.11.1, Android Gradle Plugin 8.9.1, and compile SDK 36.

The APK is an unsigned debug build intended for testing.