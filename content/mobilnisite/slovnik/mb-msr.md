---
slug: "mb-msr"
url: "/mobilnisite/slovnik/mb-msr/"
type: "slovnik"
title: "MB-MSR – Multi-Band Multi-Standard Radio"
date: 2025-01-01
abbr: "MB-MSR"
fullName: "Multi-Band Multi-Standard Radio"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mb-msr/"
summary: "Typ rádiové jednotky základnové stanice schopný současně vysílat a přijímat více rádiových přístupových technologií (např. GSM, UMTS, LTE) napříč více kmitočtovými pásmy. Umožňuje modernizaci sítě a e"
---

MB-MSR je rádiová jednotka základnové stanice schopná současně vysílat a přijímat více rádiových přístupových technologií napříč více kmitočtovými pásmy, což umožňuje modernizaci sítě a efektivní využití spektra díky konsolidaci zařízení.

## Popis

Multi-Band Multi-Standard Radio (MB-MSR, vícepásmová více standardní radiostanice) označuje sofistikovanou architekturu základnové stanice, konkrétně jednotku vysokofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) transceiveru, navrženou pro podporu více standardů mobilní komunikace (např. GSM, [WCDMA](/mobilnisite/slovnik/wcdma/), LTE, NR) a současný provoz napříč více kmitočtovými pásmy na jedné hardwarové platformě. Tato schopnost je charakteristickým rysem moderního vybavení rádiové přístupové sítě (RAN) a představuje odklon od zastaralého modelu nasazování samostatných, jednopásmových, jednotechnologických rádiových jednotek pro každý standard. Jednotka MB-MSR integruje širokopásmové výkonové zesilovače, filtry a softwarově definované rádiové komponenty, které lze dynamicky konfigurovat pro generování a zpracování signálů pro různá rozhraní vzduchu.

Architektonicky se základnová stanice typu MB-MSR typicky skládá z jednotky pro základnové pásmo (baseband) a jedné nebo více rádiových jednotek MB-MSR (často nazývaných Remote Radio Heads - [RRH](/mobilnisite/slovnik/rrh/)). Klíčová inovace spočívá v schopnosti rádiové jednotky pracovat v širokém rozsahu spektra, často prostřednictvím použití širokopásmových výkonových zesilovačů a vícekanálových technik. Dokáže vytvářet více nezávislých signálů nosných pro různé technologie a pásma, které jsou následně kombinovány a vysílány společným anténním systémem za použití filtrů a kombinátorů, aby se zabránilo interferenci. Na straně příjmu separuje a zpracovává příchozí signály z různých podporovaných pásem a standardů.

Její provoz je zásadně závislý na pokročilém digitálním zpracování signálu a softwarovém řízení. Jednotka základnového pásma posílá do jednotky MB-MSR digitalizované datové toky [IQ](/mobilnisite/slovnik/iq/) odpovídající různým nosným a standardům. Rádiová jednotka je následně převádí na analogové RF signály, zesiluje je a zvládá komplexní úkol udržení linearity a účinnosti napříč širokou šířkou pásma. To umožňuje, aby jediné místo podporovalo služby 2G, 3G, 4G a 5G současně, což dramaticky zjednodušuje infrastrukturu lokality, snižuje spotřebu energie a optimalizuje využití vzácných spektrálních zdrojů. MB-MSR je základní technologií pro iniciativy modernizace sítě, jako je sdílení RAN a plynulá migrace na novější technologie.

## K čemu slouží

MB-MSR byla vyvinuta k řešení provozních a ekonomických výzev, kterým čelí operátoři mobilních sítí při získávání nových kmitočtových pásem a nasazování postupných generací rádiové technologie (2G, 3G, 4G). Tradiční přístup vyžadoval instalaci samostatných rádiových zařízení pro každé pásmo a každý standard, což vedlo k přeplněnosti lokalit, zvýšeným kapitálovým a provozním výdajům (CapEx/OpEx), vyšší spotřebě energie a složité údržbě. Technologie MB-MSR tyto problémy řeší umožněním konsolidace hardwaru.

K jejímu vzniku motivovala potřeba větší spektrální flexibility a modernizace sítě. Když operátoři přebudovávali spektrum ze starších technologií (jako GSM) na novější (jako LTE nebo 5G NR), potřebovali flexibilní rádiový hardware, který by bylo možné přenastavovat pomocí softwaru. MB-MSR tuto flexibilitu poskytuje a umožňuje operátorům dynamicky upravovat přidělování kapacity mezi technologiemi na základě poptávky. Dále podporuje efektivní sdílení RAN více operátory, protože jedna jednotka MB-MSR může hostit nosné pro různé operátory. Šlo o klíkový vývoj oproti zařízením typu Single-Band Single-Standard Radio (SB-SSR), který připravil cestu pro softwarově definované, cloud-nativní architektury RAN plánované pro budoucí sítě.

## Klíčové vlastnosti

- Současná podpora více RAT (např. GSM, WCDMA, LTE, NR) z jedné jednotky
- Provoz napříč více, často nesousedními, kmitočtovými pásmy (např. 700 MHz, 1800 MHz, 2100 MHz, 2600 MHz)
- Využívá širokopásmové výkonové zesilovače a vícekanálové přenosové techniky
- Umožňuje softwarově konfigurovatelné přidělování nosných a podporu technologií
- Snižuje prostorové nároky na lokalitě, spotřebu energie a celkové náklady na vlastnictví
- Usnadňuje plynulé přebudování spektra a migraci technologií

## Související pojmy

- [RRH – Remote Radio Head](/mobilnisite/slovnik/rrh/)

## Definující specifikace

- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements

---

📖 **Anglický originál a plná specifikace:** [MB-MSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/mb-msr/)
