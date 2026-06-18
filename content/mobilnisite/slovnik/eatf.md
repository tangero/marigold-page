---
slug: "eatf"
url: "/mobilnisite/slovnik/eatf/"
type: "slovnik"
title: "EATF – Emergency Access Transfer Function"
date: 2025-01-01
abbr: "EATF"
fullName: "Emergency Access Transfer Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eatf/"
summary: "Funkce jádra sítě, která spravuje přenos nouzových relací, jako jsou hovory na tísňové linky (např. 112, 150), mezi různými přístupovými sítěmi nebo doménami jádra sítě. Zajišťuje kontinuitu a spolehl"
---

EATF je funkce jádra sítě, která spravuje přenos nouzových relací mezi přístupovými sítěmi nebo doménami jádra sítě, aby zajistila kontinuitu a spolehlivost hovoru při předávání spojení.

## Popis

Funkce pro přenos nouzového přístupu (Emergency Access Transfer Function, EATF) je klíčová funkční entita v subsystému IP multimédií (IMS) pro tísňové služby. Jejím hlavním úkolem je spravovat a usnadňovat přenos probíhající nouzové relace (např. nouzového hovoru v IMS) z jedné přístupové sítě do jiné nebo mezi různými doménami v rámci jádra sítě, při zachování nouzového kontextu relace a spojení s příslušným přijímacím střediskem tísňového volání ([PSAP](/mobilnisite/slovnik/psap/)). EATF slouží jako kotvící bod pro nouzovou relaci. Když uživatelské zařízení (UE) s aktivním nouzovým hovorem zahájí předání spojení – například při přechodu z LTE na Wi-Fi nebo mezi 3GPP a non-3GPP přístupem – EATF zajistí opětovné navázání signalizační a mediální cesty bez přerušení hovoru.

Z architektonického hlediska EATF interaguje s několika funkcemi jádra IMS. Typicky komunikuje s funkcí Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), což je první kontaktní bod pro UE v IMS, a funkcí Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), která zajišťuje řízení relace. Při navazování nouzové relace může P-CSCF identifikovat hovor jako nouzový a zapojit EATF. EATF se pak vloží do signalizační cesty, často jako back-to-back uživatelský agent ([B2BUA](/mobilnisite/slovnik/b2bua/)). To jí umožňuje udržovat kontrolu nad oběma větvemi hovoru: jednou větví směrem k UE a druhou směrem k PSAP. Spravuje deskriptory relace a může uchovávat více alternativních mediálních adres pro UE.

Jeho fungování zahrnuje průběžné monitorování a proaktivní správu. EATF má přehled o přístupových schopnostech UE a stavu její registrace. Když je zjištěna nebo zahájena podmínka pro předání spojení (např. prostřednictvím indikací ze sítě nebo od UE), EATF koordinuje přenos. Může použít mechanismy jako protokol [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) s metodami re-INVITE nebo REFER k aktualizaci parametrů relace na straně PSAP, zatímco UE znovu navazuje připojení přes nový přístup. Tento proces je navržen jako bezproblémový, aby se minimalizovalo přerušení nouzové komunikace. EATF také hraje roli při zpětném nouzovém volání; pokud PSAP potřebuje zavolat zpět UE, která zahájila nouzovou relaci, EATF může pomoci směrovat zpětné volání na aktuální umístění a typ přístupu UE.

## K čemu slouží

EATF byla zavedena, aby vyřešila kritický problém v nouzových službách založených na IMS: zachování kontinuity nouzového hovoru při mobilitě přístupu. Před její standardizací by se nouzové hovory navázané přes jeden typ přístupu (např. LTE) pravděpodobně přerušily, pokud by se uživatel přesunul do oblasti pokrytí používající jinou technologii (např. Wi-Fi nebo starší okruhově spínanou síť). To bylo pro životně důležitou komunikaci nepřijatelné. Vývoj směrem k plně IP sítím a rostoucí podpora hlasu přes non-3GPP přístup (jako je Wi-Fi) vytvořily složité mobilní prostředí, se kterým si tradiční architektury nouzových služeb nedokázaly poradit.

Její vytvoření ve verzi 3GPP Release 9 bylo motivováno regulatorními požadavky na spolehlivé nouzové služby a přechodem odvětví na IMS jako jedinou platformu pro hlasové a komunikační služby. EATF řeší omezení předchozích řešení pro nouzové služby specifických pro přístup tím, že poskytuje centralizovanou, na přístupu nezávislou funkci v jádru IMS. Zajišťuje, že kontext nouzové služby (jako je spojení s [PSAP](/mobilnisite/slovnik/psap/) a priorita hovoru) je zachován přes hranice sítí. To je nezbytné nejen pro mobilitu uživatele, ale také pro scénáře odolnosti sítě, jako je přenos nouzových relací při výpadku uzlu jádra sítě nebo při zhoršení primárního rádiového přístupu UE.

## Klíčové vlastnosti

- Kotví nouzové relace IMS pro přenos přístupu
- Působí jako back-to-back uživatelský agent (B2BUA) ve signalizační cestě
- Podporuje přenos mezi 3GPP a non-3GPP přístupovými sítěmi (např. z LTE na Wi-Fi)
- Udržuje kontext nouzové relace a spojení s PSAP během předání spojení
- Umožňuje zpětné nouzové volání z PSAP k roamujícímu UE
- Spolupracuje s funkcemi P-CSCF, S-CSCF a získávání polohy

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [EATF na 3GPP Explorer](https://3gpp-explorer.com/glossary/eatf/)
