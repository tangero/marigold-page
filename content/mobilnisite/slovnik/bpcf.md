---
slug: "bpcf"
url: "/mobilnisite/slovnik/bpcf/"
type: "slovnik"
title: "BPCF – Broadband Policy Control Function"
date: 2025-01-01
abbr: "BPCF"
fullName: "Broadband Policy Control Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bpcf/"
summary: "Broadband Policy Control Function (BPCF) je funkce řízení politik v sítích 3GPP, která umožňuje aplikaci pravidel 3GPP pro řízení politik a účtování (PCC) na sítě s přístupem mimo 3GPP, jako je pevný"
---

BPCF je funkce řízení politik (policy control entity), která aplikuje pravidla 3GPP pro politiky a účtování (policy and charging rules) na sítě s přístupem mimo 3GPP (non-3GPP access networks) a funguje jako proxy pro umožnění jednotného řízení napříč heterogenními technologiemi, jako je pevný broadband.

## Popis

Broadband Policy Control Function (BPCF) je specializovaná síťová funkce zavedená ve verzi 3GPP Release 10 jako součást architektury Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) pro propojení s pevným broadband přístupem (Fixed Broadband Access Interworking). Jejím hlavním úkolem je sloužit jako proxy a překladač pro řízení politik mezi rámcem PCC jádrové sítě 3GPP a mechanismy řízení politik používanými v sítích s přístupem mimo 3GPP, konkrétně v pevných broadband sítích (např. [DSL](/mobilnisite/slovnik/dsl/), kabel, optika). Architektonicky se BPCF nachází v doméně operátora 3GPP, ale komunikuje s policy serverem pevné broadband sítě, typicky s Broadband Policy Server ([BPS](/mobilnisite/slovnik/bps/)) nebo s Resource and Admission Control Subsystem ([RACS](/mobilnisite/slovnik/racs/)) podle standardů jako [BBF](/mobilnisite/slovnik/bbf/) (Broadband Forum). BPCF sama negeneruje pravidla politik; místo toho přijímá PCC pravidla od funkce 3GPP Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a mapuje je na ekvivalentní rozhodnutí nebo požadavky politik, které lze vynutit v pevné přístupové síti. Toto mapování zahrnuje překlad parametrů QoS specifických pro 3GPP (jako [QCI](/mobilnisite/slovnik/qci/), [ARP](/mobilnisite/slovnik/arp/), GBR, MBR) do parametrů srozumitelných pro vymáhací body politik v pevné síti, jako jsou brány nebo směrovače.

Operačně BPCF spolupracuje s PCRF a Packet Data Network Gateway (PGW) nebo Gateway GPRS Support Node (GGSN) pro uživatelský provoz. Když uživatel naváže připojení PDN přes důvěryhodnou síť s přístupem mimo 3GPP (jako spravovaná pevná Wi-Fi síť operátora), PGW komunikuje s PCRF pro rozhodnutí o politikách. Pokud je přístupová síť pevná broadband síť, PCRF identifikuje potřebu vzájemného propojení a komunikuje s BPCF. BPCF poté používá referenční bod S9a* založený na protokolu Diameter (nebo Rx+ v některých nasazeních) pro rozhraní s PCRF a používá jiné protokoly (jako Diameter nebo proprietární rozhraní) pro komunikaci s policy serverem pevné sítě. To umožňuje, aby centralizovaná rozhodnutí PCRF – pokrývající detekci toku služeb (service data flow detection), uzavírání (gating), řízení QoS a účtování – byla vynucována end-to-end, i když je přístup na poslední míli realizován technologií mimo 3GPP.

Klíčové komponenty BPCF zahrnují obslužné rutiny rozhraní pro stranu 3GPP (S9a*) a stranu pevné sítě, funkci pro překlad politik a logiku správy relací. Udržuje vazbu (binding) mezi relací 3GPP IP-CAN (IP Connectivity Access Network) a odpovídající relací v pevném broadbandu. To umožňuje scénáře, jako je plynulý přechod mobility mezi přístupem 3GPP a pevným přístupem (např. handover asistovaný ANDSF) s konzistentní aplikací politik. BPCF je obzvláště důležitá v kontextu konvergence pevných a mobilních sítí nové generace (Next Generation Fixed-Mobile Convergence, FMC), kde operátoři usilují o poskytnutí jednotné uživatelské zkušenosti. Rozšířením 3GPP PCC na pevný přístup mohou operátoři nabízet garantovanou QoS pro služby jako IPTV, VoIP nebo priorizovaný podnikový provoz přes své broadband linky, aplikovat konzistentní modely účtování a implementovat pokročilé rodičovské kontroly nebo bezpečnostní politiky napříč všemi typy přístupu.

## K čemu slouží

BPCF byla vytvořena, aby řešila rostoucí potřebu konvergence pevných a mobilních sítí (Fixed-Mobile Convergence, FMC) a jednotného řízení politik napříč heterogenními sítěmi. Před jejím zavedením měly sítě 3GPP vyspělou architekturu PCC (PCRF, PCEF) pro mobilní přístup, ale pevné broadband sítě používaly samostatné, často proprietární systémy řízení politik (jako RACS od BBF). To vytvářelo izolované celky (silos), kde operátoři nemohli aplikovat konzistentní QoS, účtování nebo servisní politiky na účastníky používající jak mobilní, tak pevné služby. Například služba streamování videa mohla mít garantovanou QoS na LTE, ale na domácím Wi-Fi účastníka přes DSL byla doručována jako best-effort, což vedlo k roztříštěné uživatelské zkušenosti. BPCF to řeší tím, že propojuje tyto dvě domény politik.

Historický kontext je zakořeněn v práci na "Fixed Broadband Access Interworking" ve verzi 3GPP Release 10, kterou poháněla snaha operátorů využít své pevné aktiva (jako optiku nebo kabel) k odlehčení mobilního provozu (např. přes Wi-Fi) nebo nabízet balíčkové služby. Omezením předchozích přístupů byl nedostatek standardizovaného rozhraní mezi PCRF 3GPP a policy servery pevných sítí. Bez BPCF jakékoli vzájemné propojení vyžadovalo složité, na dodavateli závislé integrace, které nebyly škálovatelné. BPCF poskytuje standardizovanou funkci definovanou 3GPP, která překládá rozhodnutí PCRF do akcí v pevné síti, což operátorům umožňuje nasadit konvergované řízení politik. To umožňuje nové obchodní modely, jako je jednotné účtování za pevná a mobilní data nebo prémiová QoS pro hraní her přes oba typy přístupu.

Dále BPCF podporuje regulatorní a technické požadavky, jako je zákonné odposlouchávání (Lawful Interception, LI) a vylepšené účtování, tím, že zajišťuje, aby události politik z pevného přístupu mohly být hlášeny zpět do účtovacích systémů 3GPP. Také usnadňuje optimalizaci síťových zdrojů tím, že umožňuje PCRF mít holistický pohled na využití zdrojů účastníka napříč všemi typy přístupu, což umožňuje chytřejší politiky směrování provozu a řízení přetížení ve skutečně konvergované síti.

## Klíčové vlastnosti

- Funguje jako proxy a překladač politik mezi 3GPP PCRF a policy servery pevného broadbandu (např. BBF RACS)
- Umožňuje aplikaci pravidel 3GPP PCC (QoS, uzavírání, účtování) na sítě s pevným přístupem mimo 3GPP
- Podporuje referenční bod S9a* (založený na protokolu Diameter) pro komunikaci s PCRF
- Usnadňuje konvergenci pevných a mobilních sítí (FMC) poskytováním jednotného řízení politik napříč přístupovými technologiemi
- Umožňuje konzistentní QoS a účtování pro účastníky používající jak mobilní, tak pevné broadband služby
- Podporuje vazbu relací (session binding) pro scénáře mobility mezi přístupem 3GPP a důvěryhodným přístupem mimo 3GPP

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.810** (Rel-13) — Diameter Load Control Study

---

📖 **Anglický originál a plná specifikace:** [BPCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bpcf/)
