"""Link 4 · Batch 15: Creio states, account menu and message pop-ups in the Studio (STU-AI-1 to 4, STU-MSG-1 to 3).
Client copy word for word, "AI Tokens" → Creio. The overlays reuse the Link 2 components and are added to the
Builder / Studio / Prepare sources by ov15.py (prop ov); these boards only pick the page and the state.
"""
import json
from l4kit import *

BOARDS = [
    ('STU-AI-1', 'Builder', {'state': 'team', 'ov': 'low'}, 'STU-AI-1 · Creio running low (18.2K)'),
    ('STU-AI-2', 'Studio', {'page': 'outcomes', 'ov': 'empty'}, 'STU-AI-2 · AI action with no Creio left (Generate from course goal)'),
    ('STU-AI-3', 'Prepare', {'page': 'nova', 'ov': 'est'}, 'STU-AI-3 · Nova Course Review: estimate before a full review'),
    ('STU-AI-4', 'Builder', {'state': 'team', 'ov': 'menu'}, 'STU-AI-4 · Account menu in the Studio'),
    ('STU-MSG-1', 'Builder', {'state': 'team', 'ov': 'msg'}, 'STU-MSG-1 · Message pop-ups in the Studio (learner, team, validator)'),
    ('STU-MSG-2', 'Builder', {'state': 'team', 'ov': 'reply'}, 'STU-MSG-2 · Quick reply to a learner without leaving the Studio'),
    ('STU-MSG-3', 'Builder', {'state': 'team', 'ov': 'sent'}, 'STU-MSG-3 · Quick reply sent'),
]

if __name__ == '__main__':
    for code, src, props, title in BOARDS:
        write(code + '.dc.html', wrapper(title + ' · Desktop', src, props, 1440, 900))
        write(code + '-Mobile.dc.html', wrapper(title + ' · Mobile', src, props, 390, 844))
    print('ok', len(BOARDS))
