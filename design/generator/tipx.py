# shared info tooltip (hover/focus) used by build22–24 cleanups
INFO = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 7.6v.2"></path></svg>'
def tip(text, cls='l'):
    return f'<span class="tip" tabindex="0" aria-label="More info">{INFO}<span class="tip-b {cls}" role="tooltip">{text}</span></span>'
TIP_CSS = '''
.tip{position:relative;display:inline-flex;align-items:center;vertical-align:-2px;margin-left:6px;color:#8A93AD;cursor:default;outline:none}
.tip:hover,.tip:focus{color:#1652F0}
.tip-b{position:absolute;bottom:calc(100% + 10px);left:-12px;width:250px;padding:12px 14px;border-radius:12px;background:#0B1433;color:#FFFFFF;font-size:13px;font-weight:400;line-height:1.45;letter-spacing:0;text-align:left;white-space:normal;box-shadow:0 14px 34px rgba(11,20,51,.22);opacity:0;visibility:hidden;transform:translateY(4px);transition:opacity .16s ease,transform .16s ease,visibility .16s;z-index:20;pointer-events:none}
.tip-b.r{left:auto;right:-12px}
.tip-b.dn{bottom:auto;top:calc(100% + 10px)}
.tip:hover .tip-b,.tip:focus .tip-b{opacity:1;visibility:visible;transform:none}
'''
