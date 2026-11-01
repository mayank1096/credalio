# shared detail-page layout (hero left + sticky card right), prefix dt-
CLOUD='/_blob/020f1a8593e80e5fcee9e0f06637f153'
WAVE='/_blob/3d4d999db1912d0cb0084365c58434d3'
SEAL='M56.5 9.0 Q64.2 6.3 68.8 13.0 Q77.0 12.8 79.3 20.7 Q87.2 23.0 87.0 31.2 Q93.7 35.8 91.0 43.5 Q96.0 50.0 91.0 56.5 Q93.7 64.2 87.0 68.8 Q87.2 77.0 79.3 79.3 Q77.0 87.2 68.8 87.0 Q64.2 93.7 56.5 91.0 Q50.0 96.0 43.5 91.0 Q35.8 93.7 31.2 87.0 Q23.0 87.2 20.7 79.3 Q12.8 77.0 13.0 68.8 Q6.3 64.2 9.0 56.5 Q4.0 50.0 9.0 43.5 Q6.3 35.8 13.0 31.2 Q12.8 23.0 20.7 20.7 Q23.0 12.8 31.2 13.0 Q35.8 6.3 43.5 9.0 Q50.0 4.0 56.5 9.0Z'
CSS=r'''
.dt-top{background:#FFFFFF url(CLOUD) center top / max(1440px,100%) auto no-repeat}
.dt-grid{max-width:1312px;margin:0 auto;padding:40px 48px 96px;box-sizing:border-box;display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:0 64px;align-items:start}
.dt-main{min-width:0;display:flex;flex-direction:column}
.dt-hero{display:flex;flex-direction:column;align-items:flex-start;gap:16px;padding-bottom:40px}
.dt-crumb{display:flex;align-items:center;gap:8px;font-size:13px;color:#8A93AD}
.dt-crumb a{color:#5B6582;text-decoration:none}
.dt-crumb a:hover{color:#1652F0}
.dt-tags{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.dt-tag{height:28px;padding:0 11px 0 9px;border-radius:999px;background:rgba(255,255,255,.85);border:1px solid #E3E8F3;display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#0B1433;white-space:nowrap}
.dt-h1{margin:0;font-size:48px;line-height:1.06;font-weight:600;letter-spacing:-1.5px;color:#0B1433;max-width:780px}
.dt-sub{margin:0;font-size:18px;line-height:1.55;color:#4A5578;max-width:680px}
.dt-by{display:flex;align-items:center;flex-wrap:wrap;gap:10px 18px;margin-top:4px;font-size:14px;color:#5B6582}
.dt-who{display:flex;align-items:center;gap:10px}
.dt-who b{font-weight:600;color:#0B1433}
.dt-av{width:36px;height:36px;border-radius:999px;background:#DCE5FB;color:#1652F0;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;flex-shrink:0}
.dt-sep{width:1px;height:18px;background:#D6DDEE}
.dt-fact{display:inline-flex;align-items:center;gap:6px;white-space:nowrap}
.dt-fact b{font-weight:600;color:#0B1433}
.dt-tabs{position:sticky;top:0;z-index:5;display:flex;gap:28px;background:#FFFFFF;border-bottom:1px solid #E6EAF3;margin-bottom:8px}
.dt-tab{position:relative;height:52px;padding:0 2px;border:none;background:none;font-family:'Google Sans',system-ui,sans-serif;font-size:15px;font-weight:500;color:#5B6582;cursor:pointer;white-space:nowrap;transition:color .2s ease}
.dt-tab::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2.5px;border-radius:3px;background:#1652F0;transform:scaleX(0);transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.dt-tab:hover{color:#0B1433}
.dt-tab-on{color:#0B1433;font-weight:600}
.dt-tab-on::after{transform:scaleX(1)}
.dt-sec{display:flex;flex-direction:column;gap:20px;padding:40px 0 8px;scroll-margin-top:56px}
.dt-h2{margin:0;font-size:26px;line-height:1.15;font-weight:600;letter-spacing:-.6px;color:#0B1433;display:flex;align-items:center;gap:8px}
.dt-sh{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.dt-sm{font-size:14px;color:#5B6582}
.dt-p{margin:0;font-size:16px;line-height:1.6;color:#3A4566;max-width:720px}
.dt-chips{display:flex;align-items:center;flex-wrap:wrap;gap:8px}
.dt-chl{font-size:13px;font-weight:500;color:#8A93AD;margin-right:4px;white-space:nowrap}
.dt-chip{height:32px;padding:0 13px;border-radius:999px;background:#F5F8FF;border:1px solid #E3E8F3;display:inline-flex;align-items:center;font-size:13px;font-weight:500;color:#0B1433;white-space:nowrap}
.dt-side{position:sticky;top:24px;z-index:6}
.dt-card{border-radius:22px;background:#FFFFFF;border:1px solid #E3E8F3;box-shadow:0 40px 80px -48px rgba(11,20,51,.45);overflow:hidden}
.dt-cbody{display:flex;flex-direction:column;gap:16px;padding:22px 24px 24px}
.dt-lab{display:flex;align-items:center;gap:7px;font-size:13px;font-weight:500;color:#8A93AD}
.dt-amt{display:flex;align-items:baseline;gap:8px;margin-top:-8px}
.dt-amt b{font-size:34px;font-weight:600;letter-spacing:-1px;color:#0B1433}
.dt-amt span{font-size:15px;font-weight:500;color:#5B6582}
.dt-btn{white-space:nowrap;height:56px;padding:0 8px 0 24px;border:none;border-radius:999px;background:#1652F0;color:#FFFFFF;display:flex;align-items:center;justify-content:space-between;font-family:'Google Sans',system-ui,sans-serif;font-size:16px;font-weight:600;cursor:pointer;text-decoration:none;transition:background .2s ease}
.dt-btn:hover{background:#0E3BB8}
.dt-btn i{width:40px;height:40px;border-radius:999px;background:#FFFFFF;display:flex;align-items:center;justify-content:center}
.dt-done{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#E7F5EE;color:#0F6B45;font-size:14px;font-weight:500}
.dt-ask{display:flex;align-items:center;justify-content:center;gap:10px;height:44px;border-radius:999px;font-size:14px;font-weight:600;color:#0B1433;text-decoration:none;border:1.5px solid #D6DDEE;transition:border-color .2s ease}
.dt-ask:hover{border-color:#1652F0}
.dt-btn:focus-visible,.dt-tab:focus-visible,.dt-ask:focus-visible,.dt-link:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:3px}
.dt-link{font-size:14px;font-weight:600;color:#1652F0;text-decoration:none;white-space:nowrap}
.dt-link:hover{color:#0E3BB8}
.dt-bar{display:none}
.dt-faq{border-radius:20px;border:1.5px solid #E6EAF3;overflow:hidden}
.dt-fq + .dt-fq{border-top:1px solid #EEF1F7}
.dt-fh{width:100%;min-height:60px;padding:12px 20px;border:none;background:#FFFFFF;display:flex;align-items:center;justify-content:space-between;gap:16px;text-align:left;font-family:'Google Sans',system-ui,sans-serif;font-size:16px;font-weight:600;color:#0B1433;cursor:pointer}
.dt-fh:hover{background:#FAFBFE}
.dt-fh:focus-visible{outline:3px solid rgba(22,82,240,.45);outline-offset:-3px}
.dt-chev{color:#8A93AD;transition:transform .3s ease;flex-shrink:0}
.dt-fq-open .dt-chev{transform:rotate(180deg)}
.dt-fa{margin:0;padding:0 20px 18px;font-size:15px;line-height:1.6;color:#3A4566;text-wrap:pretty !important}
@media (max-width: 1180px){.dt-grid{grid-template-columns:minmax(0,1fr) 340px;gap:0 40px}}
@media (max-width: 960px){
.dt-grid{grid-template-columns:minmax(0,1fr);padding-top:32px}
.dt-main{display:contents}
.dt-main > *{order:3}
.dt-hero{order:1;padding-bottom:28px}
.dt-side{order:2;position:static;margin-bottom:12px}
.dt-card{max-width:520px}
.dt-hide-t{display:none !important}
}
@media (max-width: 760px){
.dt-top{background-size:auto 340px}
.dt-grid{padding:24px 20px 0}
.dt-crumb{display:none}
.dt-hero{gap:12px;padding-bottom:24px}
.dt-h1{font-size:30px;letter-spacing:-.8px}
.dt-sub{font-size:15px}
.dt-by{gap:10px 14px;font-size:13px}
.dt-sep{display:none}
.dt-who{width:100%}
.dt-card{border-radius:20px}
.dt-cbody{padding:18px 18px 20px;gap:14px}
.dt-amt b{font-size:28px}
.dt-card .dt-btn{display:none}
.dt-tabs{margin:0 -20px 4px;padding:0 20px;gap:22px;overflow-x:auto;scrollbar-width:none}
.dt-tabs::-webkit-scrollbar{display:none}
.dt-tab{height:48px;font-size:14px;flex-shrink:0}
.dt-sec{padding-top:32px;gap:16px}
.dt-h2{font-size:21px;letter-spacing:-.4px}
.dt-p{font-size:15px}
.dt-chips{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px;padding:0 20px;scrollbar-width:none}
.dt-chips::-webkit-scrollbar{display:none}
.dt-fh{padding:12px 16px;font-size:15px}
.dt-fa{padding:0 16px 16px;font-size:14px}
.dt-bar{display:flex;order:9;position:sticky;bottom:0;z-index:20;align-items:center;justify-content:space-between;gap:12px;margin:28px -20px 0;padding:12px 16px 12px 20px;background:rgba(255,255,255,.94);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border-top:1px solid #E6EAF3}
.dt-bar > div > b{display:block;font-size:17px;font-weight:600;color:#0B1433}
.dt-bar > div > span{font-size:12px;color:#5B6582}
.dt-bar .dt-btn{height:48px;font-size:15px;gap:12px}
.dt-bar .dt-btn i{width:34px;height:34px}
}
'''.replace('CLOUD',CLOUD)
CHEV='<svg class="dt-chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"></path></svg>'
CHECK='<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
TABS_JS='''tabs: names.map(function (n) { var on = S.tab === n; return { label: n, on: on ? 'true' : 'false', cls: on ? 'dt-tab-on' : '', go: function () { self.setState({ tab: n }); var el = self.secs[n]; if (el && el.scrollIntoView) el.scrollIntoView({ behavior: 'smooth', block: 'start' }); } }; }),'''
TABS_HTML='''<div class="dt-tabs" role="tablist" aria-label="Sections">
<sc-for list="{{tabs}}" as="t" hint-placeholder-count="4">
<button class="dt-tab {{t.cls}}" type="button" role="tab" aria-selected="{{t.on}}" onClick="{{t.go}}">{{t.label}}</button>
</sc-for>
</div>'''
