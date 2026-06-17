---
slug: "ips"
url: "/mobilnisite/slovnik/ips/"
type: "slovnik"
title: "IPS – Internet Protocol Stack"
date: 2025-01-01
abbr: "IPS"
fullName: "Internet Protocol Stack"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ips/"
summary: "Internet Protocol Stack (IPS) je standardizovaná sada protokolů umožňující komunikaci založenou na IP v sítích 3GPP. Definuje vrstvovou architekturu pro přenos dat a zajišťuje interoperabilitu mezi sí"
---

IPS (Internet Protocol Stack) je standardizovaná sada protokolů, která umožňuje komunikaci založenou na IP a definuje vrstvovou architekturu pro přenos dat v sítích 3GPP, čímž zajišťuje interoperabilitu pro všechny paketově přepínané služby.

## Popis

Internet Protocol Stack (IPS) v 3GPP označuje kompletní sadu protokolových vrstev, jak jsou definovány standardy [IETF](/mobilnisite/slovnik/ietf/) a profilovány 3GPP, které jsou implementovány v uživatelském zařízení (UE) a síťových uzlech pro podporu služeb založených na IP. Nejde o jeden protokol, ale o rámec zahrnující vrstvy jako fyzická vrstva, vrstva spojení dat (např. adaptace PPP, Ethernet), síťová vrstva (IPv4, IPv6), transportní vrstva (TCP, UDP, SCTP) a aplikační protokoly. Specifikace 3GPP, zejména TS 33.108, podrobně popisují bezpečnostní a funkční požadavky pro implementaci tohoto zásobníku v mobilním ekosystému.

Architektonicky je IPS integrován do procesu zřizování jednotky protokolových dat (PDU) v 5G Core nebo PDP kontextu v EPC. Funguje tak, že umožňuje UE požádat o IP adresu a vyjednat podporované sady protokolů se sítí. Po zřízení jsou uživatelská data zapouzdřena podle vrstev zásobníku, procházejí rádiovou přístupovou sítí (RAN), přenosovou sítí a bránami jádra sítě (jako [UPF](/mobilnisite/slovnik/upf/) nebo PGW), než dosáhnou externích datových sítí. Klíčové komponenty zahrnují IP zásobník v modemu UE, odpovídající zásobník v obslužné bráně (např. SGW-U/UPF) a řídicí funkce ([SMF](/mobilnisite/slovnik/smf/)/[MME](/mobilnisite/slovnik/mme/)), které spravují parametry relace.

Jeho role je zásadní: je to kanál pro všechna paketová data. Ať už jde o prohlížení webu, streamování videa nebo telemetrii IoT, IPS poskytuje standardizovaný 'jazyk' pro výměnu dat. Konfigurace zásobníku, včetně podpory verze IP (v4/v6), komprese hlaviček (ROHC) a označení kvality služeb (QoS), je řízena sítí za účelem optimalizace výkonu a využití zdrojů. V podstatě je IPS technickou realizací konceptu 'přenosového kanálu' (bearer), který překládá požadavky služeb do skutečných datových toků napříč heterogenní síťovou infrastrukturou.

## K čemu slouží

Internet Protocol Stack byl standardizován v rámci 3GPP, aby usnadnil přechod od okruhově přepínaných, na hlas zaměřených sítí 2G k paketově přepínaným, na data zaměřeným sítím 3G a 4G. Před jeho formálním profilováním v 3GPP používaly rané mobilní datové služby proprietární nebo omezené protokoly. IPS byl vytvořen k vyřešení kritického problému interoperability, aby zajistil, že mobilní zařízení od libovolného výrobce se může bezproblémově připojit k globálnímu internetu a dalším službám založeným na IP prostřednictvím jakékoli kompatibilní sítě 3GPP.

Motivace pramenila z explozivního růstu internetu a potřeby, aby se mobilní sítě staly jeho nedílnou součástí. Přijetím a profilováním dobře zavedené sady protokolů IP od [IETF](/mobilnisite/slovnik/ietf/) se 3GPP vyhnulo znovuvynalézání kola a využilo robustní, škálovatelnou a všeobecně známou rodinu protokolů. Tím byly odstraněny limity předchozích přístupů, které byly často izolované a neefektivní pro obecné datové služby. IPS umožnil model 'trvalého připojení' (always-on), podporující širokou škálu aplikací přesahujících jednoduché zasílání zpráv, a položil základy pro pokročilé služby jako IP Multimedia Subsystem (IMS). Jeho specifikace zajišťuje, že bezpečnostní aspekty, jako je průchod firewallem a důvěryhodný bod přítomnosti IP, jsou integrovány od samého počátku.

## Klíčové vlastnosti

- Profiluje standardy IETF (IPv4, IPv6, TCP, UDP) pro mobilní prostředí
- Podporuje duální zásobník IP (IPv4v6) pro přechodové scénáře
- Integruje se s mechanismy specifickými pro 3GPP, jako je správa PDP kontextu/relace PDU
- Umožňuje kompresi hlaviček (ROHC) pro úsporu rádiových zdrojů
- Poskytuje základ pro všechny paketové datové služby a IMS
- Definuje rozhraní bezpečnostní architektury pro důvěryhodnou IP konektivitu

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [IPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ips/)
