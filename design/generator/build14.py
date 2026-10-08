# Batch 14 · Readiness task 2 · Credentials & expertise
# CR-CRED-001 hub · CR-CRED-002 add a credential (one source; variants types / degree / aws / badge = 002 / 002a / 002b / 002c)
import builtins, os
_ALLOW = {'CR-CRED-001.dc.html', 'CR-CRED-001-Mobile.dc.html', 'CR-CRED-002.dc.html', 'CR-CRED-002-Mobile.dc.html',
          'CR-CRED-002a.dc.html', 'CR-CRED-002a-Mobile.dc.html', 'CR-CRED-002b.dc.html', 'CR-CRED-002b-Mobile.dc.html',
          'CR-CRED-002c.dc.html', 'CR-CRED-002c-Mobile.dc.html'}
_ropen = builtins.open
def open(p, mode='r', *a, **k):
    # only the files of this batch may be written; everything else goes to a scratch dir
    if 'w' in mode and '/design/canvas/project/' in str(p) and os.path.basename(str(p)) not in _ALLOW:
        os.makedirs('/tmp/claude-0/-home-user-credalio/ac3a299a-59c2-576d-8df6-3f8bf66b6d40/scratchpad/discard', exist_ok=True)
        p = '/tmp/claude-0/-home-user-credalio/ac3a299a-59c2-576d-8df6-3f8bf66b6d40/scratchpad/discard/' + os.path.basename(str(p))
    return _ropen(p, mode, *a, **k)
exec(_ropen('build12.py').read())

CRED_I = '<circle cx="12" cy="9" r="5"></circle><path d="m8.5 13.2-1.5 7.8 5-2.6 5 2.6-1.5-7.8"></path>'
BRIEF_I = '<rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7M3 12.5h18"></path>'
LINK_I = '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"></path><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"></path>'
BOLT_I = '<path d="M13 3 5 13.5h6L10 21l8-10.5h-6z"></path>'
PLUS_I = '<path d="M12 5v14M5 12h14"></path>'
FILE_I = '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5"></path>'
CAL_I = '<rect x="4" y="5" width="16" height="16" rx="2.5"></rect><path d="M8 3v4M16 3v4M4 10h16"></path>'
SEARCH_I = '<circle cx="11" cy="11" r="6.5"></circle><path d="m20 20-4.2-4.2"></path>'
STATUS = {'v': ('cr-pv', 'Verified'), 'r': ('cr-pr', 'In review'), 'a': ('cr-pa', 'Needs info')}

def TASK2(fname, title, content, script, css):
    TASK(fname, title, content, script, css, 'Credentials & expertise')
    s = open(P + fname).read().replace('Readiness · task 1 of 5', 'Readiness · task 2 of 5')
    open(P + fname, 'w').write(s)

CR_CSS = FORM_CSS_LITE + '''.cr{flex-grow:1;width:min(1120px,100%);box-sizing:border-box;margin:0 auto;padding:clamp(24px,5vh,56px) 32px 48px 32px;display:grid;grid-template-columns:minmax(0,1fr) 580px;gap:64px;align-items:start}
.cr-side{position:sticky;top:104px;padding-top:6px;display:flex;flex-direction:column;align-items:flex-start}
.cr-back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:#3A4566;text-decoration:none;margin-bottom:18px;cursor:pointer;background:none;border:0;padding:0;font-family:inherit}
.cr-back:hover{color:#1652F0}
.cr-sub{margin:12px 0 0 0;font-size:16px;line-height:1.6;color:#3A4566;max-width:440px}
.cr-panel{border-radius:24px;background:#FFFFFF;border:1.5px solid #E6EAF3;box-shadow:0 18px 44px rgba(22,82,240,.08);padding:22px 24px;display:flex;flex-direction:column}
.cr-ph{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.cr-ph .sec-h{display:block}
.cr-cnt{font-size:13px;font-weight:500;color:#5B6582}
.cr-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.cr-row{border:1.5px solid #E6EAF3;border-radius:16px;padding:13px 14px;display:grid;grid-template-columns:40px minmax(0,1fr) auto;column-gap:12px;align-items:center}
.cr-ri{width:40px;height:40px;border-radius:12px;background:#F5F8FF;color:#1652F0;display:flex;align-items:center;justify-content:center}
.cr-rt{display:flex;flex-direction:column;gap:3px;min-width:0}
.cr-rt b{font-size:15px;font-weight:600;line-height:1.3}
.cr-rt > span{font-size:13px;line-height:1.35;color:#5B6582}
.cr-pill{display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:999px;font-size:12.5px;font-weight:500;white-space:nowrap}
.cr-pill i{width:6px;height:6px;border-radius:50%;background:currentColor}
.cr-pv{background:#E7F5EE;color:#0F6B45}.cr-pr{background:#EAF0FF;color:#1652F0}.cr-pa{background:#FFF3E0;color:#8A4F00}
.cr-fix{grid-column:2 / -1;margin-top:10px;display:flex;align-items:center;gap:12px;padding:10px 10px 10px 14px;border-radius:12px;background:#FFF8EC}
.cr-fix span{flex-grow:1;font-size:13.5px;line-height:1.45;color:#6B4A12}
.cr-fix .ds-ghost{height:36px;padding:0 16px;font-size:13.5px;border-color:#F0D3A0}
.cr-add{margin-top:8px;display:flex;align-items:center;gap:12px;padding:13px 14px;border-radius:16px;border:1.5px dashed #CBD3E6;color:#0B1433;text-decoration:none;transition:border-color .2s ease,background .2s ease}
.cr-add:hover{border-color:#1652F0;background:#F5F8FF}
.cr-add .cr-ri{background:#1652F0;color:#FFFFFF}
.cr-gate{margin-top:26px;width:100%;max-width:460px;box-sizing:border-box;padding:16px 18px;border-radius:18px;background:#F2FAF6;border:1.5px solid #CFEADD;display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 12px;align-items:center}
.cr-gk svg{stroke:#FFFFFF}
.cr-gk{grid-row:span 2;width:34px;height:34px;border-radius:50%;background:#0F6B45;color:#FFFFFF;display:flex;align-items:center;justify-content:center}
.cr-gate b{font-size:15px;font-weight:600;color:#0F6B45}
.cr-gate > span{font-size:13.5px;line-height:1.45;color:#3A4566}
.cr-next{margin-top:14px;width:100%;max-width:460px;box-sizing:border-box;padding:16px 16px 16px 18px;border-radius:18px;background:url(''' + BGI + ''') center / cover no-repeat,#F5F8FF;border:1.5px solid #E6EAF3;display:flex;align-items:center;gap:14px}
.cr-nt{flex-grow:1;display:flex;flex-direction:column;gap:2px}
.cr-nl{font-size:12.5px;font-weight:500;color:#8A93AD}
.cr-nt b{font-size:15.5px;font-weight:600}
.cr-nt > span:last-child{font-size:13px;color:#5B6582}
/* type picker */
.cr-types{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.cr-t{width:100%;box-sizing:border-box;display:grid;grid-template-columns:44px minmax(0,1fr) auto 16px;gap:14px;align-items:center;text-align:left;padding:14px 16px;border-radius:16px;border:1.5px solid #E6EAF3;background:#FFFFFF;font-family:inherit;color:#0B1433;cursor:pointer;transition:border-color .2s ease,background .2s ease,box-shadow .2s ease}
.cr-t:hover{border-color:#1652F0;background:#F5F8FF;box-shadow:0 0 0 4px rgba(22,82,240,.08)}
.cr-t .cr-ri{width:44px;height:44px}
.cr-t > svg{color:#8A93AD}
.cr-tag{display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:999px;background:#E7F5EE;color:#0F6B45;font-size:12px;font-weight:500;white-space:nowrap}
.cr-tag.m{background:#F2F4F9;color:#5B6582}
/* how we verify */
.cr-vr{margin-top:26px;width:100%;max-width:460px;box-sizing:border-box;display:flex;flex-direction:column;gap:10px}
.cr-v{display:grid;grid-template-columns:auto minmax(0,1fr);gap:3px 12px;align-items:center;padding:14px 16px;border-radius:16px;background:#F5F8FF;border:1.5px solid #E6EAF3}
.cr-v .cr-vi{grid-row:span 2;width:34px;height:34px;border-radius:50%;background:#FFFFFF;color:#1652F0;display:flex;align-items:center;justify-content:center;border:1.5px solid #D6DDEE}
.cr-v b{font-size:14.5px;font-weight:600}
.cr-v > span:not(.cr-vi){font-size:13px;line-height:1.45;color:#4A5578}
.cr-v.ok{background:#F2FAF6;border-color:#CFEADD}
.cr-v.ok .cr-vi{color:#0F6B45;border-color:#CFEADD}
.cr-v.ok b{color:#0F6B45}
.cr-vm{display:none}
/* form */
.cr-fh{display:flex;align-items:center;gap:12px;padding-bottom:16px;margin-bottom:18px;border-bottom:1.5px solid #F0F2F8}
.cr-fh b{font-size:17px;font-weight:600;flex-grow:1}
.cr-chg{font-size:13.5px;font-weight:600;color:#1652F0;background:none;border:0;cursor:pointer;font-family:inherit;padding:6px 0}
.cr-form{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px 12px}
.cr-f{display:flex;flex-direction:column;min-width:0}
.cr-f.s2{grid-column:span 2}.cr-f.s4{grid-column:1 / -1}
.cr-f .ob-lab em{font-style:normal;font-weight:400;color:#8A93AD}
.cr-in{width:100%;height:48px;box-sizing:border-box;padding:0 16px;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:15px;color:#0B1433;outline:none}
.cr-in:focus{border-color:#1652F0;box-shadow:0 0 0 4px rgba(22,82,240,.12)}
.cr-in.mono{letter-spacing:.06em}
.cr-ico{position:relative}.cr-ico .cr-in{padding-left:42px}.cr-ico svg{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#5B6582;pointer-events:none}
.cr-hint{margin:6px 0 0 2px;font-size:12.5px;line-height:1.4;color:#5B6582}
.cr-seg{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.cr-o{position:relative;display:flex;align-items:center;gap:8px;height:46px;padding:0 12px;box-sizing:border-box;border-radius:14px;border:1.5px solid #D6DDEE;background:#FFFFFF;font-family:inherit;font-size:14px;font-weight:500;color:#0B1433;cursor:pointer;white-space:nowrap}
.cr-o svg{color:#5B6582;flex-shrink:0}
.cr-o .cr-ok{display:none;margin-left:auto;width:18px;height:18px;border-radius:50%;background:#1652F0;color:#FFFFFF;align-items:center;justify-content:center}
.cr-o.on{background:#EAF0FF;border-color:#1652F0}
.cr-o.on svg{color:#1652F0}.cr-o.on .cr-ok{display:flex}.cr-o.on .cr-ok svg{color:#FFFFFF}
.cr-up{display:flex;align-items:center;gap:12px;min-height:64px;box-sizing:border-box;padding:10px 14px;border-radius:14px;border:1.5px dashed #CBD3E6;background:#FBFCFF;font-family:inherit;text-align:left;cursor:pointer;color:#0B1433}
.cr-up:hover{border-color:#1652F0}
.cr-up .cr-ri{width:36px;height:36px;border-radius:10px;flex-shrink:0}
.cr-up > span:not(.cr-ri){flex:1 1 auto;min-width:0}
.cr-up b{display:block;font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cr-up em{flex-shrink:0}
.cr-up > span > span{display:block;font-size:12.5px;color:#5B6582;margin-top:2px}
.cr-up.done{border-style:solid;border-color:#CFEADD;background:#F2FAF6}
.cr-up.done .cr-ri{background:#0F6B45;color:#FFFFFF}
.cr-up.done em{margin-left:auto;font-style:normal;font-size:13px;font-weight:600;color:#1652F0}
.cr-foot{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:20px;padding-top:16px;border-top:1.5px solid #F0F2F8}
.cr-foot > span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;font-size:13px;color:#5B6582}
@media (max-width: 1080px){
.cr{grid-template-columns:minmax(0,1fr) 500px;gap:40px}
}
@media (max-width: 960px){
.cr{display:flex;flex-direction:column;gap:0;padding:32px 0 0 0}
.cr-side{position:static;padding:0 16px;width:100%;box-sizing:border-box}
.cr-back{margin-bottom:14px}
.cr-sub{font-size:14.5px;margin-top:8px}
.cr-panel{border:0;border-radius:0;box-shadow:none;padding:20px 16px 0 16px;width:100%;box-sizing:border-box}
.cr-gate{margin-top:18px;max-width:none;padding:12px 14px}
.cr-gk{width:28px;height:28px}
.cr-gate b{font-size:14px}.cr-gate > span{font-size:13px}
.cr-next{display:none}
.cr-vr{display:none}
.cr-vm{display:block;margin-top:16px}
.cr-vm .cr-v{padding:12px 14px}
.cr-row{padding:12px}
.cr-pill{height:26px;padding:0 9px;font-size:12px}
.cr-fix{grid-column:1 / -1;flex-wrap:wrap}
.cr-t{grid-template-columns:40px minmax(0,1fr) 16px;padding:12px 14px;gap:12px}
.cr-t .cr-ri{width:40px;height:40px}
.cr-t .cr-tag{display:none}
.cr-form{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
.cr-f.s2{grid-column:1 / -1}.cr-f.s1m{grid-column:span 1}
.cr-seg{display:flex;overflow-x:auto;margin:0 -16px;padding:0 16px;scrollbar-width:none}
.cr-seg::-webkit-scrollbar{display:none}
.cr-o{flex-shrink:0}
.cr-foot{position:sticky;bottom:0;z-index:3;margin:20px -16px 0 -16px;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.cr-foot > span{display:none}
.cr-foot .ds-ghost{width:48px;padding:0;flex-shrink:0}
.cr-foot .ds-ghost span{display:none}
.cr-foot .ds-btn{flex-grow:1;justify-content:space-between}
.cr-mbar{position:sticky;bottom:0;z-index:3;margin-top:20px;align-self:stretch;box-sizing:border-box;padding:12px 16px;background:#FFFFFF;border-top:1.5px solid #EEF1F7}
.cr-mbar .ds-btn{width:100%;justify-content:space-between}
.cr-mbar small{display:block;text-align:center;margin-top:8px;font-size:12.5px;color:#5B6582}
}
@media (min-width: 961px){.cr-mbar{display:none}}
'''

# ---------------- CR-CRED-001 · Your credentials & expertise ----------------
ROWS = [(CAP_I, 'MSc Data Science', 'Degree · University of Lagos · 2017', 'v', ''),
        (CRED_I, 'Microsoft Certified: Power BI Data Analyst Associate', 'Certification · checked online with Microsoft', 'r', ''),
        (CRED_I, 'Google Data Analytics Certificate', 'Certification · Google · 2021', 'a', 'The scan is hard to read. Upload a clearer copy or add the credential ID.')]
rows = ''
for i, t, m, st, fx in ROWS:
    pc, pl = STATUS[st]
    rows += f'<li class="cr-row"><span class="cr-ri">{ik(i, 20, 1.9)}</span><span class="cr-rt"><b>{t}</b><span>{m}</span></span><span class="cr-pill {pc}"><i></i>{pl}</span>'
    if fx:
        rows += f'<div class="cr-fix"><span>{fx}</span><a href="CR-CRED-002b.dc.html" class="ds-ghost">Fix it</a></div>'
    rows += '</li>'
c = f'''<main class="cr">
<aside class="cr-side">
<span class="lp-eb ob-in">Credentials &amp; expertise</span>
<h1 class="lp-h1 ob-in">Show why you’re the one to teach this.</h1>
<p class="cr-sub ob-in2">Add degrees, certifications, licences or work experience. Learners and validators see what’s verified.</p>
<div class="cr-gate ob-in3"><span class="cr-gk">{ic('check', 15, 3)}</span><b>Task complete</b><span>One verified credential is all this task needs. The rest join your profile as they’re verified.</span></div>
<div class="cr-next ob-in4"><span class="cr-nt"><span class="cr-nl">Next for you</span><b>Creator orientation</b><span>About 25 minutes</span></span><a href="CR-ORI-001.dc.html" class="ds-btn sm"><span>Continue</span><span class="ob-arrow">{ic('arrow', 16, 2.4)}</span></a></div>
</aside>
<section class="cr-panel ob-in2" aria-label="Your credentials">
<div class="cr-ph"><span class="sec-h">Your credentials</span><span class="cr-cnt">1 verified · 1 in review · 1 to fix</span></div>
<ul class="cr-list">{rows}</ul>
<a href="CR-CRED-002.dc.html" class="cr-add"><span class="cr-ri">{ik(PLUS_I, 20, 2.2)}</span><span class="cr-rt"><b>Add a credential</b><span>Degree, certification, licence, work or other evidence</span></span></a>
</section>
<div class="cr-mbar"><a href="CR-ORI-001.dc.html" class="ds-btn"><span>Next: Creator orientation</span><span class="ob-arrow">{ic('arrow', 18, 2.4)}</span></a><small>About 25 minutes · you can come back to add more</small></div>
</main>'''
TASK2('CR-CRED-001.dc.html', 'Credalio · Your credentials & expertise', c, DEF_S, CR_CSS)

# ---------------- CR-CRED-002 · Add a credential (types / degree / aws / badge) ----------------
TYPES = [('degree', CAP_I, 'Degree or diploma', 'University or college qualifications', '<span class="cr-tag m">Reviewed</span>'),
         ('aws', CRED_I, 'Professional certification', 'AWS, Microsoft, Google, PMP and more', '<span class="cr-tag">' + ik(BOLT_I, 12, 2.2) + 'Checked online</span>'),
         ('lic', ID_I, 'Licence or membership', 'Professional bodies and licences', '<span class="cr-tag m">Reviewed</span>'),
         ('work', BRIEF_I, 'Work experience', 'Roles that show your expertise', '<span class="cr-tag m">Reviewed</span>'),
         ('other', FILE_I, 'Other evidence', 'Portfolio, publications, talks, awards', '<span class="cr-tag m">Reviewed</span>')]
tl = ''.join(f'<li><button type="button" class="cr-t" onClick="{{{{p_{k}}}}}"><span class="cr-ri">{ik(i, 22, 1.9)}</span><span class="cr-rt"><b>{t}</b><span>{d}</span></span>{tag}{ik(CHEV_I, 16, 2.2)}</button></li>' for k, i, t, d, tag in TYPES)

def F(label, val, span='s2', opt=False, sel=False, icon=None, mono=False, hint='', fid=''):
    lab = f'<label class="ob-lab" for="{fid}">{label}{" <em>(optional)</em>" if opt else ""}</label>'
    if sel:
        ctl = f'<div class="ob-sel"><select id="{fid}" class="ob-f"><option selected>{val}</option></select>{ik(DOWN_I, 16, 2)}</div>'
    elif icon:
        ctl = f'<div class="cr-ico">{ik(icon, 16, 2)}<input id="{fid}" class="cr-in" value="{val}"></div>'
    else:
        ctl = f'<input id="{fid}" class="cr-in{" mono" if mono else ""}" value="{val}">'
    h = f'<p class="cr-hint">{hint}</p>' if hint else ''
    return f'<div class="cr-f {span}">{lab}{ctl}{h}</div>'

def UPL(label, done, name, opt=False, span='s2'):
    lab = f'<span class="ob-lab">{label}{" <em>(optional)</em>" if opt else ""}</span>'
    if done:
        b = f'<button type="button" class="cr-up done"><span class="cr-ri">{ic("check", 14, 3)}</span><span><b>{name}</b><span>PDF · 1.2 MB</span></span><em>Replace</em></button>'
    else:
        b = f'<button type="button" class="cr-up"><span class="cr-ri">{ik(UP_I, 18, 2)}</span><span><b>{name}</b><span>PDF, JPG or PNG · up to 10 MB</span></span></button>'
    return f'<div class="cr-f {span}">{lab}{b}</div>'

SEG = '''<div class="cr-f s4"><span class="ob-lab">How should we check it?</span><div class="cr-seg" role="radiogroup" aria-label="How should we check it?">
<button type="button" role="radio" aria-checked="{{idOn}}" class="cr-o {{idCls}}" onClick="{{toId}}">''' + ik(SEARCH_I, 16, 2) + '''<span>Credential ID</span><span class="cr-ok">''' + ic('check', 10, 3.4) + '''</span></button>
<button type="button" role="radio" aria-checked="{{lkOn}}" class="cr-o {{lkCls}}" onClick="{{toLink}}">''' + ik(LINK_I, 16, 2) + '''<span>Link or badge</span><span class="cr-ok">''' + ic('check', 10, 3.4) + '''</span></button>
<button type="button" role="radio" aria-checked="false" class="cr-o">''' + ik(UP_I, 16, 2) + '''<span>Upload certificate</span><span class="cr-ok">''' + ic('check', 10, 3.4) + '''</span></button>
</div></div>'''

DEGREE = (F('Qualification', 'MSc Data Science', fid='q') + F('Field of study', 'Data Science', opt=True, fid='fs') +
          F('Institution', 'University of Lagos', fid='in') + F('Country', 'Nigeria', 's1 s1m', sel=True, fid='co') + F('Year awarded', '2017', 's1 s1m', sel=True, fid='yr') +
          UPL('Certificate', True, 'msc-certificate.pdf') + UPL('Transcript', False, 'Add your transcript', opt=True))
AWS = (F('Issuer', 'Amazon Web Services (AWS)', 's4', sel=True, fid='is') + F('Certification', 'AWS Certified Data Engineer – Associate', 's4', sel=True, fid='ce') + SEG +
       F('Credential ID', 'K7Q2LM4P9XRB1D3V', mono=True, hint='The Validation Number on your AWS certificate.', fid='id') +
       F('Issued', 'Jun 2025', 's1 s1m', fid='d1') + F('Expires', 'Jun 2028', 's1 s1m', opt=True, fid='d2'))
BADGE = (F('Issuer', 'Microsoft', 's4', sel=True, fid='is2') + F('Certification', 'Power BI Data Analyst Associate', 's4', sel=True, fid='ce2') + SEG +
         F('Badge or verification link', 'credly.com/badges/3f8c2a1e-9b74', 's2', icon=LINK_I, hint='Credly and issuer pages are checked automatically.', fid='lk') +
         F('Issued', 'Mar 2024', 's1 s1m', fid='d3') + F('Expires', 'Mar 2026', 's1 s1m', opt=True, fid='d4'))

VR_TYPES = f'''<div class="cr-v ok"><span class="cr-vi">{ik(BOLT_I, 16, 2.2)}</span><b>Checked online</b><span>AWS, Microsoft, Google and Credly badges. Usually under a minute.</span></div>
<div class="cr-v"><span class="cr-vi">{ik(CLOCK_I, 16, 2.2)}</span><b>Reviewed by our Trust team</b><span>Everything else. Usually 1 to 3 business days.</span></div>'''
VR_MAN = f'<div class="cr-v"><span class="cr-vi">{ik(CLOCK_I, 16, 2.2)}</span><b>Reviewed by our Trust team</b><span>Usually 1 to 3 business days. We may contact you or the issuer if something needs confirming.</span></div>'
VR_ON = f'<div class="cr-v ok"><span class="cr-vi">{ik(BOLT_I, 16, 2.2)}</span><b>Checked online with {{{{issuer}}}}</b><span>Usually within a minute. If it can’t be checked online, our Trust team reviews it.</span></div>'

def VR(cls):
    return f'''<sc-if value="{{{{t0}}}}" hint-placeholder-val="{{{{true}}}}">{VR_TYPES if cls == 'cr-vr' else ''}</sc-if>
<sc-if value="{{{{tD}}}}" hint-placeholder-val="{{{{false}}}}">{VR_MAN}</sc-if>
<sc-if value="{{{{tC}}}}" hint-placeholder-val="{{{{false}}}}">{VR_ON}</sc-if>'''

c = f'''<main class="cr">
<aside class="cr-side">
<button type="button" class="cr-back ob-in" onClick="{{{{back}}}}">{ic('back', 16, 2.2)}<span>{{{{backL}}}}</span></button>
<span class="lp-eb ob-in">Add a credential</span>
<h1 class="lp-h1 ob-in">{{{{h1}}}}</h1>
<p class="cr-sub ob-in2">{{{{sub}}}}</p>
<div class="cr-vr ob-in3">{VR('cr-vr')}</div>
</aside>
<section class="cr-panel ob-in2" aria-label="{{{{h1}}}}">
<sc-if value="{{{{t0}}}}" hint-placeholder-val="{{{{true}}}}">
<div class="cr-ph"><span class="sec-h">What are you adding?</span></div>
<ul class="cr-types">{tl}</ul>
</sc-if>
<sc-if value="{{{{tF}}}}" hint-placeholder-val="{{{{false}}}}">
<div class="cr-fh"><span class="cr-ri">{{{{fIcon}}}}</span><b>{{{{fTitle}}}}</b><button type="button" class="cr-chg" onClick="{{{{back}}}}">Change</button></div>
<sc-if value="{{{{tD}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cr-form">{DEGREE}</div></sc-if>
<sc-if value="{{{{tA}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cr-form">{AWS}</div></sc-if>
<sc-if value="{{{{tB}}}}" hint-placeholder-val="{{{{false}}}}"><div class="cr-form">{BADGE}</div></sc-if>
<div class="cr-vm">{VR('cr-vm')}</div>
<footer class="cr-foot"><button type="button" class="ds-ghost" onClick="{{{{back}}}}">{ic('back', 16, 2.2)}<span>Cancel</span></button><span>{{{{footNote}}}}</span><a href="#" class="ds-btn"><span>{{{{goL}}}}</span><span class="ob-arrow">{ic('arrow', 18, 2.4)}</span></a></footer>
</sc-if>
</section>
</main>'''
# icons for the form header (plain svg strings rendered via sc-if blocks would be heavy; use per-variant spans)
c = c.replace('<span class="cr-ri">{{fIcon}}</span>',
              '<span class="cr-ri"><sc-if value="{{tD}}" hint-placeholder-val="{{false}}">' + ik(CAP_I, 20, 1.9) + '</sc-if><sc-if value="{{tC}}" hint-placeholder-val="{{false}}">' + ik(CRED_I, 20, 1.9) + '</sc-if></span>')

S_CR2 = '''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { t: (props || {}).variant || 'types' };
  }
  renderVals() {
    const t = this.state.t, f = t !== 'types';
    const cert = t === 'aws' || t === 'badge';
    const go = (x) => () => this.setState({ t: x });
    return {
      t0: !f, tF: f, tD: t === 'degree', tA: t === 'aws', tB: t === 'badge', tC: cert,
      h1: !f ? 'What are you adding?' : (t === 'degree' ? 'Your degree or diploma' : 'Your certification'),
      sub: !f ? 'Pick one. The form asks only for what that type needs.' : (t === 'degree' ? 'Add it as it appears on your certificate.' : 'Tell us the issuer and how we can check it.'),
      backL: f ? 'All credential types' : 'Your credentials',
      back: () => { if (f) this.setState({ t: 'types' }); else window.location.href = 'CR-CRED-001.dc.html'; },
      fTitle: t === 'degree' ? 'Degree or diploma' : 'Professional certification',
      issuer: t === 'badge' ? 'Credly' : 'Amazon Web Services',
      footNote: cert ? 'Usually checked within a minute' : 'Reviewed in 1 to 3 days',
      goL: cert ? 'Verify now' : 'Submit for review',
      idOn: t === 'aws' ? 'true' : 'false', idCls: t === 'aws' ? 'on' : '', toId: go('aws'),
      lkOn: t === 'badge' ? 'true' : 'false', lkCls: t === 'badge' ? 'on' : '', toLink: go('badge'),
      p_degree: go('degree'), p_aws: go('aws'), p_lic: () => {}, p_work: () => {}, p_other: () => {}
    };
  }
}'''
TASK2('CR-CRED-002.dc.html', 'Credalio · Add a credential', c, S_CR2, CR_CSS)

for n, t, prop in [('CR-CRED-002a', 'Credalio · Add a credential: degree or diploma', ' variant="degree"'),
                   ('CR-CRED-002b', 'Credalio · Add a credential: certification by credential ID', ' variant="aws"'),
                   ('CR-CRED-002c', 'Credalio · Add a credential: certification by badge link', ' variant="badge"')]:
    WRAP(n + '.dc.html', 'CR-CRED-002', 1440, 820, t, prop)
    s = open(P + n + '.dc.html').read().replace('background: #F7F9FD', 'background: #FFFFFF'); open(P + n + '.dc.html', 'w').write(s)
for n, tg, prop in [('CR-CRED-001', 'CR-CRED-001', ''), ('CR-CRED-002', 'CR-CRED-002', ''),
                    ('CR-CRED-002a', 'CR-CRED-002', ' variant="degree"'), ('CR-CRED-002b', 'CR-CRED-002', ' variant="aws"'),
                    ('CR-CRED-002c', 'CR-CRED-002', ' variant="badge"')]:
    WRAP(n + '-Mobile.dc.html', tg, 390, 844, n + ' mobile preview', prop)
    s = open(P + n + '-Mobile.dc.html').read().replace('background: #F7F9FD', 'background: #FFFFFF'); open(P + n + '-Mobile.dc.html', 'w').write(s)
print('build14 done')
