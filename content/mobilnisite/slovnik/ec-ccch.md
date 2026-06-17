---
slug: "ec-ccch"
url: "/mobilnisite/slovnik/ec-ccch/"
type: "slovnik"
title: "EC-CCCH – Extended Coverage Common Control CHannel"
date: 2025-01-01
abbr: "EC-CCCH"
fullName: "Extended Coverage Common Control CHannel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-ccch/"
summary: "Logický kanál v GSM/EDGE pro rozšířené pokrytí, který kombinuje funkce RACH, AGCH a PCH. Zpracovává zprávy pro počáteční přístup, volání a přiřazení pro IoT zařízení v oblastech se slabým pokrytím. Je"
---

EC-CCCH je robustní logický kanál GSM/EDGE pro rozšířené pokrytí, který kombinuje funkce RACH, AGCH a PCH pro zvládnutí počátečního přístupu, volání a přiřazení pro IoT zařízení ve špatných signálových podmínkách.

## Popis

EC-CCCH (Extended Coverage Common Control CHannel) je složený logický kanál definovaný pro GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiový přístupový systém ([GERAN](/mobilnisite/slovnik/geran/)) v dokumentu 3GPP TS 44.060 jako součást sady funkcí EC-GSM-IoT. Jedná se o verzi standardního společného řídicího kanálu ([CCCH](/mobilnisite/slovnik/ccch/)) pro rozšířené pokrytí. Na rozdíl od vyhrazených kanálů je EC-CCCH sdílený prostředek používaný pro přenos řídicích informací mezi sítí a mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)), které aktuálně nepoužívají vyhrazený kanál. Funkčně spojuje uplinkové a downlinkové aspekty procedur počátečního přístupu k síti a zřizování hovorů v režimu rozšířeného pokrytí ([EC](/mobilnisite/slovnik/ec/)).

Technicky EC-CCCH zahrnuje několik podkanálů. Ve směru uplink zahrnuje Extended Coverage Random Access Channel ([EC-RACH](/mobilnisite/slovnik/ec-rach/)), který zařízení používají k vyžádání signalizačního kanálu odesláním přístupového pulzu. Ve směru downlink zahrnuje Extended Coverage Access Grant Channel ([EC-AGCH](/mobilnisite/slovnik/ec-agch/)) pro odesílání zpráv okamžitého přiřazení a Extended Coverage Paging Channel ([EC-PCH](/mobilnisite/slovnik/ec-pch/)) pro upozorňování zařízení na příchozí transakce. Klíčovým provozním mechanismem napříč všemi těmito podkanály je použití rozsáhlých opakování. Každá zpráva – ať už jde o přístupový pulz, přiřazení nebo volání – je přenášena vícekrát přes mnoho rádiových bloků. To umožňuje přijímači použít techniky kombinování k úspěšnému dekódování i při velmi nízkých poměrech signálu k šumu, čímž se dosahuje cíle rozšíření pokrytí o +20 dB.

Role tohoto kanálu je ústřední pro řídicí rovinu EC-GSM-IoT. Typická procedura zahrnuje, že zařízení naslouchá EC-BCCH pro získání systémových informací, které obsahují podrobné parametry plánování pro EC-CCCH. Když zařízení potřebuje zahájit transakci (např. odeslat data nebo reagovat na volání), vysílá opakované přístupové pulzy na podkanálu EC-RACH. Síť po jejich přijetí odpoví opakovaně přenášenou zprávou o přiřazení na podkanálu EC-AGCH. Podobně síť volá zařízení odesíláním opakovaných zpráv s identitou na podkanálu EC-PCH. Integrací těchto funkcí do jediného robustně navrženého logického kanálu poskytuje EC-CCCH kompletní a pokrytím vylepšené řešení pro veškerou společnou řídicí signalizaci potřebnou k přechodu IoT zařízení z klidového stavu do vyhrazeného spojení.

## K čemu slouží

EC-CCCH byl vytvořen k řešení komplexního problému selhání společné řídicí signalizace v prostředích s hlubokým pokrytím pro IoT zařízení. Standardní procedury GSM CCCH, zahrnující jednorázový nebo omezený přenos přístupových pulzů, volacích zpráv a přiřazení, byly v cílových scénářích EC-GSM-IoT vysoce náchylné k selhání. To činilo zařízení nedostupnými nebo neschopnými zahájit komunikaci, což znemožňovalo účel spolehlivé IoT sítě.

Motivací bylo navrhnout jednotnou strukturu řídicího kanálu, která aplikuje princip rozšíření pokrytí – masivní opakování – na celý dialog počátečního přístupu a volání. Předchozí přístupy zacházely s těmito signalizačními kroky odděleně, ale EC-CCCH poskytuje integrované řešení. Zajišťuje, že každý krok v procesu přechodu zařízení z klidového do připojeného stavu je stejně robustní. Tím se řeší omezení nevylepšeného CCCH, protože se garantuje, že volací zprávy dosáhnou hluboko uvnitř budov umístěných zařízení, že jejich přístupové požadavky síť uslyší a že přidělení zdrojů od sítě se úspěšně vrátí k zařízení. Tato robustnost od konce ke konci je tím, co činí EC-GSM-IoT životaschopnou a spolehlivou technologií pro aplikace kritického strojového komunikace (MTC) na stávající infrastruktuře GSM.

## Klíčové vlastnosti

- Složený logický kanál integrující EC-RACH (uplink), EC-AGCH a EC-PCH (downlink)
- Využívá rozsáhlé opakovací kódování napříč všemi podkanály pro hluboké pokrytí
- Zpracovává kompletní proceduru počátečního přístupu pro zařízení EC-GSM-IoT
- Spravuje funkci volání pro upozorňování zařízení v rozšířeném pokrytí
- Je plánován na základě parametrů vysílaných na EC-BCCH
- Poskytuje jednotnou, robustní signalizační cestu pro řídicí procedury v klidovém režimu a při navazování spojení

## Související pojmy

- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [EC-RACH – Extended Coverage Random Access Channel](/mobilnisite/slovnik/ec-rach/)
- [EC-AGCH – Extended Coverage Access Grant CHannel](/mobilnisite/slovnik/ec-agch/)
- [EC-PCH – Extended Coverage Paging Channel](/mobilnisite/slovnik/ec-pch/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-CCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-ccch/)
