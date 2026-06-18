---
slug: "pop-ran-dm"
url: "/mobilnisite/slovnik/pop-ran-dm/"
type: "slovnik"
title: "POP-RAN-DM – Participating Operator Radio Access Network Domain Manager"
date: 2025-01-01
abbr: "POP-RAN-DM"
fullName: "Participating Operator Radio Access Network Domain Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pop-ran-dm/"
summary: "Doménový manažer odpovědný za správu domény rádiového přístupového sítě (RAN) vlastněné účastnickým operátorem v nastavení s více operátory. Zajišťuje konfigurační, poruchový a výkonnostní management"
---

POP-RAN-DM je doménový manažer odpovědný za správu domény rádiového přístupového sítě (RAN) vlastněné účastnickým operátorem v nastavení s více operátory.

## Popis

Participating Operator Radio Access Network Domain Manager (POP-RAN-DM) je manažerská funkce specifikovaná v 3GPP TS 32.130, která se výhradně zaměřuje na doménu RAN účastnického operátora. V kolaborativním síťovém prostředí, jako je Multi-Operator RAN (MORAN) nebo Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)), je POP-RAN-DM entita, které je delegována pravomoc spravovat infrastrukturu RAN (např. gNB, ng-eNB, rádiové jednotky) přispěnou jejím operátorem. Funguje pod dohledem manažera vyšší úrovně, kterým může být vlastní [POP-NM](/mobilnisite/slovnik/pop-nm/) účastnického operátora nebo Network Manager hostitelského operátora.

Z architektonického hlediska rozhraní POP-RAN-DM směrem nahoru (northbound) komunikuje se svým nadřazeným manažerem pomocí standardizovaných rozhraní, jako je Itf-N, přes které přijímá servisní politiky, konfigurační šablony a požadavky na reportování výkonu. Směrem dolů (southbound) komunikuje se skutečnými síťovými prvky RAN pomocí dodavatelsky specifických nebo standardizovaných rozhraní pro správu prvků (např. založených na NETCONF/YANG pro 5G). Jeho vnitřní funkce zahrnují detailní konfigurační management RAN (např. nastavení parametrů buňky, správa sousedních relací, konfigurace agregace nosných), sledování výkonu v reálném čase (sběr [KPI](/mobilnisite/slovnik/kpi/), jako je propustnost, latence a kvalita rádiového signálu) a správu poruch (detekce a izolace problémů v doméně RAN).

Z provozní perspektivy POP-RAN-DM překládá servisní záměr vysoké úrovně (např. "poskytnout řez s vylepšeným mobilním širokopásmovým přístupem s propustností X") do specifických nastavení rádiových prostředků a konfigurace RAN. Hraje klíčovou roli při rozdělování a izolaci rádiových prostředků, když je RAN sdílena mezi více operátory nebo síťovými řezy. Zajišťuje, aby výkon domény RAN odpovídal dohodnutým [SLA](/mobilnisite/slovnik/sla/), a poskytuje detailní, doménově specifická data o poruchách a výkonu nadřazenému manažerovi pro zajištění služby end-to-end. Zapouzdřením komplexity správy RAN umožňuje POP-RAN-DM nadřazenému manažerovi zacházet s RAN jako se spravovatelnou službou typu "black-box", čímž zjednodušuje orchestraci více domén.

## K čemu slouží

POP-RAN-DM byl zaveden, aby řešil specifické výzvy správy sdílených rádiových přístupových sítí, které jsou často nejkomplexnější a nejnákladnější částí mobilní sítě na nasazení a provoz. V tradičních nasazeních jednoho operátora byla správa RAN interní záležitostí. S nástupem modelů sdílení RAN (MORAN, [MOCN](/mobilnisite/slovnik/mocn/)) a neutrálního hostitele však bylo zapotřebí mechanismu, který by umožnil operátorovi poskytnout přístup ke správě svých aktiv RAN bez vystavení plné kontroly nebo proprietárních detailů.

Účelem POP-RAN-DM je poskytnout bezpečný, standardizovaný a efektivní způsob delegování odpovědností za správu RAN. Řeší problém, jak integrovat RAN účastnického operátora do větší spravované služby, a zároveň zachovat schopnost operátora optimalizovat a řešit problémy na vlastním rádiovém vybavení. Umožňuje jasné provozní hranice: Network Manager hostitelského operátora spravuje celkovou službu, ale POP-RAN-DM si ponechává kontrolu nad parametry specifickými pro RAN, jako jsou úrovně výkonu, náklony antén a konfigurace rádiového nosiče. Toto oddělení je klíčové pro splnění regulatorních požadavků, zajištění kvality služeb pro vlastní účastníky účastnického operátora a umožnění inovací v technologii RAN v kontextu sdílené infrastruktury. Jeho vytvoření ve verzi 12 (Release 12) bylo motivováno ekonomickými přínosy a přínosy pro pokrytí plynoucími ze sdílení RAN, což vyžadovalo odpovídající rámec správy, aby bylo takové sdílení provozně praktické.

## Klíčové vlastnosti

- Delegovaná správa síťových prvků RAN (např. gNB) pro účastnického operátora
- Konfigurační management specifický pro RAN, včetně rádiových parametrů a nastavení buňky
- Sledování výkonu a sběr rádiově orientovaných klíčových ukazatelů výkonu (KPI)
- Detekce a lokalizace poruch v doméně RAN
- Abstrakce detailů správy RAN pro nadřazené Network Managery
- Podpora scénářů sdílení RAN, jako jsou MORAN a MOCN, prostřednictvím správy rozdělování prostředků

## Definující specifikace

- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements

---

📖 **Anglický originál a plná specifikace:** [POP-RAN-DM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pop-ran-dm/)
