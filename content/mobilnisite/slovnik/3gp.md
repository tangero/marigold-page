---
slug: "3gp"
url: "/mobilnisite/slovnik/3gp/"
type: "slovnik"
title: "3GP – 3GPP File Format"
date: 2025-01-01
abbr: "3GP"
fullName: "3GPP File Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3gp/"
summary: "3GP je multimediální kontejnerový formát standardizovaný organizací 3GPP pro ukládání a doručování audia, videa a časovaného textu přes mobilní sítě. Je založen na formátu ISO Base Media File Format ("
---

3GP je multimediální kontejnerový formát standardizovaný organizací 3GPP pro ukládání a doručování audia, videa a časovaného textu přes mobilní sítě, optimalizovaný pro efektivní přenos a přehrávání na zařízeních s omezenými prostředky.

## Popis

Formát souboru 3GPP (3GP) je multimediální kontejnerový formát speciálně navržený pro ukládání a doručování multimediálního obsahu přes mobilní sítě 3GPP. Je odvozen od formátu [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/), ISO/[IEC](/mobilnisite/slovnik/iec/) 14496-12), který poskytuje flexibilní rámec pro časované multimediální prezentace. Formát 3GP strukturuje multimediální data do stop (tracks), přičemž každá stopa obsahuje jediný typ média, jako je video, audio nebo text. Tyto stopy jsou synchronizovány pomocí společné časové osy, což umožňuje koordinované přehrávání různých multimediálních komponent. Formát používá hierarchickou strukturu boxů (také nazývaných atomy), které obsahují metadata a mediální data, což umožňuje efektivní parsování a streamování.

V jádru využívá 3GP architekturu systémů MPEG-4, která využívá objektové deskriptory a popis scény pro správu multimediálních prezentací. Formát souboru podporuje jak progresivní stahování, tak metody streamovaného doručování, což jej činí vhodným pro různé scénáře služeb včetně video-on-demand a živého streamování. Pro streamovací aplikace mohou být soubory 3GP strukturovány pomocí nápovědních stop (hint tracks), které poskytují instrukce pro zabalení mediálních dat do paketů protokolu Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)). To umožňuje efektivní doručování v reálném čase přes IP sítě při zachování synchronizace mezi audio a video streamy.

Formát specifikuje několik profilů a úrovní pro zajištění interoperability mezi různými zařízeními a síťovými podmínkami. Mezi ně patří základní profil 3GPP (3GPP Basic Profile) pro obecné multimediální služby a profil progresivního stahování 3GPP (3GPP Progressive Download Profile) pro služby vyžadující progresivní přehrávání. Formát souboru podporuje více kodeků prostřednictvím dobře definovaných formátů vstupů vzorků (sample entry formats), což umožňuje implementacím vybrat vhodné kodeky na základě schopností zařízení a šířky pásma sítě. Mezi klíčové podporované video kodeky patří H.263 (MPEG-4 Visual), H.264/[AVC](/mobilnisite/slovnik/avc/) a MPEG-4 Visual; zatímco audio kodeky zahrnují [AMR-NB](/mobilnisite/slovnik/amr-nb/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [AAC-LC](/mobilnisite/slovnik/aac-lc/), HE-AAC a Enhanced AAC+. Formát také podporuje stopy s časovaným textem pro titulky a skryté titulky pomocí formátu 3GPP Timed Text.

Soubory 3GP obsahují komplexní metadata prostřednictvím různých boxů, jako je Movie Box (moov), který obsahuje prezentační metadata, Media Data Box (mdat), který ukládá skutečné mediální vzorky, a Sample Table Box (stbl), který poskytuje indexační informace pro náhodný přístup. Pro streamovací aplikace formát podporuje vytváření fragmentovaných souborů, kde jsou metadata periodicky prokládána s mediálními daty, což umožňuje efektivní adaptivní streamování. Formát také zahrnuje podporu správy digitálních práv prostřednictvím schématu Common Encryption (CENC), což umožňuje ochranu obsahu při zachování kompatibility formátu.

V širší architektuře 3GPP slouží 3GP jako standardní formát souboru pro službu Multimedia Broadcast/Multicast Service (MBMS), Packet-Switched Streaming Service (PSS) a Multimedia Telephony Service (MMTel). Umožňuje efektivní ukládání a doručování multimediálního obsahu přes heterogenní sítě při zachování požadavků na kvalitu služby. Konstrukční aspekty formátu zahrnují minimální režii zpracování, efektivní využití šířky pásma a kompatibilitu s existujícími internetovými standardy, což z něj činí základní komponentu multimediálních služeb 3GPP.

## K čemu slouží

Formát souboru 3GPP byl vytvořen, aby řešil potřebu standardizovaného multimediálního kontejnerového formátu optimalizovaného pro mobilní sítě a zařízení. Před jeho standardizací existovaly různé proprietární formáty, kterým chyběla interoperabilita a které nebyly optimalizovány pro omezení mobilního prostředí. Tato omezení zahrnovala omezený výpočetní výkon, paměť a výdrž baterie na mobilních zařízeních, stejně jako proměnlivou šířku pásma a vyšší míru chyb na bezdrátových sítích. Formát 3GP byl navržen speciálně k překonání těchto omezení a zároveň poskytoval konzistentní rámec pro multimediální služby napříč různými implementacemi 3GPP.

Formát byl vyvinut jako součást specifikací služby Packet-switched Streaming Service (PSS) 3GPP, aby umožnil efektivní doručování audio a video obsahu přes paketově přepínané sítě. Řešil problém, jak zabalit multimediální obsah způsobem, který může být efektivně přenášen přes mobilní sítě s omezenou šířkou pásma, a zároveň podporovat funkce jako náhodný přístup, rychlý posun vpřed, zpět a streamování. Tím, že je formát založen na ISO Base Media File Format, využila 3GPP existující standardizační práci a přidala optimalizace a požadavky specifické pro mobilní prostředí.

Historicky byl vývoj 3GP motivován rostoucí poptávkou po multimediálních službách na sítích 3G a potřebou zajistit interoperabilitu mezi zařízeními a zařízeními různých výrobců. Formát umožnil poskytovatelům služeb nabízet konzistentní multimediální zážitky napříč různými ekosystémy zařízení a zároveň optimalizovat využití síťových zdrojů. Také řešil výzvu adaptace obsahu, což umožnilo serverům transkódovat obsah do vhodných formátů a datových toků na základě schopností zařízení a síťových podmínek, což bylo obzvláště důležité v heterogenním mobilním prostředí počátečních nasazení 3G.

## Klíčové vlastnosti

- Kompatibilita s formátem ISO Base Media File Format (ISOBMFF)
- Podpora více audio a video kodeků včetně H.263, H.264, AMR a AAC
- Optimalizace pro doručování přes mobilní sítě s efektivním zabalováním do paketů
- Podpora progresivního stahování i streamování v reálném čase
- Podpora stop s časovaným textem pro titulky a skryté titulky
- Integrace správy digitálních práv prostřednictvím Common Encryption

## Související pojmy

- [ISOBMFF – International Organization for Standards, Base Media File Format](/mobilnisite/slovnik/isobmff/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 28.406** (Rel-19) — QoE measurement collection: info definition & transport

---

📖 **Anglický originál a plná specifikace:** [3GP na 3GPP Explorer](https://3gpp-explorer.com/glossary/3gp/)
