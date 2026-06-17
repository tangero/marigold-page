---
slug: "html"
url: "/mobilnisite/slovnik/html/"
type: "slovnik"
title: "HTML – HyperText Markup Language"
date: 2025-01-01
abbr: "HTML"
fullName: "HyperText Markup Language"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/html/"
summary: "Standardní značkovací jazyk pro vytváření webových stránek a webových aplikací, na který se odkazuje ve specifikacích 3GPP. Definuje strukturu a prezentaci obsahu doručovaného přes mobilní sítě a umož"
---

HTML je standardní značkovací jazyk pro vytváření webových stránek a aplikací, který definuje strukturu a prezentaci obsahu doručovaného přes mobilní sítě.

## Popis

HyperText Markup Language (HTML) je základním jazykem World Wide Webu, standardizovaným konsorciem World Wide Web Consortium (W3C) a často zmiňovaným ve specifikacích 3GPP. V kontextu 3GPP není HTML protokolem definovaným touto skupinou, ale nedílnou součástí ekosystému servisní vrstvy, kterou jsou mobilní sítě navrženy podporovat. Je primárním formátem pro webový obsah, který je přenášen přes přenašeče definované 3GPP a přistupují k němu prohlížeče v uživatelském zařízení (UE). Dokumenty HTML jsou přenášeny pomocí protokolů jako [HTTP](/mobilnisite/slovnik/http/) nebo [HTTPS](/mobilnisite/slovnik/https/), které běží nad službou IP konektivity poskytovanou paketovým jádrem 3GPP (např. [GTP](/mobilnisite/slovnik/gtp/) tunely v PGW/[UPF](/mobilnisite/slovnik/upf/)).

Jazyk funguje pomocí systému značek (tagů) a atributů, které strukturují obsah – jako text, obrázky, hypertextové odkazy, formuláře a multimédia – do hierarchického objektového modelu dokumentu ([DOM](/mobilnisite/slovnik/dom/)). Když UE vyžádá webovou stránku, server odešle soubor HTML. Prohlížeč v UE následně HTML analyzuje, interpretuje značky a vykreslí vizuální rozložení stránky. Tento proces často zahrnuje načítání dalších prostředků odkazovaných v HTML, jako jsou kaskádové styly ([CSS](/mobilnisite/slovnik/css/)) pro vzhled a JavaScript pro interaktivitu, což spouští více následných datových relací přes mobilní síť. Z pohledu sítě je efektivní doručování HTML a jeho přidružených prostředků klíčovým hybatelem charakteru provozu, což ovlivňuje plánování rádiových zdrojů, zatížení jádra sítě a metriky kvality uživatelského zážitku (QoE).

Specifikace 3GPP odkazují na HTML v kontextech jako požadavky na služby (např. pro službu multimediálních zpráv - [MMS](/mobilnisite/slovnik/mms/), kde zprávy mohou obsahovat HTML obsah), Open Service Access ([OSA](/mobilnisite/slovnik/osa/)), aplikační programová rozhraní (API) a bezpečnostní specifikace pro webové služby. Například specifikace mohou detailně popisovat, jak je s HTML obsahem v síti nakládáno, zabezpečováno nebo přizpůsobováno (přes transkódování) pro různé možnosti zařízení. Jeho role spočívá v zajištění, že end-to-end architektura, od rádiového přístupu po jádro sítě, může efektivně podporovat doručování a vykreslování moderního webu, což je základní služba pro jakoukoli mobilní širokopásmovou síť.

## K čemu slouží

HTML je ve standardech 3GPP zmiňována, protože se mobilní sítě vyvinuly v primární přístupové médium k internetu. Hlavním účelem technologií 3GPP, zejména od 3G (UMTS) dále, se posunul od pouhé hlasové telefonie k poskytování všudypřítomné datové konektivity. Podpora webu – a tím i HTML – se stala kritickým požadavkem. Zařazení HTML do specifikací zajišťuje, že síťové funkce, jako je správa šířky pásma, účtování a zabezpečení, jsou navrženy s ohledem na charakter provozu a strukturu webového obsahu.

Historicky používaly rané mobilní datové služby jako WAP zjednodušené značkovací jazyky (WML). Motivací pro podporu plnohodnotného HTML byla snaha poskytnout na mobilních zařízeních zážitek z 'opravdového internetu' a opustit uzavřené ekosystémy portálů operátorů. To pohánělo vývoj vysokorychlostních paketových datových schopností (HSPA, LTE) a chytřejších zařízení. Odkazování na HTML umožňuje 3GPP definovat, jak síťové elementy interagují s webovým obsahem, například při přizpůsobování obsahu různým velikostem obrazovky, uplatňování řízení politik na základě typu obsahu nebo implementaci bezpečnostních mechanismů na ochranu před webovými hrozbami procházejícími mobilní infrastrukturou.

## Klíčové vlastnosti

- Standardizovaná struktura dokumentu využívající značky (tagy) a elementy
- Podpora vkládání multimédií (obrázků, videa, audia)
- Umožňuje vytváření hypertextových odkazů mezi dokumenty a prostředky
- Poskytuje formuláře pro vstup uživatelských dat a interakci
- Spolupracuje s CSS pro prezentaci a JavaScriptem pro chování
- Definuje objektový model dokumentu (DOM) pro programový přístup

## Související pojmy

- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)
- [HTTPS – Hyper Text Transfer Protocol Secure](/mobilnisite/slovnik/https/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 33.222** (Rel-19) — Secure HTTP Access in GAA
- **TS 33.823** (Rel-12) — GBA Web Browser Integration Study

---

📖 **Anglický originál a plná specifikace:** [HTML na 3GPP Explorer](https://3gpp-explorer.com/glossary/html/)
