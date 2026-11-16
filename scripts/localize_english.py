from pathlib import Path
import re

PROJECT = Path("source/lanxing-tv-1.16.6-b292")
MAIN = PROJECT / "app/src/main"
D = chr(36)

resource_translations = {
    "app_name": "LanXing TV",
    "settings": "Settings",
    "playlist_url": "Playlist URL (one per line; multiple sources supported)",
    "source_manage_hint": "Enter one playlist URL per line (.m3u/.m3u8/.txt). Save to switch sources from the list at the top.",
    "epg_url": "TV Guide URL (EPG/XMLTV)",
    "epg_url_hint": "Enter one EPG URL per line. Multiple URLs will be merged.",
    "load": "Load",
    "loading_playlist": "Loading playlist…",
    "load_failed": "Failed to load. Check the URL.",
    "no_channels": "No channels found",
    "no_channels_guide": r"No playlist source added\nPress Menu on the remote to open Settings → Sources\nOr scan the QR code with your phone to add a source",
    "saved": "Saved",
    "save_sources_hint": "The current source refreshes automatically after saving.",
    "current_source": "Current source",
    "switch_source": "Switch source",
    "source_updated": "Last updated",
    "source_never": "Never updated",
    "source_switch_hint": "Press OK to switch sources · Back to continue channel selection",
    "scan_manage": "QR Code Management (Add Sources by Phone)",
    "scan_manage_hint": "Connect your phone and TV box to the same Wi-Fi. Scan the QR code with your browser to open the management page and add or switch playlist sources or configure the TV guide.",
    "scan_qr_title": "Scan with your phone to open the management page",
    "scan_no_wifi": "Local network address not found. Check that the TV box is connected to the internet.",
    "scan_server_off": "Local network management service is not running",
    "search_hint": "Search channels…",
    "favorites": "Favorites",
    "favorites_only": "Favorites only",
    "all_channels": "All channels",
    "now": "Now",
    "next": "Next",
    "no_epg": "No program information",
    "channel_list": "Channel list",
    "favorite_hint": "Favorite",
    "channel_logo": "Channel logo",
    "play_pause": "Play/Pause",
    "stop": "Stop",
    "prev_channel": "Previous channel",
    "next_channel": "Next channel",
    "clear_favorites": "Clear favorites",
    "favorite_toggle": "Favorite or unfavorite current channel",
    "favorite_added": "Added to favorites: %1$s",
    "favorite_removed": "Removed from favorites: %1$s",
    "import_local_file": "Import local file (supports .m3u / .m3u8 / .txt)",
    "choose_file": "Choose file",
    "direct_stream": "Play a direct stream URL",
    "direct_stream_hint": "No playlist needed. Enter a single live stream URL to play.",
    "play_direct": "Play",
    "importing": "Reading file…",
    "playback_options": "Playback options",
    "aspect_ratio": "Aspect ratio",
    "aspect_fit": "Original",
    "aspect_16_9": "16:9",
    "aspect_4_3": "4:3",
    "aspect_zoom": "Zoom crop (fill screen)",
    "aspect_fill": "Stretch to full screen",
    "auto_resume": "Resume the last channel when opening the app",
    "decoder_mode": "Decoder mode",
    "decoder_auto": "Auto (hardware preferred, fallback if needed)",
    "decoder_hardware": "Hardware decoding only",
    "decoder_software": "Software decoding only",
    "nav_lineup": "Stream selection",
    "current_line": "Current stream",
    "switch_line": "Press OK to switch stream",
    "line_fmt": "Stream %1$d/%2$d",
    "line_switch_hint": "Multiple sources for the same channel are merged. Switch manually during playback or automatically after a timeout.",
    "btn_switch_line": "Switch source",
    "nav_timeout": "Source timeout",
    "switch_timeout": "Stream startup timeout (seconds)",
    "switch_timeout_hint": "If the current stream does not start within the selected time, the app switches to the next stream.",
    "nav_prefs": "Preferences",
    "pref_show_clock": "Show clock",
    "pref_show_speed": "Show network speed",
    "pref_reverse_zap": "Reverse channel order",
    "pref_cross_category": "Switch across categories",
    "pref_reverse_zap_hint": "Reverse the channel order when using the Up/Down keys.",
    "pref_cross_category_hint": "When disabled, channel switching stays within the current category.",
    "nav_exit": "Exit live TV",
    "exit_confirm": "Exit LanXing TV? All app processes will be stopped.",
    "exit_hint": "Exit and stop all app processes. No background audio will remain.",
    "auto_hide_overlay": "Automatically hide the info bar and buttons when idle",
    "ui_hint": "When disabled, the info bar and bottom buttons stay visible.",
    "nav_source": "Sources",
    "nav_player": "Player",
    "nav_ui": "Interface",
    "nav_fav": "Favorites",
    "nav_update": "Updates",
    "nav_debug": "Diagnostics",
    "about": "About",
    "close": "Close",
    "cleared": "Cleared",
    "playback_hint": "Arrow keys: change channel · OK: channel list · Menu: settings",
    "current_version": "Current version",
    "check_update": "Check for updates",
    "checking_update": "Checking for updates…",
    "update_latest": "You are up to date",
    "update_found": "New version found. Downloading…",
    "update_downloading": "Downloading %1$d%%",
    "update_done": "Download complete. Installing…",
    "update_failed": "Update failed: %1$s",
    "update_install_hint": "The system installer opens automatically after download. Confirm to upgrade. Your settings and favorites will be kept.",
    "crash_log": "Runtime log (for startup and playback troubleshooting)",
    "clear_crash_log": "Clear runtime log",
    "cleared_crash_log": "Runtime log cleared",
    "export_crash_log": "Export runtime log (.txt)",
    "exported": "Exported",
    "export_empty": "Runtime log is empty. Nothing to export.",
    "fav_count": "%1$d channels favorited",
    "backup_config": "Backup settings",
    "restore_config": "Restore settings",
    "backup_done": "Settings backed up",
    "backup_failed": "Backup failed: %1$s",
    "restore_done": "Settings restored. Reloading…",
    "restore_failed": "Restore failed: %1$s",
    "restore_confirm": "Restoring will overwrite your current sources, EPG URLs, favorites, and preferences. Continue?",
    "restore_invalid": "Invalid backup file format",
}

# Replace the app's default resource language, so English is used even on a Chinese-language TV box.
strings_file = MAIN / "res/values/strings.xml"
xml_text = strings_file.read_text(encoding="utf-8")
resource_pattern = re.compile(r'(<string\s+name="([^"]+)"[^>]*>)(.*?)(</string>)')
seen_resources = set()
def translate_resource(match):
    name = match.group(2)
    if name in resource_translations:
        seen_resources.add(name)
        return match.group(1) + resource_translations[name] + match.group(4)
    return match.group(0)
xml_text = resource_pattern.sub(translate_resource, xml_text)
missing_resources = sorted(set(resource_translations) - seen_resources)
if missing_resources:
    raise SystemExit("Missing string resources: " + ", ".join(missing_resources))
strings_file.write_text(xml_text, encoding="utf-8")

# Text hard-coded in Kotlin/Java. Match complete string literals to avoid changing comments or identifiers.
code_translations = {
    "开机启动": "Startup",
    "开机后提醒打开揽星TV": "Reminder to open LanXing TV after startup",
    "揽星TV 已就绪": "LanXing TV is ready",
    "按 OK 打开继续观看": "Press OK to open and continue watching",
    "定时关机时间到，即将退出": "Sleep timer expired. Exiting…",
    r"\n网速 ": r"\nSpeed ",
    "未另存到其他位置（备份仍在应用目录）": "Not saved elsewhere (the backup remains in the app folder).",
    "已取消恢复": "Restore canceled.",
    "还没有开启安装授权，无法更新": "Install permission is not enabled. Cannot update.",
    "启动失败（已记录日志）": "Startup failed (log saved).",
    r"请把此弹窗截图发给开发者，或在设置→调试中查看完整日志：\n\n": r"Please send a screenshot of this dialog to the developer, or view the full log in Settings > Diagnostics:\n\n",
    "知道了": "Got it",
    "检测到硬解解码器异常：如播放黑屏/无声，请重启机顶盒": "A hardware decoder issue was detected. If playback is black or silent, restart the TV box.",
    r"运行日志（可在 设置-调试 中导出）：\n$brief": r"Runtime log (export from Settings > Diagnostics):\n$brief",
    "当前频道只有 1 条线路": "This channel has only one stream.",
    "暂无直播源，请在下方添加（长按可删除）": "No playlist sources. Add one below (long-press to delete).",
    "●正常 " + D + "{health.latencyMs}ms": "● Good " + D + "{health.latencyMs} ms",
    "●较慢 " + D + "{health.latencyMs}ms": "● Slow " + D + "{health.latencyMs} ms",
    "●不可用": "● Unavailable",
    "○未检测": "○ Not tested",
    "源 ": "Source ",
    "：源 ": ": Source ",
    "删除直播源": "Delete playlist source",
    "确定删除源 ": "Delete source ",
    "）吗？": ")?",
    "删除": "Delete",
    "取消": "Cancel",
    "未配置直播源，请在设置中添加": "No playlist source configured. Add one in Settings.",
    "：未配置（OK 进设置添加）": ": Not configured (press OK to open Settings)",
    "直播源 ": "Playlist source ",
    " · OK 切换": " · Press OK to switch",
    "  ·  OK 切换": "  ·  Press OK to switch",
    "手机已保存 ": "Saved on phone: ",
    " 个直播源，正在刷新…": " playlist sources saved. Refreshing…",
    "添加直播源": "Add playlist source",
    "输入 M3U/TXT 播放列表 URL（每行一个，支持多个）": "Enter M3U/TXT playlist URLs (one per line; multiple sources supported).",
    "添加": "Add",
    "请输入有效的 URL": "Enter a valid URL.",
    "已添加 " + D + "{urls.size} 个直播源": "Added " + D + "{urls.size} playlist sources.",
    "https://example.com/epg.xml（可选，每行一个）": "https://example.com/epg.xml (optional, one per line)",
    "节目单地址（EPG）": "EPG URL",
    "输入 EPG XML/XML.GZ 地址（可选，每行一个，自动降级）": "Enter EPG XML/XML.GZ URLs (optional, one per line; automatic fallback).",
    "保存并加载": "Save and load",
    "节目单已保存，正在加载...": "EPG saved. Loading…",
    "已清除节目单地址": "EPG URL cleared.",
    "节目单缓存已清除": "EPG cache cleared.",
    "未设置（按 OK 输入）": "Not set (press OK to enter)",
    "开": "On",
    "关": "Off",
    "节目单刷新频率：" + D + "{if (hours >= 24) ": "EPG refresh interval: " + D + "{if (hours >= 24) ",
    "每天": "Daily",
    "每" + D + "{hours}小时": "Every " + D + "{hours} hours",
    r"请用手机（与机顶盒同一 Wi-Fi）扫描：\n$url\n\n可添加/切换直播源、设置节目指南、直接播放": r"Scan with your phone (connected to the same Wi-Fi as the TV box):\n$url\n\nYou can add or switch sources, configure the TV guide, or play a stream directly.",
    "无法打开文件选择器（系统无文件管理），请改用播放列表 URL 加载": "Cannot open the file picker (no file manager installed). Load a playlist URL instead.",
    "未配置直播源": "No playlist source configured.",
    "正在刷新当前源...": "Refreshing current source…",
    "暂无直播源": "No playlist sources.",
    "检测中...": "Checking…",
    "一键测速": "Speed test",
    "已自动切换到最快源（源" + D + "{fastestIdx + 1}）": "Switched to the fastest source (source " + D + "{fastestIdx + 1}).",
    "测速完成，当前已是最快源": "Speed test complete. This is already the fastest source.",
    "测速完成：" + D + "{available}/" + D + "{results.size} 个源可用": "Speed test complete: " + D + "{available}/" + D + "{results.size} sources available.",
    "已开启自动优选": "Automatic fastest-source selection enabled.",
    "已关闭自动优选": "Automatic fastest-source selection disabled.",
    D + "{next}分钟后自动关机": "Auto shutdown in " + D + "{next} minutes.",
    "定时关机已取消": "Sleep timer canceled.",
    "定时关机：关闭": "Sleep timer: Off",
    "定时关机：" + D + "{minutes}分钟": "Sleep timer: " + D + "{minutes} minutes",
    "开机自启动已开启": "Start on boot enabled.",
    "开机自启动已关闭": "Start on boot disabled.",
    "无": "None",
    r"\n播放内核：Media3 ExoPlayer（开源）": r"\nPlayback engine: Media3 ExoPlayer (open source)",
    r"\n代码仓库：https://github.com/cyj265/lanxing-tv": r"\nSource code: https://github.com/cyj265/lanxing-tv",
    r"\n开源许可：Apache-2.0 / MIT / GPL-2.0": r"\nOpen-source licenses: Apache-2.0 / MIT / GPL-2.0",
    r"\n部分源码来自开源项目（详见仓库 README 来源致谢）": r"\nSome code comes from open-source projects (see README acknowledgements).",
    "已删除直播源": "Playlist source deleted.",
    "已配置 ": "Configured ",
    " 个直播源": " playlist sources",
    r"\n当前源：": r"\nCurrent source: ",
    r"\n当前源：未配置": r"\nCurrent source: Not configured",
    r"\n节目指南：": r"\nTV guide: ",
    "未设置": "Not set",
    " 个地址": " URLs",
    "（已加载 ": "(Loaded ",
    " 条节目）": " programs)",
    "读取失败": "Read failed",
    "无法打开保存窗口：" + D + "{e.message}": "Cannot open save dialog: " + D + "{e.message}",
    "已导出到：" + D + "{outFile.absolutePath}": "Exported to: " + D + "{outFile.absolutePath}",
    "导出失败：" + D + "{e.message}": "Export failed: " + D + "{e.message}",
    "无法写入目标位置，请重试或选择其他位置": "Cannot write to the selected location. Try again or choose another location.",
    "备份完成": "Backup complete",
    r"已保存到：\n" + D + "{saved.absolutePath}" + r"\n\n": r"Saved to:\n" + D + "{saved.absolutePath}" + r"\n\n",
    r"恢复时点「恢复配置」，直接在列表里选这份备份。\n": r"To restore, select Restore Settings and choose this backup from the list.\n",
    "注意：卸载应用会一并删除此文件。": "Note: uninstalling the app will also delete this file.",
    "完成": "Done",
    "另存到其他位置": "Save to another location",
    "此设备没有可用的文件选择器，备份仍在应用目录": "No file picker is available on this device. The backup remains in the app folder.",
    "未知错误": "Unknown error",
    "已另存到所选位置": "Saved to the selected location.",
    "选择备份": "Choose backup",
    "未找到备份文件，请先点「备份配置」生成备份": "No backup file found. Select Backup Settings first to create one.",
    "选择要恢复的备份": "Select a backup to restore",
    "从其他位置选择": "Choose from another location",
    "此设备没有可用的文件选择器": "No file picker is available on this device.",
    "这份备份是空文件，请重新点「备份配置」": "This backup file is empty. Create a new backup.",
    " 秒": " sec",
    "换源超时：$sec 秒": "Source switch timed out: $sec sec",
    "揽星TV v" + D + "tag (构建 #" + D + "latestBuild) 已发布" + r"\n": "LanXing TV v" + D + "tag (build #" + D + "latestBuild) is available" + r"\n",
    "当前版本：v" + D + "{BuildConfig.VERSION_NAME} (构建 #" + D + "{BuildConfig.BUILD_NUMBER})": "Current version: v" + D + "{BuildConfig.VERSION_NAME} (build #" + D + "{BuildConfig.BUILD_NUMBER})",
    r"\n\n本次更新：\n$notes": r"\n\nWhat's new:\n$notes",
    r"\n\n是否立即更新？": r"\n\nUpdate now?",
    "网络错误": "Network error",
    "发现新版本": "New version available",
    "立即更新": "Update now",
    "直连": "Direct",
    "加速": "Accelerated",
    "线路" + D + "{idx+1}": "Line " + D + "{idx+1}",
    "正在" + D + "urlName 下载...": "Downloading from " + D + "urlName…",
    "正在下载...": "Downloading…",
    D + "name 下载中 " + D + "p%": D + "name: Downloading " + D + "p%",
    "下载中 " + D + "p%": "Downloading " + D + "p%",
    "下载失败": "Download failed",
    D + "{urlName}失败（" + D + "{lastError}），切换" + D + "{urlNames[idx+1]}...": D + "{urlName} failed (" + D + "{lastError}). Switching to " + D + "{urlNames[idx+1]}…",
    "所有线路均下载失败": "All download routes failed.",
    "无法打开安装器：" + D + "{e.message}": "Cannot open installer: " + D + "{e.message}",
    "需要授权安装更新": "Permission required to install updates",
    "Android 要求先允许本应用安装更新包。" + r"\n\n": "Android requires permission to install updates." + r"\n\n",
    "点「去授权」后在系统页面打开「允许来自此来源的应用」，": "Select Go to Settings, then enable Allow from this source on the system page.",
    "返回本应用即可继续安装。": "Return to the app to continue installation.",
    "去授权": "Go to Settings",
    "无法打开授权页面：" + D + "{e.message}": "Cannot open permission page: " + D + "{e.message}",
    "无法弹出授权提示：" + D + "{e.message}": "Cannot show permission prompt: " + D + "{e.message}",
    "缩放": "Zoom",
    "填充": "Fill",
    "适应": "Fit",
    "画面比例：" + D + "label": "Aspect ratio: " + D + "label",
    "已从播放列表自动识别节目单地址": "EPG URL detected automatically from the playlist.",
    "列表渲染失败": "Failed to render list.",
    "（已用缓存）": "(Using cached data)",
    " 个频道": " channels",
    "直接播放": "Play URL",
    "极清": "8K",
    "超清": "Ultra HD",
    "高清": "HD",
    "标清": "SD",
    "流畅": "Smooth",
    "原画": "Original",
    "蓝光": "Blu-ray",
    "当前没有正在播放的频道": "No channel is currently playing.",
    "请先把焦点移到要收藏的频道": "Move focus to the channel you want to favorite first.",
    "节目指南加载失败": "Failed to load TV guide.",
    "节目指南加载成功（": "TV guide loaded (",
    "未选择频道": "No channel selected.",
    "请先选择频道": "Please select a channel first.",
    "剩余" + D + "{remainingMin}分钟": D + "{remainingMin} minutes remaining",
    "即将结束": "Ending soon",
    "暂无节目单（请在设置中添加节目指南）": "No TV guide available (add an EPG in Settings).",
    "节目指南加载中…": "Loading TV guide…",
    "该时段暂无节目": "No program scheduled for this time.",
    " · " + D + "{lineCount}条线路": " · " + D + "{lineCount} streams",
    "第 ": "No. ",
    " 频道": " channel",
    "分辨率 ": "Resolution ",
    "剩余 " + D + "{remainingMin} 分钟": D + "{remainingMin} min remaining",
    "正在播放: " + D + "{current.title}  [$startStr-$endStr]  $remainingStr": "Now playing: " + D + "{current.title} [$startStr-$endStr] $remainingStr",
    "稍后 " + D + "{formatTime(next.start)}-" + D + "{formatTime(next.end)}  " + D + "{next.title}": "Next: " + D + "{formatTime(next.start)}-" + D + "{formatTime(next.end)} " + D + "{next.title}",
    "线路 " + D + "{playback.currentSourceIndex() + 1}/$srcCount: $message": "Line " + D + "{playback.currentSourceIndex() + 1}/$srcCount: $message",
    "播放失败: $message": "Playback failed: $message",
    "再按一次返回键退出": "Press Back again to exit.",
    "退出揽星TV": "Exit LanXing TV",
    "确定要退出应用吗？": "Are you sure you want to exit the app?",
    "退出": "Exit",
    "全部": "All",
    "未分组": "Ungrouped",
    "频道 " + D + "{index + 1}": "Channel " + D + "{index + 1}",
    "本地列表": "Local playlist",
    "正常": "Good",
    "较慢": "Slow",
    "不可用": "Unavailable",
    "未检测": "Not tested",
    "播放中断（线路 " + D + "{currentSourceIndex + 1}），请手动换线路或重新打开": "Playback interrupted (line " + D + "{currentSourceIndex + 1}). Switch streams manually or reopen the channel.",
    "线路 " + D + "{currentSourceIndex + 1} 播放失败": "Playback failed on line " + D + "{currentSourceIndex + 1}.",
    "解码器初始化失败，500ms 后自动重试…": "Decoder initialization failed. Retrying in 500 ms…",
    "视频渲染失败，" + D + "{renderRetryCount}/2 自动重试…": "Video rendering failed. Retrying (" + D + "{renderRetryCount}/2)…",
    "解码失败：硬解/软解均无法播放，请尝试更换清晰度或重启机顶盒": "Decoding failed. Try another quality setting or restart the TV box.",
    "硬解失败，正在检测解码器状态…": "Hardware decoding failed. Checking decoder status…",
    "解码器异常，请重启机顶盒后重试（已临时切换软解）": "Decoder error. Restart the TV box and try again (software decoding enabled temporarily).",
    "硬解失败，已切换软件解码": "Hardware decoding failed. Switched to software decoding.",
    "解码失败（" + D + "{error.errorCodeName}），请尝试切换解码方式或重启机顶盒": "Decoding failed (" + D + "{error.errorCodeName}). Try another decoder mode or restart the TV box.",
    "播放失败，" + D + "{retryCount} 秒后自动重试…": "Playback failed. Retrying in " + D + "{retryCount} seconds…",
    "该频道没有可用线路": "No available streams for this channel.",
    "已切换到线路 " + D + "{currentSourceIndex + 1}/" + D + "{currentSources.size}": "Switched to stream " + D + "{currentSourceIndex + 1}/" + D + "{currentSources.size}.",
    "所有线路均播放失败，请检查网络或手动换源": "All streams failed. Check your network or switch sources manually.",
    "未保存：请至少填写一个有效的直播源地址（http 开头）": "Not saved: Enter at least one valid playlist URL (starting with http).",
    "已保存 ": "Saved ",
    " 个直播源，机顶盒正在刷新播放列表…<br>你可以关闭本页面了。": " playlist sources. The TV box is refreshing the playlist…<br>You can close this page.",
    "未播放：请输入有效的直播流地址（http 开头）": "Not playing: Enter a valid stream URL (starting with http).",
    "已开始播放，返回机顶盒即可观看。": "Playback started. Return to the TV box to watch.",
    D + "reason，自动切换线路 " + D + "{currentSourceIndex + 1}/" + D + "{currentSources.size}": D + "reason. Switching to stream " + D + "{currentSourceIndex + 1}/" + D + "{currentSources.size}.",
    "线路 " + D + "{currentSourceIndex + 1} 起播超时（" + D + "{sourceTimeoutMs / 1000}s）": "Stream " + D + "{currentSourceIndex + 1} timed out while starting (" + D + "{sourceTimeoutMs / 1000}s).",
    r"\n========== 播放错误 ": r"\n========== Playback Error ",
    r"========== 结束 ==========\n": r"========== End ==========\n",
    D + "count 个频道": D + "count channels",
}

layout_translations = {
    "正在播放": "Now Playing",
    "今日节目单": "Today's TV Guide",
    "📺 直播源": "📺 Sources",
    "📅 节目单": "📅 TV Guide",
    "🔲 画面比例": "🔲 Aspect Ratio",
    "🎬 解码器": "🎬 Decoder",
    "⏱️ 超时换源": "⏱️ Source Timeout",
    "⚙️ 偏好设置": "⚙️ Preferences",
    "🔄 检查更新": "🔄 Check for Updates",
    "🐛 调试设置": "🐛 Diagnostics",
    "💾 备份恢复": "💾 Backup / Restore",
    "ℹ️ 关于": "ℹ️ About",
    "🚪 退出": "🚪 Exit",
    "当前直播源": "Current playlist source",
    "按 OK 切换到下一个源": "Press OK to switch to the next source",
    "直播源列表（OK切换，长按删除）": "Playlist sources (OK to switch, long-press to delete)",
    "一键测速": "Speed test",
    "自动优选最快源": "Automatically select the fastest source",
    "关": "Off",
    "刷新当前源（立即更新列表）": "Refresh current source (update the list now)",
    "添加直播源（URL）": "Add playlist source (URL)",
    "导入本地 M3U/TXT 文件": "Import local M3U/TXT file",
    "手机扫码管理（局域网）": "Manage by phone (local network QR code)",
    "节目单地址（EPG，可选）": "TV guide URL (EPG, optional)",
    "未设置（按 OK 输入）": "Not set (press OK to enter)",
    "显示节目信息": "Show program information",
    "开": "On",
    "刷新频率": "Refresh interval",
    "每小时": "Every hour",
    "每2小时": "Every 2 hours",
    "每天": "Daily",
    "清除节目单缓存": "Clear TV guide cache",
    "适应": "Fit",
    "缩放": "Zoom",
    "填充": "Fill",
    "5 秒": "5 sec",
    "10 秒": "10 sec",
    "15 秒": "15 sec",
    "20 秒": "20 sec",
    "25 秒": "25 sec",
    "30 秒": "30 sec",
    "60 秒": "60 sec",
    "记住上次分组": "Remember the last group",
    "定时关机：关闭": "Sleep timer: Off",
    "点击切换：关闭 → 30分钟 → 60分钟 → 90分钟": "Click to cycle: Off → 30 min → 60 min → 90 min",
    "开机自启动": "Launch on startup",
    "盒子开机后自动启动揽星TV": "Start LanXing TV when the box boots",
    "无": "None",
    "备份包含直播源、节目单地址、收藏与全部偏好。备份默认保存在应用目录，卸载应用会一并删除；也可以另存到其他位置。": "The backup includes playlist sources, TV guide URLs, favorites, and all preferences. It is saved in the app folder by default and will be deleted if the app is uninstalled. You can also save it elsewhere.",
    "启动时自动检查更新": "Check for updates on startup",
    "0 个频道": "0 channels",
    "揽星TV": "LanXing TV",
    "Android TV 播放器": "Android TV Player",
    "正在加载…": "Loading…",
}

# Translate exact Kotlin/Java string literals.
literal_pattern = re.compile(r'"((?:\\.|[^"\\])*)"')
remaining_code = []
for path in (MAIN / "java").rglob("*"):
    if not path.is_file() or path.suffix not in {".kt", ".java"}:
        continue
    text = path.read_text(encoding="utf-8")
    for old, new in code_translations.items():
        text = text.replace('"' + old + '"', '"' + new + '"')
    path.write_text(text, encoding="utf-8")

# Translate visible labels embedded directly in layout XML.
visible_attr = re.compile(r'((?:android|tools):(?:text|hint|contentDescription|title|label)=")([^"]*)(")')
remaining_xml = []
for path in (MAIN / "res").rglob("*.xml"):
    text = path.read_text(encoding="utf-8")
    def replace_attr(match):
        value = match.group(2)
        return match.group(1) + layout_translations.get(value, value) + match.group(3)
    text = visible_attr.sub(replace_attr, text)
    path.write_text(text, encoding="utf-8")

# Force the app's own locale to English, independent of the TV box system language.
app_file = MAIN / "java/com/cyj265/iptvplayer/App.kt"
app_text = app_file.read_text(encoding="utf-8")
if "override fun attachBaseContext" not in app_text:
    app_text = app_text.replace(
        "import android.app.Application",
        "import android.app.Application\nimport android.content.Context\nimport android.content.res.Configuration",
        1,
    )
    app_text = app_text.replace(
        "class App : Application() {\n",
        """class App : Application() {
    override fun attachBaseContext(base: Context) {
        Locale.setDefault(Locale.US)
        val config = Configuration(base.resources.configuration)
        config.setLocale(Locale.US)
        super.attachBaseContext(base.createConfigurationContext(config))
    }

""",
        1,
    )
app_file.write_text(app_text, encoding="utf-8")

# Validate all app-owned visible strings are English before compiling.
for match in resource_pattern.finditer(strings_file.read_text(encoding="utf-8")):
    if re.search(r"[\u4e00-\u9fff]", match.group(3)):
        remaining_xml.append("strings.xml:" + match.group(2) + "=" + match.group(3))
for path in (MAIN / "java").rglob("*"):
    if not path.is_file() or path.suffix not in {".kt", ".java"}:
        continue
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(("//", "/*", "*", "*/")):
            continue
        for match in literal_pattern.finditer(line):
            if re.search(r"[\u4e00-\u9fff]", match.group(1)):
                remaining_code.append(f"{path}:{number}: {match.group(1)}")
for path in (MAIN / "res").rglob("*.xml"):
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r'android:(?:text|hint|contentDescription|title|label)="[^"]*[\u4e00-\u9fff]', line):
            remaining_xml.append(f"{path}:{number}: {line.strip()}")
if remaining_code or remaining_xml:
    print("Untranslated Kotlin/Java UI strings:")
    for item in remaining_code[:100]:
        print(item)
    print("Untranslated XML UI strings:")
    for item in remaining_xml[:100]:
        print(item)
    raise SystemExit("English localization validation failed.")
print(f"English localization validated. Translated {len(resource_translations)} resource strings and {len(code_translations)} code strings.")
