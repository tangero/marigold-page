---
slug: "mime"
url: "/mobilnisite/slovnik/mime/"
type: "slovnik"
title: "MIME – Multi-purpose Internet Mail Extensions"
date: 2025-01-01
abbr: "MIME"
fullName: "Multi-purpose Internet Mail Extensions"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mime/"
summary: "Internetový standard, který rozšiřuje formát e-mailových zpráv, aby podporoval text v jiných znakových sadách než ASCII, a také přílohy zvuku, videa, obrázků a aplikačních programů. V 3GPP je široce p"
---

MIME je internetový standard pro rozšíření formátů zpráv, který umožňuje podporu ne-ASCII textu a multimediálních příloh. V rámci 3GPP je široce používán pro zapouzdření a popis obsahu v rámci služeb zasílání zpráv a IMS.

## Popis

Multi-purpose Internet Mail Extensions (MIME) je internetový standard (původně definovaný v [IETF](/mobilnisite/slovnik/ietf/) RFC), který zásadně rozšiřuje možnosti internetové pošty tím, že umožňuje zahrnutí různorodých typů obsahu mimo prostý ASCII text. Jeho základním mechanismem je použití standardizovaných hlaviček ve struktuře e-mailové zprávy k popisu povahy obsahu. Nejvýznamnější hlavičkou je `Content-Type`, která specifikuje typ média (např. `text/plain`, `image/jpeg`, `application/pdf`) a často i podtyp, čímž efektivně sděluje přijímajícímu poštovnímu klientovi, jak má interpretovat tělo zprávy. Další klíčovou hlavičkou je `Content-Transfer-Encoding`, která určuje, jak jsou binární nebo ne-ASCII data zakódována do formátu kompatibilního s ASCII (jako Base64 nebo quoted-printable) pro bezpečný přenos přes starší poštovní systémy.

V rámci architektury 3GPP se MIME nepoužívá přímo pro e-mail, ale využívá se jako obecný a výkonný rámec pro strukturování a popis obsahu v různých protokolech a službách. Jeho primární aplikací je formát kontejneru. Například ve službě Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)) je celá multimediální zpráva (obsahující text, obrázky, audio klipy) zabalena jako MIME multipart zpráva, což umožňuje, aby jedna zprávová entita obsahovala více částí těla různých typů. Podobně v IP Multimedia Subsystem (IMS) používají zprávy SIP (Session Initiation Protocol) MIME pro přenos informací popisu relace (pomocí typu `application/sdp`) a dalších datových bloků specifických pro aplikaci. Tělo protokolu Session Description Protocol (SDP) popisující multimediální relaci je připojeno k SIP zprávě jako MIME část.

Technická operace zahrnuje konstrukci MIME entity v odesílající aplikaci podle příslušné specifikace 3GPP. To zahrnuje nastavení příslušných hlaviček (`Content-Type`, `Content-ID`, `Content-Location`) a kódování dat těla. U multipart zpráv jsou definovány hranice pro oddělení každé části těla. Tato strukturovaná entita je poté přenášena přes síťový protokol (např. [HTTP](/mobilnisite/slovnik/http/) pro MMS, SIP pro IMS). Aplikace příjemce parsuje MIME hlavičky, aby identifikovala typ obsahu každé části, v případě potřeby dekóduje přenosové kódování a poté předá každou část příslušnému zpracovateli (např. dekodéru obrázků, audio přehrávači nebo funkci správy relace pro SDP). Tato abstrakce umožňuje službám 3GPP zpracovávat bohatý a komplexní obsah standardizovaným a interoperabilním způsobem, nezávisle na podkladovém transportním mechanismu.

## K čemu slouží

MIME byl vytvořen, aby vyřešil závažná omezení původního standardu internetové pošty (RFC 822), který podporoval pouze 7bitový ASCII text. To znemožňovalo posílání zpráv v ne-latinských abecedách (jako je japonština nebo cyrilice) a znemožňovalo zahrnutí binárních souborů, jako je software, obrázky nebo zvuk. Účelem MIME bylo tyto bariéry překonat a umožnit globální multimediální komunikaci prostřednictvím e-mailu, aniž by bylo nutné měnit stávající infrastrukturu pro přenos pošty. Toho dosáhl přidáním popisných hlaviček ke zprávám, což umožnilo označit a vhodně zakódovat obsah pošty.

3GPP MIME rozsáhle přijalo, protože poskytoval hotový, robustní a široce implementovaný standard pro zapouzdření a popis obsahu. Když 3GPP vyvíjelo multimediální služby jako [MMS](/mobilnisite/slovnik/mms/) a IMS, čelilo stejnému základnímu problému: jak zabalit a signalizovat směs různých typů médií (text, obrázek, video, řídicí informace) přes různé transportní protokoly. Vývoj nového proprietárního formátu obsahu by byl neefektivní a bránil by interoperabilitě. MIME nabídl osvědčené řešení. Pro MMS poskytl perfektní obálku pro multimediální zprávu. Pro IMS umožnil SIP, textovému signalizačnímu protokolu, přenášet binární nebo strukturovaná data relace (jako SDP) sebepopisujícím způsobem. Jeho přijetí vyřešilo problém vyjednávání a zpracování obsahu v prostředí více dodavatelů a více operátorů, což zajišťuje, že obrázková zpráva odeslaná z telefonu v jedné síti může být správně zobrazena na telefonu od jiného výrobce v jiné síti.

## Klíčové vlastnosti

- Definuje hlavičku `Content-Type` pro specifikaci typu média (např. text/html, video/mp4)
- Podporuje typy obsahu `multipart` pro zabalení více mediálních objektů do jedné zprávy
- Specifikuje přenosová kódování obsahu (Base64, quoted-printable) pro ne-ASCII data
- Poskytuje hlavičky `Content-ID` a `Content-Location` pro odkazování na vložené objekty
- Slouží jako formát zapouzdření pro 3GPP službu Multimedia Messaging Service (MMS)
- Používá se pro přenos protokolu Session Description Protocol (SDP) a dalších datových bloků v rámci SIP signalizace pro IMS

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.423** (Rel-8) — PSTN/ISDN Simulation Services XCAP Protocol
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.544** (Rel-19) — SEAL Group Management Protocol
- **TS 24.546** (Rel-19) — SEAL Configuration Management Protocol Specification
- … a dalších 40 specifikací

---

📖 **Anglický originál a plná specifikace:** [MIME na 3GPP Explorer](https://3gpp-explorer.com/glossary/mime/)
