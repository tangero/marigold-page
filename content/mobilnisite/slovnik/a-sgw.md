---
slug: "a-sgw"
url: "/mobilnisite/slovnik/a-sgw/"
type: "slovnik"
title: "A-SGW – Access Signalling Gateway"
date: 2025-01-01
abbr: "A-SGW"
fullName: "Access Signalling Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/a-sgw/"
summary: "Access Signalling Gateway (A-SGW) je prvek jádrové sítě zavedený ve specifikaci 3GPP Release 4. Funguje jako signalizační přeposílač a zprostředkovatel mezi rádiovou přístupovou sítí (RAN) a jádrovou"
---

A-SGW je prvek jádrové sítě, který přeposílá a zprostředkovává signalizační zprávy mezi rádiovou přístupovou sítí a jádrovou sítí pro okruhově přepínané služby přenášené po IP.

## Popis

Access Signalling Gateway (A-SGW) je klíčová funkční entita v architektuře jádrové sítě 3GPP, konkrétně pro okruhově přepínanou ([CS](/mobilnisite/slovnik/cs/)) doménu. Byla zavedena jako součást vývoje sítě směrem k plně IP přenosové infrastruktuře. Architektonicky je A-SGW umístěn mezi rádiovou přístupovou sítí (RAN), jako je Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)), a Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) jádrové sítě. Jeho hlavní funkcí je ukončovat a přeposílat signalizační protokoly. Na straně RAN používá rozhraní s tradičními okruhově přepínanými signalizačními protokoly, typicky založenými na [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7) s protokoly jako [BSSAP](/mobilnisite/slovnik/bssap/) (Base Station System Application Part) nebo [RANAP](/mobilnisite/slovnik/ranap/) (Radio Access Network Application Part). Na straně jádrové sítě tyto zprávy konvertuje a přenáší přes IP síť pomocí signalizačních transportních protokolů jako SIGTRAN (Signalling Transport), konkrétně vrstvy [M3UA](/mobilnisite/slovnik/m3ua/) (MTP3 User Adaptation) nebo SUA (SCCP User Adaptation). To umožňuje fyzické oddělení MSC od RAN a jejich propojení přes standardní IP síť, čímž se odděluje servisní logika od použité přenosové technologie.

Provozně A-SGW funguje jako signalizační proxy. Když BSC nebo RNC potřebuje komunikovat s MSC – například k provedení aktualizace polohy, navázání hlasového hovoru nebo zpracování předání spojení – odešle signalizační zprávu. A-SGW tuto zprávu přijme, zapouzdří signalizaci aplikační vrstvy (BSSAP/RANAP) do paketu adaptační vrstvy SIGTRAN a směruje ji přes IP síť k příslušnému MSC. Pro zprávy z MSC směrem k RAN probíhá proces obráceně. A-SGW je zodpovědný za správu signalizačních asociací, zajištění spolehlivého doručování a poskytování určité míry správy signalizačního provozu a zabezpečení na transportní vrstvě. Neinterpretuje zprávy vyšších vrstev pro řízení hovorů nebo správu mobility; jeho role je striktně zaměřena na spolehlivý transport a protokolovou adaptaci těchto zpráv.

Klíčové součásti funkčnosti A-SGW zahrnují obslužné moduly signalizačních rozhraní pro SS7 linky (např. používající MTP1, MTP2, MTP3), zásobník adaptační vrstvy SIGTRAN (M3UA/SUA přes SCTP/IP) a logiku správy spojení. Jeho role v síti je zásadní pro umožnění rozdělené architektury, kde může být MSC centralizováno nebo dokonce virtualizováno, zatímco prvky RAN mohou být distribuované. Toto oddělení snižuje náklady, zvyšuje škálovatelnost a zjednodušuje nasazení a údržbu sítě. A-SGW je základním kamenem rozdělené architektury 'MSC Server' definované ve specifikaci 3GPP Release 4, kde je řízení hovorů (MSC Server) odděleno od mediální brány (MGW). A-SGW zpracovává celou signalizační cestu k MSC Server, zatímco provoz uživatelské roviny (hlas) prochází samostatnou cestou přes Media Gateways (MGW).

## K čemu slouží

A-SGW byl vytvořen, aby řešil omezení tradičních monolitických architektur MSC v sítích 2G a raných 3G. V těchto systémech byl MSC jediný integrovaný uzel, který zpracovával jak signalizaci pro řízení hovorů, tak okruhově přepínané hlasové spojování, a byl přímo připojen k RAN přes vyhrazené TDM (Time-Division Multiplexing) linky pro signalizaci i uživatelskou rovinu. Tato architektura byla nepružná, nákladná na škálování a geograficky omezená, protože MSC muselo být fyzicky blízko obsluhovaných uzlů RAN, aby se udržely přijatelné signalizační zpoždění a náklady na linky.

Hlavní motivací pro zavedení A-SGW ve specifikaci Release 4 bylo umožnit přechod na IP transportní vrstvu jádrové sítě. Zavedením A-SGW mohli operátoři začít využívat nákladově efektivní, škálovatelné a všudypřítomné IP sítě (jako IP páteřní sítě) pro připojení distribuovaného RAN vybavení ke centralizovaným MSC. Tím se vyřešil problém drahého a nepružného TDM propojení. A-SGW konkrétně řeší problém signalizačního transportu tím, že poskytuje protokolovou konverzi mezi starší signalizací RAN založenou na SS7 a IP protokoly SIGTRAN, což umožňuje nasazení MSC Server nezávisle na použité přenosové technologii. Toto oddělení byl klíčový krok k softwarizaci sítě a následné virtualizaci síťových funkcí (NFV). Umožnilo efektivnější využití zdrojů, zjednodušilo rozšiřování sítě a připravilo cestu pro pozdější architektonické pokroky, jako je IMS (IP Multimedia Subsystem), tím, že stanovilo IP jako výchozí transport pro všechny domény jádrové sítě.

## Klíčové vlastnosti

- Protokolová konverze signalizace mezi protokoly RAN založenými na SS7 (BSSAP/RANAP) a IP protokoly SIGTRAN (M3UA/SUA)
- Umožňuje IP transport pro signalizaci okruhově přepínané jádrové sítě, čímž ji odděluje od tradičních TDM linek
- Podporuje rozdělenou architekturu MSC dle specifikace 3GPP Release 4 (MSC Server a MGW) tím, že poskytuje signalizační cestu k MSC Server
- Funguje jako signalizační přeposílač a proxy, spravuje SCTP asociace pro spolehlivý signalizační transport přes IP sítě
- Umožňuje geografickou flexibilitu tím, že podporuje centralizované nasazení MSC Server nezávisle na umístění RAN
- Poskytuje základ pro konsolidaci sítě a snížení nákladů využitím sdílené IP infrastruktury

## Související pojmy

- [MSS – Mobile Satellite Services](/mobilnisite/slovnik/mss/)
- [MGW – Media Gateway](/mobilnisite/slovnik/mgw/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)
- [M3UA – SS7 MTP3 – User Adaptation Layer](/mobilnisite/slovnik/m3ua/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [A-SGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-sgw/)
