---
slug: "isr"
url: "/mobilnisite/slovnik/isr/"
type: "slovnik"
title: "ISR – Idle mode Signalling Reduction"
date: 2025-01-01
abbr: "ISR"
fullName: "Idle mode Signalling Reduction"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/isr/"
summary: "ISR je mechanismus správy mobility, který umožňuje UE být současně registrováno v paketových doménách E-UTRAN (LTE) i UTRAN/GERAN (2G/3G). Snižuje signalizační režii při mobilitě mezi těmito systémy v"
---

ISR je mechanismus správy mobility, který snižuje signalizační režii tím, že umožňuje UE být současně registrováno v LTE i 2G/3G paketových doménách, a minimalizuje tak procedury aktualizace sledovací a směrovací oblasti během mobility v režimu nečinnosti.

## Popis

Idle mode Signalling Reduction (ISR, redukce signalizace v režimu nečinnosti) je funkce jádra sítě definovaná v architektuře Evolved Packet System (EPS) standardu 3GPP. Optimalizuje správu mobility pro uživatelské zařízení (UE) schopné operovat jak v Evolved [UTRAN](/mobilnisite/slovnik/utran/) ([E-UTRAN](/mobilnisite/slovnik/e-utran/), tj. LTE), tak v legacy přístupových sítích UTRAN nebo [GERAN](/mobilnisite/slovnik/geran/) (3G/2G). Základním principem ISR je umožnit UE být současně registrováno ve dvou různých paketových doménách jádra sítě: v [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) pro E-UTRAN a v [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node) pro UTRAN/GERAN. Při aktivaci ISR je UE přidělena dvě nezávislé, ale současně platné dočasné identity: Globally Unique Temporary Identity ([GUTI](/mobilnisite/slovnik/guti/)) od MME a Packet-Temporary Mobile Subscriber Identity ([P-TMSI](/mobilnisite/slovnik/p-tmsi/)) od SGSN. Uzly jádra sítě (MME a SGSN) jsou si vědomy vzájemného kontextu pro dané UE a vytvářejí asociaci, často prostřednictvím rozhraní S3 mezi sebou.

Fungování ISR se točí kolem chování UE při změně buňky (cell reselection) v režimu nečinnosti. Bez ISR by přesun z LTE buňky do 2G/3G buňky (nebo naopak) spustil plnou proceduru aktualizace směrovací oblasti (RAU) nebo aktualizace sledovací oblasti (TAU). Tyto procedury zahrnují signalizaci s jádrem sítě za účelem aktualizace polohy UE a potenciálně znovunavázání připojení k paketové datové síti (PDN), což spotřebovává rádiové prostředky, zatěžuje síť signalizací a vybíjí baterii UE. Při aktivovaném ISR, když UE přejde na buňku v rámci registrované směrovací oblasti (RA) nebo sledovací oblasti (TA) *druhé* přístupové technologie, nemusí okamžitě provádět aktualizační proceduru. Může se jednoduše připojit k nové buňce (camp on) využitím existující registrace v této doméně jádra sítě. UE potřebuje provést TAU nebo RAU pouze při pohybu mimo aktuálně registrovanou TA nebo RA pro příslušný systém, nebo při vypršení periodického aktualizačního časovače.

Úlohou ISR v síti je významně snížit signalizační zatížení rozhraní jádra sítě (S3, S6a, Gr) a rádiového rozhraní, zejména v nasazovacích scénářích s těsným překryvem pokrytí různých RAT (Radio Access Technology) nebo při časté změně buňky mobilními uživateli. Zlepšuje uživatelský zážitek zajištěním plynulé mobility v režimu nečinnosti s minimálním přerušením služby a šetří životnost baterie UE snížením frekvence energeticky náročných signalizačních procedur. Operátoři sítí těží ze snížení provozních nákladů díky nižšímu signalizačnímu provozu a lepší škálovatelnosti. ISR je klíčovým prvkem pro plynulou migraci sítě z 2G/3G na 4G LTE, což operátorům umožňuje využít stávající infrastrukturu při zavádění nové technologie.

## K čemu slouží

ISR bylo zavedeno za účelem řešení problému nadměrné a neefektivní signalizace generované dvou režimovými zařízeními LTE/2G-3G, která se často pohybují mezi různými rádiovými přístupovými technologiemi v režimu nečinnosti. Při nasazování LTE sítí často poskytovaly ostrovy pokrytí v širším moři 2G/3G. Mobilní zařízení pohybující se dovnitř a ven z LTE pokrytí by spustilo TAU při vstupu do LTE a RAU při návratu do 2G/3G, což vytvářelo signalizační bouři na hranicích. To plýtvalo cennými rádiovými prostředky a prostředky jádra sítě, zvyšovalo latenci pro uživatele při opětovném přechodu do aktivního stavu a vybíjelo baterie zařízení.

Motivace pro jeho vytvoření ve verzi 3GPP Release 8 byla přímo spojena se zavedením EPS a potřebou efektivní spolupráce s existujícími sítěmi GSM/GPRS a UMTS. Předchozí přístupy v systémech před Release 8 neumožňovaly současné registrace; zařízení bylo připojeno pouze k jedné paketové doméně jádra sítě najednou. To vynucovalo aktualizační proceduru při každé změně RAT. ISR tuto limitaci řešilo zavedením konceptu dvojité registrace, což efektivně 'skrylo' změny RAT před správou mobility jádra sítě, dokud se UE pohybovalo v rámci svých známých lokalizačních oblastí. Poskytlo pragmatické řešení, které vyvážilo složitost (udržování dvou kontextů) s významným přínosem redukce signalizace, což bylo klíčové pro komerční úspěch a výkonnost raných nasazení LTE.

## Klíčové vlastnosti

- Dvojitá registrace v MME a SGSN pro jedno UE
- Redukce procedur TAU a RAU během mezisystémové mobility v režimu nečinnosti
- Využití jak GUTI (od MME), tak P-TMSI (od SGSN)
- Asociační kontext udržovaný mezi MME a SGSN přes rozhraní S3
- Aktivace řízena sítí na základě schopností UE a politiky operátora
- Šetření životnosti baterie UE a snížení signalizační zátěže jádra sítě

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [TAU – Tracking Area Update](/mobilnisite/slovnik/tau/)
- [RAU – Routeing Area Update](/mobilnisite/slovnik/rau/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [ISR na 3GPP Explorer](https://3gpp-explorer.com/glossary/isr/)
