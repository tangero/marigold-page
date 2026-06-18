---
slug: "tcp-ip"
url: "/mobilnisite/slovnik/tcp-ip/"
type: "slovnik"
title: "TCP/IP – Transmission Control Protocol / Internet Protocol"
date: 2025-01-01
abbr: "TCP/IP"
fullName: "Transmission Control Protocol / Internet Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tcp-ip/"
summary: "Základní sada komunikačních protokolů internetu. Definuje, jak jsou data zabalena do paketů, adresována, přenášena, směrována a přijímána napříč sítěmi. Je nezbytná pro umožnění služeb založených na I"
---

TCP/IP je základní sada komunikačních protokolů internetu, která definuje, jak jsou data zabalena do paketů, adresována, přenášena, směrována a přijímána napříč sítěmi.

## Popis

TCP/IP není jediný protokol, ale vrstvená sada protokolů, která řídí veškerou komunikaci na internetu. V kontextu 3GPP se jedná o základní protokolovou sadu používanou pro přenos dat v doméně s přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)). Tato sada je obvykle popsána pomocí čtyřvrstvého modelu: vrstva síťového rozhraní (např. Ethernet, [PPP](/mobilnisite/slovnik/ppp/)), síťová vrstva (IP), transportní vrstva (TCP, [UDP](/mobilnisite/slovnik/udp/)) a aplikační vrstva ([HTTP](/mobilnisite/slovnik/http/), [FTP](/mobilnisite/slovnik/ftp/) atd.). Internetový protokol (IP) je zodpovědný za logické adresování (IP adresy) a směrování datagramů přes různé sítě. Jde o protokol bez spojení s doručením s nejlepším úsilím, což znamená, že negarantuje doručení, pořadí ani kontrolu chyb paketů. Protokol TCP (Transmission Control Protocol), fungující na transportní vrstvě, staví na IP a poskytuje spolehlivou, spojení orientovanou službu bytového proudu. Vytváří virtuální spojení mezi koncovými body, sekvencuje datové pakety, poskytuje řízení toku a provádí opravu chyb pomocí potvrzení a retransmisí. V rámci sítě 3GPP používá uživatelské zařízení (UE) TCP/IP ke komunikaci s aplikačními servery na internetu nebo v IP multimediální podsystému (IMS) operátora. Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) ve starších vydáních nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet Core (EPC) funguje jako rozhraní mezi interním paketovým směrováním mobilní sítě a externími IP sítěmi a vykonává funkce jako přidělování IP adres (pomocí [DHCP](/mobilnisite/slovnik/dhcp/)) a vynucování politik. Integrace TCP/IP umožňuje mobilním sítím být bezproblémově připojeny k globálnímu internetu a podporovat širokou škálu služeb od prohlížení webu po komunikaci v reálném čase.

## K čemu slouží

Účelem TCP/IP v 3GPP je poskytnout standardizovanou, univerzální a interoperabilní metodu pro datovou komunikaci, která umožňuje mobilním sítím připojit se k globálnímu internetu a stát se jeho součástí. Před plným přijetím architektur plně založených na IP používaly mobilní sítě jako GSM primárně okruhově přepínaná spojení pro hlas a omezené datové služby (např. GPRS), které byly pro přerušovaný internetový provoz neefektivní. Motivací pro integraci TCP/IP bylo využít stávajícího, masivně úspěšného ekosystému internetu a umožnit mobilním účastníkům přístup ke stejným službám dostupným ve fixních sítích. Vyřešil problém heterogenity sítí tím, že poskytl společný jazyk pro komunikaci mezi zcela odlišnými síťovými technologiemi (např. rádiové přístupové sítě a páteřní optické sítě). Jeho vznik byl hnán potřebou škálovatelných, flexibilních a nákladově efektivních datových služeb, které by překročily proprietární nebo na telefonii zaměřené protokoly. Přijetí TCP/IP jako základního transportního protokolu bylo zásadním posunem, který umožnil mobilní broadbandovou revoluci a proměnil mobilní sítě ze systémů zaměřených na hlas na univerzální datové sítě.

## Klíčové vlastnosti

- Komunikace od konce ke konci napříč heterogenními sítěmi
- Spolehlivé doručování dat ve správném pořadí pomocí TCP
- Služba datagramů bez spojení s doručením s nejlepším úsilím pomocí IP
- Globální adresní schéma využívající IP adresy
- Mechanismy řízení toku a zahlcení
- Podpora širokého spektra protokolů aplikační vrstvy

## Související pojmy

- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)
- [UDP – User Datagram Protocol](/mobilnisite/slovnik/udp/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 32.101** (Rel-19) — Management principles and high-level requirements

---

📖 **Anglický originál a plná specifikace:** [TCP/IP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tcp-ip/)
