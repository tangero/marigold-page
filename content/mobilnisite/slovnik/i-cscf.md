---
slug: "i-cscf"
url: "/mobilnisite/slovnik/i-cscf/"
type: "slovnik"
title: "I-CSCF – Interrogating-Call Session Control Function"
date: 2026-01-01
abbr: "I-CSCF"
fullName: "Interrogating-Call Session Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/i-cscf/"
summary: "Centrální směrovací uzel pro dotazy v IP Multimedia Subsystem (IMS). Jeho hlavní úlohou je identifikovat správný Serving-CSCF (S-CSCF) pro účastníka během registrace a směrovat k němu příchozí požadav"
---

I-CSCF (Interrogating-Call Session Control Function) je centrální směrovací uzel pro dotazy v IMS, který identifikuje správný S-CSCF pro účastníka a směruje k němu příchozí požadavky na relaci, přičemž slouží jako první kontaktní bod v domácí síti pro relace z externích sítí.

## Popis

Interrogating-Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/icscf/)) je základní [SIP](/mobilnisite/slovnik/sip/) proxy v jádru 3GPP IP Multimedia Subsystem (IMS), definovaná v mnoha specifikacích počínaje 3GPP Release 5. Nachází se na okraji domácí IMS sítě operátora. Když se User Equipment (UE) registruje v IMS síti, registrační požadavek po průchodu přes Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) dorazí k I-CSCF. Klíčovým úkolem I-CSCF je dotázat se Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) přes rozhraní Cx (pomocí protokolu Diameter), aby určil, který Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) má být uživateli přiřazen, nebo aby zjistil již přiřazený S-CSCF.

Během registrace I-CSCF přijme veřejnou nebo privátní identitu účastníka. Odešle HSS žádost o autorizaci uživatele (User Authorization Request, [UAR](/mobilnisite/slovnik/uar/)). HSS odpoví s požadovanými schopnostmi pro S-CSCF (S-CSCF capabilities), nebo, pokud je S-CSCF již přiřazen, s jeho adresou. I-CSCF pak tyto informace použije buď k výběru vhodného S-CSCF ze skupiny na základě požadovaných schopností, nebo k přeposlání registračního požadavku přímo již přiřazenému S-CSCF. Tento proces zajišťuje vyrovnávání zátěže a efektivní přiřazování S-CSCF.

Pro příchozí požadavky na relaci (například příchozí VoIP hovor) slouží I-CSCF jako vstupní bod do domácí sítě z externí sítě (například IMS jiného operátora). Požadavek je směrován na I-CSCF na základě [DNS](/mobilnisite/slovnik/dns/) dotazů na doménu domácí sítě. I-CSCF se pak dotáže HSS pomocí žádosti o informace o poloze (Location Information Request, [LIR](/mobilnisite/slovnik/lir/)), aby získal adresu S-CSCF, který aktuálně obsluhuje volanou stranu. Jakmile obdrží adresu S-CSCF, proxyuje SIP INVITE požadavek na tento S-CSCF pro další zpracování a doručení k UE.

Dále může I-CSCF poskytovat funkci skrytí topologie. Tím, že slouží jako jediný kontaktní bod, může skrýt konfiguraci, kapacitu a topologii vnitřní sítě (S-CSCF) před externími sítěmi. Může také mít roli při prosazování bezpečnostních politik sítě na hranici domácí sítě. Jeho činnost je bezstavová s ohledem na jednotlivé relace, zaměřuje se na směrování a interakci s HSS.

## K čemu slouží

I-CSCF byla vytvořena jako součást původní architektury IMS (3GPP R5) k řešení kritických problémů se směrováním a škálovatelností ve velké, multioperátorské síti služeb založené na SIP. V čisté SIP síti bez takové funkce by bylo obtížné najít server zodpovědný za konkrétního uživatele a mohlo by dojít k odhalení struktury vnitřní sítě.

Jejím hlavním účelem je poskytovat zjistitelný, stabilní vstupní bod do IMS sítě domácího operátora. To umožňuje jiným sítím směrovat relace k uživateli bez nutnosti znát konkrétní interní server (S-CSCF), který spravuje registraci tohoto uživatele. Odděluje veřejně směrovatelnou adresu uživatele (doména domácí sítě) od interního, potenciálně proměnlivého přiřazení serveru. To umožňuje vyrovnávání zátěže mezi více S-CSCF a umožňuje obnovu po selhání S-CSCF bez dopadu na externí směrování.

Navíc I-CSCF prostřednictvím své interakce s HSS centralizuje logiku pro přiřazování S-CSCF na základě profilů služeb uživatele a síťových schopností. To umožňuje optimalizované přidělování zdrojů. Plní také zásadní bezpečnostní a soukromou roli skrytím topologie vnitřní sítě před externími subjekty, čímž brání potenciálním útočníkům v mapování sítě nebo přímém cílení na konkrétní interní servery. Byla to klíčová inovace, která učinila IMS životaschopnou architekturou pro operátorské, interoperabilní multimediální služby.

## Klíčové vlastnosti

- Slouží jako první kontaktní bod v domácí síti pro příchozí SIP zprávy (REGISTER, INVITE).
- Dotazuje se HSS přes rozhraní Cx založené na Diameteru, aby získal informace o přiřazení S-CSCF.
- Vybere nebo identifikuje příslušný S-CSCF pro účastníka během registrace.
- Směruje příchozí požadavky na relaci k S-CSCF, který aktuálně obsluhuje volanou stranu.
- Poskytuje určitý stupeň skrytí topologie pro vnitřní IMS síť před externími protějšky.
- Podporuje vyrovnávání zátěže mezi fondem uzlů S-CSCF v domácí síti.

## Související pojmy

- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- … a dalších 29 specifikací

---

📖 **Anglický originál a plná specifikace:** [I-CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-cscf/)
