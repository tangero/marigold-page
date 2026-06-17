---
slug: "esn"
url: "/mobilnisite/slovnik/esn/"
type: "slovnik"
title: "ESN – Electronic Serial Number"
date: 2025-01-01
abbr: "ESN"
fullName: "Electronic Serial Number"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/esn/"
summary: "Elektronické sériové číslo (ESN) je jedinečný identifikátor přiřazený mobilnímu zařízení, který se historicky používal pro autentizaci a registraci zařízení v mobilních sítích. Slouží jako hardwarová"
---

ESN je jedinečný hardwarový identifikátor přiřazený mobilnímu zařízení, který se historicky používal pro jeho autentizaci, registraci a řízení přístupu k síti v mobilních sítích.

## Popis

Elektronické sériové číslo (ESN) je trvalý, ve výrobě naprogramovaný identifikátor vestavěný do hardwaru mobilního zařízení. Je základní součástí správy identity zařízení v mobilních sítích, zejména u starších generací jako CDMA2000 a UMTS. ESN je 32bitové číslo, tradičně reprezentované jako osmiciferná hexadecimální hodnota, které jedinečně identifikuje konkrétní kus mobilní stanice. Jeho primární úlohou je poskytnout neměnný hardwarový podpis, který síť může použít k rozpoznání a autentizaci zařízení.

Z architektonického hlediska je ESN uloženo v nevolatilní paměti v základnovém nebo rádiovém modulu mobilního zařízení. Během procedur registrace do sítě nebo navazování hovoru zařízení svůj ESN přenáší do sítě. Síťová infrastruktura, konkrétně Autentizační centrum (AuC) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo podobné entity, toto číslo používá jako součást procesů ověřování účastníka a zařízení. ESN je klíčový parametr v algoritmech, které generují autentizační vektory a zabezpečují rozhraní vzduchu.

V provozním kontextu sítě ESN funguje ve spojení s dalšími identifikátory, jako je International Mobile Equipment Identity ([IMEI](/mobilnisite/slovnik/imei/)) nebo Mobile Equipment Identifier ([MEID](/mobilnisite/slovnik/meid/)). Zatímco IMEI se stalo globálním standardem pro GSM a následné technologie, ESN zůstalo významné v systémech založených na [CDMA](/mobilnisite/slovnik/cdma/) a některých regulačních doménách. Umožňuje funkce jako blokování odcizených zařízení, prevenci podvodů a přesné účtování tím, že váže využití služby ke konkrétnímu fyzickému zařízení. Databáze síťového operátora uchovává záznam platných ESN a může odepřít službu zařízením nahlášeným jako odcizená nebo jinak neoprávněná.

Jeho technická implementace zahrnuje začlenění ESN do signalizačních zpráv přes rozhraní vzduchu. Například v CDMA systémech je součástí Registration Message nebo Origination Message odesílané na přístupovém kanálu. Subsystém základnové stanice tuto informaci předává do jádra sítě ke zpracování. Integrita a jedinečnost ESN jsou prvořadé; proto je jeho přidělování řízeno centrální autoritou (jako Telecommunications Industry Association v Severní Americe pro klasická ESN), aby se zabránilo duplikaci a zajistila globální jedinečnost v rámci jeho oblasti použití.

## K čemu slouží

ESN bylo vytvořeno k řešení základního problému jedinečné identifikace mobilního hardwaru v síti. Před jeho zavedením sítě postrádaly spolehlivou, standardizovanou metodu, jak na hardwarové úrovni rozlišit jednotlivá zařízení. To ztěžovalo implementaci funkcí jako autentizace zařízení, prevence krádeží a poskytování služeb založených na zařízení. ESN poskytlo neměnné, ve výrobě přiřazené číslo, které se stalo základním kamenem pro správu a zabezpečení zařízení.

Historický kontext spočívá v raném vývoji analogových a digitálních mobilních systémů, zejména v Severní Americe se sítěmi AMPS a později [CDMA](/mobilnisite/slovnik/cdma/). Regulátoři a operátoři potřebovali mechanismus, jak zabránit přístupu naklonovaných telefonů (kde je identita legitimního telefonu zkopírována do podvodného zařízení) k síti, což byla hlavní příčina ztráty příjmů. ESN, které je pevně zakódováno v zařízení, bylo mnohem obtížnější změnit než identifikátory založené na účastníkovi, čímž vytvořilo bariéru proti tomuto typu podvodu. Umožnilo vytvoření registrů identit zařízení ([EIR](/mobilnisite/slovnik/eir/)), kde mohla být uložena černá listina ESN a služba odepřena.

ESN dále řešilo potřebu funkcí a odstraňování problémů specifických pro dané zařízení. Síťoví operátoři mohli sledovat problémy s výkonem nebo závady spojené s konkrétními modely nebo várkami zařízení podle jejich rozsahů ESN. Také usnadňovalo proces počáteční aktivace, kdy síť mohla automaticky rozpoznat nové zařízení a asociovat jej s účtem účastníka. Zatímco jeho význam poklesl s globálním přijetím [IMEI](/mobilnisite/slovnik/imei/) v technologiích odvozených od GSM (3GPP), koncept ESN položil základy pro všechna následující schémata identifikace mobilních zařízení a zdůraznil nezbytnost bezpečného, jedinečného hardwarového identifikátoru ve škálovatelném telekomunikačním systému.

## Klíčové vlastnosti

- Jedinečný 32bitový hardwarový identifikátor pro mobilní zařízení
- Naprogramován ve výrobě a uložen v nevolatilní paměti
- Používá se pro autentizaci zařízení a řízení přístupu k síti
- Umožňuje blokování odcizených nebo podvodných zařízení prostřednictvím Equipment Identity Register (EIR)
- Integrální součást signalizačních zpráv během registrace a zahájení hovoru
- Historicky klíčové pro provoz CDMA sítí a prevenci podvodů

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [MEID – Mobile Equipment IDentity](/mobilnisite/slovnik/meid/)

## Definující specifikace

- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface

---

📖 **Anglický originál a plná specifikace:** [ESN na 3GPP Explorer](https://3gpp-explorer.com/glossary/esn/)
