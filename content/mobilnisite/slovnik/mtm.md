---
slug: "mtm"
url: "/mobilnisite/slovnik/mtm/"
type: "slovnik"
title: "MTM – Mobile-To-Mobile (call)"
date: 2025-01-01
abbr: "MTM"
fullName: "Mobile-To-Mobile (call)"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mtm/"
summary: "Mobile-To-Mobile (MTM) označuje hlasové nebo video volání navázané přímo mezi dvěma mobilními uživatelskými zařízeními (UE) v rámci stejné nebo různých buněčných sítí. Jedná se o základní telekomunika"
---

MTM je hlasové nebo video volání navázané přímo mezi dvěma mobilními uživatelskými zařízeními (UE) v rámci stejné nebo různých buněčných sítí.

## Popis

Mobile-To-Mobile (MTM) je základním typem služby v systémech 3GPP a označuje komunikační relaci, kde jsou jak volající strana (vysílající UE), tak volaná strana (přijímající UE) mobilní stanice fungující v rámci buněčné sítě. Termín široce zahrnuje hlasová volání a později i video hovory, které jsou směrovány výhradně přes infrastrukturu mobilní sítě bez přechodu přes tradiční veřejnou telefonní síť (PSTN) pro dokončení. MTM volání zahrnuje řadu standardizovaných signalizačních procedur a procedur přenosové cesty napříč rádiovou přístupovou sítí (RAN) a jádrovou sítí (CN) k navázání, udržení a uvolnění obousměrného komunikačního kanálu mezi dvěma UE.

Technický proces pro MTM volání začíná tím, že vysílající UE odešle požadavek na sestavení hovoru (např. zprávu SETUP v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) nebo SIP INVITE v doméně s přepojováním paketů (PS)/IMS) přes obsluhující základnovou stanici do jádrové sítě. U tradičních 2G/3G CS hovorů požadavek přijme ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)), provede analýzu čísla a určí, že volaná strana je mobilní účastník. Následně dotazuje domovský registr polohy ([HLR](/mobilnisite/slovnik/hlr/)), aby získala směrovací informace (adresu obsluhující MSC/VLR pro volaného účastníka). Vysílající MSC směruje signalizaci hovoru k přijímající MSC, která vyvolá volané UE ve své lokalizační oblasti. Po přijetí je navázána hlasová přenosová cesta: v CS se jedná o vyhrazený časový slot nebo okruh; v 4G/5G při použití Voice over LTE (VoLTE) nebo Voice over NR (VoNR) se jedná o IP-based přenosovou cestu přes PS doménu s médii zpracovávanými IP Multimedia Subsystem (IMS).

Kompletní cesta pro MTM volání typicky zahrnuje rádiové přenosové cesty mezi každým UE a jeho příslušnou základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/), NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB), backhaul připojení k jádrové síti a propojení mezi jádrovými sítěmi (např. pomocí signalizace [ISUP](/mobilnisite/slovnik/isup/) v CS nebo SIP směrování v IMS). V roamingu může hovor procházet navštívenými sítěmi obou stran a potenciálně zahrnovat mezifunkční rozhraní. Mezi klíčové síťové funkce zapojené patří MSC (pro CS), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving Gateway (SGW) pro řídicí a uživatelskou rovinu LTE, IMS Core ([CSCF](/mobilnisite/slovnik/cscf/), MGCF atd.) a Policy and Charging Rules Function (PCRF/PCF) pro řízení politik na PS přenosových cestách. Účtovací systémy generují záznamy o volání (CDR) pro volání mobilním účastníkem iniciované (MO) a mobilním účastníkem přijatá (MT) pro účely fakturace.

S vývojem směrem k plně IP sítím se MTM hovory přesunuly z převážně přepojování okruhů na přepojování paketů přes IMS. To umožňuje rozšířené služby jako High Definition (HD) hlas (pomocí kodeku AMR-WB), videohovory a rich communication services (RCS). Signalizace řízení hovoru používá SIP přes řídicí rovinu PS, zatímco hlasové/video mediální toky jsou přenášeny jako pakety RTP/UDP/IP přes uživatelskou rovinu PS přenosových cest (vyhrazené přenosové cesty s příslušnými QoS Class Identifiers pro konverzační hlas/video). Systém 5G to dále optimalizuje pomocí architektury založené na službách, kde Session Management Function (SMF) a User Plane Function (UPF) vytvářejí PDU relaci pro IMS provoz.

## K čemu slouží

Služba Mobile-To-Mobile volání je základním kamenem mobilní telefonie a umožňuje přímou komunikaci mezi mobilními účastníky. Jejím účelem je poskytnout všudypřítomné, spolehlivé a řiditelné hlasové připojení bez nutnosti prostředníků z pevných linek. Zpočátku byly mobilní sítě vnímány jako rozšíření PSTN, přičemž hovory byly často směrovány na/ze pevných linek. S rostoucí penetrací mobilních služeb se významná část provozu stala mobile-to-mobile, což pohánělo optimalizace síťového směrování, efektivity signalizace a tarifních struktur specificky pro MTM hovory.

Koncept řešil základní potřebu bezdrátové komunikace mezi osobami. Rané celulární systémy (1G) poskytovaly základní MTM schopnost, ale s omezenou škálovatelností a bez digitálního zabezpečení. Standardizace MTM procedur ve 2G (GSM) prostřednictvím 3GPP zajistila interoperabilitu, což umožnilo účastníkům v různých sítích (národních i mezinárodních) se bezproblémově spojit. To podpořilo konkurenci a růst. Služba také řešila problém správy mobility během hovoru, přičemž procedury předávání hovoru zajišťovaly kontinuitu hovoru při pohybu uživatelů mezi buňkami.

S nástupem IP sítí se motivace vyvinula k integraci MTM hovorů do domény s přepojováním paketů za účelem snížení nákladů, zjednodušení síťové architektury a umožnění konvergence s datovými službami. Přechod na VoLTE/VoNR pod IMS byl poháněn potřebou podporovat vysokokvalitní hlas v sítích LTE/5G, kterým chybí nativní CS doména. MTM v tomto kontextu využívá efektivity IP přenosu a umožňuje inovace služeb (např. video doplňky, sdílení souborů během hovorů). Zůstává kritická pro příjmy operátorů a jako základní služba, i přes existenci Over-the-Top (OTT) alternativ, díky své garantované kvalitě, spolehlivosti a bezproblémové integraci se síťovými funkcemi, jako je tísňové volání a zákonné odposlechy.

## Klíčové vlastnosti

- Přímé navázání hovoru mezi dvěma mobilními uživatelskými zařízeními (UE) v rámci buněčných sítí.
- Podporuje implementace jak v doméně s přepojováním okruhů (CS) (2G/3G), tak v doméně s přepojováním paketů/IMS (4G/5G).
- Zahrnuje směrování v jádrové síti a správu mobility (dotaz HLR/HSS, signalizace MSC/MME).
- Umožňuje kompletní hlasové a video mediální přenosové cesty s příslušnou QoS (např. konverzační třída).
- Generuje specifické účtovací záznamy (MO-MT CDR) pro účely fakturace.
- Základ pro pokročilé komunikační služby jako VoLTE, VoNR a Rich Communication Services (RCS).

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MOC – Mobile Originated Call (attempt)](/mobilnisite/slovnik/moc/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtm/)
