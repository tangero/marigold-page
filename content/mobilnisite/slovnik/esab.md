---
slug: "esab"
url: "/mobilnisite/slovnik/esab/"
type: "slovnik"
title: "ESAB – Extended Synchronization Access Burst"
date: 2025-01-01
abbr: "ESAB"
fullName: "Extended Synchronization Access Burst"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/esab/"
summary: "Vylepšený přístupový záblesk používaný v GSM/EDGE Radio Access Network (GERAN) pro počáteční synchronizaci a přístupové procedury. Rozšiřuje standardní Synchronization Access Burst (SAB) za účelem zle"
---

ESAB je vylepšený přístupový záblesk pro GSM/EDGE, který rozšiřuje standardní Synchronization Access Burst (SAB), aby zlepšil počáteční synchronizaci a výkon přístupu v náročných rádiových podmínkách, jako je rozšířené pokrytí buňky.

## Popis

Extended Synchronization Access Burst (ESAB) je specializovaná struktura záblesku na fyzické vrstvě definovaná ve specifikacích GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Používá se během počáteční přístupové fáze, kdy se mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) pokouší synchronizovat se sítí a požádat o vyhrazený kanál. ESAB je evolucí standardního Synchronization Access Burst (SAB), navrženou s delší tréninkovou sekvencí a potenciálně modifikovanou datovou částí, aby poskytovala robustnější signál pro detekci a dekódování základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) v nepříznivých podmínkách.

Z architektonického hlediska je ESAB vysílán MS na náhodném přístupovém kanálu (RACH) ve směru uplink. Jeho návrh je detailně popsán v několika technických specifikacích 3GPP (TS), především v rámci řady 45 (Rádiové aspekty), které řídí fyzickou vrstvu GERAN. Struktura záblesku zahrnuje delší synchronizační sekvenci ve srovnání se standardním přístupovým zábleskem. Tato prodloužená sekvence poskytuje větší korelační zisk na přijímači BTS, což umožňuje přesnější odhad časového předstihu (timing advance) a spolehlivou detekci i při slabém nebo interferencí narušeném přijímaném signálu. Přesná modulace, kódování a struktura jsou specifikovány v dokumentech jako TS 45.002 a TS 45.003.

Během provozu, když MS potřebuje přístup k síti (např. pro aktualizaci polohy nebo zřízení hovoru), vybere vhodný typ přístupového záblesku na základě parametrů vysílaných buňkou a vlastních schopností. Pokud MS podporuje ESAB a buňka je pro jeho použití nakonfigurována, MS vyšle ESAB. BTS po detekci tohoto záblesku provede korelaci se známou prodlouženou tréninkovou sekvencí, aby stanovila časování symbolů, vypočítala potřebný časový předstih pro MS a dekódovala informace přístupového požadavku. Tento proces je klíčový pro navázání počáteční synchronizace ve směru uplink, což je předpoklad pro jakékoli následné vyhrazené spojení.

Úlohou ESAB v síti je rozšířit efektivní dosah buňky a zlepšit úspěšnost přístupu v neideálních rádiových podmínkách. Díky robustnější struktuře záblesku zmírňuje dopad útlumu na trase, mnohocestného útlumu a ko-kanálové interference během kritické počáteční přístupové procedury. Toto vylepšení je zvláště cenné pro scénáře s omezeným pokrytím, jako jsou venkovské oblasti, nebo v hustých městských prostředích se složitými charakteristikami šíření, což přispívá k celkovému výkonu sítě a uživatelskému komfortu.

## K čemu slouží

ESAB byl zaveden, aby řešil omezení standardního Synchronization Access Burst (SAB) v sítích GSM, zejména pokud jde o spolehlivost přístupu na okraji buňky a v prostředích náchylných k interferenci. Standardní SAB, ač efektivní, měl omezenou délku tréninkové sekvence, která mohla být nedostatečná pro spolehlivou detekci při nízké síle signálu nebo při významném zpoždění. To mohlo vést k neúspěšným přístupům, nezdařeným pokusům o zřízení hovoru nebo ke snížení pokrytí buňky, což ovlivňovalo kvalitu služeb.

Historicky, jak se sítě GSM vyvíjely a byly nuceny poskytovat širší pokrytí a podporu v náročnějších rádiových podmínkách, stala se potřeba robustnějšího přístupového mechanismu zřejmou. Motivací pro vytvoření ESAB bylo zvýšit robustnost počátečního vysílání ve směru uplink od mobilní stanice bez nutnosti zásadních změn základní rámcové struktury GSM nebo definic kanálů. Představuje přírůstkové vylepšení v rámci vývojové cesty [GERAN](/mobilnisite/slovnik/geran/), které umožňuje sítím zlepšit dostupnost a potenciálně rozšířit pokrytí pro legacy služby GSM.

Řešením problému nespolehlivého počátečního přístupu pomáhá ESAB snižovat neúspěchy při zřizování hovorů a zvyšuje pravděpodobnost úspěšné aktualizace polohy. To je zvláště důležité pro zařízení pro komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) nebo uživatele v oblastech s omezeným pokrytím, a zajišťuje tak dostupnost sítě. Řešil konkrétní omezení na fyzické vrstvě a poskytl síťovým operátorům nástroj pro optimalizaci výkonu na hranici buňky, což byl častý problém v raných nasazeních GSM a zůstává relevantní pro roli GSM jako záložní technologie v zařízeních podporujících více rádiových přístupových technologií (multi-RAT).

## Klíčové vlastnosti

- Prodloužená tréninková sekvence pro lepší korelaci a robustnost detekce
- Vylepšený výkon při nízkém poměru signál-šum (SNR) a podmínkách s vysokou interferencí
- Zpětně kompatibilní provoz v rámci procedury náhodného přístupu (RACH) GSM
- Podpora přesnějšího odhadu časového předstihu (timing advance) pro vzdálené mobilní stanice
- Definován pro použití v sítích GSM/EDGE (GERAN)
- Konfigurovatelné na úrovni buňky na základě vysílaných systémových informací

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.018** (Rel-19) — GSM Radio Resource Management Procedures
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.002** (Rel-19) — GSM/EDGE Radio Physical Layer Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 45.004** (Rel-19) — GSM/EDGE Modulation Specification
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [ESAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/esab/)
