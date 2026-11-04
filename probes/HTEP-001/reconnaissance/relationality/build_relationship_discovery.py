#!/usr/bin/env python3
"""Rebuild the bounded HTEP relationship-discovery registers from a saved Koios wrapper.
No network; does not modify the source TWD action inventory.
Curated hypotheses are explicit below; evidence anchors are source metadata excerpts.
"""
import csv,json,re,sys
from pathlib import Path
from difflib import SequenceMatcher
ROOT=Path(__file__).resolve().parent
SOURCE=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'koios-proposal-list-raw.json'
payload=json.loads(SOURCE.read_text(encoding='utf-8'))
rows=payload['rows'] if isinstance(payload,dict) else payload
records=[r for r in rows if r.get('proposal_type')=='TreasuryWithdrawals']
assert len(records)==107, 'This discovery script is scoped to the 2026-11-03 snapshot of 107 TWDs'

def title(r):return ((r.get('meta_json') or {}).get('body') or {}).get('title','')
def named(substr,epoch):
    hits=[r for r in records if r['proposed_epoch']==epoch and substr.casefold() in title(r).casefold()]
    if len(hits)!=1:raise ValueError((substr,epoch,len(hits)))
    return hits[0]
def amount(r):return sum(int(e['amount']) for e in r.get('withdrawal',[]))/1e6
# target/new, source/old, relationship, phrase used as evidence search, which item text, verification grade
# Verified = direct self-description of relation, grounded in both records' distinct IDs.
# Candidate = inferred relation, not asserted as fact.
pairs=[
 ('Amaru Treasury Withdrawal 2026',614,'Amaru Treasury Withdrawal 2025',566,'continuation_of','second treasury withdrawal proposal','new','supported'),
 ('Eternl: Path to Sustainability (2026-2027)',631,'Eternl Maintenance',570,'continuation_of','2025 budget process','new','supported'),
 ('Eternl: Path to Sustainability - v2',637,'Eternl: Path to Sustainability (2026-2027)',631,'revision_of','previous proposal','new','supported'),
 ('Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2028',628,"TWEAG's Proposals",570,'continuation_of','natural continuation','new','supported'),
 ('Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027',634,'Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2028',628,'revision_of',None,'new','candidate'),
 ('Scalus 2026:',640,'Scalus: Cardano’s Application Platform',630,'revision_of','focused resubmission','new','supported'),
 ('Revised Cardano dOSPO',641,'Cardano dOSPO and OMF Program',630,'revision_of',None,'new','candidate'),
 ('Cardano Critical Integrations V2',632,'Cardano Critical Integrations Budget',599,'continuation_of','V2 exists only to sustain','new','supported'),
 ('Cardano Defi Liquidity Budget - Withdrawal 1',617,'Cardano DeFi Liquidity Budget - Withdrawal 1',607,'resubmission_of',None,'new','candidate'),
 ('Reimburse Ikigai Info Governance Action Deposit.',649,'Reimburse Ikigai Info Governance Action Deposit.',636,'resubmission_of',None,'new','candidate'),
 ('Revised Cardano Summit 2026 Singapore',627,'Cardano Summit 2026 and TOKEN2049',623,'revision_of','revised and 22% reduced','new','supported'),
 ('TOKEN2049 Singapore 2026: Baseline',628,'Cardano Summit 2026 and TOKEN2049',623,'split_from','Following the submission of the combined','new','supported'),
 ('TOKEN2049 Singapore 2026: Top-Up',628,'Cardano Summit 2026 and TOKEN2049',623,'split_from',None,'new','candidate'),
 ('Pallas by TxPipe:',638,'Pallas: Sustaining',570,'continuation_of','Intersect\'s 2025 budget cycle','new','supported'),
 ('Dolos:',638,'Dolos: Sustaining',570,'continuation_of','Intersect\'s 2025 budget cycle','new','supported'),
 ('UTxO RPC by TxPipe:',638,'UTxO RPC: Sustaining',570,'continuation_of','Intersect\'s 2025 budget cycle','new','supported'),
]
def excerpt(r,needle):
    b=(r.get('meta_json') or {}).get('body') or {}
    if needle:
        for field in ('abstract','rationale','motivation'):
            s=b.get(field) or ''
            m=re.search(re.escape(needle),s,re.I)
            if m:
                start=max(0,m.start()-95);end=min(len(s),m.end()+155)
                return field,re.sub(r'\s+',' ',s[start:end]).strip()
    return 'title_only',title(r)
found=[]
for newpat,newe,oldpat,olde,rel,needle,direction,status in pairs:
    new,old=named(newpat,newe),named(oldpat,olde)
    f,quote=excerpt(new,needle)
    if needle and f=='title_only':raise ValueError(f'Needle absent for {newpat}: {needle}')
    found.append({'relationship_id':f'R{len(found)+1:03d}','from_action_id':new['proposal_id'],'from_epoch':newe,'from_title':title(new),'to_action_id':old['proposal_id'],'to_epoch':olde,'to_title':title(old),'relationship_type':rel,'verification':status,'evidence_location':f'Koios /proposal_list → {new["proposal_id"]} → meta_json.body.{f}' if f!='title_only' else 'Titles + epoch + request amounts (candidate; explicit documentary link not established)','evidence_excerpt':quote,'source_amount_ada':f'{amount(old):.0f}','new_amount_ada':f'{amount(new):.0f}','source_snapshot':'koios-proposal-list-raw.json, retrieved 2026-11-03','notes':'Self-reported relation; independent external corroboration not performed' if status=='supported' else 'Candidate only; needs targeted verification before promotion'})
# Detect additional candidate same project through title; not added to verified relationships
# Discover external pointers to *TWD action ids* via gov_action IDs present inside proposal bodies
pat=re.compile(r'gov_action1[023456789acdefghjklmnpqrstuvwxyz]{35,}',re.I)
byid={r['proposal_id']:r for r in records}
external=[]
for r in records:
    b=(r.get('meta_json') or {}).get('body') or {}
    prose='\n'.join(str(b.get(k) or '') for k in ('abstract','rationale','motivation'))
    refs='\n'.join(str(z.get('uri','')) for z in b.get('references',[]) if isinstance(z,dict))
    for sid in set(pat.findall(prose+'\n'+refs)):
        if sid in byid and sid!=r['proposal_id']:
            external.append((r['proposal_id'],sid))
# stable csv
cols=list(found[0]);
with (ROOT/'twd-relationship-candidates.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(found)
# coverage per row: no relationship is not proof of independence
linked=set()
for a in found:linked|={a['from_action_id'],a['to_action_id']}
with (ROOT/'twd-relationship-coverage.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['action_id','submitted_epoch','title','in_bounded_candidate_set','evidence_scope','note']);w.writeheader()
    for r in sorted(records,key=lambda r:(r['proposed_epoch'],r['proposal_id'])):
        w.writerow({'action_id':r['proposal_id'],'submitted_epoch':r['proposed_epoch'],'title':title(r),'in_bounded_candidate_set':str(r['proposal_id'] in linked).lower(),'evidence_scope':'bounded_manual_discovery','note':'Not included does NOT mean no related initiative'})
summary={'total_twd_actions':len(records),'proposed_relationships':len(found),'supported_by_proposer_metadata':sum(x['verification']=='supported' for x in found),'candidate_only':sum(x['verification']=='candidate' for x in found),'distinct_actions_touched':len(linked),'explicit_twd_id_cross_references_found_in_prose_or_reference_urls':len(set(external)), 'snapshot_retrieved_at_utc':payload.get('retrieved_at_utc') if isinstance(payload,dict) else None,'limitations':['Relationships are curated, not exhaustive.','Supported means metadata explicitly describes the relationship, not that external documents were verified.','A later submission is not an edit to an earlier on-chain action.','Not included means not assessed or not selected, not independent.']}
(ROOT/'discovery-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
