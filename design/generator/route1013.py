# route1013: designer 2026-10-13 "copy the client exactly" (client Link 1 CreatorSetup `nxt`): ONB-001 Continue routes
# per role — Creator → ONB-002, Organization → ONB-002S (coming soon), Learner / Validator → stay + red error
# "Learner and Validator sign-up are designed separately. Choose Creator or Set Up an Organization." (cleared on pick).
# usage: python3 route1013.py <dir>
import os, sys
p = os.path.join(sys.argv[1], 'Main.dc.html'); s = open(p, encoding='utf-8').read()
assert 'route1013' not in s
i = s.find('<a href="CR-ONB-002.dc.html" class="cd-cta"'); j = s.find('</a>', i) + 4; assert i > 0
a = s[i:j]
inner = a[a.find('>') + 1:-4]
style = a[a.find('style="') + 7:a.find('"', a.find('style="') + 7)]
btn = ('<sc-if value="{{ctaGo}}" hint-placeholder-val="{{true}}">' + a.replace('href="CR-ONB-002.dc.html"', 'href="{{ctaHref}}"') + '</sc-if>'
       '<sc-if value="{{ctaStop}}" hint-placeholder-val="{{false}}"><button type="button" class="cd-cta" onClick="{{showErr}}" style="' + style + '; border: 0; cursor: pointer; font-family: inherit">' + inner + '</button></sc-if>')
err = ('<sc-if value="{{err}}" hint-placeholder-val="{{false}}"><p class="cd-err" role="alert" style="margin: 0; display: flex; align-items: flex-start; gap: 7px; max-width: 520px; font-size: 14px; line-height: 1.45; color: #B42318; text-align: left">'
       '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0; margin-top: 2px"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4"></path><path d="M12 16h.01"></path></svg>'
       '<span>{{err}}</span></p></sc-if>')
s = s[:i] + err + btn + s[j:]
a = "constructor(props) { super(props); this.state = { sel: 'create' };"
assert s.count(a) == 1; s = s.replace(a, "constructor(props) { super(props); this.state = { sel: 'create', err: '' };")
a = "this.setState({ sel: id }); },"
assert s.count(a) == 1; s = s.replace(a, "this.setState({ sel: id, err: '' }); },")
a = "return { c, is, not, ctaLabel: ctas[sel], panX: pans[sel] };"
assert s.count(a) == 1
s = s.replace(a, "/* route1013: per-role Continue, as in the client flow */\n"
    "    const hrefs = { create: 'CR-ONB-002.dc.html', institution: 'CR-ONB-002S.dc.html' };\n"
    "    const stop = !hrefs[sel];\n"
    "    return { c, is, not, ctaLabel: ctas[sel], panX: pans[sel], ctaGo: !stop, ctaStop: stop, ctaHref: hrefs[sel] || '#', err: this.state.err,\n"
    "      showErr: () => this.setState({ err: 'Learner and Validator sign-up are designed separately. Choose Creator or Set Up an Organization.' }) };")
open(p, 'w', encoding='utf-8').write(s); print('ok')
