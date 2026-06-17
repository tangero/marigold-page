---
slug: "gli"
url: "/mobilnisite/slovnik/gli/"
type: "slovnik"
title: "GLI – Global Line Identifier"
date: 2025-01-01
abbr: "GLI"
fullName: "Global Line Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gli/"
summary: "Globálně jednoznačný identifikátor pevné přístupové linky, standardizovaný v 3GPP pro konvergenci 5G. Jednoznačně identifikuje fyzickou linku (např. DSL, optické vlákno) spojující zákaznické místo se"
---

GLI je globálně jednoznačný identifikátor pevné přístupové linky, jako je DSL nebo optické vlákno, který umožňuje integrované ověřování a správu napříč pevnými a mobilními 5G sítěmi.

## Popis

Global Line Identifier (GLI) je klíčový identifikátor zavedený ve verzi 3GPP Release 16 jako součást podpory systému 5G pro Fixed Mobile Convergence ([FMC](/mobilnisite/slovnik/fmc/)) a integraci drátového přístupu. Je definován v několika specifikacích, včetně TS 23.003 (Číslování, adresování a identifikace), TS 29.561 (Interworking mezi 5GS a drátovým přístupem) a TS 31.102 (Aplikace UICC/USIM). GLI slouží jako trvalý, globálně jednoznačný štítek pro konkrétní fyzickou pevnou přístupovou linku, jako je Digital Subscriber Line ([DSL](/mobilnisite/slovnik/dsl/)), linka pasivní optické sítě (PON) nebo kabelové modemové připojení.

Z architektonického hlediska je GLI přidělen operátorem pevné sítě a je asociován s koncovým síťovým zařízením na zákaznickém místě (např. Residential Gateway nebo Optical Network Terminal). Ve scénáři konvergence 5G používá uživatelské zařízení (UE) – které může být například 5G residenční brána – GLI během registračních a autentizačních procedur přes pevnou přístupovou síť. GLI je přenášeno do 5G Core Network (5GC) v parametrech přístupové sítě během signalizace rozhraní [N2](/mobilnisite/slovnik/n2/) (např. v [NGAP](/mobilnisite/slovnik/ngap/) Initial UE Message nebo v autentizační signalizaci).

Jak funguje, zahrnuje několik síťových funkcí. Po přijetí GLI jej může funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) použít ke korelaci přístupové relace s daty účastníka. Funkce Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) může využít GLI, potenciálně spolu s dalšími přihlašovacími údaji, pro ověření a autorizaci. Klíčové je, že GLI umožňuje 5GC aplikovat specifické politiky pro danou pevnou linku prostřednictvím funkce Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Například umožňuje síti identifikovat, že přístup pochází z důvěryhodného pevného širokopásmového předplatného, a aplikovat příslušné politiky QoS, pravidla účtování nebo nároky na služby, které se liší od těch pro mobilní přístup.

Jeho role přesahuje pouhou identifikaci. GLI je klíčovým prvkem pro bezproblémový zážitek ze služeb napříč typy přístupu. Umožňuje operátorům nabízet jednotné tarify, kde jsou služby, bezpečnostní politiky a kvalita uživatelského zážitku předplatitele konzistentní, ať se připojí přes 5G rádio nebo domácí širokopásmovou linku. Dále napomáhá síťovému řezání pro pevný přístup, kde může být instance řezu asociována s konkrétní skupinou fyzických linek identifikovaných jejich GLI. Tato hluboká integrace identity pevné linky do jádra 5G je základním krokem k opravdu konvergentním sítím.

## K čemu slouží

GLI bylo vytvořeno k řešení problému oddělené identity a politik v konvergentních síťových architekturách. Před jeho standardizací fungovaly pevné a mobilní sítě z velké části odděleně. Pevná širokopásmová linka byla identifikována operátorsky specifickými, ne globálními identifikátory (jako jsou ID okruhů nebo hodnoty PVC/VPI) a mobilní jádro nemělo standardizovaný způsob, jak rozpoznat nebo důvěřovat větvi pevného přístupu. To bránilo nasazení skutečně jednotného ověřování, účtování a služebních politik napříč přístupovými doménami.

Motivace vycházela z průmyslového úsilí směrem k 5G Fixed Wireless Access ([FWA](/mobilnisite/slovnik/fwa/)) a hlubší Fixed Mobile Convergence. Operátoři chtěli využít své 5G jádro ke správě všech typů přístupu, včetně drátového, aby snížili provozní náklady a vytvořili nové balené služby. Globálně jednoznačný, standardizovaný identifikátor pro pevnou linku byl předpokladem této vize. Řeší omezení proprietárních nebo přístupovou technologií specifických identifikátorů, které nemohly být spolehlivě interpretovány společným mobilním jádrem sítě.

Poskytnutím GLI umožnilo 3GPP několik klíčových případů užití: bezpečné ověření residenční brány přes pevnou síť pomocí 5G přihlašovacích údajů (jako je SIM), aplikace specifických politik QoS a šířky pásma pro účastníka na základě možností fyzické linky a přesné účtování za konvergentní služby. Jeho zavedení ve verzi Release 16 byla přímá reakce na požadavky operátorů na jedinou, agilní jádrovou síť schopnou spravovat heterogenní přístup, což je ústřední princip návrhu systému 5G.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor pro fyzickou pevnou přístupovou linku
- Standardizovaný formát pro interoperabilitu napříč zařízeními a sítěmi různých dodavatelů
- Používá se v 5G registračních a autentizačních procedurách přes drátový přístup
- Umožňuje 5G jádru aplikovat politiky specifické pro linku prostřednictvím PCF
- Základní prvek pro scénáře 5G Fixed Mobile Convergence a Fixed Wireless Access
- Podporuje jednotnou správu účastníků a účtování napříč pevnou a mobilní doménou

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.594** (Rel-19) — 5G Spending Limit Control Service Stage 3
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [GLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gli/)
