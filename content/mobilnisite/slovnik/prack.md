---
slug: "prack"
url: "/mobilnisite/slovnik/prack/"
type: "slovnik"
title: "PRACK – Provisional Response Acknowledgement"
date: 2025-01-01
abbr: "PRACK"
fullName: "Provisional Response Acknowledgement"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/prack/"
summary: "PRACK je metoda SIP definovaná v RFC 3262, používaná v IMS k spolehlivému potvrzení přijetí provizorních odpovědí (1xx), jako je 180 Ringing. Zajišťuje spolehlivé doručení provizorní signalizace, což"
---

PRACK je metoda SIP používaná v IMS k spolehlivému potvrzení provizorních odpovědí, což zajišťuje důvěryhodné doručení kritické signalizace, jako jsou indikace průběhu hovoru.

## Popis

Provisional Response ACKnowledgement (PRACK) je metoda protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)), standardizovaná v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3262, která je přijata a využívána v architektuře 3GPP IP Multimedia Subsystem (IMS). SIP, jako textový signalizační protokol aplikační vrstvy, je jádrem IMS pro navazování, modifikaci a ukončování multimediálních relací. Odpovědi SIP se dělí na provizorní (1xx) a konečné (2xx-6xx). Provizorní odpovědi poskytují informační aktualizace stavu, jako jsou 100 Trying, 180 Ringing a 183 Session Progress, ale jejich doručení přes nespolehlivé transportní protokoly, jako je [UDP](/mobilnisite/slovnik/udp/), původně nebylo zaručeno.

Metoda PRACK řeší tento problém spolehlivosti. Když User Agent Client ([UAC](/mobilnisite/slovnik/uac/)), například IMS terminál, obdrží provizorní odpověď vyžadující potvrzení (což je indikováno přítomností hlavičky Require s hodnotou '100rel' v odpovědi), musí odeslat PRACK požadavek zpět k User Agent Server ([UAS](/mobilnisite/slovnik/uas/)), například IMS Application Server nebo jinému terminálu. Tento PRACK požadavek je samostatná SIP transakce, která spolehlivě potvrzuje přijetí této konkrétní provizorní odpovědi. Samotná provizorní odpověď obsahuje hlavičku RSeq (Response Sequence number) a odpovídající PRACK požadavek obsahuje hlavičku RACK, která opakuje toto číslo RSeq a sekvenční číslo CSeq z původní INVITE transakce, což zajišťuje přesné přiřazení.

V rámci IMS sítě procházejí PRACK zprávy stejnou signalizační cestou jako původní INVITE, procházejíce přes Proxy Call Session Control Functions ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), Serving CSCFs ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a případné Application Servers (AS). Tyto uzly fungují jako stavové proxy pro INVITE transakci a musí také správně zpracovat PRACK transakci, aby zachovaly stav relace. Spolehlivé doručení provizorních odpovědí umožněné pomocí PRACK je klíčové pro několik pokročilých telefonních služeb. Například umožňuje spolehlivé doručení 'ringback tone' (180 Ringing) a, což je důležitější, umožňuje relace early media. Early media umožňuje navázání mediálních proudů (jako jsou hlášení nebo hudba při čekání) před konečnou odpovědí (200 OK) na INVITE, což je nezbytné pro služby před hovorem a bezproblémový uživatelský zážitek.

Implementace a podpora PRACK je vyžadována pro IMS terminály a síťové elementy, které podporují funkce precondition a early media. Tvoří klíčovou část rámce spolehlivosti služeb IMS spolu s dalšími rozšířeními SIP, jako je UPDATE. Zpracování PRACK je specifikováno v 3GPP TS 24.229 (IP multimedia call control protocol) a je nedílnou součástí specifikací služby IMS Multimedia Telephony.

## K čemu slouží

PRACK byl vytvořen, aby vyřešil významné omezení základního protokolu SIP (RFC 3261) týkající se nespolehlivého doručování provizorních odpovědí. V původní specifikaci SIP nebyly provizorní odpovědi (1xx) potvrzovány, což je činilo nespolehlivými při přenosu přes UDP. Tato nespolehlivost mohla vést k situacím, kdy volající strana nikdy neuslyší vyzváněcí tón, protože zpráva 180 Ringing byla ztracena, nebo kdy selhala jednání o early media, což degradovalo uživatelský zážitek u služeb jako je video vyzvánění nebo hlášení před hovorem.

Motivace vycházela z požadavku telekomunikačního průmyslu na spolehlivou a předvídatelnou signalizaci, podobnou té, kterou poskytují tradiční sítě SS7/ISUP. Aby se IMS stalo životaschopnou náhradou a vylepšením služeb okruhově přepínané telefonie, muselo garantovat doručení kritických mezilehlých signalizačních zpráv. IETF definovalo toto rozšíření v RFC 3262, které 3GPP následně přijalo jako povinnou součást pro IMS implementace podporující určité funkce.

PRACK spolu s rámcem precondition umožňuje pokročilé služební schopnosti, které byly s nespolehlivými provizorními odpověďmi obtížné nebo nemožné. Řeší problém stavu soutěže během navazování relace, zejména když je zapojena rezervace zdrojů (prostřednictvím QoS mechanismů) a early media. Tím, že poskytuje spolehlivý handshake pro provizorní zprávy, zajišťuje, že oba konce relace mají konzistentní a potvrzený pohled na stav průběhu hovoru, což je základní pro složité IMS služby jako Multimedia Telephony (MMTel), Voice over LTE (VoLTE) a Rich Communication Services (RCS).

## Klíčové vlastnosti

- Definována jako metoda SIP (jako INVITE nebo BYE) pro potvrzování provizorních (1xx) odpovědí.
- Používá hlavičky RSeq a RACK k jednoznačné korelaci potvrzení s konkrétní provizorní odpovědí.
- Aktivována pomocí option tagu '100rel' v hlavičkových polích Supported nebo Require SIP dialogu.
- Vytváří samostatnou SIP transakci, čímž zajišťuje spolehlivé doručení přes nespolehlivé transporty jako UDP.
- Nezbytná pro spolehlivý provoz rámce precondition v SIP (RFC 3312).
- Základní pro umožnění spolehlivých relací early media, kde média proudí před konečnou odpovědí na relaci.

## Související pojmy

- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TR 26.982** (Rel-19) — Multiparty Real-Time Text Protocol Details
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [PRACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/prack/)
