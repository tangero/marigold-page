---
slug: "avc"
url: "/mobilnisite/slovnik/avc/"
type: "slovnik"
title: "AVC – Assured Voice Communication"
date: 2026-01-01
abbr: "AVC"
fullName: "Assured Voice Communication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/avc/"
summary: "Assured Voice Communication (AVC) je služební funkce 3GPP navržená k zajištění vysokokvalitní hlasové komunikace s vyšší spolehlivostí a prioritou, zejména pro aplikace s kritickými požadavky (mission"
---

AVC je služební funkce 3GPP navržená k zajištění vysokokvalitní, spolehlivé a prioritní hlasové komunikace pro aplikace s kritickými požadavky (mission-critical), která zaručuje preferenční zacházení v síti při přetížení.

## Popis

Assured Voice Communication (AVC) je standardizovaná služební schopnost v sítích 3GPP, která poskytuje prioritní a spolehlivé služby hlasové komunikace. Funguje tak, že vytváří vyhrazenou služební vrstvu, která interaguje s funkcemi jádra sítě – včetně funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) – aby vynutila specifické politiky kvality služeb (QoS) pro hlasový provoz. Architektura zajišťuje, že AVC relace jsou identifikovány, autorizovány a směrovány s vyšší prioritou než provoz typu best-effort, přičemž využívá identifikátory třídy QoS ([QCI](/mobilnisite/slovnik/qci/)) a parametry priority přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)) k zaručení alokace prostředků i během přetížení sítě.

Na technické úrovni implementace AVC zahrnuje několik klíčových komponent pracujících v součinnosti. Aplikační funkce ([AF](/mobilnisite/slovnik/af/)), často součást serveru pro komunikaci s kritickými požadavky, vyžádá službu AVC prostřednictvím funkce vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo u PCF. PCF pak tento požadavek přeloží do konkrétních pravidel politik, která jsou doručena SMF, jež nakonfiguruje UPF, aby uplatňovala příslušná pravidla pro přeposílání paketů. To zahrnuje označování paketů pomocí kódových bodů služeb s diferenciovaným přístupem ([DSCP](/mobilnisite/slovnik/dscp/)) s vysokou prioritou a zajištění cest s nízkou latencí přes přenosovou síť. Systém také zahrnuje účtovací funkce pro oddělené sledování využití AVC od standardních hlasových služeb.

Služba funguje tak, že vytváří prioritní přenosový kanál (bearer) typu end-to-end speciálně pro hlasový provoz. Když je zahájena AVC relace, síť provede rozšířené kontroly řízení přístupu, aby ověřila, že jsou k dispozici dostatečné prostředky pro udržení požadované úrovně kvality. Během celé relace probíhá nepřetržité monitorování jak v řídicí rovině (pro kontinuitu relace), tak v uživatelské rovině (pro metriky ztráty paketů, zpoždění a kolísání). Pokud se síťové podmínky zhorší, AVC relace dostanou preferenční zacházení v procesech přerozdělování prostředků, což může zahrnovat vytěsnění provozu s nižší prioritou za účelem udržení kvality hlasu. Tento mechanismus je klíčový pro scénáře veřejné bezpečnosti, kde spolehlivost komunikace může přímo ovlivnit efektivitu operací a bezpečnost.

Role AVC v síti přesahuje pouhou priorizaci; představuje komplexní rámec pro zajištěnou komunikaci. Integruje se s IMS (IP Multimedia Subsystem) pro řízení relací a přidává specializovaná vylepšení pro spolehlivost. Služba podporuje různé provozní režimy včetně hovorů typu point-to-point, skupinové komunikace a scénářů nouzového vysílání. Dále AVC zahrnuje záložní mechanismy pro udržení kontinuity služby během předávání mezi různými přístupovými technologiemi (např. z LTE na 5G NR) nebo při výpadcích prvků jádra sítě, což zajišťuje, že kritická hlasová komunikace zůstane dostupná i v náročných síťových podmínkách.

## K čemu slouží

AVC bylo vytvořeno, aby vyřešilo kritickou potřebu spolehlivé hlasové komunikace pro veřejnou bezpečnost, záchranné složky a průmyslové aplikace s kritickými požadavky. Před jeho standardizací spoléhaly organizace veřejné bezpečnosti na vyhrazené systémy pozemní mobilní radiokomunikace (LMR), které nabízely spolehlivost, ale postrádaly šířku pásma, datové schopnosti a úspory z rozsahu komerčních mobilních sítí. Zatímco komerční Voice over LTE (VoLTE) poskytovalo vysokokvalitní hlas, nemohlo zaručit dostupnost služby během přetížení sítě nebo mimořádných událostí, kdy zatížení sítě dramaticky vzroste. Toto omezení se stalo zvláště zřejmým během přírodních katastrof a rozsáhlých mimořádných událostí, kdy byly komerční sítě zahlceny, což znemožňovalo efektivní komunikaci záchranným složkám.

Technologie řeší několik klíčových problémů: Za prvé poskytuje deterministickou kvalitu služeb pro hlasovou komunikaci i v podmínkách přetížené sítě. Za druhé umožňuje orgánům veřejné bezpečnosti využívat komerční buněčnou infrastrukturu při zachování standardů spolehlivosti vyžadovaných pro komunikaci kritickou pro životy. Za třetí usnadňuje interoperabilitu mezi různými agenturami a jurisdikcemi tím, že poskytuje standardizovaný přístup k prioritní komunikaci. Tím se řeší historická výzva fragmentovaných komunikačních systémů, která bránila koordinovaným záchranným akcím.

Motivováno poučením z velkých mimořádných událostí po celém světě začal 3GPP vyvíjet AVC jako součást širších standardů pro komunikaci s kritickými požadavky. Vytvoření bylo hnací silou požadavků organizací veřejné bezpečnosti z celého světa, které potřebovaly alternativy k tradičním LMR systémům založené na buněčné technologii. AVC konkrétně řeší omezení předchozích přístupů tím, že poskytuje standardizovaný mechanismus fungující napříč více generacemi buněčné technologie (od 4G LTE přes 5G a dále), což zajišťuje dlouhodobou životaschopnost a zpětnou kompatibilitu při současném splnění přísných požadavků na spolehlivost služeb hlasové komunikace s kritickými požadavky.

## Klíčové vlastnosti

- Zaručená QoS s vytvořením vyhrazeného přenosového kanálu (bearer) pro hlasový provoz
- Rozšířené řízení přístupu upřednostňující AVC relace před standardním provozem
- Prioritizace typu end-to-edge napříč rádiovým přístupem, přenosovou sítí a jádrem sítě
- Integrace s IMS pro řízení a správu relací
- Podpora nouzových záložních mechanismů a mechanismů kontinuity služby
- Oddělené účtování a řízení politik pro komunikaci s kritickými požadavky

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.790** (Rel-15) — FRMCS Gap Analysis and Architecture Enhancements
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [AVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/avc/)
