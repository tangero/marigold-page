---
slug: "cjt"
url: "/mobilnisite/slovnik/cjt/"
type: "slovnik"
title: "CJT – Coherent Joint Transmission"
date: 2025-01-01
abbr: "CJT"
fullName: "Coherent Joint Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cjt/"
summary: "Coherent Joint Transmission (CJT) je koordinační technika více TRP (Transmission Reception Point), při níž více geograficky oddělených TRP vysílá stejný datový proud k jednomu UE s fázovým sladěním. T"
---

CJT je koordinační technika více TRP, při níž více oddělených vysílacích bodů koherentně vysílá stejný datový proud k jednomu uživatelskému zařízení, aby zvýšilo sílu signálu konstruktivní interferencí.

## Popis

Coherent Joint Transmission (CJT) je sofistikované schéma koordinace více bodů pro downlink, standardizované ve 3GPP Release 18. Funguje v rámci nasazení více TRP (mTRP), kde je uživatelské zařízení (UE) obsluhováno více vysílacími body současně. Na rozdíl od nekoherentního společného vysílání nebo koordinovaného plánování je definující vlastností CJT přesné fázové sladění vysílaných signálů od zúčastněných TRP. To vyžaduje pokročilou zpětnou vazbu informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) a těsnou synchronizaci mezi spolupracujícími TRP, často umožněnou vysokokapacitními přenosovými spoji s nízkou latencí v přístupové části sítě, typicky v rámci architektury centralizované nebo distribuované jednotky ([CU](/mobilnisite/slovnik/cu/)/[DU](/mobilnisite/slovnik/du/)).

Technická realizace závisí na schopnosti UE měřit a hlásit podrobné CSI pro každý TRP zapojený do potenciální CJT sady. Síť na základě této zpětné vazby vypočítává komplexní předkódovací váhy pro antény každého TRP. Tyto váhy upravují fázi (a volitelně amplitudu) vysílaného signálu tak, aby se více signálových drah dostalo k přijímači UE koherentně – tedy se stejnou fází. Tato konstruktivní superpozice mění to, co by bylo interferencí z více drah, na silný kombinovaný signál, což dramaticky zlepšuje přijímaný poměr signálu k šumu a interferenci (SINR). Z pohledu sítě je vysílání spravováno jako jeden fyzický downlinkový sdílený kanál ([PDSCH](/mobilnisite/slovnik/pdsch/)), ale s prostředky a vrstvami mapovanými napříč koordinovanými TRP.

Klíčové součásti umožňující CJT zahrnují rozšířený rámec CSI pro provoz s více TRP, specifikovaný v 38.214, a odpovídající signalizaci [RRC](/mobilnisite/slovnik/rrc/) pro konfiguraci CJT hypotéz a sad prostředků, podrobně popsanou v 38.331. UE musí podporovat schopnosti pro zpracování předpokladů kvazi-kolokace (QCL) vztahujících se k více TRP a pro výpočet kombinovaných ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) v rámci CJT hypotézy. Z pohledu sítě je centrální plánovací entita (např. v rámci CU) zodpovědná za dynamický výběr TRP, výpočet předkódování a společné přidělování prostředků, což vyžaduje koordinaci a sdílení dat mezi TRP v reálném čase.

Úlohou CJT je posouvat hranice spektrální účinnosti a pokrytí v hustých sítích 5G-Advanced. Je obzvláště účinná ve scénářích s vysokou pravděpodobností přímé viditelnosti mezi TRP a UE, jako jsou vnitřní hotspoty nebo nasazení na úrovni ulic. Tím, že mění interferenci na užitečnou energii signálu, CJT přímo zvyšuje propustnost a spolehlivost pro uživatele na okraji buňky, což z ní činí základní technologii pro dosažení konzistentního vysoce výkonného poskytování služeb v celé síti, což je klíčový požadavek pro pokročilé mobilní širokopásmové připojení a scénáře využití ultra-spolehlivé komunikace s nízkou latencí (URLLC).

## K čemu slouží

CJT byla vyvinuta k řešení základních omezení tradičních schémat vysílání z jedné buňky a základních vícebodových schémat. Jak se sítě zahušťují větším počtem malých buněk a TRP, stává se správa interference prvořadou. Jednoduchý výběr buňky nebo nekoordinované vysílání vede k vážné mezi-bunkové interferenci na hranicích a omezuje propustnost pro okrajové uživatele. Dřívější techniky více TRP, jako je Dynamický výběr bodu (DPS) nebo nekoherentní JT, zlepšovaly spolehlivost prostřednictvím makro-diverzity, ale nevyužívaly maximálně možný zisk výkonu signálu z přítomnosti více vysílacích bodů.

Primární motivací pro CJT je odemknout plný potenciál zhušťování sítí a massive [MIMO](/mobilnisite/slovnik/mimo/). Zatímco přidávání dalších TRP zvyšuje kapacitu, bez koherentní koordinace se výnosy snižují kvůli zvýšené interferenci. CJT to řeší tím, že umožňuje husté sadě TRP fungovat jako geograficky rozložený fázovaný anténní systém. To mění režim omezený interferencí na režim omezený výkonem, což síti umožňuje přesně zaměřovat vysokofrekvenční energii na uživatele. Řeší kritickou výzvu poskytování jednotně vysokých přenosových rychlostí a nízké latence nejen ve středu buňky, ale v celé servisní oblasti, což je nezbytné pro budoucí aplikace, jako je imerzivní XR a průmyslová automatizace.

Historicky bylo dosažení takové koherence považováno za nepraktické kvůli přísným požadavkům na synchronizaci a režii zpětné vazby [CSI](/mobilnisite/slovnik/csi/). Pokrok v technologiích přenosové části přístupové sítě (např. enhanced Common Public Radio Interface, eCPRI), výkonnější schopnosti zpracování UE a sofistikovaný návrh referenčních signálů (jako CSI-RS pro více TRP) v 5G NR však učinily CJT proveditelnou. Její zavedení v Rel-18 představuje významný krok nad rámec základních funkcí více připojení z dřívějších vydání, přecházející od vysílání orientovaného na diverzitu ke skutečné agregaci zisku beamformingu napříč více síťovými uzly.

## Klíčové vlastnosti

- Přesné fázové sladění vysílaných signálů z více TRP k jednomu UE
- Konstruktivní superpozice signálů na přijímači pro zvýšený SINR
- Spoléhá se na pokročilou zpětnou vazbu CSI pro více TRP a výpočet předkódování v síti
- Spravováno jako jedno PDSCH vysílání s prostředky rozdělenými napříč TRP
- Vyžaduje těsnou synchronizaci a koordinaci s nízkou latencí mezi zúčastněnými TRP
- Obzvláště účinná ve scénářích nasazení s přímou nebo téměř přímou viditelností

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CJT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cjt/)
