---
slug: "m3ua"
url: "/mobilnisite/slovnik/m3ua/"
type: "slovnik"
title: "M3UA – SS7 MTP3 – User Adaptation Layer"
date: 2025-01-01
abbr: "M3UA"
fullName: "SS7 MTP3 – User Adaptation Layer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/m3ua/"
summary: "M3UA je adaptační vrstva SIGTRAN, která umožňuje přenos signalizačních zpráv SS7 MTP3 přes IP sítě na IP aplikační servery. Umožňuje telekomunikačním aplikacím, jako je ISUP nebo SCCP, běžet přes IP,"
---

M3UA je adaptační vrstva SIGTRAN, která přenáší signalizační zprávy SS7 MTP3 přes IP sítě, aby umožnila telekomunikačním aplikacím, jako je ISUP, fungovat v IP architekturách typu softswitch a IMS.

## Popis

M3UA ([SS7](/mobilnisite/slovnik/ss7/) [MTP3](/mobilnisite/slovnik/mtp3/) – User Adaptation Layer) je klíčový protokol v sadě [IETF](/mobilnisite/slovnik/ietf/) SIGTRAN, přijatý organizací 3GPP, který adaptuje Signalizační systém č. 7 (SS7), konkrétně jeho část Message Transfer Part Level 3 (MTP3), pro přenos přes IP sítě. Umožňuje komunikaci mezi tradičními síťovými prvky SS7, jako jsou Signalizační přepojovací uzly ([STP](/mobilnisite/slovnik/stp/)), a IP aplikačními servery ([AS](/mobilnisite/slovnik/as/)), například softswitche nebo uzly IP Multimedia Subsystem (IMS). Architektonicky M3UA funguje v modelu klient-server, kde Signalizační brána ([SG](/mobilnisite/slovnik/sg/)) s funkcí M3UA spolupracuje s IP aplikačním serverem (AS). SG ukončuje linky SS7 MTP3 ze starší sítě, zapouzdřuje zprávy MTP3 (a jejich vložené uživatelské části jako [ISUP](/mobilnisite/slovnik/isup/) nebo [SCCP](/mobilnisite/slovnik/sccp/)) do paketů M3UA a přenáší je přes asociace protokolu Stream Control Transmission Protocol (SCTP) k AS.

Jak M3UA funguje, zahrnuje několik vrstev a procedur. Na SG vrstva M3UA přijímá zprávy MTP3, včetně jednotek Message Signal Units (MSU) obsahujících datovou část ISUP, TUP nebo SCCP. Odstraní směrovací štítek MTP3 a přidá hlavičku M3UA, která obsahuje informace jako typ Protocol Data Unit (PDU), síťový vzhled (network appearance) a směrovací kontext. Tento zapouzdřený paket je pak předán SCTP pro spolehlivý přenos přes IP k jednomu nebo více AS. Na AS vrstva M3UA dekapacituje paket, rekonstruuje informace o doručení MTP3 a předá zprávu nadřazené aplikaci (např. zásobníku ISUP), jako kdyby dorazila přes tradiční rozhraní MTP3. M3UA také spravuje stav cílů a tras SS7 prostřednictvím správy stavu ASP (Application Server Process), včetně procedur ASP Up/Down a ASP Active/Inactive, za účelem řízení toku provozu a zajištění redundance.

Klíčové komponenty zahrnují Signalizační bránu (SG), Aplikační server (AS) a samotnou vrstvu M3UA s jejími různými typy zpráv: přenosové zprávy pro datovou část, zprávy správy signalizační sítě SS7 (SSNM) pro stav tras a zprávy pro údržbu stavu ASP. Její role v síti je zásadní v architekturách příští generace, protože umožňuje oddělení řízení hovorů a servisní logiky od starších okruhově přepínaných tras. Je široce používána v sítích Voice over IP (VoIP), v IMS pro přenos signalizace ISUP přes IP (např. v MGCF) a v jádrových sítích 4G/5G pro určité scénáře vzájemného propojení, poskytuje škálovatelnost, flexibilitu a úsporu nákladů ve srovnání se signalizací založenou na TDM.

## K čemu slouží

M3UA byla vyvinuta za účelem usnadnění evoluce telefonních sítí z okruhově přepínaných infrastruktur TDM na paketově přepínané IP sítě. Historicky signalizace SS7 pro řízení hovorů (ISUP) a databázové služby (SCCP/TCAP) zcela závisela na MTP3 přes fyzické linky TDM (MTP1/MTP2). Tato architektura byla rigidní, nákladná na škálování a nekompatibilní s nově vznikajícími IP platformami služeb, jako jsou softswitche a aplikační servery. Omezení spočívalo v neschopnosti IP aplikací přímo komunikovat se signalizační sítí SS7 bez nákladných a složitých bran, které prováděly konverzi protokolů na vyšších vrstvách.

Primární problém, který M3UA řeší, je umožnění bezproblémového přenosu signalizace uživatelských částí MTP3 (např. ISUP, SCCP) přes IP na distribuované aplikační servery, čímž odděluje servisní logiku od fyzických signalizačních linek. Umožňuje síťovým operátorům nasazovat IP prvky pro řízení hovorů, které mohou odesílat a přijímat standardní zprávy SS7, aniž by vyžadovaly kompletní zásobník SS7 s hardwarovou vrstvou MTP2. To podporuje architektury, kde signalizační brány koncentrují linky SS7 a přeposílají signalizační provoz přes IP na více geograficky rozptýlených aplikačních serverů, čímž zlepšují využití zdrojů a umožňují nové modely nasazování služeb.

Její vznik byl hnán cílem pracovní skupiny IETF SIGTRAN definovat kompletní sadu adaptačních vrstev pro SS7 přes IP. M3UA konkrétně řeší scénář "backhaul", kde je aplikace (uživatel MTP3) vzdálena od sítě SS7. To bylo motivováno vzestupem VoIP a potřebou standardizovaných, interoperabilních způsobů integrace IP telefonie s globální PSTN/PLMN. V rámci 3GPP se stala nezbytnou pro IMS a pozdější generace jádrových sítí pro vzájemné propojení se staršími okruhově přepínanými sítěmi, což zajišťuje kontinuitu služeb během migrace na plně IP jádra.

## Klíčové vlastnosti

- Přenáší signalizační zprávy SS7 MTP3 (ISUP, SCCP) přes IP sítě
- Používá SCTP pro spolehlivý, spojově orientovaný přenos s podporou multihoming
- Podporuje správu signalizační sítě (SSNM) pro dostupnost tras a zahlcení
- Umožňuje redundanci ASP a sdílení zátěže pro vysokou dostupnost
- Umožňuje oddělení funkcí signalizační brány a aplikačního serveru
- Umožňuje škálovatelnou, distribuovanou architekturu pro telekomunikační služby přes IP

## Související pojmy

- [M2PA – Message Transfer Part 2 - User Peer-to-Peer Adaptation Layer](/mobilnisite/slovnik/m2pa/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile

---

📖 **Anglický originál a plná specifikace:** [M3UA na 3GPP Explorer](https://3gpp-explorer.com/glossary/m3ua/)
