---
slug: "mprach"
url: "/mobilnisite/slovnik/mprach/"
type: "slovnik"
title: "MPRACH – MBMS Packet Random Access Channel"
date: 2025-01-01
abbr: "MPRACH"
fullName: "MBMS Packet Random Access Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mprach/"
summary: "MPRACH je logický kanál v MBMS (Multimedia Broadcast Multicast Service) používaný UEs k odesílání zpráv na náhodném přístupovém kanálu (RACH) pro procedury získání multicastové služby a sčítání. Umožň"
---

MPRACH je logický kanál v MBMS, který UEs využívají k odesílání RACH zpráv pro získání multicastové služby a procedury sčítání, což síti umožňuje odhadnout zájem uživatelů pro rozhodování o přenosu typu point-to-point nebo point-to-multipoint.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Packet Random Access Channel (MPRACH) je logický kanál definovaný v rámci specifikace 3GPP pro službu Multimedia Broadcast Multicast Service (MBMS), konkrétně pro proceduru náhodného přístupu ([RA](/mobilnisite/slovnik/ra/)) související s multicastovými službami. Funguje jako součást řídicí roviny MBMS. Hlavní funkcí MPRACH je poskytnout mechanismus, kterým uživatelská zařízení (UE) mohou signalizovat síti svůj zájem o příjem konkrétní MBMS služby. Toto se primárně používá v proceduře 'sčítání'. Když se má MBMS služba spustit nebo již probíhá, síť může iniciovat žádost o sčítání vysíláním oznámení na [MCCH](/mobilnisite/slovnik/mcch/) (MBMS Control Channel). UEs se zájmem o službu odpovídají vysláním specifického preambule [RACH](/mobilnisite/slovnik/rach/) na fyzických prostředcích [PRACH](/mobilnisite/slovnik/prach/) (Physical RACH), které jsou vyhrazeny pro MPRACH. Síť po detekci těchto preambulí může odhadnout počet UEs v buňce, která si přejí příjem multicastového přenosu. Tento odhad je zásadní pro rozhodování sítě v oblasti správy rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)). Pokud je počet zainteresovaných UEs vysoký, je efektivnější aktivovat přenos v MBMS Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)), což je point-to-multipoint vysílání na vyhrazené nosné nebo v subrámci. Pokud je počet nízký, může být efektivnější z hlediska využití spektra doručit obsah prostřednictvím běžných unicastových (point-to-point) přenosů. Procedura MPRACH zahrnuje specifické signatury (sekvence preambulí) vyhrazené pro MBMS sčítání, aby se odlišila od běžného RACH používaného pro počáteční přístup nebo handover. Síť tyto parametry (jako dostupné indexy preambulí a přidružené časování) konfiguruje prostřednictvím systémové informace. Z architektonického hlediska interakce přes MPRACH zahrnuje UE, eNodeB (v LTE) a entitu koordinace MBMS ([MCE](/mobilnisite/slovnik/mce/)). eNodeB provádí detekci preambulí a hlásí výsledek sčítání MCE, které činí konečné rozhodnutí o režimu přenosu.

## K čemu slouží

MPRACH byl vytvořen k řešení klíčového problému efektivity v doručování multicastových služeb: stanovení, zda použít cenné rádiové prostředky pro broadcastový/multicastový přenos, nebo pro více individuálních unicastových přenosů. Bez mechanismu sčítání by síť mohla slepě aktivovat MBSFN přenos pro službu, kterou chce jen hrstka uživatelů, a plýtvat tak vysílacími prostředky, které by mohly být použity pro jiné služby nebo unicastový provoz. Naopak by mohla použít více unicastových přenosů pro oblíbenou službu, což by způsobilo zbytečné zahlcení a neefektivní využití spektra. Účelem MPRACH je poskytnout lehkou, sítí řízenou metodu, kterou UEs mohou signalizovat svůj zájem, což umožňuje informované rozhodnutí správy rádiových prostředků (RRM). Tím se řeší omezení dřívějších vysílacích systémů, kterým chyběla dynamická zpětná vazba od populace přijímačů. Procedura sčítání prostřednictvím MPRACH umožňuje síti přizpůsobit strategii přenosu (broadcast vs. unicast) na základě aktuální velikosti publika v každé buňce, čímž optimalizuje celkovou kapacitu systému a využití prostředků. Byla zavedena s vylepšeními MBMS, aby se multicastové služby staly pro mobilní operátory ekonomicky a technicky životaschopnými, což umožňuje služby jako mobilní TV nebo streamování živých událostí.

## Klíčové vlastnosti

- Umožňuje zpětnou vazbu od UE pro procedury sčítání MBMS služeb
- Používá vyhrazené preambule RACH odlišné od těch používaných pro unicastový přístup
- Je spouštěn síťovým vysíláním žádosti o MBMS sčítání na MCCH
- Poskytuje síti odhad počtu zainteresovaných UEs na buňku
- Podporuje efektivní rozhodování mezi režimy doručování MBSFN (broadcast) a unicast
- Integruje se s architekturou řídicí roviny MBMS a funkcemi RRM

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [RACH – Random Access Channel](/mobilnisite/slovnik/rach/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 43.246** (Rel-19) — MBMS in GERAN Stage 2 Specification
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MPRACH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mprach/)
