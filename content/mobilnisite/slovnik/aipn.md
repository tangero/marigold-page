---
slug: "aipn"
url: "/mobilnisite/slovnik/aipn/"
type: "slovnik"
title: "AIPN – All-IP Network"
date: 2025-01-01
abbr: "AIPN"
fullName: "All-IP Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aipn/"
summary: "AIPN je architektonický rámec 3GPP, v němž jsou všechny síťové služby – hlas, data a signalizace – poskytovány přes IP transport. Nahrazuje starší okruhově přepínané sítě jednotnou infrastrukturou s p"
---

AIPN je architektonický rámec 3GPP, v němž jsou všechny síťové služby poskytovány přes IP transport, čímž nahrazuje starší okruhově přepínané sítě jednotnou infrastrukturou s přepínáním paketů.

## Popis

All-IP Network (AIPN) je komplexní architektonický paradigma definované organizací 3GPP, které převádí mobilní sítě z tradičních okruhově přepínaných ([CS](/mobilnisite/slovnik/cs/)) domén pro hlas a oddělených paketově přepínaných ([PS](/mobilnisite/slovnik/ps/)) domén pro data na plně konvergovanou infrastrukturu založenou na IP. V této architektuře jsou všechny služby – včetně hlasu v reálném čase (prostřednictvím Voice over LTE neboli VoLTE a později Voice over NR), videa, zasílání zpráv a signalizace – přenášeny jako IP pakety. Jádrová síť se vyvíjí tak, aby pro poskytování služeb využívala IP Multimedia Subsystem (IMS), zatímco transportní vrstvy využívají IP protokoly end-to-end, od uživatelského zařízení (UE) přes rádiovou přístupovou síť (RAN) a jádro až k externím sítím.

Architektonicky AIPN integruje několik klíčových komponent. Evolved Packet Core (EPC) ve 4G a 5G Core (5GC) slouží jako centrální jádrové sítě založené na IP, které spravují konektivitu, mobilitu a politiky. IMS poskytuje servisní vrstvu pro multimediální služby a využívá Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro řízení relací. Transportní sítě využívají pro backhaul a konektivitu jádra IP/[MPLS](/mobilnisite/slovnik/mpls/) nebo Ethernet a zajišťují kvalitu služeb (QoS) prostřednictvím mechanismů jako je DiffServ. Na přístupové straně jsou rádiová rozhraní LTE a 5G NR nativně založena na IP, s protokoly jako [GTP-U](/mobilnisite/slovnik/gtp-u/) pro tunelování uživatelské roviny a [SCTP](/mobilnisite/slovnik/sctp/) over IP pro signalizaci.

Jak AIPN funguje, zahrnuje směrování IP paketů end-to-end. Když se UE připojí, naváže výchozí IP bearer pro konektivitu. Pro služby jako hlas se UE zaregistruje u IMS a signalizace SIP nastaví vyhrazený bearer s příslušnými parametry QoS (např. pro garantovaný přenosový výkon). Pakety jsou zapouzdřeny a směrovány přes IP tunely (např. [GTP](/mobilnisite/slovnik/gtp/) tunely mezi eNodeB/gNB a jádrovými bránami), s vynucováním politik prostřednictvím [PCRF](/mobilnisite/slovnik/pcrf/) ve 4G nebo PCF v 5G. Tento jednotný přístup eliminuje potřebu samostatných CS síťových prvků, jako je MSC, zjednodušuje provoz sítě a umožňuje bezproblémovou integraci služeb.

Role AIPN v síti je transformační. Poskytuje škálovatelný a flexibilní základ pro multimediální služby, snižuje provozní náklady konsolidací sítí a podporuje inovace prostřednictvím webových API a síťové expozice. Standardizací na IP zajišťuje interoperabilitu s pevnými sítěmi a internetem, což usnadňuje konvergenci (např. prostřednictvím fixed-mobile convergence). V 5G principy AIPN tvoří základ network slicing a edge computing, což umožňuje dynamickou alokaci zdrojů pro různé případy užití od vylepšeného mobilního širokopásmového připojení až po kritický IoT.

## K čemu slouží

AIPN bylo vytvořeno za účelem řešení omezení starších mobilních sítí, které používaly oddělené okruhově přepínané domény pro hlas a paketově přepínané domény pro data. Tento dvoudoménový přístup vedl k neefektivitám: vysokým provozním nákladům z udržování paralelních infrastruktur, složitosti integrace služeb a omezené podpoře nově vznikajících multimediálních aplikací. Rozšíření internetových služeb a poptávka po mobilních širokopásmových datech poháněly potřebu po jednotné síti, která by mohla efektivně zpracovávat všechny typy provozu přes IP, což odráželo vývoj v pevných sítích.

Historicky se sítě 2G a 3G spoléhaly na CS pro hlas, což vyžadovalo vyhrazené zdroje na každé volání, zatímco datové služby byly doplňkem s nižším výkonem. Jak narůstalo využívání dat, tento model se stal neudržitelným. AIPN, zavedené v 3GPP Release 7, mělo za cíl přejít na jednotnou infrastrukturu založenou na IP, snížit náklady konsolidací a umožnit nové zdroje příjmů ze služeb založených na IP, jako je VoIP, videokonference a rich communication services (RCS). Také se sladilo s průmyslovými trendy směřujícími k síťové konvergenci a all-IP transportu.

Problémy, které AIPN řeší, zahrnují zjednodušení sítě, lepší škálovatelnost a zvýšenou agilitu služeb. Eliminací CS prvků operátoři snižují kapitálové i provozní výdaje. Statické multiplexování IP umožňuje efektivnější využití zdrojů ve srovnání s okruhovým přepínáním. Navíc AIPN umožňuje bezproblémovou integraci s IMS pro pokročilé služby, podporuje vyšší datové rychlosti a poskytuje základnu připravenou na budoucnost pro technologie jako LTE, 5G a IoT, čímž zajišťuje, že se sítě mohou vyvíjet s měnícími se požadavky.

## Klíčové vlastnosti

- Jednotný IP transport pro všechny služby (hlas, data, signalizace)
- Integrace s IMS pro poskytování multimediálních služeb
- End-to-end správa QoS prostřednictvím řízení politik
- Podpora síťové konvergence (fixed-mobile, multi-access)
- Škálovatelná architektura umožňující vysokorychlostní širokopásmový přenos
- Zjednodušení provozu konsolidací síťových prvků

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TS 22.258** (Rel-7) — All-IP Network Service Requirements
- **TS 22.259** (Rel-19) — Personal Network Management Requirements
- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [AIPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/aipn/)
