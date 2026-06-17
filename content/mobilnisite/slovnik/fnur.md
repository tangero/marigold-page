---
slug: "fnur"
url: "/mobilnisite/slovnik/fnur/"
type: "slovnik"
title: "FNUR – Fixed Network User Rate"
date: 2025-01-01
abbr: "FNUR"
fullName: "Fixed Network User Rate"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fnur/"
summary: "Standardizovaný parametr kvality služby (QoS) v 3GPP, který definuje garantovanou, konstantní přenosovou rychlost pro přenos uživatelských dat přes segment pevné sítě. Zajišťuje předvídatelný výkon pr"
---

FNUR je standardizovaný parametr kvality služby (QoS) 3GPP, který definuje garantovanou, konstantní přenosovou rychlost pro přenos uživatelských dat přes segment pevné sítě, aby zajistil předvídatelný výkon.

## Popis

Fixed Network User Rate (FNUR, uživatelská rychlost v pevné síti) je identifikátor třídy QoS standardizovaný ve specifikacích 3GPP, konkrétně podrobně popsaný v dokumentech TS 22.034 a slovníku TS 21.905. Patří do rodiny parametrů QoS navržených pro charakterizaci požadovaných schopností zpracování provozu pro různé služby v síti. FNUR konkrétně definuje třídu provozu, kde je přenosová rychlost uživatelských dat sítí garantována jako konstantní a pevná. To je v protikladu k proměnlivým nebo best-effort přenosovým rychlostem a poskytuje deterministickou alokaci šířky pásma.

Z architektonického hlediska je FNUR implementován v rámci frameworku řízení politik a účtování (PCC) v jádru sítě. Když je vytvořen datový tok služby – například pro videohovor ve vysoké kvalitě – aplikační funkce ([AF](/mobilnisite/slovnik/af/)) nebo samotné uživatelské zařízení (UE) může požadovat specifickou QoS včetně FNUR. Tento požadavek zpracuje funkce Policy and Charging Rules Function (PCRF), která jej převede na konkrétní pravidla řízení politik a účtování (PCC). Tato pravidla jsou pak vynucována v bránových uzlech, jako je Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v 4G nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G, což zajišťuje, že datový tok po celou dobu své relace obdrží předem alokovanou, konstantní přenosovou rychlost.

Klíčový provozní princip zahrnuje rezervaci zdrojů a řízení přístupu. Síť musí před přijetím relace zkontrolovat, zda jsou k dispozici dostatečné zdroje (např. šířka pásma na pevných backhaulových spojích), aby mohla poskytnout požadovanou pevnou rychlost. Po přijetí relace funkce monitorování a tvarování provozu v místech vynucení zajistí, že uživatelský provoz odpovídá smluvně dohodnutému FNUR, přičemž mohou nadlimitní pakety označovat nebo zahazovat. Tento mechanismus je klíčový pro udržování smluv o úrovni služeb (SLA) a poskytování předvídatelného uživatelského zážitku pro aplikace v reálném čase s konstantní přenosovou rychlostí, čímž tvoří základní prvek řízené QoS v konvergovaných pevných a mobilních sítích.

## K čemu slouží

FNUR byl zaveden, aby vyřešil potřebu garantované, předvídatelné datové propustnosti pro specifické aplikace v telekomunikačních sítích. Rané datové služby primárně nabízely best-effort doručování, což bylo nedostatečné pro aplikace v reálném čase, jako je VoIP nebo videokonference, které trpí kolísáním zpoždění a ztrátou paketů při proměnlivé šířce pásma. Vytvoření standardizovaných parametrů QoS, jako je FNUR, umožnilo síťovým operátorům nabízet služby s různými úrovněmi a s výkonnostními zárukami.

Historický kontext spočívá ve vývoji standardů 3GPP pro podporu multimediálních služeb. Jak sítě postupovaly od základního hlasu a SMS k bohatým multimédiím, požadavek na diferencované zacházení s provozem se stal prvořadým. FNUR jako součást širšího frameworku QoS definovaného ve vydání Release 4 poskytl nástroj pro modelování a podporu zdrojů provozu s konstantní přenosovou rychlostí ([CBR](/mobilnisite/slovnik/cbr/)). Vyřešil problém, jak formálně požadovat a síťově spravovat službu, která potřebuje stabilní, neměnnou šířku pásma, což umožnilo spolehlivou podporu starších CBR kodeků a některých streamovacích protokolů v rámci paketově spínaného paradigmatu.

Odstranil omezení předchozích IP sítí typu 'jedna velikost pro všechny' tím, že umožnil explicitní rezervaci zdrojů. Bez takového parametru by podpora vysoce kvalitních služeb v reálném čase vyžadovala masivní nadměrnou dimenzaci nebo by vedla ke špatné kvalitě. FNUR umožnil efektivní využití sítě při splnění přísných výkonnostních kritérií, což usnadnilo komerční zavádění prémiových služeb s garantovanou přenosovou rychlostí.

## Klíčové vlastnosti

- Definuje konstantní, garantovanou přenosovou rychlost pro datové toky uživatele
- Integruje se s architekturou 3GPP Policy and Charging Control (PCC) pro dynamické vynucování politik
- Umožňuje řízení přístupu, aby se zabránilo přetížení sítě pro garantované služby
- Podporuje monitorování a tvarování provozu na síťových bránách pro vynucení smluvní rychlosti
- Zásadní pro podporu aplikací v reálném čase s přísnými požadavky na zpoždění a jeho kolísání
- Poskytuje základ pro smlouvy o úrovni služeb (SLA) mezi operátory a zákazníky

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1

---

📖 **Anglický originál a plná specifikace:** [FNUR na 3GPP Explorer](https://3gpp-explorer.com/glossary/fnur/)
