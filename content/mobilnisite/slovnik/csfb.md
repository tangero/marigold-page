---
slug: "csfb"
url: "/mobilnisite/slovnik/csfb/"
type: "slovnik"
title: "CSFB – Circuit Switched Fallback"
date: 2025-01-01
abbr: "CSFB"
fullName: "Circuit Switched Fallback"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csfb/"
summary: "Circuit Switched Fallback (CSFB) je mechanismus 3GPP, který umožňuje zařízením v síti LTE přistupovat k legacy službám hlasu a SMS v přepojování okruhů tím, že dočasně přepnou na sítě 2G/3G. Byl klíčo"
---

CSFB je mechanismus 3GPP, který umožňuje zařízením v síti LTE přistupovat k legacy službám hlasu a SMS v přepojování okruhů tím, že dočasně přepnou na sítě 2G nebo 3G.

## Popis

Circuit Switched Fallback (CSFB) je standardizované řešení mobility definované 3GPP, které umožňuje uživatelskému zařízení (UE) připojenému k síti LTE přistupovat ke službám domény přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) – především hovorům a SMS – tím, že dočasně přesměruje UE na síť 2G ([GERAN](/mobilnisite/slovnik/geran/)) nebo 3G (UTRAN), která tyto legacy služby podporuje. Architektura spoléhá na těsnou integraci mezi LTE Evolved Packet Core (EPC) a legacy sítí přepojování okruhů, zprostředkovanou rozhraním SGs mezi Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPC a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) Server v CS core. Toto rozhraní umožňuje kombinované procedury připojení EPS/[IMSI](/mobilnisite/slovnik/imsi/), koordinaci pagingu a správu mobility pro CS služby, zatímco je UE registrováno v LTE.

Když UE s podporou CSFB provádí počáteční připojení k síti LTE, oznámí svou CSFB schopnost MME, které následně provede kombinované připojení EPS/IMSI přes rozhraní SGs, aby zaregistrovalo UE jak pro paketové služby LTE, tak pro CS služby v legacy MSC. MSC udržuje stav CS registrace UE a považuje UE za ve stavu 'SGs-associated', přičemž MME funguje jako proxy pro signalizaci CS domény. Pro CS služby s příchozím voláním (jako příchozí hovor) MSC odešle požadavek na paging přes SGs k MME, které následně provede paging UE přes LTE rádiové rozhraní pomocí signalizace S1-AP. Po přijetí pagingu UE zahájí CSFB procedury pro přechod na buňku 2G/3G.

Samotný mechanismus přepnutí zahrnuje několik možných metod definovaných ve specifikacích 3GPP. Nejběžnější je PS Handover, kde síť připraví handover UE z LTE na buňku 2G/3G s vyhrazeným kanálem pro přenos hovoru pro CS hovor. Alternativně lze použít Cell Change Order ([CCO](/mobilnisite/slovnik/cco/)) nebo [RRC](/mobilnisite/slovnik/rrc/) Connection Release with Redirection, kde je UE instruováno, aby opustilo LTE a připojilo se k určené buňce 2G/3G, a poté tam navázalo CS spojení. Volba závisí na schopnostech sítě, podpoře UE a konfiguraci operátora. Po ukončení CS služby (např. hovoru) se UE typicky vrací do LTE pomocí mechanismů jako Fast Return nebo převýběr v idle módu, v závislosti na síťových politikách a schopnostech UE.

Klíčové síťové prvky zahrnují UE (které musí podporovat CSFB a příslušné rádiové přístupové technologie 2G/3G), eNodeB (který spravuje řízení rádiových zdrojů během přepnutí), MME (které koordinuje s MSC a zajišťuje správu mobility) a MSC Server (který poskytuje logiku CS služby). Řešení vyžaduje dostatečné překrytí pokrytí LTE a 2G/3G a UE musí podporovat měření a procedury pro cílovou RAT. CSFB bylo kritické přechodné řešení, které umožnilo operátorům rychle zavést služby LTE dat, přičemž se mohli spolehnout na zralé, stávající sítě s přepojováním okruhů pro hlas, a získat tak čas pro vývoj a nasazení nativních řešení hlasu přes LTE jako VoLTE.

## K čemu slouží

CSFB bylo vytvořeno, aby řešilo zásadní výzvu v raném nasazování sítí LTE: LTE bylo navrženo jako plně IP systém pouze s přepojováním paketů bez nativní podpory služeb přepojování okruhů, přičemž hlasová telefonie a SMS byly nezbytné služby generující příjmy, které operátoři nemohli opustit. Když bylo LTE poprvé standardizováno v Release 8, hlas přes LTE (VoLTE) založený na IP Multimedia Subsystem (IMS) byl stále nezralý, vyžadoval významné nasazení IMS core a chyběla mu široká podpora zařízení. Operátoři potřebovali praktický způsob, jak nabízet hlasové služby na svých nových sítích LTE, aniž by museli čekat na vývoj plného ekosystému VoLTE.

Tato technologie vyřešila problém kontinuity služeb pro účastníky migrující na LTE zařízení a sítě. Bez CSFB by zařízení pouze s LTE nebyla schopna uskutečňovat nebo přijímat tradiční hlasové hovory, což by vážně omezilo adopci LTE. CSFB umožnilo operátorům využít jejich stávající investice do sítí přepojování okruhů ([MSC](/mobilnisite/slovnik/msc/)) a rádiových přístupových sítí (GERAN/UTRAN) při zavádění LTE pro vysokorychlostní data. Poskytlo přechodovou technologii, která zajistila, že účastníci mohou používat jedno zařízení jak pro LTE data, tak pro legacy hlas, s bezproblémovým přepnutím spouštěným automaticky při zahájení nebo přijetí hovoru.

CSFB řešilo specifická omezení předchozích přístupů, které mohly zahrnovat zařízení s duálním rádiem pracující současně na LTE a 2G/3G, což vedlo k vyšší spotřebě baterie a nákladům. Standardizací procedur přepnutí umožnilo 3GPP efektivní, sítí řízenou mobilitu mezi RAT. Také vyřešilo problém koordinace pagingu – zajištění, že příchozí CS hovory mohou dosáhnout UE připojeného k LTE prostřednictvím signalizace mezi MME a MSC. To učinilo nasazení LTE komerčně životaschopným v časovém období 2010-2015 a sloužilo jako dominantní řešení hlasu pro LTE, dokud VoLTE nedozrálo a nebylo široce nasazeno.

## Klíčové vlastnosti

- Umožňuje LTE UE přistupovat k legacy službám hlasu a SMS v přepojování okruhů
- Používá rozhraní SGs mezi MME a MSC pro kombinované připojení EPS/IMSI a koordinaci pagingu
- Podporuje více mechanismů přepnutí: PS Handover, Cell Change Order (CCO) a uvolnění RRC spojení s přesměrováním
- Umožňuje spouštění CS služeb s příchozím i odchozím voláním z LTE
- Zahrnuje mechanismy pro návrat do LTE po dokončení CS služby (např. Fast Return)
- Vyžaduje podporu relevantních RAT 2G/3G a CSFB procedur na straně UE

## Definující specifikace

- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 48.008** (Rel-19) — BSS-MSC Interface Layer 3 Procedures

---

📖 **Anglický originál a plná specifikace:** [CSFB na 3GPP Explorer](https://3gpp-explorer.com/glossary/csfb/)
