"""Batch 15 overlays: Creio states, account menu and message pop-ups in the Studio, reusing the Link 2 components
(CR-CREIO-POP popover, CR-CREIO-011b not-enough / estimate cards, CR-PM account menu, CR-MSG pop-ups).

Post-step run by layout.py: Builder, Studio and Prepare get an `ov` prop (low | empty | est | menu | msg | reply | sent).
The token pill shows the balance state, the anchor gets a ring, and the overlay is added inside the page root.
"""
import os, re, sys
from l4kit import ic, ck, btn

SOURCES = ['Builder.dc.html', 'Studio.dc.html', 'Prepare.dc.html']
KINDS = ['low', 'empty', 'est', 'menu', 'msg', 'reply', 'sent']

WARN = ic('warn', 12, 2.6)
ROLE = {'learner': ('book', 'Learner', 'Your courses, programs and progress'), 'creator': ('pencil', 'Creator', 'You’re here'),
        'validator': ('valid', 'Validator', '2 review requests waiting')}

LOW = '''<sc-if value="{{ov_low}}" hint-placeholder-val="{{ false }}"><div class="tp-scrim" aria-hidden="true"></div><section class="tp-p ov-r2" role="dialog" aria-label="Creio">
<span class="tp-lab">Creio</span><span class="tp-big"><span class="tp-coin" aria-hidden="true"></span>18,240</span>
<p class="tp-warn"><span class="tp-i">%s</span><span>Your balance is running low.</span></p>
<div class="tp-f"><a href="#" class="ds-btn tp-go"><span>Buy Creio</span></a><a href="#" class="ds-link tp-u">View usage</a></div></section></sc-if>''' % WARN

EMPTY = '''<sc-if value="{{ov_empty}}" hint-placeholder-val="{{ false }}"><div class="tp-scrim" aria-hidden="true"></div><section class="ac ns ov-p ov-r2" role="dialog" aria-label="Not enough Creio">
<span class="ns-h"><span class="tp-i">%s</span>Not enough Creio</span><b class="ov-h">You don’t have enough Creio to complete this AI action.</b>
<dl class="ns-d one"><div><dt>Current balance</dt><dd><span class="ns-c" aria-hidden="true"></span>0 Creio</dd></div></dl>
<p class="ns-p">You can keep working by hand: editing, uploading, building and submitting all still work.</p>
<div class="ac-f"><a href="#" class="ds-btn ac-go"><span>Buy Creio</span></a><a href="STU-014.dc.html" class="ac-x">Continue manually</a></div></section></sc-if>''' % WARN

EST = '''<sc-if value="{{ov_est}}" hint-placeholder-val="{{ false }}"><div class="tp-scrim" aria-hidden="true"></div><section class="ac ns est ov-p ov-r2" role="dialog" aria-label="Large AI action estimate">
<span class="ns-h"><span class="tp-i">%s</span>Large AI action · estimate</span><b class="ov-h">Nova will review your complete course: structure, content and assessments.</b>
<dl class="ns-d"><div><dt>Estimated usage</dt><dd><span class="ns-c" aria-hidden="true"></span>~8,000–12,000</dd></div><div><dt>Available</dt><dd><span class="ns-c" aria-hidden="true"></span>72,450</dd></div></dl>
<p class="ns-p">Everyday Copilot help doesn’t ask first. Only large actions like this show an estimate.</p>
<div class="ac-f"><a href="STU-042.dc.html" class="ds-btn ac-go"><span>Run Review</span></a><a href="STU-042.dc.html" class="ac-x">Cancel</a></div></section></sc-if>''' % ic('nova', 12, 2.4)

def prole(k, cur=False, badge=''):
    icn, t, d = ROLE[k]
    tag = 'div' if cur else 'a'
    return '<%s %sclass="pm-r%s"%s><span class="pm-ri">%s</span><span><b>%s</b><span>%s</span></span>%s%s</%s>' % (
        tag, '' if cur else 'href="#" ', ' cur' if cur else '', ' aria-current="true"' if cur else '', ic(icn, 18, 2) if icn != 'book' else ic('course', 18, 2),
        t, d, ('<span class="pm-ck">%s</span>' % ck(13)) if cur else '', ('<span class="pm-bd">%s</span>' % badge) if badge else '', tag)
MENU = '''<sc-if value="{{ov_menu}}" hint-placeholder-val="{{ false }}"><div class="pm-scrim" aria-hidden="true"></div><section class="pm-p ov-r1" role="dialog" aria-label="Account menu">
<div class="pm-me"><span class="pm-a">AO<span class="pm-dot"></span></span><span><b>Ada Ononuju</b><span>ada.ononuju@example.com</span><span class="ds-tag blue pm-tg">Creator</span></span></div>
<div class="pm-sec"><span class="pm-lab">Status</span><div class="pm-st" role="radiogroup" aria-label="Status"><button type="button" role="radio" aria-checked="true" class="on"><i></i>Online</button><button type="button" role="radio" aria-checked="false" class="aw"><i></i>Away</button><button type="button" role="radio" aria-checked="false" class="dn"><i></i>Appear offline</button></div></div>
<nav class="pm-l" aria-label="Profile"><a href="#">%s<span>View public profile</span></a><a href="#">%s<span>Edit Creator Profile</span></a></nav>
<div class="pm-sec"><span class="pm-lab">Switch role</span><div class="pm-rl">%s%s%s</div></div>
<nav class="pm-l" aria-label="Account"><a href="#">%s<span>Settings</span></a><a href="#">%s<span>Help &amp; Support</span></a><a href="#" class="pm-out">%s<span>Sign out</span></a></nav></section></sc-if>''' % (
    ic('user', 18, 2), ic('edit', 18, 2), prole('learner'), prole('creator', True), prole('validator', badge='2'),
    ic('settings', 18, 2), ic('help', 18, 2), ic('back', 18, 2))

MSG = [('MO', 'Mary O.', 'Learner', 'now', 'Learner Support · Data Analysis with SQL · a lesson', 'I tried your hint but my answer still doesn’t match. Can you check my approach?', 'Open conversation', '#', True, ''),
       ('JA', 'John Adeyemi', 'Co-Creator', '1 min', 'Team Chat · Data Analysis with SQL', 'I’ve uploaded the case study. Can you check the numbers before Friday?', 'Open Team Chat', '#', True, 'm2'),
       ('AB', 'Dr. Amina Bello', 'Validator', '3 min', 'Validation · Data Analysis with SQL · Request #16', 'Please share the source data so I can check the results.', 'Open request', 'STU-055A.dc.html', False, 'm3')]
def mcard(i, m, mode):
    ini, n, role, t, ctx, body, op, href, rep, cls = m
    first = i == 0
    if first and mode == 'reply':
        foot = ('<label class="mg-in"><span class="sr-only">Reply to Mary O.</span><input value="Yes, add city to the GROUP BY as well." aria-label="Reply to Mary O."><a href="STU-MSG-3.dc.html" class="mg-go" aria-label="Send">%s</a></label>'
                '<div class="mg-f"><a href="#" class="mg-o">Open conversation</a><a href="STU-MSG-1.dc.html" class="mg-b">Cancel</a></div>') % ic('arrowr', 15, 2.4)
    elif first and mode == 'sent':
        foot = '<span class="mg-ok"><i>%s</i>Sent to Mary. It’s in the conversation.</span><div class="mg-f"><a href="#" class="mg-o">Open conversation</a></div>' % ck(11)
    else:
        foot = '<div class="mg-f">%s<a href="%s" class="mg-o">%s</a>%s</div>' % (
            ('<a href="%s" class="mg-b">Reply</a>' % ('STU-MSG-2.dc.html' if first else '#')) if rep else '', href, op, '' if rep else '<span class="mg-w">Respond in the workspace</span>')
    return ('<section class="mg-c %s" role="status" aria-label="New message from %s"><div class="mg-h"><span class="mg-a" aria-hidden="true">%s</span><span class="mg-t"><span class="mg-n">%s<span class="ds-tag line mg-rl">%s</span><em>%s</em></span>'
            '<span class="mg-x">%s</span></span><button type="button" class="mg-ib" aria-label="Dismiss">%s</button></div><p class="mg-p">%s</p>%s</section>') % (
        cls, n, ini, n, role, t, ctx, ic('x', 14, 2.2), body, foot)
def mstack(mode):
    return ('<sc-if value="{{ov_%s}}" hint-placeholder-val="{{ false }}"><div class="mg" aria-live="polite">%s<a href="#" class="mg-more mg-m"><span><b>3 new messages</b></span><span>View all</span></a></div></sc-if>') % (
        mode, ''.join(mcard(i, m, mode) for i, m in enumerate(MSG)))

OVERLAY = LOW + EMPTY + EST + MENU + mstack('msg') + mstack('reply') + mstack('sent')
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ov15.css')).read()
JS = '''
  renderVals() {
    var v = this._rv15(), o = (this.props && this.props.ov) || '';
    %s.forEach(function (k) { v['ov_'.concat(k)] = o === k; });
    v.tokT = o === 'low' ? '18.2K' : (o === 'empty' ? '0' : '72.4K');
    v.tokOn = o === 'low' || o === 'empty' || o === 'est' ? 'tp-on' : '';
    v.meOn = o === 'menu' ? 'pm-on' : '';
    return v;
  }''' % repr(KINDS).replace("'", '"')

def patch(s):
    s = s.replace('<a href="#" class="ds-tok" aria-label="72,450 Creio">', '<a href="#" class="ds-tok {{tokOn}}" aria-label="72,450 Creio">')
    s = re.sub(r'(<a href="#" class="ds-tok \{\{tokOn\}\}"[^>]*>.*?)<span>72\.4K</span>', r'\1<span>{{tokT}}</span><sc-if value="{{ov_low}}" hint-placeholder-val="{{ false }}"><span class="tk-low">Low</span></sc-if><sc-if value="{{ov_empty}}" hint-placeholder-val="{{ false }}"><span class="tk-low emp">Empty</span></sc-if>', s, flags=re.S)
    s = s.replace('class="cw-me"', 'class="cw-me {{meOn}}"')
    j = s.index('<div', s.index('</helmet>')); k = s.index('>', j) + 1
    s = s[:k] + '\n' + OVERLAY + s[k:]
    i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
    s = s.replace('  renderVals() {', '  _rv15() {', 1)
    head = 'class Component extends DCLogic {'
    i = s.index(head) + len(head); s = s[:i] + JS + s[i:]
    return s

def run(out):
    for f in SOURCES:
        p = os.path.join(out, f)
        s = open(p).read()
        if '_rv15' in s:
            continue
        open(p, 'w').write(patch(s))

if __name__ == '__main__':
    run(sys.argv[1])
