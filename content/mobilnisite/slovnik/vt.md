---
slug: "vt"
url: "/mobilnisite/slovnik/vt/"
type: "slovnik"
title: "VT – Mobile Terminating in VMSC"
date: 2025-01-01
abbr: "VT"
fullName: "Mobile Terminating in VMSC"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vt/"
summary: "VT (Mobile Terminating in VMSC) je model volání a koncept směrování v mobilních sítích s přepojováním okruhů, při kterém je volání k mobilnímu účastníkovi ukončeno v navštívené ústředně mobilní sítě ("
---

VT je model volání v mobilních sítích s přepojováním okruhů, při kterém je volání k mobilnímu účastníkovi ukončeno v navštívené ústředně mobilní sítě (Visited Mobile Switching Center), která obsluhuje aktuální polohu účastníka.

## Popis

VT, neboli Mobile Terminating in [VMSC](/mobilnisite/slovnik/vmsc/), je základní procedura obsluhy hovorů definovaná v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) dle 3GPP, primárně pro sítě GSM a UMTS. Popisuje architektonický model a signalizační tok pro doručení mobilního příchozího hovoru – například hlasového hovoru od jiného účastníka – k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), která je aktuálně obsluhována navštívenou ústřednou mobilní sítě (Visited Mobile Switching Center, VMSC). VMSC je [MSC](/mobilnisite/slovnik/msc/) v síti, kde účastník právě roamuje, na rozdíl od jeho domovské MSC (HMSC) v jeho předplacené domovské síti. Model VT je nedílnou součástí podsystémů správy mobility a směrování hovorů.

Proces začíná, když je hovor směrován do domovské sítě účastníka na základě jeho čísla [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Subscriber Integrated Services Digital Network Number). Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) v domovské síti dotazuje domovský registr polohy ([HLR](/mobilnisite/slovnik/hlr/)), aby získal informace pro směrování. HLR, který udržuje informace o aktuální poloze účastníka (adresu obsluhující VMSC), následně dotazuje registr návštěvníků ([VLR](/mobilnisite/slovnik/vlr/)) asociovaný s touto VMSC, aby získal dočasné roamovací číslo nazývané Mobile Station Roaming Number (MSRN). Toto MSRN je vráceno GMSC přes HLR. GMSC poté použije toto MSRN k přímému směrování hovoru k VMSC obsluhující účastníka. VMSC po přijetí příchozího požadavku na sestavení hovoru provede prostřednictvím svého asociovaného VLR a rádiové přístupové sítě procedury pagingu a autentizace, aby lokalizovala a upozornila konkrétní mobilní stanici.

Klíčové komponenty zapojené do procedury VT zahrnují GMSC, HLR, VLR a VMSC. GMSC funguje jako vstupní bod a bod rozhodování o směrování. HLR je centrální databáze účastníků. VLR je dočasná lokální databáze v navštívené síti, která uchovává kopii profilu služeb účastníka a informace o oblasti polohy. VMSC je ústředna, která zajišťuje sestavení hovoru, správu rádiových zdrojů a přepojování pro ukončení hovoru. Tato architektura odlehčuje domovskou síť od zpracování rádiově souvisejících aspektů hovoru a umožňuje generování záznamů pro účtování v navštívené síti (pro ukončovací úsek) a v domovské síti (pro úseky vzniku a směrování), což je klíčové pro vypořádání mezi operátory.

Role VT v síti je zásadní pro globální roaming. Umožňuje plynulé doručování hovorů k účastníkům kdekoli na světě dynamickým určováním jejich bodu připojení. Odděluje funkce řízení hovoru a správy mobility, což domovské síti umožňuje udržovat kontrolu nad daty a autentizací účastníka, zatímco fyzické spojení hovoru deleguje na lokální navštívenou síť. Tento model je efektivní, protože vytváří přímé spojení mezi GMSC a VMSC, optimalizuje přenosové cesty a snižuje zpoždění po vytočení. Koncept VT je základním kamenem jádra sítě s přepojováním okruhů GSM/UMTS a je podrobně specifikován v mnoha technických specifikacích 3GPP pokrývajících požadavky na služby, procedury řízení hovorů a specifikace kodeků.

## K čemu slouží

Model volání VT byl vytvořen, aby vyřešil základní problém doručování hlasových hovorů s přepojováním okruhů k mobilním účastníkům, kteří roamují mimo pokrytí své domovské sítě. Před standardizovanými celulárními systémy byla telefonie pevná a založená na poloze. Nástup GSM přinesl osobní mobilitu, což vyžadovalo síťovou architekturu schopnou najít a spojit se s účastníkem, jehož poloha byla proměnná a volajícímu neznámá. Model VT tuto potřebu naplňuje zavedením úrovně nepřímosti prostřednictvím HLR a dynamické alokace čísel (MSRN).

Řeší omezení zjednodušeného přístupu, při kterém by všechny hovory byly nejprve směrovány do domovské sítě, která by pak musela hovorové spojení mezinárodně prodloužit k aktuální poloze účastníka. To by bylo neefektivní, nákladné a zvyšovalo by latenci. Model VT optimalizuje směrovací cestu. Získáním dočasného lokálního čísla (MSRN) v navštívené síti může být hovor směrován přímo z GMSC k VMSC, často přes přímější mezinárodní spoje. Tím se snižují přenosové náklady a zlepšuje se kvalita hlasu minimalizací počtu síťových uzlů.

Model VT navíc vytváří jasný rámec pro účtování a vypořádání mezi operátory. Navštívená síť, která poskytuje rádiové zdroje a přepojování pro ukončení, může generovat záznamy o hovorech (CDR) pro fakturaci domovského operátora. Tím byl vytvořen komerční a technický základ pro globální roamingové dohody. Jeho vznik byl motivován potřebou škálovatelné, efektivní a komerčně životaschopné architektury pro mezinárodní mobilní telekomunikace, což byla klíčová prodejní výhoda GSM oproti dřívějším celulárním systémům.

## Klíčové vlastnosti

- Dynamické směrování hovorů prostřednictvím dotazu HLR na polohu účastníka
- Použití roamovacího čísla mobilní stanice (MSRN) jako dočasné směrovací adresy
- Ukončení hovoru v navštívené MSC (VMSC) v roamující síti
- Oddělení řízení domovského účastníka (HLR) od obsluhy hovoru v navštívené síti (VMSC/VLR)
- Umožňuje generování záznamů pro účtování v domovské i navštívené síti pro vypořádání
- Základ pro plynulý mezinárodní roaming pro služby s přepojováním okruhů

## Související pojmy

- [VMSC – Visited Mobile Switching Center](/mobilnisite/slovnik/vmsc/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)

## Definující specifikace

- **TR 22.903** (Rel-19) — CS Videotelephony Service Analysis
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.944** (Rel-19) — QoE, ESQoS and SQoS metrics for 3G multimedia services

---

📖 **Anglický originál a plná specifikace:** [VT na 3GPP Explorer](https://3gpp-explorer.com/glossary/vt/)
