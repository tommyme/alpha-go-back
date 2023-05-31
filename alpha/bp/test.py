def getCookie():
    import http.cookies
    cookie = http.cookies.SimpleCookie()
    s = "buvid3=FFDD56E9-FF76-D86C-DE26-24708422974117169infoc; i-wanna-go-back=-1; _uuid=F10331081C-E154-3FD4-CA4F-59DE7C6B5AE817406infoc; DedeUserID=306062555; DedeUserID__ckMd5=8a7ac316753f2294; b_ut=5; header_theme_version=CLOSE; CURRENT_PID=c3d85b80-d7a7-11ed-88c8-317f4804c0e3; rpdid=|(J|)lk|lJ)u0J'uY)uuJlu|Y; buvid_fp_plain=undefined; home_feed_column=5; nostalgia_conf=-1; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; i-wanna-go-feeds=-1; LIVE_BUVID=AUTO6816812998878297; CURRENT_FNVAL=4048; fingerprint=b21328ff229865f45e62a8701d87028f; buvid_fp=b21328ff229865f45e62a8701d87028f; hit-new-style-dyn=0; hit-dyn-v2=1; b_nut=1684034543; PVID=1; SESSDATA=6624e4ce,1700803386,91b19*52; bili_jct=57a5b0c8fccbe573b80b7933ea646db7; sid=57j8gu1c; b_lsid=B4C519107_188679D6C15; bp_video_offset_306062555=801126544744382500; innersign=0; buvid4=9BD3729B-6409-0CC1-444A-D2DB3F711FB017910-023041021-ydify6rEqFT418hRkL73qw=="
    cookie.load(s)

    res = {k:v.value for k, v in cookie.items()}
    return res
