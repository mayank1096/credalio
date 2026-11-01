BASE_CSS = r'''body{margin:0;background:#FFFFFF}
h1,h2,h3,p{text-wrap:pretty}
@media (min-width: 761px){p{text-wrap:balance}}
.sx-nav{max-width:1360px;margin:0 auto;height:72px;padding:0 24px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:16px}
.sx-logo{display:flex;align-items:center;gap:8px;text-decoration:none;flex-shrink:0}
.sx-mark{display:block;width:28px;height:28px;background:url(/_blob/f81e36d31295a0d0737959589ec1abd4) center/contain no-repeat}
.sx-word{display:block;height:24px;aspect-ratio:292/56;background:url(/_blob/8acabcff7ece53343d63205e8b7321a2) left center/contain no-repeat}
.sx-links{display:flex;align-items:center;gap:4px}
.sx-link{height:40px;padding:0 12px;border-radius:999px;display:flex;align-items:center;font-size:15px;font-weight:500;color:#3A4566;text-decoration:none;white-space:nowrap;transition:color .2s ease,background .2s ease}
.sx-link:hover{color:#0B1433;background:#F5F8FF}
.sx-link-on{color:#0B1433;background:#EAF0FF}
.sx-cta{height:44px;padding:0 20px;border-radius:999px;display:flex;align-items:center;background:#1652F0;color:#FFFFFF;font-size:15px;font-weight:600;text-decoration:none;transition:background .2s ease}
.sx-cta:hover{background:#0E3BB8}
.sx-menu{display:none;width:44px;height:44px;border-radius:999px;border:none;background:transparent;color:#0B1433;align-items:center;justify-content:center;cursor:pointer}
.sx-link:focus-visible,.sx-cta:focus-visible,.sx-menu:focus-visible,.sx-logo:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
.sx-tip{position:relative;display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:999px;border:1.5px solid #B5BDD3;font-size:11px;font-weight:600;color:#8A93AD;letter-spacing:0;cursor:help;flex-shrink:0;font-style:normal}
.sx-tip:hover::after,.sx-tip:focus::after{content:attr(data-tip);position:absolute;left:-10px;top:calc(100% + 8px);width:240px;padding:10px 12px;border-radius:10px;background:#0B1433;color:#FFFFFF;font-size:12px;font-weight:400;line-height:1.45;text-align:left;white-space:normal;z-index:30}
.sx-tip-r:hover::after,.sx-tip-r:focus::after{left:auto;right:-10px}
.sx-tip:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:2px}
.sx-orb{border-radius:999px;flex-shrink:0;background:radial-gradient(circle at 34% 28%,#DCE7FF 0%,#7FA4FF 24%,#1652F0 62%,#0B2A8F 100%)}
.sx-foot{border-top:1px solid #EEF1F7;background:#FFFFFF}
.sx-fin{max-width:1312px;margin:0 auto;padding:40px 48px;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;font-size:13px;color:#5B6582}
.sx-fin nav{display:flex;gap:20px;flex-wrap:wrap}
.sx-fin a{color:#3A4566;text-decoration:none}
.sx-fin a:hover{color:#1652F0}
@media (max-width: 1180px){.sx-links{display:none}.sx-menu{display:flex}}
@media (max-width: 520px){.sx-login{display:none !important}}
@media (max-width: 760px){.sx-nav{height:60px;padding:0 16px}.sx-word{height:20px}.sx-cta{height:40px;padding:0 16px;font-size:14px}.sx-fin{padding:28px 20px;flex-direction:column;align-items:flex-start;gap:14px}.sx-tip:hover::after,.sx-tip:focus::after{width:200px}}
'''
LINKS=['Explore learning','Career paths','Certifications','Pricing','For creators','For institutions']
def nav(active):
    ls='\n'.join('<a class="sx-link%s" href="#"%s>%s</a>'%(' sx-link-on' if l==active else '',' aria-current="page"' if l==active else '',l) for l in LINKS)
    return '''<header class="sx-nav">
<a class="sx-logo" href="#" aria-label="Credalio home"><span class="sx-mark" aria-hidden="true"></span><span class="sx-word" aria-hidden="true"></span></a>
<nav class="sx-links" aria-label="Main">
%s
</nav>
<div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0">
<a class="sx-link sx-login" href="#" style="font-weight: 600; color: #0B1433">Log in</a>
<a class="sx-cta" href="#">Create account</a>
<button class="sx-menu" type="button" aria-label="Open menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button>
</div>
</header>'''%ls
FOOT='''<footer class="sx-foot">
<div class="sx-fin">
<a class="sx-logo" href="#" aria-label="Credalio home"><span class="sx-mark" aria-hidden="true"></span><span class="sx-word" aria-hidden="true"></span></a>
<nav aria-label="Footer"><a href="#">Courses</a><a href="#">Career Paths</a><a href="#">Certifications</a><a href="#">Pricing</a><a href="#">For Creators</a><a href="#">Privacy</a><a href="#">Terms</a></nav>
<span>© 2026 magnummeta. All rights reserved.</span>
</div>
</footer>'''
ARROW='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
def page(title,css,top_open,body,script,h=2000,props=''):
    return '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&amp;display=swap">
<style>
%s%s
</style>
</helmet>
<div style="font-family: 'Google Sans', system-ui, sans-serif; color: #0B1433; background: #FFFFFF">
%s
%s
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{%s"$preview":{"width":1440,"height":%d}}'>
%s
</script>
</body>
</html>
'''%(title,BASE_CSS,css.strip(),top_open,body,props,h,script.strip())
