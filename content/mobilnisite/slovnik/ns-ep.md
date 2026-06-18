---
slug: "ns-ep"
url: "/mobilnisite/slovnik/ns-ep/"
type: "slovnik"
title: "NS/EP – National Security and Emergency Preparedness"
date: 2025-01-01
abbr: "NS/EP"
fullName: "National Security and Emergency Preparedness"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ns-ep/"
summary: "NS/EP označuje telekomunikační služby a schopnosti s prioritou určené pro použití národními bezpečnostními složkami a záchrannými týmy během krizí nebo národních stavů nouze. V rámci 3GPP zahrnuje sta"
---

NS/EP je rámec 3GPP pro prioritní telekomunikační standardy, včetně prioritní služby a vytěsnění, zajišťující spolehlivou komunikaci pro národní bezpečnostní a krizové složky při přetížení sítě nebo v krizových situacích.

## Popis

Národní bezpečnost a připravenost na krizové situace (National Security and Emergency Preparedness – [NS](/mobilnisite/slovnik/ns/)/[EP](/mobilnisite/slovnik/ep/)) v kontextu 3GPP definuje rámec požadavků, schopností a funkcí v mobilních sítích pro podporu komunikace autorizovaných vládních uživatelů a záchranných složek v období krize, katastrofy nebo národní nouze. Nejde o jedinou technologii, ale o komplexní soubor standardizovaných služebních prvků, které zajišťují, že kritická komunikace může být zachována i při extrémním přetížení, částečném výpadku nebo cíleném útoku na veřejné sítě. Specifikace 3GPP, jako jsou TS 22.854 (Požadavky na službu pro NS/EP), TS 22.862 (Prioritní služba) a TS 22.953 (Misi kritické služby), tvoří základ těchto schopností.

Architektonicky jsou funkce NS/EP integrovány napříč více síťovými doménami. Mezi klíčové komponenty patří uživatelské zařízení (UE), které musí podporovat identifikační moduly a klientské funkce pro prioritní přístup; rádiový přístupový síť (RAN), která implementuje plánování rádiových zdrojů a řízení přístupu na základě priority; a jádro sítě (Core Network), které zajišťuje autorizaci služby, správu relací a vynucování politik. Ústředním prvkem je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), který ukládá profily účastníků s uvedením úrovní autorizace pro NS/EP (např. úrovně priority). Funkce Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) tyto profily používá k formulaci politik, které jsou vynucovány funkcí Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G, nebo analogickými uzly v předchozích generacích.

Fungování zahrnuje vícevrstvý přístup. Za prvé, **Prioritní služba** zajišťuje, že hovory nebo relace autorizovaných uživatelů NS/EP dostávají vyšší prioritu v síťových procedurách. To zahrnuje prioritní přístup (získání signalizačního kanálu během náhodného přístupu), prioritní plánování (získání rádiových zdrojů při přetížení) a prioritní fronty v prvcích jádra sítě. Za druhé, **Vytěsnění** může být vyvoláno při extrémním nedostatku zdrojů. To umožňuje, aby relace NS/EP s vysokou prioritou odpojila nebo degradovala existující relaci s nižší prioritou, aby uvolnila potřebné zdroje. Síť používá standardizované identifikátory kvality služby (QoS) (hodnoty [QCI](/mobilnisite/slovnik/qci/)/5QI vyhrazené pro prioritní služby) k rozlišení provozu. Za třetí, funkce **Odolnosti a Robustnosti** zajišťují kontinuitu služby. To zahrnuje mechanismy pro přechod na jiné rádiové přístupové technologie (např. z 5G na 4G), směrování relací přes geograficky rozmanité síťové cesty a podporu služby v izolovaném režimu pro omezenou místní komunikaci při ztrátě backhaulového spojení. Kompletní vyvolání služby je typicky spuštěno tím, že UE během registrace a navázání relace indikuje své prioritní přihlašovací údaje, které síť ověřuje vůči pravidlům politik.

## K čemu slouží

Standardizace schopností NS/EP v rámci 3GPP byla motivována kritickou potřebou zajistit, aby mobilní sítě, které se staly primární komunikační infrastrukturou, mohly sloužit jako spolehlivý nástroj pro národní bezpečnostní agentury, záchranné složky (policie, hasiči, zdravotníci) a vládní vedení během katastrofických událostí. Historické události, jako jsou přírodní katastrofy (např. zemětřesení, hurikány) a teroristické útoky, ukázaly, že veřejné sítě se rychle přetíží, což znemožňuje efektivní koordinaci záchranných týmů. Před standardizovanými funkcemi NS/EP byla řešení často proprietární, specifická pro daný stát, nebo se spoléhala na samostatné vyhrazené sítě (jako TETRA nebo FirstNet), které jsou nákladné a postrádají všudypřítomnost a pokročilé funkce komerčních celulárních sítí.

Práce 3GPP integruje tyto kritické schopnosti přímo do komerčních standardů, což umožňuje síťovým operátorům nabízet je jako servisní vrstvu. Tím se řeší omezení předchozích přístupů využitím rozsahu, kontinuální inovace a širokého pokrytí veřejných sítí při současném zajištění garantovaného přístupu pro autorizované uživatele. Řeší problém scénářů "síť obsazena" zavedením řízené priority v rámci sdíleného fondu zdrojů. Dále poskytuje globálně harmonizovaný rámec, který je nezbytný pro interoperabilitu během mezinárodních incidentů nebo pro roaming záchranného personálu. Vytvoření těchto standardů představuje společný úsilí telekomunikačního průmyslu a vládních subjektů směřující ke zvýšení veřejné bezpečnosti a národní bezpečnosti prostřednictvím lepší odolnosti komunikace.

## Klíčové vlastnosti

- Prioritní přístup, plánování a fronty pro autorizované uživatele při přetížení sítě.
- Mechanismy vytěsnění pro uvolnění zdrojů pro komunikaci s nejvyšší prioritou.
- Použití standardizovaných identifikátorů QoS (např. specifických hodnot 5QI) pro provoz NS/EP.
- Autorizace a řízení politik na síťové úrovni pro vyvolání služby NS/EP.
- Podpora kontinuity služby a odolnosti, včetně přechodů a izolovaného provozu.
- Rámec použitelný napříč architekturami systémů 4G (EPS) a 5G (5GS).

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.862** (Rel-14) — Critical Communications Feasibility Study
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [NS/EP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ns-ep/)
